#
# spec file for package python-influxdb
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


# Legacy package not compatible with Python 3.12 and newer. Move your consuming library to a more modern version!
%define skip_python312 1
%define skip_python313 1
Name:           python-influxdb
Version:        5.3.2
Release:        0
Summary:        InfluxDB client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/influxdb/influxdb-python
Source:         https://files.pythonhosted.org/packages/source/i/influxdb/influxdb-%{version}.tar.gz
# https://github.com/influxdata/influxdb-python/pull/835
Patch0:         python-influxdb-remove-nose.patch
# PATCH-FIX-UPSTREAM influxdb-pr845-pandas-future.patch -- gh#influxdb/influxdb-python#845
Patch1:         influxdb-pr845-pandas-future.patch
# do not require six (repo archived in favour of influxdb2, not reporting)
Patch2:         python-influxdb-no-six.patch
# fix tests with newer pandas
Patch3:         python-influxdb-new-pandas.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil >= 2.6.0}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.17.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack
Requires:       python-python-dateutil >= 2.6.0
Requires:       python-pytz
Requires:       python-requests >= 2.17.0
# Pandas is optional but only works with pandas >= 2.1. If pandas < 2.1 is installed, the module throws an ImportError
Conflicts:      python-pandas < 2.1
ExcludeArch:    %ix86 %arm ppc
# SECTION test requirements
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pandas >= 2.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  influxdb
%if 0%{?suse_version} >= 1500
BuildRequires:  hostname
%endif
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
InfluxDB-Python is a client for interacting with InfluxDB 1.x

%prep
%autosetup -p1 -n influxdb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove extra mock
sed -e 's/^import mock/from unittest import mock/' \
    -e 's/^from mock import/from unittest.mock import/' \
    -i influxdb/tests/*.py influxdb/tests/*/*.py
# https://github.com/influxdata/influxdb-python/issues/884
donttest="test_write_points_from_dataframe_with_nan_json or test_write_points_from_dataframe_with_tags_and_nan_json"
# don't work with numpy 2
donttest+=" or test_multiquery_into_dataframe_dropna"
%pytest influxdb -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/influxdb
%{python_sitelib}/influxdb-%{version}.dist-info

%changelog
