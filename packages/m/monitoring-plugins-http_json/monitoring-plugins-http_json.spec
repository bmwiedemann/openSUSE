#
# spec file for package monitoring-plugins-http_json
#
# Copyright (c) 2024 SUSE LLC
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


%define modname monitoring-plugins-http_json
%define pythons python3
Name:           monitoring-plugins-http_json
Version:        2.2.0
Release:        0
Summary:        Plugin for Nagios which checks json values from a given HTTP endpoint
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/drewkerrigan/nagios-http-json
Source:         https://github.com/drewkerrigan/nagios-http-json/archive/v%{version}.tar.gz#/nagios-http-json-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  nagios-rpm-macros
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A generic plugin for Icinga/Nagios which checks json values from a given
HTTP endpoint against argument specified rules and determines the
status and performance data for that service.

%prep
%setup -q -n nagios-http-json-%{version}
sed -i -e '1{s:^#!\s*/usr/bin/env python:#!%{_bindir}/python:}' *.py

%build
/bin/true

%install
install -Dpm 0755 check_http_json.py %{buildroot}%{nagios_plugindir}/check_http_json

%check
# There are no tests upstream, don’t pretend there are.

%files %{python_files}
%license LICENSE
%doc README.md docs
%doc contrib/icinga2_check_command_definition.conf
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_http_json

%changelog
