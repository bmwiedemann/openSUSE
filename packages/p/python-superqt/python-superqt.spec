#
# spec file for package python-superqt
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


Name:           python-superqt
Version:        0.6.7
Release:        0
Summary:        Missing widgets and components for PyQt/PySide
License:        BSD-3-Clause
URL:            https://github.com/pyapp-kit/superqt
Source:         https://files.pythonhosted.org/packages/source/s/superqt/superqt-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-QtPy >= 1.1.0
Requires:       python-pygments >= 2.4.0
Requires:       python-typing-extensions >= 3.7.4.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pint}
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module QtPy >= 1.1.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pygments >= 2.4.0}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.3}
BuildRequires: python3-pyside2
BuildRequires: python3-pyside6
#BuildRequires:  %%{python_module cmap}
#BuildRequires:  %%{python_module pyconify}
# /SECTION
%python_subpackages

%description
superqt provides a variety of widgets that are not included in the native
QtWidgets module, including multihandle (range) sliders, comboboxes, and more.

%prep
%autosetup -p1 -n superqt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip flaky tests marked @skip_on_ci by upstream
export CI=1
for PYTEST_QT_API in pyqt5 pyqt6; do
  export PYTEST_QT_API
  %pytest
done
# The pysides are only for the primary python
for PYTEST_QT_API in pyside2 pyside6; do
  export PYTEST_QT_API
  %python3_pytest
done

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/superqt
%{python_sitelib}/superqt-%{version}.dist-info

%changelog
