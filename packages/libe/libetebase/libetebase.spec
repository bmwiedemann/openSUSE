#
# spec file for package libetebase
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


%define sover 0
Name:           libetebase
Release:        0
Summary:        A C library for Etebase
License:        (Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 WITH LLVM-exception AND CC-BY-SA-4.0 AND MPL-2.0 AND CC0-1.0 AND (Apache-2.0 OR BSL-1.0) AND (GPL-2.0-or-later OR MIT) AND GPL-2.0-or-later WITH Autoconf-exception-3.0 AND GPL-2.0-or-later WITH Libtool-exception
URL:            https://github.com/etesync/libetebase
#               This will be set by osc services, that will run after this.
Version:        0.5.5
Source0:        libetebase-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
# See https://github.com/etesync/libetebase/issues/14
Patch0:         configurable-libdir-support.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  extra-cmake-modules
BuildRequires:  libopenssl-devel
BuildRequires:  libsodium-devel
BuildRequires:  pkgconfig

%description
Etebase is an end-to-end encrypted backend as a service. Think Firebase, but encrypted in a way that only your users can access their data.

Etebase makes it easy to build end-to-end encrypted applications by taking care of the encryption and its related challenges. It is fully open-source (clients and server) so anyone can review, audit or contribute to its development!

%prep
%autosetup -a1 -n libetebase-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%make_build PREFIX=%{_prefix} LIB=%{_lib} pkgconfig
%{cargo_build}

%package -n libetebase%{sover}
Summary:        A C shared library for Etebase

%description -n libetebase%{sover}
Etebase is an end-to-end encrypted backend as a service. Think Firebase, but encrypted in a way that only your users can access their data.

Etebase makes it easy to build end-to-end encrypted applications by taking care of the encryption and its related challenges. It is fully open-source (clients and server) so anyone can review, audit or contribute to its development!

%install
# Install manually. libetebase's install directive does not use lib64 etc paths automatically
# Need to fix .so naming manually
# see https://github.com/etesync/libetebase/issues/4
install -Dm755 target/release/libetebase.so -T %{buildroot}%{_libdir}/libetebase.so.%{sover}
ln -s libetebase.so.%{sover} %{buildroot}%{_libdir}/libetebase.so

install -Dm644 EtebaseConfig.cmake -t %{buildroot}%{_libdir}/cmake/Etebase/
install -Dm644 target/etebase.pc -t %{buildroot}%{_libdir}/pkgconfig/
install -Dm644 target/etebase.h -t %{buildroot}%{_includedir}/etebase/

# libetebase has no tests yet, not running check and cargo_test
%ldconfig_scriptlets -n libetebase%{sover}

%files -n libetebase%{sover}
%{_libdir}/libetebase.so.%{sover}

%package -n libetebase-devel
Summary:        Development package for the etesync shared library
Requires:       libetebase%{sover} = %{version}-%{release}

%description -n libetebase-devel
A C and Rust client library for EteSync. Development package.

%files -n libetebase-devel
%{_libdir}/libetebase.so
%dir %{_libdir}/cmake
%{_libdir}/pkgconfig/etebase.pc
%dir %{_libdir}/cmake/Etebase
%{_libdir}/cmake/Etebase/EtebaseConfig.cmake
%dir %{_includedir}/etebase
%{_includedir}/etebase/etebase.h

%changelog
