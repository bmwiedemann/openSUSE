#
# spec file for package qoi
#
# Copyright (c) 2025 mantarimay
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           qoi
Version:        0~20250212
Release:        0
Summary:        Quite OK Image Format
License:        MIT
URL:            https://github.com/phoboslab/qoi
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  stb-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(libpng)

%description
QOI is fast. It losslessly compresses images to a similar size of PNG,
while offering 20x-50x faster encoding and 3x-4x faster decoding.

QOI is simple. The reference en-/decoder fits in about 300 lines of C.
The file format specification is a single page PDF.

%package tools	
Summary:        A tools for QOI

%description tools
A tools for fast, lossless image compression using the "Quite OK Image
Format".

%package devel
Summary:        Development header for The “Quite OK Image Format”
BuildArch:      noarch

%description devel
Development header for The “Quite OK Image Format”.

%prep
%autosetup 

%build
%make_build CFLAGS="-I /usr/include/stb/"

%install
install -Dpm755 qoi{bench,conv} -t %{buildroot}%{_bindir}
install -Dpm644 qoi.h -t %{buildroot}%{_includedir}

%files tools
%license LICENSE
%doc README.md
%{_bindir}/qoibench
%{_bindir}/qoiconv

%files devel
%license LICENSE
%{_includedir}/%{name}.h

%changelog
