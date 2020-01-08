#
# spec file for package mingw64-pkgconf
#
# Copyright (c) 2019 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define pkgconfig_ver 0.29.2
# For obsoleting pkgconfig, bump the ver to a number higher than latest version
%define pkgconfig_obsver %{pkgconfig_ver}+1

Name:           mingw64-pkgconf
Version:        1.6.3
Release:        0
Summary:        Package compiler and linker metadata toolkit
License:        ISC
Group:          Development/Tools/Building
URL:            http://pkgconf.org/
Source0:        https://distfiles.dereferenced.org/pkgconf/pkgconf-%{version}.tar.xz
#!BuildIgnore: post-build-checks
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-filesystem
Conflicts:      mingw64-pkg-config < %{pkgconfig_obsver}
Obsoletes:      mingw64-pkg-config < %{pkgconfig_obsver}
Provides:       mingw64-pkg-config = %{pkgconfig_obsver}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw64_package_header_debug
BuildArch:      noarch

%description
pkgconf is a program which helps to configure compiler and linker flags
for development frameworks. It is similar to pkg-config from freedesktop.org
and handles .pc files in a similar manner as pkg-config.

%_mingw64_debug_package

%prep
%setup -q -n pkgconf-%{version}

%build
%{_mingw64_configure} \
  --disable-static

make %{?_smp_mflags} || make

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# compat
ln -s pkgconf.exe %{buildroot}%{_mingw64_bindir}/pkg-config.exe

%files
%defattr(-,root,root)
%{_mingw64_bindir}/pkgconf.exe
%{_mingw64_bindir}/pkg-config.exe
%{_mingw64_bindir}/libpkgconf-3.dll
%{_mingw64_libdir}/libpkgconf.dll.a
%{_mingw64_includedir}/pkgconf
%{_mingw64_libdir}/pkgconfig
%{_mingw64_mandir}/man?/*
%{_mingw64_datadir}/aclocal/pkg.m4
%{_mingw64_docdir}

%changelog
