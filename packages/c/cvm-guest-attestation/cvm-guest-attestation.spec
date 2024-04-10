#
# spec file for package cvm-guest-attestation
#
# Copyright (c) 2024 SUSE LLC
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


%define somajor 1
%define libname libazguestattestation%somajor

Name:           cvm-guest-attestation
Version:        20240316.b613bcd
Release:        0
Summary:        Confidential computing cvm guest attestation
License:        MIT
URL:            https://github.com/Azure/confidential-computing-cvm-guest-attestation
Group:          Productivity/Security
Source0:        %name-%version.tar.xz
Patch0:         %name.patch
Requires:       %libname = %version-%release
ExclusiveArch:  x86_64
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-tcti-device)

%description
Confidential computing cvm guest attestation

%package -n %libname
Summary:        Confidential computing cvm guest attestation library
Group:          System/Libraries

%description -n %libname
Confidential computing cvm guest attestation library

%package devel
Summary:        Confidential computing cvm guest attestation devel files
Group:          Development/Libraries/C and C++
Requires:       %libname = %version-%release

%description devel
Confidential computing cvm guest attestation devel files

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %libname

%files
%doc *.md *.pdf *.png
%license LICENSE
%_bindir/AttestationClient

%files -n %libname
%license LICENSE
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*

%changelog
