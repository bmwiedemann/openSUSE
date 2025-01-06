#
# spec file for package m17n-db
#
# Copyright (c) 2025 SUSE LLC
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


Name:           m17n-db
Version:        1.8.9
Release:        0
Summary:        Database Needed by the m17n Library m17n-lib
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Public-Domain AND MIT
Group:          System/I18n/Japanese
URL:            https://www.m17n.org/m17n-lib/
Source0:        http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Patch0:         bnc429430-ar-kbd.patch

BuildRequires:  glibc-i18ndata
BuildRequires:  pkgconfig
Provides:       m17n-contrib > 1.1.14
Obsoletes:      m17n-contrib <= 1.1.14
BuildArch:      noarch

%description
Database that is needed by the m17n library "m17n-lib".

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang m17n-db

%files
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%dir %{_datadir}/m17n/
%{_datadir}/m17n/*
%{_bindir}/*
%{_datadir}/pkgconfig/m17n-db.pc

%files lang -f m17n-db.lang

%changelog
