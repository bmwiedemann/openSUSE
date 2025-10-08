#
# spec file for package pngquant
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        3.0.3
Release:        0
Summary:        Tool for lossy compression of PNG images
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://pngquant.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
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
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -Dm0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license COPYRIGHT
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
