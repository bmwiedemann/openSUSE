#
# spec file for package python-defcon
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-defcon
Version:        0.8.1
Release:        0
Summary:        A set of flexible objects for representing UFO data
License:        MIT
URL:            http://code.typesupply.com
Source:         https://files.pythonhosted.org/packages/source/d/defcon/defcon-%{version}.zip
BuildRequires:  %{python_module fs}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 4.10.2
Suggests:       python-fontPens >= 0.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 4.10.2}
BuildRequires:  %{python_module pytest >= 3.0.3}
# /SECTION
%python_subpackages

%description
A set of flexible objects for representing UFO data.

%prep
%setup -q -n defcon-%{version}
sed -i -e '1{\,^#!%{_bindir}/env python,d}' Lib/defcon/test/tools/test_unicodeTools.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license License.txt
%{python_sitelib}/*

%changelog
