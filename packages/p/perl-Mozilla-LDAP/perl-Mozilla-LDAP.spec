#
# spec file for package perl-Mozilla-LDAP
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define nspr_name	mozilla-nspr
%define nss_name	mozilla-nss

Name:      perl-Mozilla-LDAP
Summary:   LDAP module that wraps the OpenLDAP C SDK
Version:   1.5.3
Release:   1
License:   MPL-1.1 or GPL-2.0+ or LGPL-2.0+
Group:     Development/Libraries/Perl
Url:       http://www.mozilla.org/directory/perldap.html
Requires:  perl-base = %{perl_version}
Source0:   ftp://ftp.mozilla.org/pub/mozilla.org/directory/perldap/releases/%{version}/src/perl-mozldap-%{version}.tar.gz
# Original from ftp://ftp.mozilla.org/pub/mozilla.org/directory/perldap/releases/1.5/src/Makefile.PL.rpm
# Enhanced to support OpenLDAP
Source1:   Makefile.PL.rpm
Patch:     API.xs.patch
BuildRequires: perl >= 5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-macros
BuildRequires: %{nspr_name}-devel >= 4.6
BuildRequires: %{nss_name}-devel >= 3.11
BuildRequires: openldap2-devel >= 2.4.22
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

%description
A perl LDAP module that wraps the OpenLDAP C SDK.


%prep
%setup -q -n perl-mozldap-%{version}
%patch

# Filter unwanted Provides:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
  sed -e '/perl(Mozilla::LDAP::Entry)$/d'
EOF

%define __perl_provides %{_builddir}/perl-mozldap-%{version}/%{name}-prov
chmod +x %{__perl_provides}

# Filter unwanted Requires:
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(Mozilla::LDAP::Entry)/d'
EOF

%define __perl_requires %{_builddir}/perl-mozldap-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
LDAPPKGNAME=openldap CFLAGS="$RPM_OPT_FLAGS" perl %{SOURCE1} INSTALLDIRS=vendor < /dev/null
make OPTIMIZE="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} all

%check
#make test

%install
eval `perl '-V:installarchlib'`

%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,-)
%doc CREDITS ChangeLog README MPL-1.1.txt

%changelog

