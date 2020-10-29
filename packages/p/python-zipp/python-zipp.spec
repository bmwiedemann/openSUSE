#
# spec file for package python-zipp
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
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-zipp%{psuffix}
Version:        3.2.0
Release:        0
Summary:        Pathlib-compatible object wrapper for zip files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/zipp
Source:         https://files.pythonhosted.org/packages/source/z/zipp/zipp-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
Requires:       python-more-itertools
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jaraco.itertools}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest >= 3.5}
%endif
%python_subpackages

%description
A pathlib-compatible Zipfile object wrapper.

%prep
%setup -q -n zipp-%{version}
# we don't need the extensions for smoke testing
rm -f pytest.ini

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# skip performance test (we do not have func_timeout sofar)
sed -i -e 's:import func_timeout::' \
       -e 's:@func_timeout.func_set_timeout(.):@unittest.skip("skip performance test"):' \
       test_zipp.py
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
