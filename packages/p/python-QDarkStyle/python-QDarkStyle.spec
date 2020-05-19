#
# spec file for package python-QDarkStyle
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define         X_display         ":98"
Name:           python-QDarkStyle%{psuffix}
Version:        2.8.1
Release:        0
Summary:        A dark stylesheet for Python and Qt applications
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source:         https://github.com/ColinDuquesnoy/QDarkStyleSheet/archive/v%{version}.tar.gz#/QDarkStyle-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-QtPy >= 1.9
Requires:       python-helpdev >= 0.6.10
Requires:       python-setuptools
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module QDarkStyle = %{version}}
BuildRequires:  %{python_module QtPy >= 1.9}
BuildRequires:  %{python_module helpdev >= 0.6.10}
BuildRequires:  %{python_module pyside2}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  xvfb-run
%endif
%python_subpackages

%description
QDarkStyle is a dark stylesheet for Python and Qt applications.

%prep
%setup -q -n QDarkStyleSheet-%{version}
sed -i '1{\,^#!%{_bindir}/env python,d}' qdarkstyle/*.py qdarkstyle/utils/*.py

%build
%if !%{with test}
%python_build
%endif

%if %{with test}
%check
export LANG=C.UTF-8
export PYTHONDONTWRITEBYTECODE=1

%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run $python example/example.py --qt_from=pyqt5 --test
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run $python example/example.py --qt_from=pyqt5 --test --no_dark
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run $python example/example.py --qt_from=pyside2 --test
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run $python example/example.py --qt_from=pyside2 --test --no_dark
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if !%{with test}
%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.rst
%{_bindir}/qdarkstyle
%{python_sitelib}/qdarkstyle
%{python_sitelib}/QDarkStyle-*.egg-info
%endif

%changelog
