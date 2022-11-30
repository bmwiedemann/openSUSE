#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%if "%{flavor}" == "test-pyqt5"
%define psuffix -%{flavor}
%define test_qtapi pyqt5
%bcond_without test
BuildRequires:  %{python_module qt5}
BuildConflicts: %{python_module PyQt6}
BuildConflicts: %{python_module pyside2}
BuildConflicts: %{python_module pyside6}
%endif
%if "%{flavor}" == "test-pyqt6"
%define psuffix -%{flavor}
%define test_qtapi pyqt6
%bcond_without test
BuildRequires:  %{python_module PyQt6}
BuildConflicts: %{python_module pyside2}
BuildConflicts: %{python_module pyside6}
BuildConflicts: %{python_module qt5}
%endif
%if "%{flavor}" == "test-pyside2"
%define psuffix -%{flavor}
# pyside is for the primary python3 flavor only
%define pythons python3
%define test_qtapi pyside2
%bcond_without test
BuildRequires:  %{python_module pyside2}
BuildConflicts: %{python_module PyQt6}
BuildConflicts: %{python_module pyside6}
BuildConflicts: %{python_module qt5}
%endif
%if "%{flavor}" == "test-pyside6"
%define psuffix -%{flavor}
# pyside is for the primary python3 flavor only
%define pythons python3
%define test_qtapi pyside6
%bcond_without test
BuildRequires:  %{python_module pyside6}
BuildConflicts: %{python_module PyQt6}
BuildConflicts: %{python_module pyside2}
BuildConflicts: %{python_module qt5}
%endif

Name:           python-pytest-qt%{psuffix}
Version:        4.2.0
Release:        0
Summary:        Pytest support for PyQt and PySide applications
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest-qt
Source:         https://files.pythonhosted.org/packages/source/p/pytest-qt/pytest-qt-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210608
# https://github.com/pytest-dev/pytest-qt/issues/317
Requires:       bitstream-vera-fonts
Requires:       python-pytest >= 3.0
Suggests:       python-PyQt6
Suggests:       python-pyside2
Suggests:       python-pyside6
Suggests:       python-qt5
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Requires:       (python-qt5 or python-PyQt6 or python3-pyside2 or python3-pyside6)
%else
Requires:       (python-qt5 or python-PyQt6)
%endif
%if %{with test}
BuildRequires:  %{python_module pytest-qt = %{version}}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Pytest-qt is a pytest plugin that allows programmers to write tests
for PySide and PyQt applications.

The main usage is to use the `qtbot` fixture, responsible for handling `qApp`
creation as needed and provides methods to simulate user interaction,
like key presses and mouse clicks.

%prep
%setup -q -n pytest-qt-%{version}
dos2unix LICENSE

%if ! %{with test}
%build
%python_build
%endif

%if ! %{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export QT_QPA_PLATFORM=offscreen
export PYTEST_QT_API=%{test_qtapi}
%pytest
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/pytestqt
%{python_sitelib}/pytest_qt-%{version}-py*.egg-info
%endif

%changelog
