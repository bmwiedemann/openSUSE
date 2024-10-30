#
# spec file for package python-tabula-py
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
Name:           python-tabula-py
Version:        2.10.0
Release:        0
Summary:        Simple wrapper for tabula-java, read tables from PDF into DataFrame
License:        MIT
URL:            https://github.com/chezou/tabula-py
Source:         https://files.pythonhosted.org/packages/source/t/tabula-py/tabula_py-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module JPype1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas >= 0.25.3}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-distro
Requires:       python-numpy
Requires:       python-pandas >= 0.25.3
BuildArch:      noarch
%python_subpackages

%description
tabula-py is a simple Python wrapper of tabula-java, which can read tables in a PDF. You can read tables
from a PDF and convert them into a pandas DataFrame. tabula-py also enables you to convert a PDF file into
a CSV, a TSV or a JSON file.

%prep
%autosetup -p1 -n tabula_py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (remote or test_read_pdf_with_silent_true)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/tabula
%{python_sitelib}/tabula_py-%{version}*-info

%changelog
