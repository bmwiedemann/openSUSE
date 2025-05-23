#
# spec file for package python-nbdime
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define pyver 4.0.2
%define labver 3.0.2
%define jupver  7.0.2
# always cut trailing .0
%define pyverdist 4.0.2
%define mainbins nbdime nbshow nbdiff nbdiff-web nbmerge nbmerge-web
%define gitbins  git-nbdifftool git-nbmergetool git-nbdiffdriver git-nbmergedriver
%define hgbins   hg-nbdiff hg-nbdiffweb hg-nbmerge hg-nbmergeweb
Name:           python-nbdime
Version:        %{pyver}
Release:        0
Summary:        Tools for diffing and merging Jupyter Notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbdime
Source0:        https://files.pythonhosted.org/packages/source/n/nbdime/nbdime-%{pyver}.tar.gz
# package-lock.json file generated with command:
# npm install --package-lock-only --legacy-peer-deps --ignore-scripts
Source1:        package-lock.json
# node_modules generated using "osc service mr" with the https://github.com/openSUSE/obs-service-node_modules
Source2:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
BuildRequires:  %{python_module GitPython >= 2.1.6}
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.5}
BuildRequires:  %{python_module hatchling >= 1.5.0}
BuildRequires:  %{python_module jupyter-server-mathjax >= 0.2.2}
BuildRequires:  %{python_module jupyter-server}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  local-npm-registry
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jupyter-server-test if %python-base >= 3.10}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module notebook if %python-base >= 3.10}
BuildRequires:  %{python_module pytest >= 3.6}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-tornado}
# /SECTION
Requires:       jupyter-nbdime = %{jupver}
Requires:       python-GitPython >= 2.1.6
Requires:       python-Jinja2 >= 2.9
Requires:       python-Pygments
Requires:       python-colorama
Requires:       python-jupyter-server
Requires:       python-jupyter-server-mathjax >= 0.2.2
Requires:       python-nbformat
Requires:       python-requests
Requires:       python-tornado
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Conflicts:      python-jupyter_nbdime-git < 1.0.5
Conflicts:      python-jupyter_nbdime-hg < 1.0.5
Recommends:     python-tabulate
Suggests:       python-notebook
Provides:       python-jupyter_nbdime = %{pyver}-%{release}
Obsoletes:      python-jupyter_nbdime < %{pyver}-%{release}
BuildArch:      noarch
%python_subpackages

%description
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides the python interface.

%package     -n jupyter-nbdime
Version:        %{jupver}
Summary:        A JupyterLab extension for showing Notebook diffs
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(nbdime) = %{pyverdist}
Suggests:       python3-nbdime
Conflicts:      python3-jupyter_nbdime < 1.0.5

%description -n jupyter-nbdime
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides the tools and jupyter notebook extension.

%package     -n jupyter-nbdime-jupyterlab
Version:        %{labver}
Release:        0
Summary:        A JupyterLab extension for showing Notebook diffs
Requires:       jupyter-jupyterlab
# Any flavor is okay, but suggest the primary one for automatic zypper choice -- boo#1214354
Requires:       python3dist(nbdime) = %{pyverdist}
Suggests:       python3-nbdime

%description -n jupyter-nbdime-jupyterlab
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides the JupyterLab extension.

%package git
Version:        %{pyver}
Summary:        Git integration for python-nbdime
Requires:       git-core
Requires:       python-nbdime = %{pyver}
# python3-jupyter_nbdime-git = JUPVER (!) was provided by a jupyter-nbdime-git package until end of 2022
Provides:       python-jupyter_nbdime-git = %{jupver}-%{release}
Obsoletes:      python-jupyter_nbdime-git < %{jupver}-%{release}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-nbdime-git = %{jupver}-%{release}
Obsoletes:      jupyter-nbdime-git < %{jupver}-%{release}
%else
Conflicts:      jupyter-nbdime-git < %{jupver}-%{release}
%endif
%if %{with libalternatives}
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%description git
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides git integration.

%package hg
Version:        %{pyver}
Summary:        Mercurial integration for python-nbdime
Requires:       mercurial
Requires:       python-nbdime = %{pyver}
# python3-jupyter_nbdime-hg = JUPVER (!) was provided by a jupyter-nbdime-git package until end of 2022
Provides:       python-jupyter_nbdime-hg = %{jupver}-%{release}
Obsoletes:      python-jupyter_nbdime-hg < %{jupver}-%{release}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-nbdime-hg = %{jupver}-%{release}
Obsoletes:      jupyter-nbdime-hg < %{jupver}-%{release}
%else
Conflicts:      jupyter-nbdime-hg < %{jupver}-%{release}
%endif
%if %{with libalternatives}
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%description hg
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides mercurial integration.

