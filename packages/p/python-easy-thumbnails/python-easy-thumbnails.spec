#
# spec file for package python-easy-thumbnails
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
Name:           python-easy-thumbnails
Version:        2.7
Release:        0
Summary:        Easy thumbnails for Django
License:        BSD-2-Clause
URL:            https://github.com/SmileyChris/easy-thumbnails
Source:         https://files.pythonhosted.org/packages/source/e/easy-thumbnails/easy-thumbnails-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-Pillow
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module Pillow}
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
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
