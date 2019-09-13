#
# spec file for package fstrcmp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 0

Name:           fstrcmp
Version:        0.7.D001
Release:        0
Summary:        Fuzzy string compare
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            http://fstrcmp.sourceforge.net
Source:         fstrcmp-0.7.D001.tar.gz
BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The fstrcmp package provides a library which may be used to make fuzzy
comparisons of strings and byte arrays.  It also provides simple
commands for use in shell scripts.

%package devel
Summary:        Development files for lib%{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%package     -n lib%{name}%{sover}
Summary:        Fuzzy string compare
Group:          System/Libraries

%description -n lib%{name}%{sover}
A library for fuzzy comparisons of strings and byte arrays.

%prep
%autosetup -p1

%build
autoreconf -fi
export GROFF=$(type -P groff)
export MANPATH_PROG=$(type -P true)
export REFER=$(type -P true)
export SOELIM=$(type -P soelim)
%configure \
	--disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.a" -print -delete
find %{buildroot} -name "*.la" -print -delete
find %{buildroot} -name "*.pdf" -print -delete

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%{_bindir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man?/*

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
