#
# spec file for package python-djangorestframework-simplejwt
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
%define skip_python2 1
Name:           python-djangorestframework-simplejwt
Version:        4.6.0
Release:        0
Summary:        JSON Web Token authentication for Django REST Framework
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/davesque/django-rest-framework-simplejwt
Source:         https://github.com/davesque/django-rest-framework-simplejwt/archive/v%{version}.tar.gz#/djangorestframework_simplejwt-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/jazzband/django-rest-framework-simplejwt/commit/ae1ea58daacb76a1d72e202198734053022a6efe Support jwt 2
Patch0:         jwt2.patch
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT
Requires:       python-djangorestframework
Recommends:     python-python-jose
BuildArch:      noarch
%python_subpackages

%description
A minimal JSON Web Token authentication plugin for the Django REST Framework.

%prep
%setup -q -n django-rest-framework-simplejwt-%{version}
%autopatch -p1

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE.txt licenses/*
%doc README.rst CHANGELOG.md
%{python_sitelib}/*

%changelog
