#
# spec file for package python-easy-thumbnails
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


Name:           python-easy-thumbnails
Version:        2.10
Release:        0
Summary:        Easy thumbnails for Django
License:        BSD-2-Clause
URL:            https://github.com/SmileyChris/easy-thumbnails
Source:         https://files.pythonhosted.org/packages/source/e/easy_thumbnails/easy_thumbnails-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/SmileyChris/easy-thumbnails/pull/650 Add support for Python 3.13
Patch:          py313.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 4.2
Requires:       python-Pillow
Recommends:     python-reportlab
Recommends:     python-svglib
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 4.2}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module svglib}
BuildRequires:  %{python_module testfixtures}
# /SECTION
%python_subpackages

%description
The powerful, yet easy to implement thumbnailing application for Django.

%prep
%autosetup -p1 -n easy_thumbnails-%{version}
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
# skip two non-functioning optimize tests https://github.com/SmileyChris/easy-thumbnails/issues/652
sed -i '/^.*optimize.*$/d' easy_thumbnails/tests/settings.py
%python_exec -m django test -v 2

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/easy_thumbnails
%{python_sitelib}/easy_thumbnails-%{version}*info

%changelog
