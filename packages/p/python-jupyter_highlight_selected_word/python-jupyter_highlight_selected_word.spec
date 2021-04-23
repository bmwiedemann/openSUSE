#
# spec file for package python-jupyter_highlight_selected_word
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
Name:           python-jupyter_highlight_selected_word
Version:        0.2.0
Release:        0
Summary:        Jupyter notebook extension to highlight every instance of the current word
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jcb91/jupyter_highlight_selected_word
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_highlight_selected_word/jupyter_highlight_selected_word-%{version}.tar.gz
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-notebook
Recommends:     jupyter-jupyter_highlight_selected_word = %{version}
BuildArch:      noarch

%python_subpackages

%description
Jupyter notebook extension that enables highlighting of all instances of the
currently-selected or cursor-adjecent word in either the current cell's editor,
or in the whole notebook.

This package provides the python interface.

%package     -n jupyter-jupyter_highlight_selected_word
Summary:        Jupyter notebook extension to highlight every instance of the current word
Group:          Development/Languages/Python
Requires:       jupyter-notebook
Requires:       python3-jupyter_highlight_selected_word = %{version}

%description -n jupyter-jupyter_highlight_selected_word
Jupyter notebook extension that enables highlighting of all instances of the
currently-selected or cursor-adjecent word in either the current cell's editor,
or in the whole notebook.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_highlight_selected_word-%{version}

%build
%python_build

%install
%python_install
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/jupyter_highlight_selected_word-%{version}-py*.egg-info/PKG-INFO
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{jupyter_nbextension_install jupyter_highlight_selected_word}

PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter nbextension install jupyter_highlight_selected_word --user --py
PYTHONPATH=%{buildroot}%{python3_sitelib} jupyter nbextension enable jupyter_highlight_selected_word --user --py

for f in ~/.jupyter/nbconfig/*.json ; do
    tdir=$( basename -s .json ${f} )
    install -Dm 644 ${f} %{buildroot}%{_jupyter_nb_confdir}/${tdir}.d/highlight_selected_word.json
done

%{fdupes %{buildroot}%{_jupyter_prefix} %{buildroot}%{_jupyter_confdir}}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jupyter_highlight_selected_word
%{python_sitelib}/jupyter_highlight_selected_word-%{version}-py*.egg-info

%files -n jupyter-jupyter_highlight_selected_word
%license LICENSE.txt
%{_jupyter_nbextension_dir}/highlight_selected_word/
%config %{_jupyter_nb_notebook_confdir}/highlight_selected_word.json

%changelog
