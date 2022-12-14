#
# spec file for package giflib
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


%define lname   libgif7
Name:           giflib
Version:        5.2.1
Release:        0
Summary:        A Library for Working with GIF Images
License:        MIT
URL:            https://giflib.sourceforge.net/
Source:         https://downloads.sf.net/giflib/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         PIE.patch
Patch2:         reproducible.patch
BuildRequires:  libtool >= 2

%description
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%package -n %{lname}
Summary:        A Library for Working with GIF Images

%description -n %{lname}
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%package progs
Summary:        Tools for Working with the GIF Library
Provides:       ungif = %{version}
Obsoletes:      ungif < %{version}

%description progs
A tool for converting GIFs to various formats.

%package devel
Summary:        Library for Working with GIF Images - Files Mandatory for Development
Requires:       %{lname} = %{version}

%description devel
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install PREFIX="%{_prefix}" LIBDIR="%{_libdir}"
find %{buildroot} -type f -name "*.la" -delete -print
find doc -name "Makefile*" -print -delete

# Drop static library
rm -f %{buildroot}%{_libdir}/libgif.a

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/gif_lib.h
%{_libdir}/lib*.so

%files progs
%license COPYING
%doc NEWS README doc
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
