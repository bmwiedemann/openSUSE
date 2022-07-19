#
# spec file for package python-pypandoc
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
Name:           python-pypandoc
Version:        1.6.4
Release:        0
Summary:        Thin wrapper for pandoc
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bebraw/pypandoc
Source:         https://github.com/NicklasTegner/pypandoc/archive/refs/tags/v%{version}.tar.gz#/pypandoc-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/NicklasTegner/pypandoc/master/tests.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-xcolor
Requires:       pandoc
Requires:       python-pip
Requires:       python-wheel
Suggests:       ghc-citeproc
ExcludeArch:    %{ix86}
%python_subpackages

%description
pypandoc provides a thin wrapper for pandoc, a universal document converter.

%prep
%setup -q -n pypandoc-%{version}

cp %{SOURCE1} tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_basic_conversion_from_http_url needs network
%pytest tests.py -k 'not test_basic_conversion_from_http_url'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
