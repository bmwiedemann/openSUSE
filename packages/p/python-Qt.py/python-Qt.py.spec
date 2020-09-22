#
# spec file for package python-Qt.py
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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
Name:           python-Qt.py
Version:        1.3.1
Release:        0
Summary:        Python compat-wrapper around all Qt bindings
License:        MIT
URL:            https://github.com/mottosso/Qt
Source:         https://files.pythonhosted.org/packages/source/Q/Qt.py/Qt.py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-qt5
BuildArch:      noarch
%python_subpackages

%description
Python 2 & 3 compatibility wrapper around all Qt bindings -
PySide, PySide2, PyQt4 and PyQt5."

%prep
%setup -q -n Qt.py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# wrong path
rm -f %{buildroot}%{_prefix}/LICENSE

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
