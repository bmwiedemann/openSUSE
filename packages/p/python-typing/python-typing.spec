#
# spec file for package python-typing
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
%if 0%{?suse_version} >= 1500 || %{python3_version_nodots} > 34
%define skip_python3 1
%endif
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-typing%{psuffix}
Version:        3.7.4.1
Release:        0
Summary:        Type Hints for Python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://docs.python.org/3.5/library/typing.html
Source:         https://files.pythonhosted.org/packages/source/t/typing/typing-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Backport of the standard library typing module for Python versions older than 3.5.

%prep
%setup -q -n typing-%{version}
ln -s python2 python_%{python2_bin_suffix}
ln -s src python_%{python3_bin_suffix}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
export PYTHONDONTWRITEBYTECODE=1
%python_expand pushd python_%{$python_bin_suffix} ; $python -m unittest test_typing ; popd
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
