#
# spec file for package m17n-db
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           m17n-db
Version:        1.7.0
Release:        0
Summary:        Database Needed by the m17n Library m17n-lib
License:        GPL-2.0+ and LGPL-2.1+ and SUSE-Public-Domain and MIT
Group:          System/I18n/Japanese
Url:            http://www.m17n.org/m17n-lib/
Source0:        http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Patch0:         bnc429430-ar-kbd.patch
BuildRequires:  glibc-i18ndata
BuildRequires:  pkg-config
Recommends:     %{name}-lang
Provides:		m17n-contrib > 1.1.14
Obsoletes:		m17n-contrib <= 1.1.14
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Database that is needed by the m17n library "m17n-lib".

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_sm_mflags}

%install
%makeinstall

%find_lang m17n-db

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README ChangeLog
%dir %{_datadir}/m17n/
%{_datadir}/m17n/*
%{_bindir}/*
%{_datadir}/pkgconfig/m17n-db.pc

%files lang -f m17n-db.lang

%changelog
