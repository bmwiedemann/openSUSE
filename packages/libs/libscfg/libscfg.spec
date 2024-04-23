#
# spec file for package libscfg
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

%define libname libscfg1

Name:           libscfg
Version:        0.1.1
Release:        0
Summary:        A C library for a simple configuration file format
Group:          Development/Libraries/C and C++
License:        MIT
URL:            https://git.sr.ht/~emersion/libscfg
Source0:        %{url}/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/refs/download/v%{version}/%{name}-%{version}.tar.gz.sig
# https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM smolsheep@opensuse.org -- Set sover and library version. Commit 3bdba8c2
Patch1:         set-soversion.patch
BuildRequires:  gcc
BuildRequires:  meson

%description
This is a C library for a simple configuration file format (scfg).

%package -n %{libname}
Summary:        A C library for a simple configuration file format
Group:          System/Libraries

%description -n %{libname}
This is a C library for a simple configuration file format (scfg).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description devel
This package provides the header file and the pkg-config metadata file.

%prep
%autosetup -p 1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libscfg.so.1
%{_libdir}/libscfg.so.0.1.1
 
%files devel
%{_includedir}/scfg.h
%{_libdir}/libscfg.so
%{_libdir}/pkgconfig/scfg.pc

%changelog
