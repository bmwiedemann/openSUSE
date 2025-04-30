#
# spec file for package python-drf-standardized-errors
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


Name:           python-drf-standardized-errors
Version:        0.14.1
Release:        0
Summary:        Standardize your API error responses
License:        MIT
URL:            https://github.com/ghazi-git/drf-standardized-errors
Source:         https://files.pythonhosted.org/packages/source/d/drf-standardized-errors/drf_standardized_errors-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/ghazi-git/drf-standardized-errors/pull/96 fix test_openapi_utils
Patch:          fix-test.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module django-filter}
BuildRequires:  %{python_module djangorestframework >= 3.12}
BuildRequires:  %{python_module drf-spectacular >= 0.27.0}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 3.2
Requires:       python-djangorestframework >= 3.12
Suggests:       python-pre-commit
Suggests:       python-sphinx
Suggests:       python-sphinx-autobuild
Suggests:       python-sphinx_rtd_theme >= 1.1.0
Suggests:       python-myst-parser
Suggests:       python-flit
Suggests:       python-keyring
Suggests:       python-tbump
Suggests:       python-drf-spectacular >= 0.27.0
Suggests:       python-inflection
BuildArch:      noarch
%python_subpackages

%description
# DRF Standardized Errors

Standardize your DRF API error responses.

- Highly customizable: gives you flexibility to define your own standardized error responses and override
specific aspects the exception handling process without having to rewrite everything.
- Supports nested serializers and ListSerializer errors
- Plays nicely with error monitoring tools (like Sentry, ...)

%prep
%autosetup -p1 -n drf_standardized_errors-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest

%files %{python_files}
%{python_sitelib}/drf_standardized_errors
%{python_sitelib}/drf_standardized_errors-%{version}.dist-info

%changelog
