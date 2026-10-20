#
# spec file for package libimagequant
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover   0_4
%define libname %{name}%{sover}
Name:           libimagequant
Version:        4.4.1
Release:        0
Summary:        Palette quantization library
License:        GPL-3.0-or-later
URL:            https://pngquant.org/lib/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-c
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.70

%description
C library for conversion of RGBA images to 8-bit indexed-color
(palette) images.

%package -n %{libname}
Summary:        Palette quantization library

%description -n %{libname}
C library for conversion of RGBA images to 8-bit indexed-color
(palette) images.

%package devel
Summary:        Development files for libimagequant
Requires:       %{libname} = %{version}

%description devel
C library for conversion of RGBA images to 8-bit indexed-color
(palette) images.

%prep
%autosetup -p1 -a1

%build
export RUSTFLAGS="%{build_rustflags}"
cd imagequant-sys
CFLAGS="%{optflags}" cargo cbuild --release --offline

%install
cd imagequant-sys
cargo cinstall --release --offline \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}
# no static library in the shlib policy packages
rm -f %{buildroot}%{_libdir}/libimagequant.a

%check
export RUSTFLAGS="%{build_rustflags}"
cargo test --release --offline

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%doc README.md CHANGELOG
%license COPYRIGHT
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/imagequant.pc

%changelog
