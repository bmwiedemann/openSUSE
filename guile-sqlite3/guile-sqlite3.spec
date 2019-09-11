#
# spec file for package guile-sqlite3
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           guile-sqlite3
Version:        0.1.0
Release:        0
Summary:        SQLite3 database access from Guile
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/Other
Url:            https://notabug.org/guile-sqlite3/guile-sqlite3
Source0:        https://notabug.org/guile-sqlite3/%{name}/archive/v%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  guile-devel >= 2.0.10
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sqlite3)
Requires:       guile >= 2.0.10
Requires:       sqlite3-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides Guile bindings to the SQLite3 database system.

%prep
%setup -q -n %{name}

%build
autoreconf -vfi
%configure \
	   --disable-silent-rules

make %{?_smp_mflags}

%check
make check

%install
%make_install

%files 
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING COPYING.LESSER
%{_datadir}/guile
%{_libdir}/guile

%changelog
