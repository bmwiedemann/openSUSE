#
# spec file for package python-djangorestframework
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-djangorestframework%{psuffix}
Version:        3.11.2
Release:        0
Summary:        A REST Framework for Django
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://django-rest-framework.org/
Source:         https://github.com/encode/django-rest-framework/archive/%{version}.tar.gz#/djangorestframework-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Recommends:     python-Markdown
Recommends:     python-Pygments
Recommends:     python-coreapi
Recommends:     python-coreschema
Recommends:     python-requests
Suggests:       python-psycopg2
Provides:       python-django-rest-framework = %{version}
Obsoletes:      python-django-rest-framework < %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Markdown >= 2.6.11}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module coreapi >= 2.3.1}
BuildRequires:  %{python_module coreschema >= 0.0.4}
BuildRequires:  %{python_module django-guardian >= 2.2.0}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pytest-django >= 3.9.0}
BuildRequires:  python3-django-filter >= 1.1.0
%endif
%python_subpackages

%description
Django REST framework is a library for building Web APIs. It is
modular and the architecture can be customized, based on Django's
class based views.

Web APIs built using REST framework are fully self-describing and web
browseable. It also supports a wide range of media types,
authentication and permission policies out of the box.

%prep
%setup -q -n django-rest-framework-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.md
%{python_sitelib}/*
%endif

%changelog
