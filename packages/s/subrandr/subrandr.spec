#
# spec file for package subrandr
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


%define sover 0
%define libname libsubrandr

Name:           subrandr
Version:        1.1.0
Release:        0
Summary:        Library to render non-ASS subtitles
Group:          Development/Libraries/Rust
License:        MPL-2.0
URL:            https://github.com/afishhh/subrandr
Source0:        subrandr-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-c
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)

%description
Subtitle rendering library for rendering non-ASS subtitles

%package devel
Summary:        Development libraries for %name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{sover} = %{version}

%description devel
The %{name}-devel package contains C header files for
developing applications that use %{name}.

%package     -n %{libname}%{sover}
Summary:        Library to render non-ASS subtitles
Group:          System/Libraries

%description -n %{libname}%{sover}
Subtitle rendering library for rendering non-ASS subtitles


%prep
%autosetup -a1

%build
RUSTFLAGS=' -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2 -C strip=none' \
cargo run --package xtask -- build

%install
RUSTFLAGS=' -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2 -C strip=none' \
cargo run --package xtask -- install \
    --libdir=lib64 \
    --prefix=%{_prefix} \
    --destdir=%{buildroot}%{_prefix}

%post   -n %{libname}%{sover} -p /sbin/ldconfig
%postun -n %{libname}%{sover} -p /sbin/ldconfig

%files -n %{libname}%{sover}
%license LICENSE
%doc README.md
%{_libdir}/%{libname}.so.*

%files devel
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/subrandr.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/subrandr.h
%{_includedir}/%{name}/logging.h

%changelog
