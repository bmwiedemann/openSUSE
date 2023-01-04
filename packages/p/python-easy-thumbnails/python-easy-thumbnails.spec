#
# spec file for package python-easy-thumbnails
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-easy-thumbnails
Version:        2.8.4
Release:        0
Summary:        Easy thumbnails for Django
License:        BSD-2-Clause
URL:            https://github.com/SmileyChris/easy-thumbnails
Source:         https://files.pythonhosted.org/packages/source/e/easy-thumbnails/easy-thumbnails-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-Pillow
Requires:       python-lxml
Requires:       python-reportlab
Requires:       python-svglib
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cssselect2}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module svglib}
# /SECTION
%python_subpackages

%description
The powerful, yet easy to implement thumbnailing application for Django.

%prep
%setup -q -n easy-thumbnails-%{version}
sed -i '1 { /^#!/ d }' easy_thumbnails/tests/mock*.py
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# this runs 119 tests, which pyunittest or pytest won't make
export DJANGO_SETTINGS_MODULE='easy_thumbnails.tests.settings'
export PYTHONPATH=${PWD}
%python_exec -m django test -v 2

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
