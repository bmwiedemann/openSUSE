#
# spec file for package python-djangorestframework-simplejwt
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


%{?sle15_python_module_pythons}
Name:           python-djangorestframework-simplejwt
Version:        5.3.1
Release:        0
Summary:        JSON Web Token authentication for Django REST Framework
License:        MIT
URL:            https://github.com/davesque/django-rest-framework-simplejwt
Source:         https://files.pythonhosted.org/packages/source/d/djangorestframework-simplejwt/djangorestframework_simplejwt-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n djangorestframework_simplejwt-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE.txt licenses/*
%doc README.rst CHANGELOG.md
%{python_sitelib}/rest_framework_simplejwt
%{python_sitelib}/djangorestframework_simplejwt-%{version}.dist-info

%changelog
