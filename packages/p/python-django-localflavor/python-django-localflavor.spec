#
# spec file for package python-django-localflavor
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


Name:           python-django-localflavor
Version:        4.0
Release:        0
Summary:        Country-specific Django helpers
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django/django-localflavor
Source:         https://github.com/django/django-localflavor/archive/%{version}.tar.gz#/django-localflavor-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/django/django-localflavor/commit/a0bb1b5b56be1d3f1a4ebb886621961b458ab74e Fix # 502 -- Update Python and Django versions
Patch0:         dj5.patch
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
%autosetup -p1 -n django-localflavor-%{version}

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
%{python_sitelib}/localflavor
%{python_sitelib}/django_localflavor-%{version}*info

%changelog
