#
# spec file for package owasp-modsecurity-crs
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Alessandro de Oliveira Faria (A.K.A CABELO) <cabelo@opensuse.org>
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


Name:           owasp-modsecurity-crs
Version:        4.10.0
Release:        0
Summary:        OWASP ModSecurity Common Rule Set (CRS)
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://coreruleset.org
Source0:        https://github.com/coreruleset/coreruleset/archive/refs/tags/v%{version}.tar.gz#/coreruleset-%{version}.tar.gz
Source1:        https://github.com/coreruleset/coreruleset/releases/download/v%{version}/coreruleset-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source10:       README.SUSE
BuildRequires:  apache-rpm-macros
Provides:       %{name} = %{version}
BuildArch:      noarch

%description
The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity
or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks,
including the OWASP Top Ten, with a minimum of false alerts.

%package apache2
Summary:        OWASP ModSecurity Common Rule Set (CRS)
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}
Requires:       apache2-mod_security2

%description apache2
The OWASP ModSecurity Core Rule Set (CRS) Apache2 HTTPD configuration.

%prep
%autosetup -p1 -n coreruleset-%{version}
cp %{SOURCE10} .

%build

%install
# rules
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -ra rules %{buildroot}%{_datadir}/%{name}
# top-level Apache2 conf for mod_security2
mkdir -p %{buildroot}%{apache_sysconfdir}/mod_security2.d/rules
# has to be read before rules
cp -a crs-setup.conf.example %{buildroot}%{apache_sysconfdir}/mod_security2.d/modsecurity-crf-setup.conf
# rules linked to mod_security2 conf
for rule in `ls %{buildroot}%{_datadir}/%{name}/rules` ; do 
    ln -s %{_datadir}/%{name}/rules/$rule %{buildroot}%{apache_sysconfdir}/mod_security2.d/rules/$rule
done

%files
%doc CONTRIBUTING.md CHANGES.md KNOWN_BUGS.md README.md README.SUSE SECURITY.md SPONSORS.md docs/README.md
%license LICENSE
%{_datadir}/%{name}

%files apache2
%dir %{apache_sysconfdir}
%dir %{apache_sysconfdir}/mod_security2.d
%config %{apache_sysconfdir}/mod_security2.d/*
%dir %{apache_sysconfdir}/mod_security2.d/rules
%config %{apache_sysconfdir}/mod_security2.d/rules/*

%changelog
