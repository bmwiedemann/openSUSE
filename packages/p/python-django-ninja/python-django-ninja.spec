#
# spec file for package python-django-ninja
#
# Copyright (c) 2026 SUSE LLC
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

%define pkgname django_ninja

Name:           python-django-ninja
Version:        1.6.2
Release:        0
Summary:        Django Ninja - Fast Django REST framework
License:        MIT
URL:            https://django-ninja.dev
Source:         https://files.pythonhosted.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.1}
BuildRequires:  %{python_module pydantic >= 2.0}
BuildRequires:  %{python_module django-stubs}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module ruff}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 3.1
Requires:       python-pydantic >= 2.0
Suggests:       python-mkdocs
Suggests:       python-mkdocs-material
Suggests:       python-markdown-include
Suggests:       python-mkdocstrings
Suggests:       python-pre-commit
BuildArch:      noarch
%python_subpackages

%description
Django Ninja is a web framework for building APIs with Django and
Python 3.6+ type hints.

Key features:

- Easy: Designed to be easy to use and intuitive.
- FAST execution: Very high performance thanks to Pydantic and async support.
- Fast to code: Type hints and automatic docs lets you focus only on business
  logic.
- Standards-based: Based on the open standards for APIs: OpenAPI (previously
  known as Swagger) and JSON Schema.
- Django friendly: (obviously) has good integration with the Django core and
  ORM.
- Production ready: Used by multiple companies on live projects

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/ninja
%{python_sitelib}/django_ninja-%{version}.dist-info

%changelog
