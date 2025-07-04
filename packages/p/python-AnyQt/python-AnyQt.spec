#
# spec file for package python-AnyQt
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


%{?sle15_python_module_pythons}
%if %{suse_version} > 1600
%bcond_with pyqt5
%bcond_without pyqt6
%else
%bcond_without pyqt5
%bcond_with pyqt6
%endif

Name:           python-AnyQt
Version:        0.2.0
Release:        0
Summary:        PyQt4/PyQt5 compatibility layer
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/ales-erjavec/anyqt
Source:         https://github.com/ales-erjavec/anyqt/archive/refs/tags/%{version}.tar.gz#/AnyQt-%{version}-gh.tar.gz
# PATCH-FIX-SLE do-not-test-pyqt4.patch alarrosa@suse.com -- Do not try testing the PyQt4 api
Patch0:         do-not-test-pyqt4.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-PyQt6
BuildArch:      noarch
# Mirror with qt6-webengine
ExclusiveArch:  aarch64 x86_64 riscv64
# SECTION test requirements
%if %{with pyqt5}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtwebengine-qt5}
%endif
%if %{with pyqt6}
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module PyQt6-WebEngine}
%endif
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xvfb}
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
%autosetup -p1 -n anyqt-%{version}

rm AnyQt/QtWinExtras.py
rm AnyQt/QtMacExtras.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we do not test pyside2 anymore
# TODO enable pyside6, which is in the module but maybe not up to date
qtset=""
%if %{with pyqt5}
qtset+=" pyqt5"
%endif
%if %{with pyqt6}
qtset+=" pyqt6"
%endif
for q in $qtset; do
  export QT_API=$q
  %pytest --ignore test/
done
# this doesn't return error codes, check output manually
unset QT_API
%python_exec test/test_import.py

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitelib}/AnyQt
%{python_sitelib}/[aA]ny[qQ]t-%{version}.dist-info

%changelog
