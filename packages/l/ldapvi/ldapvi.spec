#
# spec file for package ldapvi
#
# Copyright (c) 2026 SUSE LLC
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


Name:           ldapvi
Version:        1.8
Release:        0
Summary:        Interactive LDAP Client for Unix Terminals
License:        GPL-2.0-only
URL:            http://www.lichteblau.com/ldapvi/
Source:         https://github.com/ldapvi/ldapvi/archive/refs/tags/%{version}.tar.gz#/ldapvi-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  cyrus-sasl-devel
BuildRequires:  glib2-devel
BuildRequires:  libopenssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  popt-devel
BuildRequires:  readline-devel
## tests fail on i586, aarch64
ExclusiveArch:  x86_64

%description
ldapvi is an interactive LDAP client for Unix terminals.  Using it, you can
update LDAP entries with a text editor.  Think of it as vipw(1) for LDAP.

%prep
%autosetup -p1
## fix compile error (getc_unlocked undeclared)
sed -e /_XOPEN_SOURCE/d -i ldapvi/parseldif.c

%build
cd ldapvi
./autogen.sh
%configure
%make_build

%install
cd ldapvi
%make_install

%check
cd ldapvi
%make_build test

%files
%license ldapvi/COPYING
%doc ldapvi/NEWS README.md
%{_bindir}/ldapvi
%{_mandir}/man1/ldapvi.1%{?ext_man}

%changelog
