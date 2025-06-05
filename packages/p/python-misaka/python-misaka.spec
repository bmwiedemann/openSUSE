#
# spec file for package python-misaka
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


%bcond_without libalternatives
Name:           python-misaka
Version:        2.1.1
Release:        0
Summary:        A CFFI binding for Hoedown, a markdown parsing library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/FSX/misaka
Source:         https://files.pythonhosted.org/packages/source/m/misaka/misaka-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.12.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tidy
Requires:       alts
Requires:       python-cffi >= 1.12.0
%python_subpackages

%description
A CFFI binding for Hoedown_ (version 3), a markdown parsing library.

%prep
%setup -q -n misaka-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/misaka
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand $python setup.py build_ext --inplace
$python tests/run_tests.py
}

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative misaka

# post and postun calls are not needed with libalternatives only

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/misaka
%{python_sitearch}/misaka
%{python_sitearch}/misaka-%{version}*-info

%changelog
