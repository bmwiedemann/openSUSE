#
# spec file for package python-reportlab
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
%define oldpython python
Name:           python-reportlab
Version:        3.5.59
Release:        0
Summary:        The Reportlab Toolkit
License:        BSD-3-Clause
URL:            https://www.reportlab.com/
Source0:        https://files.pythonhosted.org/packages/source/r/reportlab/reportlab-%{version}.tar.gz
Source1:        encryption.gif
Patch0:         reportlab-missing-includes.patch
BuildRequires:  %{python_module Pillow >= 4.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 4.0.0
Provides:       python-ReportLab = %{version}
Obsoletes:      python-ReportLab < %{version}
%ifpython2
Obsoletes:      %{oldpython}-ReportLab < %{version}
Provides:       %{oldpython}-ReportLab = %{version}
%endif
%python_subpackages

%description
The ReportLab Toolkit. An Open Source Python library for generating PDFs and graphics.

%prep
%setup -q -n reportlab-%{version}
%autopatch -p1
sed -i "1d" src/reportlab/lib/{formatters,fonts,corp,units,pagesizes,__init__,randomtext,logger,normalDate}.py
sed -i "1d" src/reportlab/graphics/{widgets/table,barcode/test,testdrawings,testshapes}.py # Fix non-executable bits

%build
export CFLAGS="%{optflags}"
%python_build --no-download-t1-files

PYTHONPATH=$(readlink -f build/lib.linux-*/) \
    python3 docs/genAll.py

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CFLAGS="%{optflags}"
export LANG=en_US.UTF-8
pushd tests
# make online tests offline
cp %{SOURCE1} .
sed -i 's@http://www.reportlab.com/rsrc/@@' test_*.py
###
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python runAll.py
}

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.md README.txt docs/reportlab-userguide.pdf
%{python_sitearch}/reportlab/
%{python_sitearch}/reportlab-%{version}-py*.egg-info

%changelog
