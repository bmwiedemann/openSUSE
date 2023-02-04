#
# spec file for package pngquant
#
# Copyright (c) 2023 SUSE LLC
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


Name:           pngquant
Version:        2.18.0
Release:        0
Summary:        Tool for lossy compression of PNG images
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://pngquant.org/
Source:         https://github.com/kornelski/pngquant/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(imagequant) >= %{version}
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
pngquant is a command-line utility and a library for lossy
compression of PNG images.

The conversion reduces file sizes by converting images to 1/2/4/8-bit
paletted PNG format with alpha channel (often 60-80%% smaller than
24/32-bit PNG files). Generated images are compatible with all modern
web browsers, and have better fallback in IE6 than 24-bit PNGs.

%prep
%setup -q

%build
# not autoconf
./configure \
	--prefix=%{_prefix} \
%ifarch x86_64
	--enable-sse \
%else
	--disable-sse \
%endif
	--extra-cflags='%{optflags}' \
	--with-libimagequant=%{_libdir} \
	--with-openmp
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
