#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-nbconvert%{psuffix}
Version:        6.4.0
Release:        0
Summary:        Conversion of Jupyter Notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbconvert
Source0:        https://files.pythonhosted.org/packages/source/n/nbconvert/nbconvert-%{version}.tar.gz
# License Source3: BSD-3-Clause
Source3:        https://files.pythonhosted.org/packages/source/m/mistune/mistune-0.8.4.tar.gz
# PATCH-FIX-OPENSUSE nbconvert-vendorize-mistune.patch -- gh#jupyter/nbconvert#1685
Patch1:         nbconvert-vendorize-mistune.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-nbconvert = %{version}
Requires:       python-Jinja2 >= 2.4
Requires:       python-Pygments >= 2.4.1
Requires:       python-bleach
Requires:       python-defusedxml
Requires:       python-entrypoints >= 0.2.2
Requires:       python-jupyter-core
Requires:       python-jupyterlab-pygments
Requires:       python-nbclient >= 0.5
Requires:       python-nbformat >= 4.4
Requires:       python-pandocfilters >= 1.4.1
Requires:       python-testpath
Requires:       python-traitlets >= 5.0
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
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipywidgets >= 7}
BuildRequires:  %{python_module nbconvert = %{version}}
BuildRequires:  %{python_module pytest-dependency}
%endif
%python_subpackages

%description
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package provides the python interface.

%package     -n jupyter-nbconvert
Summary:        Conversion of Jupyter Notebooks
Requires:       jupyter-ipykernel
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

%prep
%autosetup -p1 -n nbconvert-%{version} -b3

mkdir nbconvert/vendor
touch nbconvert/vendor/__init__.py
cp ../mistune-0.8.4/mistune.py nbconvert/vendor/
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
%python_clone -a %{buildroot}%{_bindir}/jupyter-dejavu

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
%python_install_alternative jupyter-nbconvert jupyter-dejavu

%postun
%python_uninstall_alternative jupyter-nbconvert

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/nbconvert-%{version}*-info
%{python_sitelib}/nbconvert/
%python_alternative %{_bindir}/jupyter-nbconvert
%python_alternative %{_bindir}/jupyter-dejavu

%files -n jupyter-nbconvert
%license LICENSE
%dir %{_datadir}/jupyter/
%dir %{_datadir}/jupyter/nbconvert
%{_datadir}/jupyter/nbconvert/templates

%files -n jupyter-nbconvert-latex
%license LICENSE
%endif

%changelog
