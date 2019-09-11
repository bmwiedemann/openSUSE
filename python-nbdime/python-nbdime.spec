#
# spec file for package python-nbdime
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
%define mainver 1.0.5
%define labver  0.6.1
Name:           python-nbdime
Version:        %{mainver}
Release:        0
Summary:        Tools for diffing and merging Jupyter Notebooks
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/nbdime
Source:         https://files.pythonhosted.org/packages/py2.py3/n/nbdime/nbdime-%{mainver}-py2.py3-none-any.whl
BuildRequires:  %{python_module GitPython >= 2.1.6}
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyterlab
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  python-backports.functools_lru_cache
BuildRequires:  python-backports.shutil_which
Requires:       jupyter-nbdime = %{mainver}
Requires:       python-GitPython >= 2.1.6
Requires:       python-Jinja2 >= 2.9
Requires:       python-colorama
Requires:       python-nbformat
Requires:       python-notebook
Requires:       python-requests
Requires:       python-six
Requires:       python-tornado
%ifpython2
Requires:       python-backports.functools_lru_cache
Requires:       python-backports.shutil_which
Provides:       python-jupyter_nbdime-hg = %{mainver}
Obsoletes:      python-jupyter_nbdime-hg < %{mainver}
Provides:       python-jupyter_nbdime-git = %{mainver}
Obsoletes:      python-jupyter_nbdime-git < %{mainver}
%else
Conflicts:      python-jupyter_nbdime-hg < 1.0.5
Conflicts:      python-jupyter_nbdime-git < 1.0.5
%endif
Recommends:     python-tabulate
Provides:       python-jupyter_nbdime = %{mainver}
Obsoletes:      python-jupyter_nbdime < %{mainver}
BuildArch:      noarch
%python_subpackages

%description
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides the python interface.

%package     -n jupyter-nbdime
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
Summary:        Git integration for jupyter-nbdime
Group:          Development/Languages/Python
Requires:       git
Requires:       jupyter-nbdime = %{mainver}
Provides:       python3-jupyter_nbdime-git = %{mainver}
Obsoletes:      python3-jupyter_nbdime-git < %{mainver}

%description -n jupyter-nbdime-git
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides git integration.

%package     -n jupyter-nbdime-hg
Summary:        Mercurial integration for jupyter-nbdime
Group:          Development/Languages/Python
Requires:       jupyter-nbdime = %{mainver}
Requires:       mercurial
Provides:       python3-jupyter_nbdime-hg = %{mainver}
Obsoletes:      python3-jupyter_nbdime-hg < %{mainver}

%description -n jupyter-nbdime-hg
The nbdime package provides tools for diffing and merging of
Jupyter Notebooks.

This package provides mercurial integration.

%prep
%setup -q -c -T
unzip %{SOURCE0} 'nbdime/*'
find nbdime/ -type f -name "*.py" -exec sed -i 's/\r$//' {} +
find nbdime/ -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} +
zip -r %{SOURCE0} nbdime
rm -rf nbdime

%build
# Not needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}

%{jupyter_move_config}

cp %{buildroot}%{python3_sitelib}/nbdime-%{mainver}.dist-info/LICENSE.md .
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{python3_sitelib}}

%files %{python_files}
%license %{python_sitelib}/nbdime-%{mainver}.dist-info/LICENSE.md
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
%config %{_jupyter_servextension_confdir}/nbdime.json
%config %{_jupyter_nb_notebook_confdir}/nbdime.json

%files -n jupyter-nbdime-jupyterlab
%license LICENSE.md
%{_jupyter_labextensions_dir}/nbdime-jupyterlab-%{labver}.tgz

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
