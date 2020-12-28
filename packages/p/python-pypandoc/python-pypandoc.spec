#
# spec file for package python-pypandoc
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.5
Release:        0
Summary:        Thin wrapper for pandoc
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bebraw/pypandoc
Source:         https://pypi.org/packages/source/p/pypandoc/pypandoc-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-test.patch -- ATX-style headings are default for
# markdown, see https://pandoc.org/MANUAL#option--markdown-headings
Patch1:         fix-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  ghc-citeproc
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-latex-bin
Requires:       pandoc
Requires:       python-pip
Requires:       python-wheel
Suggests:       ghc-citeproc
BuildArch:      noarch
%python_subpackages

%description
pypandoc provides a thin wrapper for pandoc, a universal document converter.

%prep
%setup -q -n pypandoc-%{version}
%autopatch -p1
# Disable test that requires internet
sed -i 's/\(test_basic_conversion_from_http_url\)/_\1/' tests.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_conversion_with_citeproc_filter depends on ghc-pandoc-citeproc
# which was removed from factory
%pytest tests.py -k 'not test_conversion_with_citeproc_filter'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
