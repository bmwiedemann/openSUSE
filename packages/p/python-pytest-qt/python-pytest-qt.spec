#
# spec file for package python-pytest-qt
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
Name:           python-pytest-qt
Version:        3.3.0
Release:        0
Summary:        Pytest support for PyQt and PySide applications
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/pytest-dev/pytest-qt
Source:         https://files.pythonhosted.org/packages/source/p/pytest-qt/pytest-qt-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.0
Requires:       python-qt5
# https://github.com/pytest-dev/pytest-qt/issues/317
Requires:       free-ttf-fonts
BuildArch:      noarch
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_QT_API=pyqt5
# test_qt_api_ini_config* needs the qt4 and pyside/etc
# test_wait_window fails randomly on OBS
%pytest -k 'not (test_qt_api_ini_config or test_wait_window)'

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/pytestqt
%{python_sitelib}/pytest_qt-%{version}-py*.egg-info

%changelog
