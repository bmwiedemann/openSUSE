#
# spec file for package python-kitchen
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


Name:           python-kitchen
Version:        1.2.6
Release:        0
Summary:        Kitchen contains a cornucopia of useful code
License:        LGPL-2.1-or-later
URL:            https://github.com/fedora-infra/kitchen/
Source:         https://files.pythonhosted.org/packages/source/k/kitchen/kitchen-%{version}.tar.gz
# https://github.com/fedora-infra/kitchen/pull/33
Patch0:         python-kitchen-remove-nose.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A bunch of useful python functions to be used in other projects.

%prep
%autosetup -p1 -n kitchen-%{version}
sed -i '1s/^#!.*//' kitchen2/kitchen/pycompat24/base64/_base64.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG='en_US.UTF8'
pushd kitchen3
%pytest -k 'not (test_internal_generate_combining_table or test_easy_gettext_setup_non_unicode or test_invalid_fallback_no_raise or test_lgettext or test_lngettext)'

%files %{python_files}
%license COPYING COPYING.LESSER
%doc NEWS.rst README.rst
%{python_sitelib}/kitchen
%{python_sitelib}/kitchen-%{version}.dist-info

%changelog
