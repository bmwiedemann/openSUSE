#
# spec file for package python-path
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define modname path
%{?sle15_python_module_pythons}
Name:           python-path%{psuffix}
Version:        17.1.0
Release:        0
Summary:        A module wrapper for os.path
License:        MIT
URL:            https://github.com/jaraco/path
Source:         https://files.pythonhosted.org/packages/source/p/path/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# Renaming package
Provides:       python-path.py = %{version}-%{release}
Obsoletes:      python-path.py < %{version}-%{release}
%if %{with test}
# use a multibuild test flavor so that there is no circular dependency with pytest
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module path >= %{version}}
%endif
%python_subpackages

%description
The path package implements a path objects as first-class
entities, allowing common operations on files to be invoked
on those path objects directly.

%prep
%setup -q -n %{modname}-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# need to set locale to avoid UnicodeEncodeError
export LANG=en_US.UTF-8
# test_import_time -> relies on timing that varies in OBS
%pytest -k 'not test_import_time'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%{python_sitelib}/path
%{python_sitelib}/path-%{version}.dist-info
%endif

%changelog
