#
# spec file for package python-djangorestframework-stubs
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
%define short_name djangorestframework-stubs
%define package_name djangorestframework_stubs
%{?sle15_python_module_pythons}
Name:           python-djangorestframework-stubs%{psuffix}
Version:        3.16.2
Release:        0
Summary:        PEP-484 stubs for django-rest-framework
License:        MIT
URL:            https://github.com/typeddjango/djangorestframework-stubs
Source:         %{short_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-django-stubs
Requires:       python-django-stubs-ext
Requires:       python-requests
Requires:       python-types-PyYAML
Requires:       python-types-requests
Requires:       python-typing_extensions
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module django-stubs-ext}
BuildRequires:  %{python_module django-stubs}
BuildRequires:  %{python_module pytest-mypy-plugins}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module types-PyYAML}
BuildRequires:  %{python_module types-requests}
BuildRequires:  %{python_module typing_extensions}
%endif
%python_subpackages

%description
Mypy stubs for Django REST Framework. Supports Python 3.10 and up.

%prep
%autosetup -p1 -n %{short_name}-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/rest_framework-stubs
%python_expand %fdupes %{buildroot}%{$python_sitelib}/mypy_drf_plugin
%endif

%check
%if %{with test}
%python_expand PYTHONPATH=$PWD
%pytest --mypy-only-local-stub
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/rest_framework-stubs
%{python_sitelib}/%{package_name}-%{version}.*-info
%{python_sitelib}/mypy_drf_plugin
%endif

%changelog
