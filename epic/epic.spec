#
# spec file for package epic
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           epic
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
Provides:       epic4
Provides:       ircii
Provides:       irciihlp
Obsoletes:      epic4
Obsoletes:      ircii
Obsoletes:      irciihlp
Version:        2.10.6
Release:        0
Summary:        Enhanced Programmable ircII Client
License:        BSD-3-Clause
Group:          Productivity/Networking/IRC
Url:            http://www.epicsol.org
Source0:        epic4-%version.tar.gz
Source1:        epic4-help-20070412.tar.bz2
Patch:          epic4-config.patch
# PATCH-FIX-UPSTREAM
Patch1:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
EPIC is an IRC client almost 100% compatible with the old ircII client
from which it was derived. It has improved scripting, better
configurability, and more.



Authors:
--------
    EPIC Software Labs

%prep
%setup -q -n epic4-%version -a 1
%patch -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -O2 -Wall -fno-strict-aliasing" ./configure \
	--prefix=/usr \
	--mandir=%_mandir \
	--with-ipv6 \
	--libexecdir=/usr/lib/epic
make

%install
make prefix=$RPM_BUILD_ROOT/usr libexecdir=$RPM_BUILD_ROOT/usr/lib/epic \
mandir=$RPM_BUILD_ROOT/%_mandir installeverything
make prefix=$RPM_BUILD_ROOT/usr libexecdir=$RPM_BUILD_ROOT/usr/lib/epic \
mandir=$RPM_BUILD_ROOT/%_mandir installhelp
find $RPM_BUILD_ROOT/usr/share -name CVS -print0 | xargs -0 rm -rf

%files
%defattr(-,root,root)
/usr/share/epic
/usr/lib/epic
/usr/bin/*
%_mandir/man1/*

%changelog
