#
# spec file for package lbdb
#
# Copyright (c) 2020 SUSE LLC
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


Name:           lbdb
Version:        0.48.1
Release:        0
Summary:        Address Database for mutt
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://www.spinnaker.de/lbdb/
Source:         http://www.spinnaker.de/debian/lbdb_%{version}.tar.xz
Patch0:         lbdb.rc.dif
Patch2:         lbdb-hostname.diff
Suggests:       perl(Getopt::Long)
Suggests:       perl(Net::LDAP)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Little Brother's Database (lbdb) consists of a set of small tools
that collect mail addresses from several sources and offer these
addresses to the external query feature of the Mutt mail reader.

To use the fetch address feature, put the following lines in your
.procmailrc:

:0hc | lbdb-fetchaddr

To use the database in mutt, put the following line into your .muttrc:

set query_command="lbdbq %{s}"

%prep
%setup -q -n lbdb-%{version}
%patch0 -p1
%patch2 -p1

%build
export \
  CFLAGS="%{optflags} -fno-strict-aliasing" \
  PGP="%{_bindir}/pgp" \
  PGPK="%{_bindir}/pgpk" \
  GPG="%{_bindir}/gpg" \
  FINGER="%{_bindir}/finger" \
  ABOOK="%{_bindir}/abook" \
  ADDR_EMAIL="%{_bindir}/addr-email" \
  SH="/bin/sh" \
  YPCAT="%{_bindir}/ypcat" \
  MAWK="%{_bindir}/awk"
%configure \
	--libdir=%{_libdir}/lbdb \
	--enable-lbdb-dotlock
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_sysconfdir}
make \
  prefix=%{buildroot}%{_prefix} \
  bindir=%{buildroot}%{_bindir} \
  sysconfdir=%{buildroot}%{_sysconfdir} \
  mandir=%{buildroot}%{_mandir} \
  libdir=%{buildroot}%{_libdir}/lbdb \
  install

%files
%defattr(-, root, root)
%doc README COPYING TODO
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/*
%{_libdir}/lbdb/*
%dir %{_libdir}/lbdb
%{_mandir}/man?/*

%changelog
