#
# spec file for package python-django-stubs
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
%{?sle15_python_module_pythons}
%define short_name django-stubs
Name:           python-django-stubs%{psuffix}
Version:        5.2.9
Release:        0
Summary:        PEP-484 stubs for Django
License:        MIT
URL:            https://github.com/typeddjango/django-stubs/
Source:         %{short_name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
%if %{with test}
BuildRequires:  %{python_module Django >= 5.0}
BuildRequires:  %{python_module django-stubs = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mypy-plugins}
BuildRequires:  %{python_module pytest-shard}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module types-PyYAML}
BuildRequires:  %{python_module redis}
# Not needed since python-redis is >= 5.0.0
# BuildRequires:  % {python_module types-redis}
%endif
BuildRequires:  gdal-devel
BuildRequires:  fdupes
Requires:       python-Django >= 5.0
Requires:       python-types-PyYAML
Requires:       python-django-stubs-ext
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
This package contains type stubs and a custom mypy plugin to provide more precise static types and type inference for
Django framework. Django uses some Python "magic" that makes having precise types for some code patterns problematic.
This is why we need this project. The final goal is to be able to get precise types for most common patterns.

%package ext
Summary:       Extensions and monkey-patching for django-stubs 

%description ext
This package contains extensions and monkey-patching functions for the django-stubs package. Certain features of
django-stubs (i.e. generic django classes that don't define the "__class_getitem__" method) require runtime
monkey-patching, which can't be done with type stubs. These extensions were split into a separate package so library
consumers don't need mypy as a runtime dependency (https://github.com/typeddjango/django-stubs/pull/526).

%prep
%autosetup -p1 -n %{short_name}-%{version}

%build
%pyproject_wheel
cd ext; %pyproject_wheel

%install
%if !%{with test}
%pyproject_install
cd ext; %pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{short_name}
%python_expand %fdupes %{buildroot}%{$python_sitelib}/django_stubs_ext
%python_expand %fdupes %{buildroot}%{$python_sitelib}/mypy_django_plugin
%endif

%check
%if %{with test}
# models_triple_circular_reference and from_queryset_with_manager_in_another_directory_and_imports fail because of https://github.com/typeddjango/django-stubs/pull/2744, which is huge
%pytest -k "not (models_triple_circular_reference or from_queryset_with_manager_in_another_directory_and_imports)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/%{short_name}
%{python_sitelib}/django_stubs-%{version}.dist-info
%{python_sitelib}/mypy_django_plugin

%files %{python_files ext}
%{python_sitelib}/django_stubs_ext
%{python_sitelib}/django_stubs_ext-%{version}.dist-info
%endif

%changelog

