#
# spec file for package fcft
#
# Copyright (c) 2025 SUSE LLC
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


%define libname libfcft4
Name:           fcft
Version:        3.1.10
Release:        0
Summary:        A library for font loading and glyph rasterization using FreeType/pixman
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://codeberg.org/dnkl/fcft
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xb19964fbba09664cc81027ed5bbd4992c116573f
Source2:        %{name}.keyring
%if 0%{?sle_version} >= 150400
BuildRequires:  gcc11
BuildRequires:  python3-dataclasses
%endif
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scdoc
BuildRequires:  cmake(NanoSVG)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2) >= 2.12
BuildRequires:  pkgconfig(harfbuzz) >= 5.2
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1

%description
fcft is a font loading and glyph rasterization library built on-top
of FontConfig, FreeType2 and pixman.

%package -n %{libname}
Summary:        A library for font loading and glyph rasterization using FreeType/pixman
Group:          System/Libraries

%description -n %{libname}
fcft is a font loading and glyph rasterization library built on-top
of FontConfig, FreeType2 and pixman.

%package devel
Summary:        Header files for fcft,  a font loading and rasterization library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
fcft is a font loading and glyph rasterization library built on-top
of FontConfig, FreeType2 and pixman.

%prep
%autosetup

%build
%if 0%{?sle_version} >= 150400
export CC=gcc-11
%endif
%meson \
	-Ddocs=enabled \
	-Dexamples=false \
	-Dgrapheme-shaping=enabled \
	-Drun-shaping=enabled \
	-Dsvg-backend=nanosvg \
	-Dsystem-nanosvg=enabled \
	-Dtest-text-shaping=false
%meson_build

%install
%meson_install
rm -r %{buildroot}/%{_datadir}/doc/%{name}/

%check
%meson_test

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/libfcft.so.*

%files devel
%license LICENSE
%doc README.md CHANGELOG.md
%{_includedir}/%{name}/
%{_libdir}/libfcft.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/fcft_*.3.gz

%changelog
