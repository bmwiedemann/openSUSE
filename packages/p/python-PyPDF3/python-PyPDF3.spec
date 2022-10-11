#
# spec file for package python-PyPDF3
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-PyPDF3
Version:        1.0.6
Release:        0
Summary:        Pure Python PDF toolkit
License:        BSD-3-Clause
URL:            https://github.com/sfneal/PyPDF3
Source:         https://files.pythonhosted.org/packages/source/P/PyPDF3/PyPDF3-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-tqdm
BuildArch:      noarch
%python_subpackages

%description
PyPDF3 is a pure-python PDF library capable of splitting, merging together,
cropping, and transforming the pages of PDF files. It can also add custom data,
viewing options, and passwords to PDF files. It can retrieve text and metadata
from PDFs as well as merge entire files together.

%prep
%setup -q -n PyPDF3-%{version}
#remove shebang
sed -i '1{\@^#!/usr/bin/env@ d}' PyPDF3/pagerange.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/*.py

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/*

%changelog
