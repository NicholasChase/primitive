package primitive

import "testing"

func TestApplyFilter(t *testing.T) {
	filter := 0
	r := 12
	g := 255
	b := 61
	alpha := 1

	color := applyFilter(filter, r, g, b, alpha)
	expectedColor := Color{r, g, b, alpha}

	if color != expectedColor {
		t.Errorf("The computed color was incorrect, got: r=%d g=%d b=%d, want: r=%d g=%d b=%d", color.R, color.G, color.B, expectedColor.R, expectedColor.G, expectedColor.B)
	}

	filter = 1
	color = applyFilter(filter, r, g, b, alpha)
	expectedColor = GrayScaleFilter(r, g, b, alpha)
	if color != expectedColor {
		t.Errorf("The computed color was incorrect, got: r=%d g=%d b=%d, want: r=%d g=%d b=%d", color.R, color.G, color.B, expectedColor.R, expectedColor.G, expectedColor.B)
	}

	filter = 2
	color = applyFilter(filter, r, g, b, alpha)
	expectedColor = SepiaFilter(r, g, b, alpha)
	if color != expectedColor {
		t.Errorf("The computed color was incorrect, got: r=%d g=%d b=%d, want: r=%d g=%d b=%d", color.R, color.G, color.B, expectedColor.R, expectedColor.G, expectedColor.B)
	}

	filter = 3
	color = applyFilter(filter, r, g, b, alpha)
	expectedColor = NegativeFilter(r, g, b, alpha)
	if color != expectedColor {
		t.Errorf("The computed color was incorrect, got: r=%d g=%d b=%d, want: r=%d g=%d b=%d", color.R, color.G, color.B, expectedColor.R, expectedColor.G, expectedColor.B)
	}
}

func TestSepiaFilter(t *testing.T) {
	color := SepiaFilter(12, 255, 61, 1)
	if color.R != 211 || color.G != 189 || color.B != 147 {
		t.Errorf("The computed color was incorrect, got: r=%d g=%d b=%d, want: r=%d g=%d b=%d", color.R, color.G, color.B, 211, 189, 147)
	}
}

func TestNegativeFilter(t *testing.T) {
	color := NegativeFilter(12, 255, 61, 1)
	if color.R != 243 || color.G != 0 || color.B != 194 {
		t.Errorf("The computed color was incorrect, got: r=%d g=%d b=%d, want: r=%d g=%d b=%d", color.R, color.G, color.B, 211, 189, 147)
	}
}
