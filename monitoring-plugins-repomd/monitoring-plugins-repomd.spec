#
# spec file for package monitoring-plugins-repomd
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


Name:           monitoring-plugins-repomd
Summary:        Plugin to check freshness of repomd.xml file
License:        BSD-3-Clause
Group:          System/Monitoring
Version:        2.1
Release:        0
Url:            http://en.opensuse.org/%{name}
Source0:        check_repomd
Source1:        usr.lib.nagios.plugins.check_repomd
Requires:       bash
Requires:       curl
Requires:       grep
Requires:       monitoring-plugins-common
Recommends:     apparmor-parser
BuildRequires:  monitoring-plugins-common
BuildRequires:  nagios-rpm-macros
%if 0%{?suse_version} >= 1500
BuildRequires:  sed
%endif
Provides:       nagios-plugins-repomd = %{version}-%{release}
Obsoletes:      nagios-plugins-repomd < %{version}-%{release}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin checks the up-to date state of repomd.xml.

Important options:
 -u <url_to_repomd.xml> : please enter the full URL to the repomd.xml file
 -o <days>              : days unless a repomd.xml file is handled as outdated (default: 30)
 

%prep

%build

%install
install -D -m755 %{SOURCE0} %buildroot/%{nagios_plugindir}/check_repomd
install -D -m644 %{SOURCE1} %buildroot/%{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_repomd
%if 0%{?suse_version} >= 1500
sed -i "s|/bin/grep|%{_bindir}/grep|; \
		s|/bin/cat|%{_bindir}/cat|; \
		s|/bin/mktemp|%{_bindir}/mktemp|" %buildroot/%{nagios_plugindir}/check_repomd
%endif

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
%dir %{_sysconfdir}/apparmor.d
%{nagios_plugindir}/check_repomd
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.nagios.plugins.check_repomd

%changelog
