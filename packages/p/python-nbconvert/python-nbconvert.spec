#
# spec file for package python-nbconvert
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
%define doc_ver 5.6.0
Name:           python-nbconvert
Version:        5.6.0
Release:        0
Summary:        Conversion of Jupyter Notebooks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/nbconvert
Source0:        https://files.pythonhosted.org/packages/source/n/nbconvert/nbconvert-%{version}.tar.gz
Source1:        https://media.readthedocs.org/pdf/nbconvert/%{doc_ver}/nbconvert.pdf
Source2:        https://media.readthedocs.org/htmlzip/nbconvert/%{doc_ver}/nbconvert.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Pebble}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module entrypoints >= 0.2.2}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter_client >= 5.3.1}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module mistune >= 0.7.4}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nbformat >= 4.4}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pandocfilters >= 1.4.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module tornado >= 4.0}
BuildRequires:  %{python_module traitlets >= 4.2}
# /SECTION
Requires:       jupyter-nbconvert = %{version}
Requires:       python-Jinja2
Requires:       python-Pygments
Requires:       python-bleach
Requires:       python-defusedxml
Requires:       python-entrypoints >= 0.2.2
Requires:       python-jupyter_core
Requires:       python-jupyter_client >= 5.3.1
Requires:       python-mistune >= 0.7.4
Requires:       python-nbformat >= 4.4
Requires:       python-pandocfilters >= 1.4.1
Requires:       python-testpath
Requires:       python-traitlets >= 4.2
Recommends:     pandoc
Recommends:     python-tornado >= 4.0
Suggests:       %{name}-latex
Provides:       python-jupyter_nbconvert = %{version}
Obsoletes:      python-jupyter_nbconvert < %{version}
BuildArch:      noarch
%python_subpackages

%description
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package provides the python interface.

%package     -n jupyter-nbconvert
Summary:        Conversion of Jupyter Notebooks
Requires:       jupyter-ipykernel
Requires:       jupyter-jupyter_client >= 4.2
Requires:       jupyter-jupyter_core
Requires:       jupyter-nbformat >= 4.4
Requires:       python3-nbconvert = %{version}
Conflicts:      python3-jupyter_nbconvert < 5.5.0

%description -n jupyter-nbconvert
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package provides the jupyter components.

%package     -n jupyter-nbconvert-latex
Summary:        LaTeX support for nbconvert
Group:          Development/Languages/Python
Requires:       jupyter-nbconvert = %{version}
Requires:       texlive-bibtex
Requires:       texlive-makeindex
Requires:       tex(adjustbox.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(ulem.sty)
Provides:       %{python_module nbconvert-latex = %{version}}
Provides:       %{python_module jupyter_nbconvert-latex = %{version}}
Obsoletes:      %{python_module jupyter_nbconvert-latex < %{version}}

%description -n jupyter-nbconvert-latex
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package pulls in the LaTeX dependencies for nbconvert.

%package     -n jupyter-nbconvert-doc
Summary:        Documentation for Jupyter's notebook converter
Group:          Documentation/Other
Provides:       %{python_module nbconvert-doc = %{version}}
Provides:       %{python_module jupyter_nbconvert-doc = %{version}}
Obsoletes:      %{python_module jupyter_nbconvert-doc < %{version}}

%description -n jupyter-nbconvert-doc
Documentation and help files for Jupyter's notebook converter.

%prep
%setup -q -n nbconvert-%{version}
cp %{SOURCE1} .
unzip %{SOURCE2} -d docs
mv docs/nbconvert-* docs/html
rm docs/html/.buildinfo
sed -i -e '/^#!\//, 1d' nbconvert/nbconvertapp.py
sed -i -e '/^#!\//, 1d' nbconvert/filters/filter_links.py

%build
%python_build

%install
%python_install

mkdir -p %{buildroot}%{_docdir}/jupyter-nbconvert

cp %{SOURCE1} %{buildroot}%{_docdir}/jupyter-nbconvert/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-nbconvert/

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_docdir}/jupyter-nbconvert/

%check
pushd docs
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
# test_run_notebooks disabled until IPython 7 incompatibility in tests fixed.
# See https://github.com/jupyter/nbconvert/issues/898
# parallel notebooks don't work reliably on python 2.x
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B -m ipykernel.kernelspec --user
%pytest --pyargs -k 'not (test_svg_handling or test_run_notebooks or test_parallel_notebooks or test_many_parallel_notebooks)' nbconvert
}
popd

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/nbconvert-%{version}-py*.egg-info
%{python_sitelib}/nbconvert/

%files -n jupyter-nbconvert
%license LICENSE
%{_bindir}/jupyter-nbconvert

%files -n jupyter-nbconvert-latex
%license LICENSE

%files -n jupyter-nbconvert-doc
%license LICENSE
%dir %{_docdir}/jupyter-nbconvert/
%{_docdir}/jupyter-nbconvert/nbconvert.pdf
%{_docdir}/jupyter-nbconvert/html

%changelog
