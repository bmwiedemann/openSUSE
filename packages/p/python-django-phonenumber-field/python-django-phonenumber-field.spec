#
# spec file for package python-django-phonenumber-field
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python36 1
Name:           python-django-phonenumber-field
Version:        5.1.0
Release:        0
Summary:        International phone number field for django models
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/stefanfoulis/django-phonenumber-field
Source:         https://files.pythonhosted.org/packages/source/d/django-phonenumber-field/django-phonenumber-field-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel
Requires:       python-Django >= 2.2
Requires:       python-phonenumbers >= 7.0.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module phonenumbers}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
An international phone number field for django models.

%prep
%setup -q -n django-phonenumber-field-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -m django test --settings=tests.settings

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
