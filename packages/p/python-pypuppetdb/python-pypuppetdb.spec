#
# spec file for package python-pypuppetdb
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pypuppetdb
Version:        2.5.1
Release:        0
Summary:        Library to work with PuppetDB's REST API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nedap/pypuppetdb
Source:         https://github.com/voxpupuli/pypuppetdb/archive/v%{version}.tar.gz
BuildRequires:  %{python_module httpretty >= 0.9.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 3.0.1}
BuildRequires:  %{python_module pytest-cov >= 2.2.1}
BuildRequires:  %{python_module requests >= 2.22.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.22.0
BuildArch:      noarch
%python_subpackages

%description
This library is a wrapper around the REST API providing some convinience functions and objects to request and hold data from PuppetDB.
More information: https://github.com/nedap/pypuppetdb

%prep
%setup -q -n pypuppetdb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# requirements-test.txt packages oddly
rm %{buildroot}%{_prefix}/requirements_for_tests/requirements-test.txt

%check
# https://github.com/voxpupuli/pypuppetdb/issues/227
sed -i 's:import mock:from unittest import mock:' tests/test_*.py
%pytest

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/pypuppetdb
%{python_sitelib}/pypuppetdb-%{version}*-info

%changelog
