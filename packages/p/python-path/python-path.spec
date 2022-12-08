#
# spec file
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


%{?!python_module:%define python_module() python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
%define modname path
Name:           python-path%{psuffix}
Version:        16.6.0
Release:        0
Summary:        A module wrapper for os.path
License:        MIT
URL:            https://github.com/jaraco/path
Source:         https://files.pythonhosted.org/packages/source/p/path/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
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
%doc CHANGES.rst README.rst
%{python_sitelib}/path
%{python_sitelib}/path-%{version}*-info
%endif

%changelog
