#
# spec file for package python-python-utils
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


Name:           python-python-utils
Version:        3.4.5
Release:        0
Summary:        Utilities not included with the standard Python install
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/WoLpH/python-utils
Source:         https://files.pythonhosted.org/packages/source/p/python-utils/python-utils-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module loguru}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-loguru
BuildArch:      noarch

%python_subpackages

%description
Python Utils is a collection of Python functions and
classes which make common patterns shorter and easier.

%prep
%setup -q -n python-utils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv pytest.ini{,.hide}
skip='test_timeout_generator' # obs rq#1042418
%pytest -k "not $skip"
mv pytest.ini{.hide,}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
