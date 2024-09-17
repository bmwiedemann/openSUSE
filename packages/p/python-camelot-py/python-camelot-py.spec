#
# spec file for package python-camelot-py
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
Name:           python-camelot-py
Version:        0.11.0
Release:        0
Summary:        PDF Table Extraction for Humans
License:        MIT
URL:            https://github.com/camelot-dev/camelot
Source:         https://github.com/camelot-dev/camelot/archive/refs/tags/v%{version}.tar.gz#/camelot-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module chardet >= 3.0.4}
BuildRequires:  %{python_module click >= 6.7}
BuildRequires:  %{python_module ghostscript >= 0.7}
BuildRequires:  %{python_module numpy >= 1.13.3}
BuildRequires:  %{python_module opencv >= 3.4.2.17}
BuildRequires:  %{python_module openpyxl >= 2.5.8}
BuildRequires:  %{python_module pandas >= 0.23.4}
BuildRequires:  %{python_module pdfminer.six >= 20200726}
BuildRequires:  %{python_module pypdf >= 3.0.0}
BuildRequires:  %{python_module tabulate >= 0.8.9}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 5.4.3}
BuildRequires:  %{python_module pytest-cov >= 2.10.0}
BuildRequires:  %{python_module pytest-mpl >= 0.11}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRequires:  fdupes
Requires:       python-chardet >= 3.0.4
Requires:       python-click >= 6.7
Requires:       python-numpy >= 1.13.3
Requires:       python-openpyxl >= 2.5.8
Requires:       python-pandas >= 0.23.4
Requires:       python-pdfminer.six >= 20200726
Requires:       python-pypdf >= 3.0.0
Requires:       python-tabulate >= 0.8.9
BuildArch:      noarch 
%python_subpackages

%description
Camelot is a Python library that can help you extract tables from PDFs!

%prep
%setup -q -n camelot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/camelot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative camelot

%postun
%python_uninstall_alternative camelot

%check
# Disable tests that require network connection
donttest="test_url_poppler or test_url_ghostscript or test_pages_poppler or test_pages_ghostscript"
# Disable tests that require pdftopng package
donttest+=" or test_repr_poppler or test_lattice_contour_plot_poppler or test_line_plot_poppler or test_joint_plot_poppler or test_grid_plot_poppler"
# Disable test failing due to issue https://github.com/camelot-dev/camelot/issues/480 
donttest+=" or test_cli_output_format"
# Disable tests that fail due to small differences caused by ghostscript version 
# (https://github.com/camelot-dev/camelot/pull/356#issuecomment-1474776857)
donttest+=" or test_lattice_contour_plot_ghostscript or test_joint_plot_ghostscript"
%pytest -k "not ($donttest)"


%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/camelot
%{python_sitelib}/camelot
%{python_sitelib}/camelot_py-%{version}.dist-info

%changelog
