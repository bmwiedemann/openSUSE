#
# spec file for package python-nbconvert
#
# Copyright (c) 2021 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

# Note: only update to > 6.0 when there is no python36 Jupyter stack anymore
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define doc_ver 6.0.7
Name:           python-nbconvert%{psuffix}
Version:        6.0.7
Release:        0
Summary:        Conversion of Jupyter Notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbconvert
Source0:        https://files.pythonhosted.org/packages/source/n/nbconvert/nbconvert-%{version}.tar.gz
Source1:        https://media.readthedocs.org/pdf/nbconvert/%{doc_ver}/nbconvert.pdf
Source2:        https://media.readthedocs.org/htmlzip/nbconvert/%{doc_ver}/nbconvert.zip
# License Source3: BSD-3-Clause
Source3:        https://files.pythonhosted.org/packages/source/m/mistune/mistune-0.8.4.tar.gz
# PATCH-FIX-OPENSUSE nbconvert-vendorize-mistune.patch -- gh#jupyter/nbconvert#1685
Patch1:         nbconvert-vendorize-mistune.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-nbconvert = %{version}
Requires:       python-Jinja2
Requires:       python-Pygments
Requires:       python-bleach
Requires:       python-defusedxml
Requires:       python-entrypoints >= 0.2.2
Requires:       python-jupyter-client >= 5.3.1
Requires:       python-jupyter-core
Requires:       python-jupyterlab-pygments
Requires:       python-mistune >= 0.7.4
Requires:       python-nbclient >= 0.5
Requires:       python-nbformat >= 4.4
Requires:       python-pandocfilters >= 1.4.1
Requires:       python-testpath
Requires:       python-traitlets >= 4.2
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Recommends:     pandoc
Recommends:     python-tornado >= 4.0
Suggests:       %{name}-latex
Provides:       python-jupyter_nbconvert = %{version}
Obsoletes:      python-jupyter_nbconvert < %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Pebble}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module bleach}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module entrypoints >= 0.2.2}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter-client >= 5.3.1}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module jupyterlab-pygments}
BuildRequires:  %{python_module mistune >= 0.7.4}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nbclient >= 0.5}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat >= 4.4}
BuildRequires:  %{python_module pandocfilters >= 1.4.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module tornado >= 4.0}
BuildRequires:  %{python_module traitlets >= 4.2}
%endif
%python_subpackages

%description
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package provides the python interface.

%package     -n jupyter-nbconvert
Summary:        Conversion of Jupyter Notebooks
Requires:       jupyter-ipykernel
Requires:       jupyter-jupyter-client >= 4.2
Requires:       jupyter-jupyter-core
Requires:       jupyter-nbformat >= 4.4
Requires:       python3-nbconvert = %{version}
Conflicts:      python3-jupyter_nbconvert < 5.5.0

%description -n jupyter-nbconvert
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package provides the jupyter components.

%package     -n jupyter-nbconvert-latex
Summary:        LaTeX support for nbconvert
Requires:       jupyter-nbconvert = %{version}
Requires:       texlive-bibtex
Requires:       texlive-makeindex
Requires:       tex(adjustbox.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(ulem.sty)
Provides:       %{python_module jupyter_nbconvert-latex = %{version}}
Provides:       %{python_module nbconvert-latex = %{version}}
Obsoletes:      %{python_module jupyter_nbconvert-latex < %{version}}

%description -n jupyter-nbconvert-latex
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package pulls in the LaTeX dependencies for nbconvert.

%package     -n jupyter-nbconvert-doc
Summary:        Documentation for Jupyter's notebook converter
Provides:       %{python_module jupyter_nbconvert-doc = %{version}}
Provides:       %{python_module nbconvert-doc = %{version}}
Obsoletes:      %{python_module jupyter_nbconvert-doc < %{version}}

%description -n jupyter-nbconvert-doc
Documentation and help files for Jupyter's notebook converter.

%prep
%autosetup -p1 -n nbconvert-%{version} -b3

cp %{SOURCE1} .
mkdir nbconvert/vendor
touch nbconvert/vendor/__init__.py
cp ../mistune-0.8.4/mistune.py nbconvert/vendor/
unzip %{SOURCE2} -d docs
mv docs/nbconvert-* docs/html
rm docs/html/.buildinfo
sed -i -e '/^#!\//, 1d' nbconvert/nbconvertapp.py
sed -i -e '/^#!\//, 1d' nbconvert/filters/filter_links.py

# Ignore maxversion requirements
sed -i -e "/nbclient/ s/,<.*'/'/" setup.py

%build
%python_build

%install
%if ! %{with test}
%python_install

%python_clone -a %{buildroot}%{_bindir}/jupyter-nbconvert

mkdir -p %{buildroot}%{_docdir}/jupyter-nbconvert

cp %{SOURCE1} %{buildroot}%{_docdir}/jupyter-nbconvert/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-nbconvert/

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_docdir}/jupyter-nbconvert/
%endif

%if %{with test}
%check
pushd docs
export LANG=en_US.UTF-8
%{python_expand # installed package in :test flavor
$python -B -m ipykernel.kernelspec --user
# not test_webpdf: no pyppeteer, not even offline
pytest-%{$python_bin_suffix} -v -m 'not network' -k "not test_webpdf" --pyargs nbconvert
}
popd
%endif

%if !%{with test}
%pre
%python_libalternatives_reset_alternative jupyter-nbconvert

%post
%python_install_alternative jupyter-nbconvert

%postun
%python_uninstall_alternative jupyter-nbconvert

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/nbconvert-%{version}-py*.egg-info
%{python_sitelib}/nbconvert/
%python_alternative %{_bindir}/jupyter-nbconvert

%files -n jupyter-nbconvert
%license LICENSE
%dir %{_datadir}/jupyter/
%dir %{_datadir}/jupyter/nbconvert
%{_datadir}/jupyter/nbconvert/templates

%files -n jupyter-nbconvert-latex
%license LICENSE

%files -n jupyter-nbconvert-doc
%license LICENSE
%dir %{_docdir}/jupyter-nbconvert/
%{_docdir}/jupyter-nbconvert/nbconvert.pdf
%{_docdir}/jupyter-nbconvert/html
%endif

%changelog
