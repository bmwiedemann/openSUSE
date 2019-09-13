#
# spec file for package python-influxdb
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-influxdb
Version:        5.2.3
Release:        0
Summary:        InfluxDB client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/influxdb/influxdb-python
Source:         https://github.com/influxdata/influxdb-python/archive/v%{version}.tar.gz
# fix module 'distutils' has no attribute 'spawn'
Patch1:         python-influxdb-fix-testsuite.patch
BuildRequires:  %{python_module python-dateutil >= 2.0.0}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 1.0.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.6.0
Requires:       python-pytz
Requires:       python-requests >= 1.17.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  influxdb
%if 0%{?suse_version} >= 1500
BuildRequires:  hostname
%endif
# /SECTION
%python_subpackages

%description
InfluxDB-Python is a client for interacting with InfluxDB_. Maintained by @aviau (https://github.com/aviau).

%prep
%setup -q -n influxdb-python-%{version}
%patch1 -p1

%build
%python_build

%check
%python_expand nosetests-%{$python_bin_suffix} -v

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
