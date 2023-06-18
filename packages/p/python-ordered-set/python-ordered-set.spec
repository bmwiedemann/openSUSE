#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


# in order to avoid rewriting for subpackage generator
%define mypython python
%global modname ordered-set
%global dir_name ordered_set
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-%{modname}%{psuffix}
Version:        4.1.0
Release:        0
Summary:        Custom MutableSet that remembers its order
License:        MIT
URL:            https://github.com/rspeer/ordered-set
Source:         https://files.pythonhosted.org/packages/source/o/%{modname}/%{modname}-%{version}.tar.gz
# this package is build dependency of setuptools
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
%endif
# work around boo#1186870
Provides:       %{mypython}%{python_version}dist(%modname) = %{version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{mypython}3dist(%modname) = %{version}
%endif
%python_subpackages

%description
An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.

%prep
%setup -q -n %{modname}-%{version}
# we are build dep of setuptools
sed -i -e 's:from setuptools :from distutils.core :g' setup.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license MIT-LICENSE
%doc README.md
%{python_sitelib}/%{dir_name}/
# Note: The distutils generated egg-info is not a directory
%{python_sitelib}/%{dir_name}-%{version}-py%{python_version}.egg-info
%endif

%changelog
