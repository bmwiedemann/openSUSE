#
# spec file for package python-social-auth-app-django
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-social-auth-app-django
Version:        5.5.1
Release:        0
Summary:        Python Social Authentication, Django integration
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-social-auth/social-app-django
Source:         https://files.pythonhosted.org/packages/source/s/social_auth_app_django/social_auth_app_django-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 5.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module social-auth-core >= 4.4.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 5.1
Requires:       python-social-auth-core >= 4.4.0
BuildArch:      noarch
%python_subpackages

%description
This is the Django component of the python-social-auth ecosystem,
it implements the needed functionality to integrate social-auth-core
in a Django based project.

%prep
%setup -q -n social_auth_app_django-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%python_exec manage.py test --verbosity 2

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/social_django/
%{python_sitelib}/social_auth_app_django-*/

%changelog
