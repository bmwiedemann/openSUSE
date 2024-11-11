#
# spec file for package python-sphinxcontrib-svg2pdfconverter
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
Name:           python-sphinxcontrib-svg2pdfconverter
Version:        1.2.3
Release:        0
Summary:        Sphinx SVG to PDF converter extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-svg2pdfconverter/sphinxcontrib_svg2pdfconverter-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.6.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.6.3
Recommends:     python-CairoSVG >= 1.0
BuildArch:      noarch
%python_subpackages

%description
Sphinx SVG to PDF converter extension

%prep
%autosetup -p1 -n sphinxcontrib_svg2pdfconverter-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib*.pth
%{python_sitelib}/sphinxcontrib_svg2pdfconverter-%{version}.dist-info

%changelog
