#
# spec file for package enchant-1
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


%define _name   enchant
Name:           enchant-1
Version:        1.6.1
Release:        0
Summary:        Generic Spell Checking Library
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
URL:            https://abiword.github.io/enchant/
Source:         https://github.com/AbiWord/enchant/releases/download/enchant-1-6-1/enchant-1.6.1.tar.gz
# PATCH-FIX-UPSTREAM enchant-hunspell-1.4.0.patch dimstar@opensuse.org -- Fix build against hunspell 1.4.0, where WORDMAXLEN is no longer exported
Patch0:         enchant-hunspell-1.4.0.patch
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  hunspell-devel
BuildRequires:  libvoikko-devel

%description
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package tools
Summary:        Generic Spell Checking Library - Command Line Tools
Group:          Productivity/Text/Spell

%description tools
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

This package provides command-line tools to interact with enchant.

%package data
Summary:        Data files for libenchant
Group:          Productivity/Text/Spell
Conflicts:      enchant-data
# enchant up to version 1.6.1 was not packaged properly according the SLPP
Conflicts:      libenchant1 < 1.6.1
Provides:       libenchant1:%{_datadir}/enchant/enchant.ordering
# Enchant data (and thus the configuration) is provided by all versions of enchant
# Newest one will be installed
Provides:       enchant-data = %{version}

%description data
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

This package provides data/configuration files for libenchant.

%package -n enchant-1-backends
Summary:        ISpell/Myspell backends for libenchant
# enchant up to version 1.6.1 was not packaged properly according the SLPP
Group:          Productivity/Text/Spell
Conflicts:      libenchant1 < 1.6.1
Provides:       enchant-1-backend
Provides:       libenchant1:%{_libdir}/enchant/libenchant_ispell.so

%description -n enchant-1-backends
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

This package provides the ispell and myspell backends.

%package -n enchant-1-backend-voikko
Summary:        Generic Spell Checking Library - Voikko Plugin
Group:          Productivity/Text/Spell
Provides:       enchant-1-backend
Requires:       enchant-1-backends
Provides:       locale(%{name}:fi)
# Package was renamed from enchant-voikko to enchant-1-backend-voikke with version 1.6.1
Obsoletes:      enchant-voikko < 1.6.1

%description -n enchant-1-backend-voikko
Voikko plugin (Finnish) for enchant, a library providing an efficient
extensible abstraction for dealing with different spell checking
libraries.

%package -n enchant-1-backend-zemberek
Summary:        Generic Spell Checking Library - Zemberek Plugin
# Only zemberek-server over D-Bus is supported. Server must be installed locally:
Group:          Productivity/Text/Spell
Recommends:     zemberek-server
Supplements:    packageand(libenchant1:zemberek-server)
Provides:       enchant-1-backend
Provides:       locale(%{name}:az)
Provides:       locale(%{name}:tk)
Provides:       locale(%{name}:tr)
Provides:       locale(%{name}:tt)
# Package was renamed from enchant-voikko to enchant-1-backend-voikke with version 1.6.1
Obsoletes:      enchant-zemberek < 1.6.1

%description -n enchant-1-backend-zemberek
Zemberek plugin (Azeri, Turkmen, Turkish, Tatar) for enchant, a library
providing an efficient extensible abstraction for dealing with
different spell checking libraries.

%package -n libenchant1
Summary:        Generic Spell Checking Library
Group:          System/Libraries
Requires:       enchant-1-backend
Recommends:     enchant-1-backends
Provides:       enchant = %{version}
Obsoletes:      enchant < %{version}

%description -n libenchant1
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libenchant1 = %{version}
Requires:       libstdc++-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build

# Work-around boo#1221684
%global optflags %{optflags} -fpermissive

%configure --with-pic \
    --disable-static \
    --enable-zemberek \
    --with-myspell-dir=%{_datadir}/myspell

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libenchant1 -p /sbin/ldconfig
%postun -n libenchant1 -p /sbin/ldconfig

%files tools
%{_bindir}/enchant
%{_bindir}/enchant-lsmod
%{_mandir}/man1/enchant.1%{?ext_man}

%files data
%dir %{_datadir}/enchant
%{_datadir}/enchant/enchant.ordering

%files -n libenchant1
# AUTHORS == MAINTAINERS in 1.3.0, TODO is 1 byte, BUGS has nothing interesting
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files -n enchant-1-backends
%dir %{_libdir}/enchant
%{_libdir}/enchant/libenchant_ispell.so
%{_libdir}/enchant/libenchant_myspell.so

%files -n enchant-1-backend-voikko
%dir %{_libdir}/enchant
%{_libdir}/enchant/libenchant_voikko.so

%files -n enchant-1-backend-zemberek
%dir %{_libdir}/enchant
%{_libdir}/enchant/libenchant_zemberek.so

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
