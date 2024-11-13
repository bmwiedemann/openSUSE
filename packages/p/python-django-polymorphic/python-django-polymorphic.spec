#
# spec file for package python-django-polymorphic
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


Name:           python-django-polymorphic
Version:        3.1
%define twodotsversion 3.1.0
Release:        0
Summary:        Polymorphic inheritance for Django models
License:        BSD-3-Clause
URL:            https://github.com/jazzband/django-polymorphic
Source:         https://github.com/jazzband/django-polymorphic/archive/v%{version}.tar.gz#/django-polymorphic-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#jazzband/django-polymorphic#63d291f8771847e716a37652f239e3966a3360e1
Patch0:         support-new-django.patch
# PATCH-FIX-OPENSUSE Skip two broken tests -- remove when upgrading to 4.0
Patch1:         skip-two-lookup-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.1}
BuildRequires:  %{python_module dj-database-url}
# /SECTION
%python_subpackages

%description
Seamless polymorphic inheritance for Django models.

%prep
%autosetup -p1 -n django-polymorphic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec runtests.py -v 2

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/polymorphic
%{python_sitelib}/django_polymorphic-%{twodotsversion}.dist-info

%changelog
