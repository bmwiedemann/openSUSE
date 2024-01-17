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


%define apxs2 %{_bindir}/apxs
%define apache2 apache2
%define apache2_mm %(MMN=$(%{apxs2} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
%define apache2_libexecdir %(%{apxs2} -q LIBEXECDIR)
%define apache2_sysconfdir %(%{apxs2} -q SYSCONFDIR)
%define apache2_includedir %(%{apxs2} -q INCLUDEDIR)
%define apache2_serverroot %(%{apxs2} -q PREFIX)
%define apache2_localstatedir %(%{apxs2} -q LOCALSTATEDIR)
Name:           owasp-modsecurity-crs
Version:        3.3.5
Release:        0
Summary:        OWASP ModSecurity Common Rule Set (CRS)
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://coreruleset.org
Source0:        https://github.com/coreruleset/coreruleset/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source99:       README.SUSE
Source100:      %{name}-rpmlintrc
BuildRequires:  apache2-devel
BuildRequires:  gcc-c++
BuildRequires:  rpm-devel
BuildRequires:  zlib-devel
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
The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity
or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks,
including the OWASP Top Ten, with a minimum of false alerts.

Includes Apache httpd 2.x rules

%prep
%setup -q -n coreruleset-%{version}
sed -i -e '/^#!/c#!%{_bindir}/perl' util/*/*.pl
cp %{SOURCE99} .

%build
# Build configuration files
mkdir -p .%{_sysconfdir}/%{name}/rules.d
mkdir -p .%{_sysconfdir}/%{name}/rules

for rule in rules/*.conf
do
  RULE=$(basename ${rule})
  echo "Include \"%{_datadir}/%{name}/rules/$RULE\"" > .%{_sysconfdir}/%{name}/rules/$RULE
  echo "Include \"%{_sysconfdir}/%{name}/rules/$RULE\"" >> .%{_sysconfdir}/%{name}/rules.conf
done
ln -s ../rules.conf .%{_sysconfdir}/%{name}/rules.d/rules.conf

echo "Include \"%{_datadir}/%{name}/crs-setup.conf.example\"" > .%{_sysconfdir}/%{name}/crs-setup.conf
# Create Apache2 include
mkdir -p .%{apache2_sysconfdir}/conf.d
echo "<IfModule mod_security2.c>" > .%{apache2_sysconfdir}/conf.d/%{name}.conf
echo -e "\tInclude \"%{_sysconfdir}/%{name}/crs-setup.conf\"" >> .%{apache2_sysconfdir}/conf.d/%{name}.conf
echo -e "\tInclude \"%{_sysconfdir}/%{name}/rules.d/*\"" >> .%{apache2_sysconfdir}/conf.d/%{name}.conf
echo "</IfModule>" >> .%{apache2_sysconfdir}/conf.d/%{name}.conf

%install
# CRS data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -dr {util,*.conf*} %{buildroot}%{_datadir}/%{name}/
for rule_set in %{rule_sets}
do
cp -r rules %{buildroot}%{_datadir}/%{name}/
done
# Configuration files
mkdir -p %{buildroot}/%{_sysconfdir}
cp -dr .%{_sysconfdir}/* %{buildroot}%{_sysconfdir}/

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md README.SUSE
%license LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/util
%attr(0754, root, root) %{_datadir}/%{name}/util/av-scanning/runav.pl
%attr(0754, root, root) %{_datadir}/%{name}/util/crs2-renumbering/update.py
%attr(0754, root, root) %{_datadir}/%{name}/util/join-multiline-rules/join.py
%attr(0754, root, root) %{_datadir}/%{name}/util/regexp-assemble/regexp-assemble-v2.pl
%attr(0754, root, root) %{_datadir}/%{name}/util/regexp-assemble/regexp-assemble.pl
%attr(0754, root, root) %{_datadir}/%{name}/util/regexp-assemble/regexp-cmdline.py
%attr(0754, root, root) %{_datadir}/%{name}/util/send-payload-pls.sh
%attr(0754, root, root) %{_datadir}/%{name}/util/verify.rb
%attr(0754, root, root) %{_datadir}/%{name}/util/virtual-patching/arachni2modsec.pl
%attr(0754, root, root) %{_datadir}/%{name}/util/virtual-patching/zap2modsec.pl
%{_datadir}/%{name}/*.conf*
%{_datadir}/%{name}/rules

%files apache2
%config(noreplace) %{apache2_sysconfdir}/conf.d/%{name}.conf
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/rules.d
%config(noreplace) %{_sysconfdir}/%{name}/crs-setup.conf
%config(noreplace) %{_sysconfdir}/%{name}/rules
%config(noreplace) %{_sysconfdir}/%{name}/rules.conf
%config(noreplace) %{_sysconfdir}/%{name}/rules.d/rules.conf

%changelog
