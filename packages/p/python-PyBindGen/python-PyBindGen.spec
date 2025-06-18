#
# spec file for package python-PyBindGen
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


Name:           python-PyBindGen
Version:        0.22.1
Release:        0
Summary:        Python Bindings Generator
License:        LGPL-2.1-only
Group:          Development/Libraries/Python
URL:            https://github.com/gjcarneiro/pybindgen
Source0:        https://pypi.io/packages/source/P/PyBindGen/PyBindGen-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A tool to generate Python bindings for C/C++ code.

%prep
%setup -q -n PyBindGen-%{version}
# Remove some pointless she-bangs
find pybindgen/ -iname \*.py -exec sed -ie '1 { \#/usr/bin# d }' '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%files %{python_files}
%license COPYING
%{python_sitelib}/pybindgen
%{python_sitelib}/[Pp]y[Bb]ind[Gg]en-%{version}.dist-info

%changelog
