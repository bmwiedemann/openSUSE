#
# spec file for package python-reportlab
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-reportlab
Version:        4.4.4
Release:        0
Summary:        The Reportlab Toolkit
License:        BSD-3-Clause
URL:            https://www.reportlab.com/
Source0:        https://files.pythonhosted.org/packages/source/r/reportlab/reportlab-%{version}.tar.gz
Source1:        encryption.gif
BuildRequires:  %{python_module Pillow >= 9.0.0}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module charset-normalizer}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 9.0.0
Requires:       python-charset-normalizer
Provides:       python-ReportLab = %{version}
Obsoletes:      python-ReportLab < %{version}
%ifpython2
Obsoletes:      %{oldpython}-ReportLab < %{version}
Provides:       %{oldpython}-ReportLab = %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
The ReportLab Toolkit. An Open Source Python library for generating PDFs and graphics.

%prep
%autosetup -p1 -n reportlab-%{version}
sed -i "1d" src/reportlab/lib/{formatters,fonts,corp,units,pagesizes,__init__,randomtext,logger,normalDate}.py
sed -i "1d" src/reportlab/graphics/{widgets/table,barcode/test,testdrawings,testshapes}.py # Fix non-executable bits

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

mypython=%{expand:%%__%(pythons="%{pythons}"; echo ${pythons##python* })}
PYTHONPATH=src $mypython docs/genAll.py

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
export PYTHONPATH=%{buildroot}%{python_sitelib}
( cd docs/userguide && python3 genuserguide.py )

%check
export CFLAGS="%{optflags}"
export LANG=en_US.UTF-8
pushd tests
# make online tests offline
cp %{SOURCE1} .
sed -i 's@http://www.reportlab.com/rsrc/@@' test_*.py
###
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python runAll.py --verbosity=2
}

%files %{python_files}
%license LICENSE
%doc CHANGES.md README.txt docs/reportlab-userguide.pdf
%{python_sitelib}/reportlab/
%{python_sitelib}/reportlab-%{version}.dist-info

%changelog
