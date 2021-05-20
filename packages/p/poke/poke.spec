#
# spec file for package poke
#
# Copyright (c) 2021 SUSE LLC
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


%define sover   0
Name:           poke
Version:        1.2
Release:        0
Summary:        An interactive, extensible editor for binary data
License:        GPL-3.0-only
URL:            https://www.gnu.org/software/poke/
Source:         https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
BuildRequires:  autoconf >= 2.62
BuildRequires:  automake >= 1.16
BuildRequires:  bison >= 3.6
BuildRequires:  dejagnu
BuildRequires:  flex >= 2.5.37
BuildRequires:  gawk
BuildRequires:  gettext >= 0.18.2
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  lua53
BuildRequires:  makeinfo >= 6.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bdw-gc)
# /SECTION
%if 0%{?suse_version} > 1500
BuildRequires:  libtextstyle-devel
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif

%description
GNU poke is an interactive, extensible editor for binary data. Not limited to
editing basic entities such as bits and bytes, it provides a full-fledged
procedural, interactive programming language designed to describe data
structures and to operate on them.

%package devel
Summary:        Devel package for %{name}
Requires:       lib%{name}%{sover} = %{version}

%description devel
Development package for %{name}.

%package -n lib%{name}%{sover}
Summary:        Support library for %{name}

%description -n lib%{name}%{sover}
Contains support library for %{name}.

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/%{name}
%{_bindir}/pk-elfextractor
%{_bindir}/pk-strings
%{_datadir}/%{name}
%{_datadir}/emacs/site-lisp/*
%{_infodir}/%{name}.info%{?ext_info}
%{_infodir}/%{name}.info-1%{?ext_info}
%{_infodir}/%{name}.info-2%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files devel
%{_includedir}/libpoke.h
%{_libdir}/lib%{name}.so

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%changelog
