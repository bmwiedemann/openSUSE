#
# spec file for package python-django-dropulous
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-django-dropulous
Version:        0.1.1
Release:        0
Summary:        Django form widgets for Dropulous
License:        BSD-3-Clause
URL:            https://radiac.net/projects/django-dropulous/
Source:         https://github.com/radiac/django-dropulous/archive/refs/tags/v%{version}.tar.gz#/django_dropulous-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 3.2
BuildArch:      noarch
%python_subpackages

%description
Django form widgets for Dropulous

%prep
%autosetup -p1 -n django-dropulous-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/django_dropulous
%{python_sitelib}/django_dropulous-%{version}.dist-info

%changelog
