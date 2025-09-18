#
# spec file for package python-ghostscript
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


%{?sle15_python_module_pythons}
Name:           python-ghostscript
Version:        0.8.1
Release:        0
License:        GPL-3.0-or-later
Summary:        Python interface to the Ghostscript C-API
Group:          Development/Languages/Python
URL:            https://gitlab.com/pdftools/python-ghostscript
Source:         https://files.pythonhosted.org/packages/source/g/ghostscript/ghostscript-%{version}.tar.gz
Source1:        https://gitlab.com/pdftools/python-ghostscript/-/raw/develop/test/testimage.bmp
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ghostscript >= 9.0.8
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       ghostscript >= 9.0.8
Requires:       python-setuptools
BuildArch:      noarch

%python_subpackages

%description
Python interface to the Ghostscript C-API, both high and low-level, based on ctypes.

%prep
%autosetup -p1 -n ghostscript-%{version}
cp %{SOURCE1} test

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/ghostscript
%{python_sitelib}/ghostscript-%{version}*-info

%changelog
