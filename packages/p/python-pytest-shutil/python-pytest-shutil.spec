#
# spec file for package python-pytest-shutil
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


%bcond_without python2
Name:           python-pytest-shutil
Version:        1.7.0
Release:        0
Summary:        A goodie-bag of unix shell and environment tools for pytest
License:        MIT
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-shutil/pytest-shutil-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM pytest-fixtures-pr171-remove-mock.patch -- gh#man-group#pytest-plugins#171
Patch1:         pytest-fixtures-pr171-remove-mock.patch
BuildRequires:  %{python_module execnet}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module termcolor}
BuildRequires:  fdupes
%if %{with python2}
BuildRequires:  python-contextlib2
BuildRequires:  python-mock
BuildRequires:  python-path.py
%endif
%if 0%{?suse_version} < 1550
BuildRequires:  python3-path.py
%else
BuildRequires:  %{python_module path}
%endif
BuildRequires:  python-rpm-macros
Requires:       python-execnet
%if 0%{suse_version} < 1550
Requires:       python-path.py
%else
Requires:       python-path
%endif
Requires:       python-pytest
Requires:       python-six
Requires:       python-termcolor
%ifpython2
Requires:       python-contextlib2
Requires:       python-mock
Requires:       python-path.py
%endif
BuildArch:      noarch

%python_subpackages

%description
This library is a goodie-bag of Unix shell and environment management
tools for automated tests.

%prep
%autosetup -p2 -n pytest-shutil-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable test_pretty_formatter test that fails in osc build but it works when
# run manually. It should be something related to the shell and termcolor
%pytest -k "not test_pretty_formatter"

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/pytest_shutil
%{python_sitelib}/pytest_shutil-%{version}*-info

%changelog
