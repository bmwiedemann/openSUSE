#
# spec file for package python-QtPy
#
# Copyright (c) 2021 SUSE LLC
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
%bcond_without python2
Name:           python-QtPy
Version:        1.11.1
Release:        0
Summary:        Abstraction layer on top of Qt bindings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/qtpy
Source:         https://files.pythonhosted.org/packages/source/Q/QtPy/QtPy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Note: Don't add any Requires, Recommends, or Suggests here,
# because we need to minimize the space occupied on the
# Tumbleweed DVD. The application importing QtPy will have to
# know what backend to recommend and what extras to require (e.g.
# qtwebengine). Note that setup.py does not declare any requirements,
# either.
BuildArch:      noarch
# SECTION test requirements
%if %{with python2}
BuildRequires:  python2-mock
%endif
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt3d-qt5}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtcharts-qt5}
BuildRequires:  %{python_module qtdatavis3d-qt5}
BuildRequires:  %{python_module qtwebengine-qt5}
BuildRequires:  python3-pyside2
BuildRequires:  xvfb-run
# /SECTION
%python_subpackages

%description
QtPy is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout (where
the QtGui module has been split into QtGui and QtWidgets).

Basically, you can write your code as if you were using PySide2 but import Qt
modules from qtpy instead of PySide2 (or PyQt5)

%prep
%setup -q -n QtPy-%{version}
# wrong EOL encondig
sed -i 's/\r$//' LICENSE.txt *.md
# remove mock dependency for Python 3
sed -i '/^import mock/ c try:\
    from unittest import mock\
except ImportError:\
    import mock' qtpy/tests/test_macos_checks.py
# qtcharts is present in our PyQt5 and Pyside2
sed -i '/skipif.*not PYSIDE2/ d' qtpy/tests/test_qtcharts.py
# remove script calling pytest so that pytest does not discover it
rm qtpy/tests/runtests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export QT_HASH_SEED=0
export PYTHONDONTWRITEBYTECODE=1
mkdir empty
pushd empty
%{python_expand # pytest-xvfb unfortunately fails here
export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run --server-args="-screen 0 1920x1080x24" pytest-%{$python_bin_suffix} -rwEfs -v ../qtpy/tests/
}
export QT_API=pyside2 FORCE_QT_API=1
xvfb-run --server-args="-screen 0 1920x1080x24" pytest-%{python3_bin_suffix} -rwEfs -v ../qtpy/tests/
popd

%files %{python_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/qtpy
%{python_sitelib}/QtPy-%{version}-py*.egg-info

%changelog
