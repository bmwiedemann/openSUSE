#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-semantic_version%{psuffix}
Version:        2.10.0
Release:        0
Summary:        A library implementing the 'SemVer' scheme
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rbarrois/python-semanticversion
Source:         https://files.pythonhosted.org/packages/source/s/semantic_version/semantic_version-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} > 1550
# Django 4.0 dropped support for Python < 3.8
BuildRequires:  %{python_module Django >= 1.11 if (%python-base without python36-base)}
%endif
%endif
%python_subpackages

%description
This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.

%prep
%autosetup -n semantic_version-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# Django 4.0 dropped support for Python < 3.8
python36_flags="--ignore tests/test_django.py"
%pytest ${$python_flags}

%else

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/semantic_version
%{python_sitelib}/semantic_version-%{version}*-info
%endif

%changelog
