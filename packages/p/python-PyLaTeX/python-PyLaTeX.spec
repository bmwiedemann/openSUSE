#
# spec file for package python-PyLaTeX
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
%define         skip_python2 1
Name:           python-PyLaTeX
Version:        1.3.2
Release:        0
Summary:        A Python library for creating LaTeX files and snippets
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/JelteF/PyLaTeX
Source:         https://github.com/JelteF/PyLaTeX/archive/v%{version}.tar.gz#/PyLaTeX-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ordered-set
Requires:       texlive-latex
Recommends:     python-matplotlib
Recommends:     python-numpy
Recommends:     python-quantities
Recommends:     tex(amsmath.sty)
Recommends:     tex(booktabs.sty)
Recommends:     tex(cleveref.sty)
Recommends:     tex(color.sty)
Recommends:     tex(enumitem.sty)
Recommends:     tex(fancyhdr.sty)
Recommends:     tex(fontenc.sty)
Recommends:     tex(geometry.sty)
Recommends:     tex(graphicx.sty)
Recommends:     tex(hyperref.sty)
Recommends:     tex(inputenc.sty)
Recommends:     tex(lastpage.sty)
Recommends:     tex(lmodern.sty)
Recommends:     tex(longtable.sty)
Recommends:     tex(ltablex.sty)
Recommends:     tex(mdframed.sty)
Recommends:     tex(microtype.sty)
Recommends:     tex(multirow.sty)
Recommends:     tex(parskip.sty)
Recommends:     tex(pgfplots.sty)
Recommends:     tex(ragged2e.sty)
Recommends:     tex(siunitx.sty)
Recommends:     tex(subcaption.sty)
Recommends:     tex(tabu.sty)
Recommends:     tex(tabularx.sty)
Recommends:     tex(textcomp.sty)
Recommends:     tex(textpos.sty)
Recommends:     tex(tikz.sty)
Recommends:     tex(xcolor.sty)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module ordered-set}
BuildRequires:  texlive-latex
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(booktabs.sty)
BuildRequires:  tex(cleveref.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(lmodern.sty)
BuildRequires:  tex(longtable.sty)
BuildRequires:  tex(ltablex.sty)
BuildRequires:  tex(mdframed.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(pgfplots.sty)
BuildRequires:  tex(ragged2e.sty)
BuildRequires:  tex(siunitx.sty)
BuildRequires:  tex(subcaption.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(textcomp.sty)
BuildRequires:  tex(textpos.sty)
BuildRequires:  tex(tikz.sty)
BuildRequires:  tex(xcolor.sty)
# /SECTION
%python_subpackages

%description
PyLaTeX is a Python library for creating and compiling LaTeX files.

%prep
%setup -q -n PyLaTeX-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Quantities is an optional dependency that currently doesn't work
%python_expand nosetests-%{$python_bin_suffix} -v -e 'test_quantities'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
