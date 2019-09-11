#
# spec file for package python-sphinxcontrib-svg2pdfconverter
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
Name:           python-sphinxcontrib-svg2pdfconverter
Version:        0.1.0
Release:        0
Summary:        Sphinx SVG to PDF converter extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.org/missinglinkelectronics/sphinxcontrib-svg2pdfconverter
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-svg2pdfconverter/sphinxcontrib-svg2pdfconverter-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
BuildArch:      noarch

%python_subpackages

%description
Sphinx SVG to PDF converter extension

%prep
%setup -q -n sphinxcontrib-svg2pdfconverter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
