#
# spec file for package python-nbconvert
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
# X.X.0 gets abbreviated by pythondistdeps
%define shortversion 7.16.6
%{?sle15_python_module_pythons}
Name:           python-nbconvert%{psuffix}
Version:        7.16.6
Release:        0
Summary:        Conversion of Jupyter Notebooks
License:        BSD-3-Clause AND MIT
URL:            https://github.com/jupyter/nbconvert
Source0:        https://files.pythonhosted.org/packages/source/n/nbconvert/nbconvert-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling >= 0.25}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-nbconvert = %{version}
Requires:       python-Jinja2 >= 3.0
Requires:       python-MarkupSafe >= 2.0
Requires:       python-Pygments >= 2.4.1
Requires:       python-beautifulsoup4
Requires:       python-defusedxml
Requires:       python-jupyter-core >= 4.7
Requires:       python-jupyterlab-pygments
Requires:       python-nbclient >= 0.5
Requires:       python-nbformat >= 5.7
Requires:       python-packaging
Requires:       python-pandocfilters >= 1.4.1
Requires:       python-traitlets >= 5.1
Requires:       (python-tinycss2 >= 1.1.0 with python-tinycss2 < 1.5)
## pyproject.toml says bleach[css], this is bleach w/ tinycss2, see above
Requires:       (python-bleach without python-bleach = 5.0.0)
Requires:       (python-mistune >= 2.0.3 with python-mistune < 4)
Recommends:     pandoc >= 2.9.2
Recommends:     python-tornado >= 6.1
Suggests:       %{name}-latex
Suggests:       python-qtwebengine-qt5 >= 5.15
Provides:       python-jupyter_nbconvert = %{version}
Obsoletes:      python-jupyter_nbconvert < %{version}
BuildArch:      noarch
%if 0%{python_version_nodots} < 310
Requires:       python-importlib-metadata >= 3.6
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipywidgets >= 7.5}
BuildRequires:  %{python_module nbconvert = %{version}}
BuildRequires:  %{python_module pytest >= 7}
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
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(nbconvert) = %{shortversion}
Suggests:       python3-nbconvert
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

%description -n jupyter-nbconvert-latex
The jupyter nbconvert package converts notebooks to various other formats
via Jinja templates.

This package pulls in the LaTeX dependencies for nbconvert.

%prep
%autosetup -p1 -n nbconvert-%{version}
for f in nbconvert/nbconvertapp.py nbconvert/filters/filter_links.py; do
  sed -i -e '/^#!\//, 1d' $f
  chmod -x $f
done
sed -i '/addopts/,/\]/ s/"--color=yes",//' pyproject.toml

%build
%if ! %{with test}
%pyproject_wheel
%endif

%install
%if ! %{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-nbconvert
%python_clone -a %{buildroot}%{_bindir}/jupyter-dejavu
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_docdir}/jupyter-nbconvert/
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
# requires modules not installed: https://github.com/jupyter/nbconvert/issues/1846
donttest="test_convert_full_qualified_name or test_post_processor"
# mv the source out of PYTHONPATH
mv nbconvert nbconvert.moved
%{python_expand #
$python -m ipykernel.kernelspec --user
pytest-%{$python_bin_suffix} -v -m 'not network' -k "not ($donttest)"
}
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
%{python_sitelib}/nbconvert-%{version}.dist-info
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
