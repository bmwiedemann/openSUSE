#
# spec file for package python-nbdime
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define mainver 3.0.0
%define jupver  6.1.0
%define labver  2.1.0
Name:           python-nbdime
Version:        %{mainver}
Release:        0
Summary:        Tools for diffing and merging Jupyter Notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbdime
Source:         https://files.pythonhosted.org/packages/py2.py3/n/nbdime/nbdime-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module GitPython >= 2.1.6}
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module jupyter-server-mathjax >= 0.2.2}
BuildRequires:  %{python_module jupyter-server}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab-filesystem
BuildRequires:  python-rpm-macros
# SECTION test requirements (including jupyter_server[test])
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-tornado}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest}
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
Requires:       python-six
Requires:       python-tornado
Conflicts:      python-jupyter_nbdime-git < 1.0.5
Conflicts:      python-jupyter_nbdime-hg < 1.0.5
Recommends:     python-tabulate
Suggests:       python-notebook
Provides:       python-jupyter_nbdime = %{mainver}
Obsoletes:      python-jupyter_nbdime < %{mainver}
BuildArch:      noarch
%python_subpackages

%description
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides the python interface.

%package     -n jupyter-nbdime
Version:        %{jupver}
Summary:        A JupyterLab extension for showing Notebook diffs
Requires:       jupyter-nbformat
Requires:       jupyter-notebook
Requires:       python3-nbdime = %{mainver}
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
Requires:       python3-nbdime = %{mainver}
Provides:       python3-jupyter_nbdime_jupyterlab = %{labver}
Obsoletes:      python3-jupyter_nbdime_jupyterlab < %{labver}

%description -n jupyter-nbdime-jupyterlab
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides the JupyterLab extension.

%package     -n jupyter-nbdime-git
Version:        %{jupver}
Summary:        Git integration for jupyter-nbdime
Requires:       git-core
Requires:       jupyter-nbdime = %{jupver}
Provides:       python3-jupyter_nbdime-git = %{jupver}
Obsoletes:      python3-jupyter_nbdime-git < %{jupver}

%description -n jupyter-nbdime-git
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides git integration.

%package     -n jupyter-nbdime-hg
Version:        %{jupver}
Summary:        Mercurial integration for jupyter-nbdime
Requires:       jupyter-nbdime = %{jupver}
Requires:       mercurial
Provides:       python3-jupyter_nbdime-hg = %{jupver}
Obsoletes:      python3-jupyter_nbdime-hg < %{jupver}

%description -n jupyter-nbdime-hg
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides mercurial integration.

%prep
%setup -q -c -T

%build
:

%install
%pyproject_install %{SOURCE0}

%{jupyter_move_config}
%python_expand sed -i 's/^import mock/from unittest import mock/' %{buildroot}%{$python_sitelib}/nbdime/tests/test_*.py
%python_expand find %{buildroot}%{$python_sitelib} -type f -name "*.py" -exec sed -i 's/\r$//' {} +
%python_expand find %{buildroot}%{$python_sitelib} -type f -name "*.ipynb" -exec sed -i 's/\r$//' {} +
%python_expand find %{buildroot}%{$python_sitelib}/nbdime/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
%python_expand rm %{buildroot}%{$python_sitelib}/nbdime/labextension/schemas/nbdime-jupyterlab/package.json.orig
%python_compileall
rm %{buildroot}%{_jupyter_prefix}/labextensions/nbdime-jupyterlab/schemas/nbdime-jupyterlab/package.json.orig
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{_jupyter_prefix}
cp %{buildroot}%{python3_sitelib}/nbdime-%{mainver}.dist-info/LICENSE.md .

%check
export PATH=$PATH:%{buildroot}%{_bindir}
git config --global user.email "test@test.com"
git config --global user.name "tester"
%pytest --pyargs nbdime

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/nbdime/
%{python_sitelib}/nbdime-%{mainver}.dist-info/

%files -n jupyter-nbdime
%license LICENSE.md
%{_bindir}/nbdime
%{_bindir}/nbshow
%{_bindir}/nbdiff
%{_bindir}/nbdiff-web
%{_bindir}/nbmerge
%{_bindir}/nbmerge-web
%{_jupyter_nbextension_dir}/nbdime/
%config %{_jupyter_server_confdir}/nbdime.json
%config %{_jupyter_servextension_confdir}/nbdime.json
%config %{_jupyter_nb_notebook_confdir}/nbdime.json

%files -n jupyter-nbdime-jupyterlab
%license LICENSE.md
%dir %{_jupyter_prefix}/labextensions
%{_jupyter_prefix}/labextensions/nbdime-jupyterlab
%{_jupyter_prefix}/lab/extensions/nbdime-jupyterlab-%{labver}.tgz

%files -n jupyter-nbdime-git
%license LICENSE.md
%{_bindir}/git-nbdiffdriver
%{_bindir}/git-nbdifftool
%{_bindir}/git-nbmergedriver
%{_bindir}/git-nbmergetool

%files -n jupyter-nbdime-hg
%license LICENSE.md
%{_bindir}/hg-nbdiff
%{_bindir}/hg-nbdiffweb
%{_bindir}/hg-nbmerge
%{_bindir}/hg-nbmergeweb

%changelog
