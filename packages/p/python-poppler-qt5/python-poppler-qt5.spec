#
# spec file for package python-poppler-qt5
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{suse_version} < 1550
%{?!use_sip4:%define use_sip4 1}
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
%define pythons python3
Name:           python-poppler-qt5
Version:        0.75.0
Release:        0
Summary:        Python binding to poppler-qt5
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://pypi.org/project/python-poppler-qt5/
Source0:        https://files.pythonhosted.org/packages/source/p/python-poppler-qt5/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM poppler-qt5-pr33-sip5.patch gh#frescobaldi/python-poppler-qt5#33 -- support SIP5
Patch1:         https://github.com/frescobaldi/python-poppler-qt5/pull/33.patch#/poppler-qt5-pr33-sip5.patch
# PATCH-FIX-UPSTREAM poppler-qt5-pr41-sip5.patch gh#frescobaldi/python-poppler-qt5#41 -- use SIP5
Patch2:         https://github.com/frescobaldi/python-poppler-qt5/pull/41.patch#/poppler-qt5-pr41-sip5.patch
BuildRequires:  %{python_module qt5-devel}
%if 0%{?use_sip4}
BuildRequires:  %{python_module sip4-devel}
Requires:       python-sip(api) = %{python_sip_api_ver}
%else
BuildRequires:  %{python_module pyqt-builder}
BuildRequires:  %{python_module sip-devel > 5.3}
%endif
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  python-pyqt-rpm-macros
BuildRequires:  python-rpm-macros
%requires_eq    python-qt5

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

%build
%if 0%{?use_sip4}
export PATH=%{_libdir}/qt5/bin:$PATH
%python_build
%else
%pyqt_build
%endif

%install
%if 0%{?use_sip4}
export PATH=%{_libdir}/qt5/bin:$PATH
%python_install
%else
%pyqt_install
%endif

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c 'import popplerqt5; print(popplerqt5.version())'

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst TODO
%{python_sitearch}/popplerqt5*.so
%{python_sitearch}/python_poppler_qt5-%{version}*-info

%if ! 0%{?use_sip4}
%files %{python_files devel}
%license LICENSE
%{python_sitearch}/PyQt5/bindings/popplerqt5
%{_libqt5_datadir}/qsci/api/python_%{python_bin_suffix}/python-poppler-qt5.api
%endif

%changelog
