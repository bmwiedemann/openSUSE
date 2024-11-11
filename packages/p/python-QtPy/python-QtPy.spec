#
# spec file for package python-QtPy
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
BuildArch:      noarch
%endif
%bcond_without pyqt5
%bcond_without pyqt6
%ifnarch %power64 s390x
%bcond_without pyside2
%bcond_without pyside6
%else
%bcond_with pyside2
%bcond_with pyside6
%endif
# make sure using pytest-3.11 on Leap 15.6
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150500
%define python3_bin_suffix 3.11
%endif
%{?sle15_python_module_pythons}
Name:           python-QtPy%{psuffix}
Version:        2.4.2
Release:        0
Summary:        Abstraction layer on top of Qt bindings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/qtpy
Source:         https://files.pythonhosted.org/packages/source/Q/QtPy/qtpy-%{version}.tar.gz
# from https://github.com/spyder-ide/qtpy/pull/466
Patch1:         qt6.6-deprecations.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Note: Don't add any Requires, Recommends, or Suggests for a
# specific backend here, because we need to minimize the space
# occupied on the Tumbleweed DVD. The application importing QtPy
# will have to know what backend to recommend and what extras to
# require (e.g. qtwebengine). Note that setup.py does not declare
# any requirements, in this regard either.
%if %{with test}
BuildRequires:  %{python_module QtPy-test = %{version}}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-qt}
%if %{with pyqt5}
BuildRequires:  %{python_module qt3d-qt5}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtcharts-qt5}
BuildRequires:  %{python_module qtdatavis3d-qt5}
%ifnarch %{power64} s390x
BuildRequires:  %{python_module qtwebengine-qt5}
%endif
%endif
%if %{with pyqt6}
BuildRequires:  %{python_module PyQt6-3D}
BuildRequires:  %{python_module PyQt6-Charts}
BuildRequires:  %{python_module PyQt6-DataVisualization}
BuildRequires:  %{python_module PyQt6}
BuildRequires:  qt6-sql-sqlite
%ifnarch %{ix86} %{arm} %{power64} s390x
# QtWebEngine 6.3.0 ceased support for 32-bit
BuildRequires:  %{python_module PyQt6-WebEngine}
%endif
%endif
%if %{with pyside2}
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150500
BuildRequires:  %{python_module pyside2}
%else
BuildRequires:  python3-pyside2
%endif
%endif
%if %{with pyside6}
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150500
BuildRequires:  %{python_module pyside6}
%else
BuildRequires:  python3-pyside6 > 6.8.0
%endif
BuildRequires:  qt6-sql-sqlite
%endif
%endif
%python_subpackages

%description
QtPy is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt6, PySide6, PySide2 using the Qt5
layout (where the QtGui module has been split into QtGui and QtWidgets).
Basically, you can write your code as if you were using PyQt or PySide
directly, but import Qt modules from qtpy instead of PyQt5, PySide2,
PyQt6 or PySide6.

%package test
Summary:        The qtpy.tests module
Requires:       %{name} = %{version}

%description test
QtPy is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

This subpackage separately provides the qtpy.tests module
in order to avoid stupid rpmlint errors.

%prep
%autosetup -p1 -n qtpy-%{version}
# wrong EOL encondig
sed -i 's/\r$//' LICENSE.txt *.md
# qtcharts is present in our PyQt
sed -i '/skipif.*not PYSIDE2/ d' qtpy/tests/test_qtcharts.py
sed -i '/addopts/ {s/--cov=.*//; s/--color=yes//}' pytest.ini

%build
%if ! %{with test}
%pyproject_wheel
%endif

%install
%if ! %{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/qtpy
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export QT_HASH_SEED=0
export QT_QPA_PLATFORM="offscreen"
mkdir empty
pushd empty
# expects an unset FORCE_QT_API
donttest_qt_api="test_qt_api_environ"
# too wide in our setup (and upstream doesn't care: https://github.com/spyder-ide/qtpy/issues/371)
donttest=" or test_qfontmetrics_width"
%ifarch %{arm} aarch64
# no QtOpenGL for these platforms
donttest+=" or test_qtopengl"
%endif
%if %{with pyqt5}
# no QtSensors in our PyQt5
donttest_pyqt5=" or test_qtsensors"
%ifarch %{power64} s390x
# No QtWebengine on ppc and s390x
donttest_pyqt5="${donttest_pyqt5} or test_qtwebengine or test_qt_api"
%endif
export QT_API=pyqt5 FORCE_QT_API=1
%pytest -rwEfs -v ../qtpy -k "not ($donttest_qt_api $donttest $donttest_pyqt5)"
%endif
%if %{with pyqt6}
%ifarch %{ix86} %{arm} %{power64} s390x
# QtWebEngine 6.3.0 ceased support for 32-bit
# No QtWebengine on ppc and s390x
donttest_pyqt6=" or test_qtwebengine"
%endif
export QT_API=pyqt6 FORCE_QT_API=1
%pytest -rwEfs -v ../qtpy -k "not ($donttest_qt_api $donttest $donttest_pyqt6)"
%endif
%if %{with pyside2}
export QT_API=pyside2 FORCE_QT_API=1
pytest-%{python3_bin_suffix} -rwEfs -v ../qtpy -k "not ($donttest_qt_api $donttest)"
%endif
%if %{with pyside6}
# no pyside6-uic
donttest_pyside6=" or test_load_ui_type"
export QT_API=pyside6 FORCE_QT_API=1
pytest-%{python3_bin_suffix} -rwEfs -v ../qtpy -k "not ($donttest_qt_api $donttest $donttest_pyside6)"
%endif
# Default backend
unset QT_API
unset FORCE_QT_API
%pytest -rwEfs -vvv ../qtpy -k "not (dummyprefix $donttest $donttest_pyqt5)"
popd
%endif

%post
%python_install_alternative qtpy

%postun
%python_uninstall_alternative qtpy

%if ! %{with test}
%files %{python_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/qtpy
%exclude %{python_sitelib}/qtpy/tests
%{python_sitelib}/QtPy-%{version}.dist-info
%python_alternative %{_bindir}/qtpy

%files %{python_files test}
%license LICENSE.txt
%{python_sitelib}/qtpy/tests
%endif

%changelog
