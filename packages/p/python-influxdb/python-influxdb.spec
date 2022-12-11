#
# spec file for package python-influxdb
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-influxdb
Version:        5.3.1
Release:        0
Summary:        InfluxDB client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/influxdb/influxdb-python
Source:         https://files.pythonhosted.org/packages/source/i/influxdb/influxdb-%{version}.tar.gz
# https://github.com/influxdata/influxdb-python/pull/835
Patch0:         python-influxdb-remove-nose.patch
# PATCH-FIX-UPSTREAM influxdb-pr845-pandas-future.patch -- gh#influxdb/influxdb-python#845
Patch1:         https://github.com/influxdata/influxdb-python/pull/845.patch#/influxdb-pr845-pandas-future.patch
BuildRequires:  %{python_module python-dateutil >= 2.6.0}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.17.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack
Requires:       python-python-dateutil >= 2.6.0
Requires:       python-pytz
Requires:       python-requests >= 2.17.0
Requires:       python-six >= 1.10.0
ExcludeArch:    %ix86 %arm ppc
# SECTION test requirements
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  influxdb
%if 0%{?suse_version} >= 1500
BuildRequires:  hostname
%endif
# /SECTION
%python_subpackages

%description
InfluxDB-Python is a client for interacting with InfluxDB 1.x

%prep
%autosetup -p1 -n influxdb-%{version}
# remove extra mock
sed -e 's/^import mock/from unittest import mock/' \
    -e 's/^from mock import/from unittest.mock import/' \
    -i influxdb/tests/*.py influxdb/tests/*/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/influxdata/influxdb-python/issues/884
donttest="test_write_points_from_dataframe_with_nan_json or test_write_points_from_dataframe_with_tags_and_nan_json"
%pytest influxdb -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/influxdb
%{python_sitelib}/influxdb-%{version}*-info

%changelog
