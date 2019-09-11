#
# spec file for package python-pytest-qt
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
Name:           python-pytest-qt
Version:        3.2.2
Release:        0
Summary:        Pytest support for PyQt and PySide applications
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/pytest-dev/pytest-qt
Source:         https://files.pythonhosted.org/packages/source/p/pytest-qt/pytest-qt-%{version}.tar.gz
Patch0:         skip-timeout-tests.patch
BuildRequires:  %{python_module pytest >= 2.7.0}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       python-pytest >= 2.7.0
Requires:       python-qt5
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
%patch0 -p1
dos2unix LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_QT_API=pyqt5
export PYTHONDONTWRITEBYTECODE=1
# skip test_qt_api_ini_config_with_envvar as it needs the qt4 and pyside/etc
# same applies for test_qt_api_ini_config
%{python_expand export PYTHONPATH="%{buildroot}%{$python_sitelib}"
xvfb-run --server-args="-screen 0 1920x1080x24" py.test-%{$python_bin_suffix} -k 'not test_qt_api_ini_config_with_envvar and not test_qt_api_ini_config'
}

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
