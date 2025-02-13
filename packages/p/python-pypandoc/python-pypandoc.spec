#
# spec file for package python-pypandoc
#
# Copyright (c) 2025 SUSE LLC
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


%define base_name pypandoc
%{?sle15_python_module_pythons}
Name:           python-pypandoc
Version:        1.15
Release:        0
Summary:        Thin wrapper for pandoc
License:        MIT
URL:            https://github.com/JessicaTegner/pypandoc
Source:         https://github.com/JessicaTegner/pypandoc/archive/refs/tags/v%{version}.tar.gz#/pypandoc-%{version}.tar.gz
BuildRequires:  %{python_module pandocfilters}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-xcolor
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(bookmark.sty)
Requires:       pandoc
Suggests:       ghc-citeproc
ExcludeArch:    %{ix86}
BuildArch:      noarch
%python_subpackages

%description
pypandoc provides a thin wrapper for pandoc, a universal document converter.

%prep
%autosetup -p1 -n pypandoc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# 'test_basic_conversion_from_http_url' needs network
# 'test_conversion_with_data_files' => https://github.com/JessicaTegner/pypandoc/issues/278
%pytest tests.py -k 'not test_basic_conversion_from_http_url and not test_conversion_with_data_files and not test_basic_conversion_from_file_pattern_pathlib_glob'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pypandoc
%{python_sitelib}/pypandoc-%{version}.dist-info

%changelog
