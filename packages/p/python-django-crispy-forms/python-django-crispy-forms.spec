#
# spec file for package python-django-crispy-forms
#
# Copyright (c) 2024 SUSE LLC
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
# Multibuild: break cycles with crispy-bootstrap{3,4,5}
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define mod_name django_crispy_forms
%{?sle15_python_module_pythons}
Name:           python-django-crispy-forms%{psuffix}
Version:        2.3
Release:        0
Summary:        Django DRY Forms
License:        MIT
URL:            https://github.com/maraujop/django-crispy-forms
Source:         https://files.pythonhosted.org/packages/source/d/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module crispy-bootstrap3}
BuildRequires:  %{python_module crispy-bootstrap4}
BuildRequires:  %{python_module crispy-bootstrap5}
BuildRequires:  %{python_module django-crispy-forms = %{version}}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
%endif
Requires:       python-Django >= 4.2
Recommends:     python-crispy-bootstrap3
Recommends:     python-crispy-bootstrap4
Recommends:     python-crispy-bootstrap5
BuildArch:      noarch
%python_subpackages

%description
A module to build programmatic reusable layouts out of components
with control over the rendered HTML without writing HTML in
templates, and without breaking the standard way of doing things in
Django.

%prep
%setup -q -n %{mod_name}-%{version}

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
export DJANGO_SETTINGS_MODULE=tests.test_settings
export PYTHONPATH=${PWD}
%pytest -rs tests/
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CONTRIBUTORS.txt README.rst
%{python_sitelib}/*crispy[-_]forms*/
%endif

%changelog
