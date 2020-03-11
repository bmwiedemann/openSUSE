#
# spec file for package python-nagios-http-json
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


%define modname nagios-http-json
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-nagios-http-json
Version:        1.4+git.1583782740.e7cf7ca
Release:        0
Summary:        Plugin for Nagios which checks json values from a given HTTP endpoint
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/drewkerrigan/nagios-http-json
Source:         %{modname}-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post):    update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
A generic plugin for Nagios which checks json values from a given
HTTP endpoint against argument specified rules and determines the
status and performance data for that service.

%prep
%setup -q -n %{modname}-%{version}
sed -i -e '1{s:^#!\s*/usr/bin/env python:#!%{_bindir}/python:}' *.py

%build
/bin/true

%install
install -Dpm 0755 check_http_json.py %{buildroot}%{_bindir}/check_http_json
%python_clone %{buildroot}%{_bindir}/check_http_json
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative check_http_json

%postun
%python_uninstall_alternative check_http_json

%files %{python_files}
%license LICENSE
%doc README.md docs
%python_alternative %{_bindir}/check_http_json

%changelog
