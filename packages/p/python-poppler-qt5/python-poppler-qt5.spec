#
# spec file for package python-poppler-qt5
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011 LISA GmbH, Bingen, Germany.
# Copyright (c) 2012 Johannes Engel <jcnengel@gmail.com>
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
Name:           python-poppler-qt5
Version:        21.3.0
Release:        0
Summary:        Python binding to poppler-qt5
License:        LGPL-2.1-or-later
URL:            https://pypi.org/project/python-poppler-qt5/
Source0:        https://files.pythonhosted.org/packages/source/p/python-poppler-qt5/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pyqt-builder}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip-devel > 5.3}
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-qt5 = %(rpm -q --whatprovides python3-qt5 --qf "%%{version}")
%python_subpackages

%description
A Python binding for libpoppler-qt5 that aims for completeness
and for being actively maintained.

%package devel
Summary:        Devel package for %{name}
Group:          Development/Languages/Python
Requires:       libpoppler-qt5-devel
Requires:       python-qt5-devel
Requires:       python-sip-devel

%description devel
A Python binding for libpoppler-qt5 that aims for completeness
and for being actively maintained.

This package contains the SIP and Qscintilla API files to build
python packages using python-poppler

%prep
%autosetup -p1
# use the aliased keyword for subprocess.check_call() that is also known by Python 3.6 gh#frescobaldi/python-poppler-qt5#44
sed -i 's/text=True/universal_newlines=True/' project.py

%build
# https://github.com/frescobaldi/python-poppler-qt5/issues/61
%pyqt_build -s %{quote:--qmake-setting 'CONFIG += c++17'}

%install
%pyqt_install

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c 'import popplerqt5; print(popplerqt5.version())'

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst TODO
%{python_sitearch}/popplerqt5*.so
%{python_sitearch}/python_poppler_qt5-%{version}*-info

%files %{python_files devel}
%license LICENSE
%{python_sitearch}/PyQt5/bindings/popplerqt5
%{_libqt5_datadir}/qsci/api/python_%{python_bin_suffix}/python-poppler-qt5.api

%changelog
