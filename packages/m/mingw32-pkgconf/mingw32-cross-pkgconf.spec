#
# spec file for package mingw32-cross-pkg-config
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           mingw32-cross-pkgconf
Version:        1.6.3
Release:        0
Summary:        Package compiler and linker metadata toolkit
License:        ISC
Group:          Development/Tools/Building
URL:            http://pkgconf.org/
Source0:        https://distfiles.dereferenced.org/pkgconf/pkgconf-%{version}.tar.xz
#!BuildIgnore:  mingw32-cross-binutils-utils
#!BuildIgnore:  mingw32-cross-pkgconf-utils
BuildRequires:  mingw32-filesystem
BuildRequires:  pkgconf
# NB: This must be left in.
# requires currently disabled debuginfo in project settings
Requires:       mingw32-filesystem
# Because we will not install the pkg.m4 package
Requires:       pkg-config
# This package is used by mingw32-filesystem to
# avoid cyclic dependencies (boo#1204985)
Provides:       mingw32-cross-pkgconf-utils
# compat. May move to separate package like native version but I'm lazy
Conflicts:      mingw32-cross-pkg-config < %{pkgconfig_obsver}
Obsoletes:      mingw32-cross-pkg-config < %{pkgconfig_obsver}
Provides:       mingw32-cross-pkg-config = %{pkgconfig_obsver}

%description
pkgconf is a program which helps to configure compiler and linker flags
for development frameworks. It is similar to pkg-config from freedesktop.org
and handles .pc files in a similar manner as pkg-config.

%prep
%setup -q -n pkgconf-%{version}

%build
CFLAGS="%{optflags}" \
./configure \
  --prefix=%{_prefix} \
  --program-prefix=%{_mingw32_target}- \
  --disable-shared \
  --with-pkg-config-dir=%{_mingw32_libdir}/pkgconfig:%{_mingw32_datadir}/pkgconfig

make %{?_smp_mflags} || make

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# compat
ln -s %{_bindir}/%{_mingw32_target}-pkgconf %{buildroot}%{_bindir}/%{_mingw32_target}-pkg-config

# These files conflict with ordinary pkgconf
rm -rf %{buildroot}%{_datadir}/aclocal
rm -rf %{buildroot}%{_datadir}/doc
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_prefix}/lib
# not needed
rm -rf %{buildroot}%{_mandir}/man[57]

%files
%defattr(-,root,root)
%{_bindir}/%{_mingw32_target}-pkgconf
%{_bindir}/%{_mingw32_target}-pkg-config
%{_mandir}/man?/%{_mingw32_target}-*

%changelog
