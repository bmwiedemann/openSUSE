#
# spec file for package python-djet
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-djet
Version:        0.3.0
Release:        0
Summary:        Set of helpers for easy testing of Django apps
License:        MIT
URL:            https://github.com/sunscrapers/djet
Source:         https://files.pythonhosted.org/packages/source/d/djet/djet-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#sunscrapers/djet#f97c37afeb1b6f17055d2eebadaa42bc316cd15f
Patch0:         support-public-httpresponse.patch
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-Pillow
Suggests:       python-djangorestframework
BuildArch:      noarch
%python_subpackages

%description
Set of helpers for easy testing of Django apps.

%prep
%autosetup -p1 -n djet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd testproject/
export DJANGO_SETTINGS_MODULE=settings
# test_make_inmemory_image_should_pass fails on s390x and ppc64
# PIL/ImageFile.py:496: SystemError: tile cannot extend outside image
# https://github.com/sunscrapers/djet/issues/31
%pytest -k 'not (test_make_inmemory_image_should_pass or test_listdir_should_return_proper_paths)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/djet
%{python_sitelib}/djet-%{version}.dist-info

%changelog
