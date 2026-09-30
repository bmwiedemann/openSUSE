#
# spec file for package nv-attestation
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

Name:           nv-attestation
Version:        2026.06.09~git0.9d12801
Release:        0
Summary:        collect device attestation evidence for NVIDIA hardware
License:        Apache-2.0
URL:            https://github.com/NVIDIA/attestation-sdk
ExclusiveArch:  x86_64
Source0:        %name-%version.tar.xz
Source1:        jwt-cpp-e71e0c2d584baff06925bbb3aad683f677e4d498.tar.xz
Source2:        corrosion-6be991bb34c348dfb8344be22f3606288ea5c7fd.tar.xz
Source3:        regorus-c7bf460bc160c96e38048296e5708943d2e43909.tar.xz
Source4:        vendor.tar.xz
Source5:        CLI11-bfffd37e1f804ca4fae1caae106935791696b6a9.tar.xz
Patch0:         %name.patch
BuildRequires:  cargo
BuildRequires:  cmake >= 3.28
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(xmlsec1-openssl)
BuildRequires:  rust
Requires:       libnvat1 = %version-%release
%description
command‑line tool built on the NVIDIA Attestation SDK to collect device
attestation evidence and verify integrity for NVIDIA GPUs and Switches.

%package -n libnvat1
Summary:        core library for %name
%description -n libnvat1
libnvat (or “NV Attest”) is an SDK that supports device attestation for NVIDIA products such as GPUs and the NVLink Switch.

%package devel
Summary:        Development files and documentation for %{name}
Requires:       libnvat1 = %version-%release
%description devel
This package contains development files and documentation
for %{name}. Install this package if you want to develop
plugins for %{name}. 

%prep
%autosetup -p1 -n %name-%version

%build
mkdir jwt-cpp
tar --extract --auto-compress --strip-components=1 --directory=jwt-cpp --file=%{SOURCE1}
jwt_cpp=$(readlink -f jwt-cpp)
mkdir corrosion
tar --extract --auto-compress --strip-components=1 --directory=corrosion --file=%{SOURCE2}
corrosion=$(readlink -f corrosion)
mkdir regorus
tar --extract --auto-compress --strip-components=1 --directory=regorus --file=%{SOURCE3}
tar --extract --auto-compress --strip-components=0 --directory=regorus --file=%{SOURCE4}
regorus=$(readlink -f regorus)
sed -i~ '
s|^\[\[test\]\]|[[foo]]|
' regorus/Cargo.toml
diff -u "$_"~ "$_" && exit 123
mkdir CLI11
tar --extract --auto-compress --strip-components=1 --directory=CLI11 --file=%{SOURCE5}
CLI11=$(readlink -f CLI11)
%cmake \
	-DUSE_SYSTEM_DEPS=ON \
	-DCLI11_FUZZ_TARGET=OFF \
	-DFETCHCONTENT_SOURCE_DIR_JWT-CPP:PATH="${jwt_cpp}" \
	-DFETCHCONTENT_SOURCE_DIR_CORROSION:PATH="${corrosion}" \
	-DFETCHCONTENT_SOURCE_DIR_REGORUS:PATH="${regorus}" \
	-DFETCHCONTENT_SOURCE_DIR_CLI11:PATH="${CLI11}" \
	%nil
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libnvat1

%files
%_bindir/*

%files -n libnvat1
%license LICENSE
%_libdir/*.so.1*

%files devel
%_libdir/*.so
%_includedir/*
%_datadir/cmake

%changelog

