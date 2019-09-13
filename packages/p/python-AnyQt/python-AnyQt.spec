#
# spec file for package python-AnyQt
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
Name:           python-AnyQt
Version:        0.0.10
Release:        0
Summary:        PyQt4/PyQt5 compatibility layer
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/ales-erjavec/anyqt
Source:         https://files.pythonhosted.org/packages/source/A/AnyQt/AnyQt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-qt5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtwebengine-qt5}
# /SECTION
%python_subpackages

%description
PyQt4/PyQt5 compatibility layer.

Features include:

* At the top level, AnyQt exports a Qt5 compatible module namespace along with
  some minimal renames to better support portability between different
  versions.
* The "QT_API" environment variable controls which Qt API/backend is used.
* The API can be chosen/forced programmatically (as long as no
  PyQt4/PyQt5/PySide was already imported).
* An optional compatibility import hook that denies imports from
  conflicting Qt APIs, or intercepts and fakes Qt4 API imports to use a Qt5
  compatible API (some monkey patching is involved).

%prep
%setup -q -n AnyQt-%{version}
rm AnyQt/QtWinExtras.py
rm AnyQt/QtMacExtras.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitelib}/*

%changelog
