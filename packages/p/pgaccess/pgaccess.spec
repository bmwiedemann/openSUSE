#
# spec file for package pgaccess (Version 0.99.0.20040219)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           pgaccess
Summary:        Database Management Tool for PostgreSQL
Version:        0.99.0.20040219
Release:        1
License:        PostgreSQL
Group:          Productivity/Databases/Tools
Url:            http://www.pgaccess.org
Requires:       PgTcl tk tcllib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Source0:        pgaccess-0_99_0_20040219.tar.bz2
Patch0:         %name.patch

%description
PgAccess is a graphical interface and application building environment
for PostgreSQL.

%prep
%setup -q -n pgaccess-0_99_0_20040219
%patch0
chmod -R a+rX .

%build

%install
make DESTDIR=%buildroot libdir=/usr/share bindir=%_bindir install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc README changelog copyright known_bugs todo demo doc/html
/usr/share/pgaccess
/usr/bin/pgaccess

%changelog
