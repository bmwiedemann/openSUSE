#
# spec file for package jupyter-jupyter-wysiwyg
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


%define pythons python3
%bcond_without  test
Name:           jupyter-jupyter-wysiwyg
Version:        19.10
Release:        0
Summary:        WYSIWYG editing functionality for markdown/HTML cells in Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/genepattern/jupyter-wysiwyg/
Source:         https://files.pythonhosted.org/packages/py3/j/jupyter-wysiwyg/jupyter_wysiwyg-%{version}-py3-none-any.whl
BuildRequires:  fdupes
BuildRequires:  jupyter
BuildRequires:  jupyter-notebook
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
Requires:       jupyter-notebook
Requires(post): jupyter-notebook
Requires(preun): jupyter-notebook
Provides:       python3-jupyter_wysiwyg = %{version}
Obsoletes:      python3-jupyter_wysiwyg < %{version}
Provides:       python3-jupyter-wysiwyg = %{version}
BuildArch:      noarch

%description
This is an nbextension that enables WYSIWYG editing functionality for
HTML/Markdown cells in Jupyter.

%prep
%setup -q -T -c

%build
# Not needed

%install
cp -a %{SOURCE0} .
%pyproject_install
export PYTHONDONTWRITEBYTECODE=1

%{jupyter_nbextension_install jupyter_wysiwyg}
%{jupyter_move_config}
find %{buildroot} -name '.DS_Store' -delete
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_jupyter_nbextension_dir}
%fdupes %{buildroot}%{_jupyter_nb_notebook_confdir}

%post
%{jupyter_nbextension_enable jupyter_wysiwyg}

%preun
%{jupyter_nbextension_disable jupyter_wysiwyg}

%files
%license %{python3_sitelib}/jupyter_wysiwyg-%{version}.dist-info/LICENSE.txt
%{python3_sitelib}/jupyter_wysiwyg/
%{python3_sitelib}/jupyter_wysiwyg-%{version}.dist-info/
%{_jupyter_nbextension_dir}/jupyter_wysiwyg/
%config %{_jupyter_nb_notebook_confdir}/jupyter_wysiwyg.json

%changelog
