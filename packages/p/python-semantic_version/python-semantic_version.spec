#
# spec file for package python-semantic_version
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} >= 1600 && 0%{?is_opensuse} == 0
# No django in SLFO:Main
%bcond_with django
%else
%bcond_without django
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-semantic_version%{psuffix}
Version:        2.10.0
Release:        0
Summary:        A library implementing the 'SemVer' scheme
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rbarrois/python-semanticversion
Source:         https://files.pythonhosted.org/packages/source/s/semantic_version/semantic_version-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%if %{with django}
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
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%if %{without django}
python_flags="--ignore tests/test_django.py"
%else
# Django 4.0 dropped support for Python < 3.8
python36_flags="--ignore tests/test_django.py"
%endif

%pytest ${$python_flags} ${python_flags}

%else

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/semantic_version
%{python_sitelib}/semantic_version-%{version}.dist-info
%endif

%changelog
