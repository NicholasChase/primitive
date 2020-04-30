package primitive

import (
	"image"
	"math"
)

func computeColor(target, current *image.RGBA, lines []Scanline, alpha int, filter int) Color {
	var rsum, gsum, bsum, count int64
	a := 0x101 * 255 / alpha
	for _, line := range lines {
		i := target.PixOffset(line.X1, line.Y)
		for x := line.X1; x <= line.X2; x++ {
			tr := int(target.Pix[i])
			tg := int(target.Pix[i+1])
			tb := int(target.Pix[i+2])
			cr := int(current.Pix[i])
			cg := int(current.Pix[i+1])
			cb := int(current.Pix[i+2])
			i += 4
			rsum += int64((tr-cr)*a + cr*0x101)
			gsum += int64((tg-cg)*a + cg*0x101)
			bsum += int64((tb-cb)*a + cb*0x101)
			count++
		}
	}
	if count == 0 {
		return Color{}
	}
	r := clampInt(int(rsum/count)>>8, 0, 255)
	g := clampInt(int(gsum/count)>>8, 0, 255)
	b := clampInt(int(bsum/count)>>8, 0, 255)

	return applyFilter(filter, r, g, b, alpha)
}

func copyLines(dst, src *image.RGBA, lines []Scanline) {
	for _, line := range lines {
		a := dst.PixOffset(line.X1, line.Y)
		b := a + (line.X2-line.X1+1)*4
		copy(dst.Pix[a:b], src.Pix[a:b])
	}
}

// Req. 4.4
// This function takes the user's input of filter as well as the
// rgb value of the current location and applies the filter of the
// user's selection
func applyFilter(filter, r, g, b, alpha int) Color {
	// no filter
	if filter == 0 {
		return Color{r, g, b, alpha}
	}
	// applies gray scale filter
	if filter == 1 {
		return GrayScaleFilter(r, g, b, alpha)
	}
	// applies sepia filter
	if filter == 2 {
		return SepiaFilter(r, g, b, alpha)
	}
	// applies negative filter
	if filter == 3 {
		return NegativeFilter(r, g, b, alpha)
	}

	return Color{r, g, b, alpha}
}

// GrayScale Filter
// Req. 4.1
// This Function takes the rgb values of the current location and converts
// them into grayscale values
func GrayScaleFilter(r, g, b, alpha int) Color {
	newRed := int(0.21 * float64(r))
	newGreen := int(0.72 * float64(g))
	newBlue := int(0.07 * float64(b))
	return Color{newRed, newGreen, newBlue, alpha}
}

// Sepia Filter
// Req. 4.2
// This Function takes the rgb values of the current location and converts
// them into sepia values
func SepiaFilter(r, g, b, alpha int) Color {
	var tr = int(0.339*float64(r) + 0.768*float64(g) + 0.189*float64(b))
	var tg = int(0.349*float64(r) + 0.686*float64(g) + 0.168*float64(b))
	var tb = int(0.272*float64(r) + 0.534*float64(g) + 0.131*float64(b))

	if tr > 255 {
		tr = 255
	}
	if tg > 255 {
		tg = 255
	}
	if tb > 255 {
		tb = 255
	}

	return Color{tr, tg, tb, alpha}
}

// NegativeFiler
// Req. 4.3
// This Function takes the rgb values of the current location and converts
// them into negative values
func NegativeFilter(r, g, b, alpha int) Color {
	r = 255 - r
	g = 255 - g
	b = 255 - b
	return Color{r, g, b, alpha}
}

func drawLines(im *image.RGBA, c Color, lines []Scanline) {
	const m = 0xffff
	sr, sg, sb, sa := c.NRGBA().RGBA()
	for _, line := range lines {
		ma := line.Alpha
		a := (m - sa*ma/m) * 0x101
		i := im.PixOffset(line.X1, line.Y)
		for x := line.X1; x <= line.X2; x++ {
			dr := uint32(im.Pix[i+0])
			dg := uint32(im.Pix[i+1])
			db := uint32(im.Pix[i+2])
			da := uint32(im.Pix[i+3])
			im.Pix[i+0] = uint8((dr*a + sr*ma) / m >> 8)
			im.Pix[i+1] = uint8((dg*a + sg*ma) / m >> 8)
			im.Pix[i+2] = uint8((db*a + sb*ma) / m >> 8)
			im.Pix[i+3] = uint8((da*a + sa*ma) / m >> 8)
			i += 4
		}
	}
}

func differenceFull(a, b *image.RGBA) float64 {
	size := a.Bounds().Size()
	w, h := size.X, size.Y
	var total uint64
	for y := 0; y < h; y++ {
		i := a.PixOffset(0, y)
		for x := 0; x < w; x++ {
			ar := int(a.Pix[i])
			ag := int(a.Pix[i+1])
			ab := int(a.Pix[i+2])
			aa := int(a.Pix[i+3])
			br := int(b.Pix[i])
			bg := int(b.Pix[i+1])
			bb := int(b.Pix[i+2])
			ba := int(b.Pix[i+3])
			i += 4
			dr := ar - br
			dg := ag - bg
			db := ab - bb
			da := aa - ba
			total += uint64(dr*dr + dg*dg + db*db + da*da)
		}
	}
	return math.Sqrt(float64(total)/float64(w*h*4)) / 255
}

func differencePartial(target, before, after *image.RGBA, score float64, lines []Scanline) float64 {
	size := target.Bounds().Size()
	w, h := size.X, size.Y
	total := uint64(math.Pow(score*255, 2) * float64(w*h*4))
	for _, line := range lines {
		i := target.PixOffset(line.X1, line.Y)
		for x := line.X1; x <= line.X2; x++ {
			tr := int(target.Pix[i])
			tg := int(target.Pix[i+1])
			tb := int(target.Pix[i+2])
			ta := int(target.Pix[i+3])
			br := int(before.Pix[i])
			bg := int(before.Pix[i+1])
			bb := int(before.Pix[i+2])
			ba := int(before.Pix[i+3])
			ar := int(after.Pix[i])
			ag := int(after.Pix[i+1])
			ab := int(after.Pix[i+2])
			aa := int(after.Pix[i+3])
			i += 4
			dr1 := tr - br
			dg1 := tg - bg
			db1 := tb - bb
			da1 := ta - ba
			dr2 := tr - ar
			dg2 := tg - ag
			db2 := tb - ab
			da2 := ta - aa
			total -= uint64(dr1*dr1 + dg1*dg1 + db1*db1 + da1*da1)
			total += uint64(dr2*dr2 + dg2*dg2 + db2*db2 + da2*da2)
		}
	}
	return math.Sqrt(float64(total)/float64(w*h*4)) / 255
}
