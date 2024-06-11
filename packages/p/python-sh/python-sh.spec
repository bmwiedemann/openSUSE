#
# spec file for package python-sh
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


%{?sle15_python_module_pythons}
Name:           python-sh
Version:        2.0.7
Release:        0
Summary:        Python subprocess interface
License:        MIT
URL:            https://github.com/amoffat/sh
Source:         https://files.pythonhosted.org/packages/source/s/sh/sh-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%{?sle15_python_module_pythons}
%python_subpackages

%description
sh is a full-fledged subprocess replacement for Python 2.6 - 3.6, PyPy
and PyPy3 that allows you to call any program as if it were a
function:

    from sh import ifconfig
    print ifconfig("eth0")

sh is not a collection of system commands implemented in Python.

%prep
%autosetup -p1 -n sh-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export SH_TESTS_RUNNING=1
export SH_TESTS_USE_SELECT=0
export LANG=C
# disable broken tests in obs environment
donttest="test_stringio_output"
donttest+=" or test_environment"
donttest+=" or test_no_interfere1"
donttest+=" or test_set_in_parent_function"
donttest+=" or test_basic"
donttest+=" or test_multiline_defaults"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.rst
%{python_sitelib}/sh.py
%pycache_only %{python_sitelib}/__pycache__/sh.*pyc
%{python_sitelib}/sh-%{version}*-info

%changelog
