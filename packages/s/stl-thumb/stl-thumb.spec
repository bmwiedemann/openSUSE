#
# spec file for package stl-thumb
#
# Copyright (c) 2022 SUSE LLC
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           stl-thumb
Version:        0.5.0~0
Release:        0
Summary:        Stl-thumb is a fast lightweight thumbnail generator for STL files.
License:        MIT
URL:            https://github.com/unlimitedbacon/stl-thumb
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  rust-packaging

%description
Stl-thumb is a fast lightweight thumbnail generator for STL files.
It can show previews for STL files in your file manager on Linux and Windows.
It is written in Rust and uses OpenGL.

%package devel
Summary:        Files needed for stl-thumb development
Group:          Development/Languages/C and C++
Requires:       libstl-thumb = %{version}

%description devel
Files needed to develop applications for the stl-thumb.

%package -n libstl-thumb
Summary:        stl-thumb Libraries
Group:          System/Libraries

%description -n libstl-thumb
stl-thumb Libraries

%prep
%autosetup -a1 -p1
cp %{SOURCE2} .cargo/config

%build
#RUSTFLAGS=%{rustflags} cargo build --release
%{cargo_build}

%install
# RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .
install --mode 0755 -D target/release/stl-thumb       %{buildroot}%{_bindir}/stl-thumb
install --mode 0755 -D target/release/libstl_thumb.so %{buildroot}%{_libdir}/libstl_thumb.so
install --mode 0644 -D target/release/libstl_thumb.a  %{buildroot}%{_libdir}/libstl_thumb.a
install --mode 0644 -D stl-thumb.thumbnailer          %{buildroot}%{_datadir}/thumbnailers/stl-thumb.thumbnailer
install --mode 0644 -D libstl_thumb.h                 %{buildroot}%{_includedir}/libstl_thumb.h

%files
%{_bindir}/stl-thumb
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/stl-thumb.thumbnailer

%files -n libstl-thumb
%{_libdir}/libstl_thumb.so

%files devel
%{_libdir}/libstl_thumb.a
%{_includedir}/libstl_thumb.h

%changelog
