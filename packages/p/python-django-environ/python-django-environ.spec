#
# spec file for package python-django-environ
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
Name:           python-django-environ
Version:        0.11.2
Release:        0
Summary:        Django application configuration via environment variables
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/joke2k/django-environ
Source:         https://files.pythonhosted.org/packages/source/d/django-environ/django-environ-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
Django-environ allows utilizing 12factor inspired environment
variables to configure Django applications.

%prep
%setup -q -n django-environ-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/environ
%{python_sitelib}/django_environ-%{version}.dist-info

%changelog
