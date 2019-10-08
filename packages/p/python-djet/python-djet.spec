#
# spec file for package python-djet
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-djet
Version:        0.2.2
Release:        0
Summary:        Set of helpers for easy testing of Django apps
License:        MIT
URL:            https://github.com/sunscrapers/djet
Source:         https://github.com/sunscrapers/djet/archive/%{version}.tar.gz#/djet-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module djangorestframework}
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
%setup -q -n djet-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd testproject/
export DJANGO_SETTINGS_MODULE=settings
# test_make_inmemory_image_should_pass fails on s390x and ppc64
# PIL/ImageFile.py:496: SystemError: tile cannot extend outside image
# https://github.com/sunscrapers/djet/issues/31
%pytest -k 'not test_make_inmemory_image_should_pass'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