%prep
%autosetup -p1 -n nbdime-%{pyver}
local-npm-registry %{_sourcedir} install --include=dev --include=peer
find . -type f -name "*.py" -exec sed -i 's/\r$//' {} +
find . -type f -name "*.ipynb" -exec sed -i 's/\r$//' {} +
find ./nbdime/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
rm nbdime/labextension/schemas/nbdime-jupyterlab/package.json.orig

%build
%pyproject_wheel

%install
%pyproject_install
for b in %mainbins %gitbins %hgbins; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%{jupyter_move_config}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}

%check
# tornado mock setup failures: no auth_url
donttest="(test_cli_apps and (test_git_difftool or test_git_mergetool))"
donttest="$donttest or (test_web and (test_fetch_diff or test_fetch_merge))"
# freshly to be install libalternatives commands are not yet flavorbinned automatically
%if %{with libalternatives}
%{python_expand mkdir -p build/flavorbin
for b in %mainbins %gitbins %hgbins; do
  ln -s %{buildroot}%{_bindir}/$b-%{$python_bin_suffix} build/flavorbin/$b
done
}
%endif
%python_flavored_alternatives
git config --global user.email "test@test.com"
git config --global user.name "tester"
git config --global init.defaultBranch master
export PYTHONDONTWRITEBYTECODE=1
%{python_expand # don't test anything on python39: no jupyter-server-test anymore
export PYTHONPATH=%{buildroot}%{$python_sitelib}
if [ "${python_flavor}" != "python39" ]; then
  $python -m pytest -v --pyargs nbdime -k "not ($donttest)"
fi
}

%pre
# remove any non-symlink bin before installing the alternative links
for b in %mainbins; do
  [ -f %{_bindir}/$b -a ! -h %{_bindir}/$b ] && rm %{_bindir}/$b
done
%python_libalternatives_reset_alternative nbdime

%post
%python_install_alternative %mainbins

%postun
%python_uninstall_alternative nbdime

%pre git
# remove any non-symlink bin before installing the alternative links
for b in %gitbins; do
  [ -f %{_bindir}/$b -a ! -h %{_bindir}/$b ] && rm %{_bindir}/$b
done
%python_libalternatives_reset_alternative git-nbdifftool

%post git
%python_install_alternative %gitbins

%postun git
%python_uninstall_alternative git-nbdifftool

%pre hg
# remove any non-symlink bin before installing the alternative links
for b in %hgbins; do
  [ -f %{_bindir}/$b -a ! -h %{_bindir}/$b ] && rm %{_bindir}/$b
done
%python_libalternatives_reset_alternative hg-nbdiff

%post hg
%python_install_alternative %hgbins

%postun hg
%python_uninstall_alternative hg-nbdiff

%files %{python_files}
%license LICENSE.md
%python_alternative %{_bindir}/nbdime
%python_alternative %{_bindir}/nbshow
%python_alternative %{_bindir}/nbdiff
%python_alternative %{_bindir}/nbdiff-web
%python_alternative %{_bindir}/nbmerge
%python_alternative %{_bindir}/nbmerge-web
%{python_sitelib}/nbdime/
%{python_sitelib}/nbdime-%{pyver}.dist-info/

%files %{python_files git}
%license LICENSE.md
%python_alternative %{_bindir}/git-nbdiffdriver
%python_alternative %{_bindir}/git-nbdifftool
%python_alternative %{_bindir}/git-nbmergedriver
%python_alternative %{_bindir}/git-nbmergetool

%files %{python_files hg}
%license LICENSE.md
%python_alternative %{_bindir}/hg-nbdiff
%python_alternative %{_bindir}/hg-nbdiffweb
%python_alternative %{_bindir}/hg-nbmerge
%python_alternative %{_bindir}/hg-nbmergeweb

%files -n jupyter-nbdime
%license LICENSE.md
%{_jupyter_nbextension_dir}/nbdime/
%_jupyter_config %{_jupyter_server_confdir}/nbdime.json
%_jupyter_config %{_jupyter_servextension_confdir}/nbdime.json
%_jupyter_config %{_jupyter_nb_notebook_confdir}/nbdime.json

%files -n jupyter-nbdime-jupyterlab
%license LICENSE.md
%dir %{_jupyter_prefix}/labextensions
%{_jupyter_labextensions_dir3}/nbdime-jupyterlab

%changelog
