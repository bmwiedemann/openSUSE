#
# spec file for package owasp-modsecurity-crs
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Thomas Worm <thomas.worm@datev.de>
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


Name:           owasp-modsecurity-crs

BuildRequires:  apache2-devel
BuildRequires:  gcc-c++
BuildRequires:  rpm-devel
BuildRequires:  zlib-devel

Version:        2.2.9
Release:        0
Provides:       %{name} = %{version}
Source0:        https://github.com/SpiderLabs/owasp-modsecurity-crs/archive/%{version}.tar.gz
Source99:       README.SUSE
Source100:      %{name}-rpmlintrc
Url:            https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        OWASP ModSecurity Common Rule Set (CRS)
License:        Apache-2.0
Group:          Productivity/Networking/Security
Requires:       apache2-mod_security2

%define rule_sets base_rules experimental_rules optional_rules slr_rules
%define apxs2 %{_sbindir}/apxs2
%define apache2 apache2
%define apache2_mm %(MMN=$(%{apxs2} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
%define apache2_libexecdir %(%{apxs2} -q LIBEXECDIR)
%define apache2_sysconfdir %(%{apxs2} -q SYSCONFDIR)
%define apache2_includedir %(%{apxs2} -q INCLUDEDIR)
%define apache2_serverroot %(%{apxs2} -q PREFIX)
%define apache2_localstatedir %(%{apxs2} -q LOCALSTATEDIR)

%description
ModSecurity™ is a web application firewall engine that provides very little protection on its own. In order to become useful, ModSecurity™ must be configured with rules. In order to enable users to take full advantage of ModSecurity™ out of the box, Trustwave's SpiderLabs is providing a free certified rule set for ModSecurity™ 2.x. Unlike intrusion detection and prevention systems, which rely on signatures specific to known vulnerabilities, the Core Rules provide generic protection from unknown vulnerabilities often found in web applications, which are in most cases custom coded. The Core Rules are heavily commented to allow it to be used as a step-by-step deployment guide for ModSecurity™. 

Core Rules Content 

In order to provide generic web applications protection, the Core Rules use the following techniques: 

HTTP Protection - detecting violations of the HTTP protocol and a locally defined usage policy. 
Real-time Blacklist Lookups - utilizes 3rd Party IP Reputation 
Web-based Malware Detection - identifies malicious web content by check against the Google Safe Browsing API. 
HTTP Denial of Service Protections - defense against HTTP Flooding and Slow HTTP DoS Attacks. 
Common Web Attacks Protection - detecting common web application security attack. 
Automation Detection - Detecting bots, crawlers, scanners and other surface malicious activity. 
Integration with AV Scanning for File Uploads - detects malicious files uploaded through the web application. 
Tracking Sensitive Data - Tracks Credit Card usage and blocks leakages. 
Trojan Protection - Detecting access to Trojans horses. 
Identification of Application Defects - alerts on application misconfigurations. 
Error Detection and Hiding - Disguising error messages sent by the server. 



%prep
%setup -q -n %{name}-%{version}
sed -i -e '/^#!/c#!/usr/bin/lua' lua/*.lua
sed -i -e '/^#!/c#!/usr/bin/perl' util/*/*.pl util/*/*.cgi
%{__cp} %{S:99} .

%build
# Build configuration files
mkdir -p .%{_sysconfdir}/%{name}/rules.d
for rule_set in %{rule_sets}
do
  mkdir -p .%{_sysconfdir}/%{name}/$rule_set
  for rule in `find $rule_set -name *.conf -printf "%f\\n"|sort`
  do
    echo "Include \"%{_datadir}/%{name}/$rule_set/$rule\"" > .%{_sysconfdir}/%{name}/$rule_set/$rule
    echo "Include \"%{_sysconfdir}/%{name}/$rule_set/$rule\"" >> .%{_sysconfdir}/%{name}/$rule_set.conf
  done
  ln -s ../$rule_set.conf .%{_sysconfdir}/%{name}/rules.d/$rule_set.conf
done
echo "Include \"%{_datadir}/%{name}/modsecurity_crs_10_setup.conf.example\"" > .%{_sysconfdir}/%{name}/modsecurity_crs_10_setup.conf
# Create Apache2 include
mkdir -p .%{apache2_sysconfdir}/conf.d
echo "<IfModule mod_security2.c>" > .%{apache2_sysconfdir}/conf.d/%{name}.conf
echo -e "\tInclude \"%{_sysconfdir}/%{name}/modsecurity_crs_10_setup.conf\"" >> .%{apache2_sysconfdir}/conf.d/%{name}.conf
echo -e "\tInclude \"%{_sysconfdir}/%{name}/rules.d/*\"" >> .%{apache2_sysconfdir}/conf.d/%{name}.conf
echo "</IfModule>" >> .%{apache2_sysconfdir}/conf.d/%{name}.conf

%install
# CRS data
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -dr {lua,util,*.conf*} %{buildroot}%{_datadir}/%{name}/
for rule_set in %{rule_sets}
do
cp -r $rule_set %{buildroot}%{_datadir}/%{name}/
done
# Configuration files
mkdir -p %{buildroot}/%{_sysconfdir}
cp -dr .%{_sysconfdir}/* %{buildroot}%{_sysconfdir}/

%files
%defattr(644,root,root,755)
%doc CHANGES
%doc LICENSE
%doc README.md
%doc README.SUSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lua
%{_datadir}/%{name}/util
%{_datadir}/%{name}/*.conf*
%config(noreplace) %{apache2_sysconfdir}/conf.d/%{name}.conf
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/rules.d
%config(noreplace) %{_sysconfdir}/%{name}/modsecurity_crs_10_setup.conf

%package base_rules
Summary:        Base rules for OWASP ModSecurity CRS
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description base_rules
Base rules for HTTP Protocol Validation, Common Web Attacks Protection, Trojan Protection, InfoLeakages, ...

%files base_rules
%defattr(644,root,root,755)
%{_datadir}/%{name}/base_rules
%config(noreplace) %{_sysconfdir}/%{name}/base_rules*
%config(noreplace) %{_sysconfdir}/%{name}/rules.d/base_rules.conf

%package optional_rules
Summary:        Optional rules for OWASP ModSecurity CRS
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description optional_rules
Optional rules for HTTP Protocol Validation, Common Web Attacks Protection, Request Header Tagging, ...

%files optional_rules
%defattr(644,root,root,755)
%{_datadir}/%{name}/optional_rules
%config(noreplace) %{_sysconfdir}/%{name}/optional_rules*
%config(noreplace) %{_sysconfdir}/%{name}/rules.d/optional_rules.conf

%package experimental_rules
Summary:        Experimental rules for OWASP ModSecurity CRS
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description experimental_rules
Experimental rules for OWASP ModSecurity CRS

%files experimental_rules
%defattr(644,root,root,755)
%{_datadir}/%{name}/experimental_rules
%config(noreplace) %{_sysconfdir}/%{name}/experimental_rules*
%config(noreplace) %{_sysconfdir}/%{name}/rules.d/experimental_rules.conf

%package slr_rules
Summary:        SpiderLabs Research (SLR) rules for OWASP ModSecurity CRS
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}

%description slr_rules
SpiderLabs Research rules for ModSecurity CRS

%files slr_rules
%defattr(644,root,root,755)
%{_datadir}/%{name}/slr_rules
%config(noreplace) %{_sysconfdir}/%{name}/slr_rules*
%config(noreplace) %{_sysconfdir}/%{name}/rules.d/slr_rules.conf

%changelog
