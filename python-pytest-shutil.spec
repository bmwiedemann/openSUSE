#
# spec file for package python-pytest-shutil
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
%bcond_without python2
Name:           python-pytest-shutil
Version:        1.7.0
Release:        0
Summary:        A goodie-bag of unix shell and environment tools for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-shutil/pytest-shutil-%{version}.tar.gz
BuildRequires:  %{python_module execnet}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module termcolor}
BuildRequires:  fdupes
%if %{with python2}
BuildRequires:  python-contextlib2
%endif
BuildRequires:  python-rpm-macros
Requires:       python-execnet
Requires:       python-mock
Requires:       python-path.py
Requires:       python-pytest
Requires:       python-six
Requires:       python-termcolor
%ifpython2
Requires:       python-contextlib2
%endif
BuildArch:      noarch

%python_subpackages

%description
This library is a goodie-bag of Unix shell and environment management
tools for automated tests.

%prep
%setup -q -n pytest-shutil-%{version}
sed -i '/contextlib2/d' setup.py
sed -i '/path.\py/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/*

%changelog
