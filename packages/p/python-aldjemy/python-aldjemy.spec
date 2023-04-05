#
# spec file for package python-aldjemy
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
%global skip_python36 1
Name:           python-aldjemy
Version:        1.0.0
Release:        0
Summary:        SQLAlchemy to Django integration library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Deepwalker/aldjemy/
Source:         https://files.pythonhosted.org/packages/source/a/aldjemy/aldjemy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-SQLAlchemy >= 1.3.20
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module SQLAlchemy >= 1.3.20}
BuildRequires:  %{python_module django-extensions}
# /SECTION
%python_subpackages

%description
SQLAlchemy to Django integration library.

%prep
%setup -q -n aldjemy-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/test_project/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
cd test_project
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python manage.py migrate
$python manage.py test --no-input
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*aldjemy*/

%changelog
