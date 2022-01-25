#
# spec file for package ldap-yp-tools
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ldap-yp-tools
Version:        1.13
Release:        0
Summary:        LDAP YP Tools
License:        BSD-2-Clause 
Group:          Applications/Internet
Url:            https://downloads.sourceforge.net/project/%{name}/
Source:         https://downloads.sourceforge.net/project/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         ldap-yp-tools-1.13.dif
BuildRequires:  openldap2-devel
BuildRequires:  perl
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(URI)
Requires:       perl
Requires:       perl(Net::LDAP)
Requires:       perl(URI)

%description
LDAP equivalents of yp tools ypcat, ypmatch and chsh

%debug_package

%prep
%setup -q
%patch0

%build
%configure --docdir=%{_docdir}/%{name} \
        --with-perl=/usr/bin/perl
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%doc README
%{_bindir}/ldap*
%{_mandir}/man1/ldap*.1%{ext_man}
%{_docdir}/%{name}/*.ldapcat

%changelog
