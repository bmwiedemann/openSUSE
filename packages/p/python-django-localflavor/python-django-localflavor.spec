#
# spec file for package python-django-localflavor
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-django-localflavor
Version:        3.0.1
Release:        0
Summary:        Country-specific Django helpers
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django/django-localflavor
Source:         https://github.com/django/django-localflavor/archive/%{version}.tar.gz#/django-localflavour-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-python-stdnum >= 1.6
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module invoke >= 1.2}
BuildRequires:  %{python_module python-stdnum >= 1.6}
# /SECTION
%python_subpackages

%description
Country-specific Django helpers.

%prep
%setup -q -n django-localflavor-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m invoke test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
