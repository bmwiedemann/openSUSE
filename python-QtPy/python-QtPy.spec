#
# spec file for package python-QtPy
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
Name:           python-QtPy
Version:        1.9.0
Release:        0
Summary:        Abstraction layer on top of Qt bindings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/qtpy
Source:         https://files.pythonhosted.org/packages/source/Q/QtPy/QtPy-%{version}.tar.gz
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       python-qt5
Requires:       python-sip
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
QtPy (pronounced 'cutie pie') is a small abstraction layer that lets you
write applications using a single api call to either PyQt or PySide.

It provides support for PyQt5, PyQt4 and PySide using the PyQt5 layout (where
the QtGui module has been split into QtGui and QtWidgets).

Basically, you write your code as if you were using PyQt5 but import qt from
`qtpy` instead of `PyQt5`.

%prep
%setup -q -n QtPy-%{version}
sed -i 's/\r$//' LICENSE.txt

%build
%python_build

%install
%python_install
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/qtpy/tests/runtests.py
sed -i "s|^#!%{_bindir}/env python$|#!%__$python|" %{buildroot}%{$python_sitelib}/qtpy/tests/runtests.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/qtpy/tests/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/qtpy/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export QT_HASH_SEED=0
export PYTHONDONTWRITEBYTECODE=1
mkdir empty
pushd empty
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run --server-args="-screen 0 1920x1080x24" py.test-%{$python_bin_suffix} ../qtpy/tests/
}
popd

%files %{python_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
