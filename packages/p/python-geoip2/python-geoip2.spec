#
# spec file for package python-geoip2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-geoip2
Version:        4.1.0
Release:        0
Summary:        MaxMind GeoIP2 Python API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/maxmind/GeoIP2-python
Source:         https://files.pythonhosted.org/packages/source/g/geoip2/geoip2-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 >= 1.25.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aiohttp >= 3.6.2}
BuildRequires:  %{python_module maxminddb >= 2.0.0}
BuildRequires:  %{python_module mocket >= 3.8.6}
BuildRequires:  %{python_module python-magic >= 0.4.18}
BuildRequires:  %{python_module requests >= 2.24.0}
# /SECTION
Requires:       python-aiohttp >= 3.6.2
Requires:       python-maxminddb >= 2.0.0
Requires:       python-requests >= 2.24.0
Requires:       python-urllib3 >= 1.25.2
BuildArch:      noarch
%ifpython2
Recommends:     python2-ipaddress
%endif
%python_subpackages

%description
This package provides an API for the GeoIP2 web services and databases.
The API also works with MaxMind's free GeoLite2 databases.

%prep
%setup -q -n geoip2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest tests/*_test.py -v

%files %{python_files}
%license LICENSE
%doc README.rst HISTORY.rst
%{python_sitelib}/geoip2
%{python_sitelib}/geoip2-%{version}*-info

%changelog
