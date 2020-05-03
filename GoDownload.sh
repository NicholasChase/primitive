#!/bin/sh
#This program is meant to download Go for Linux users to set up the go 
#environment needed to run primitive on their home systems
wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
export PATH=$PATH:/usr/local/go/bin

