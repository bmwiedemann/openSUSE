#
# spec file for package jupyter-jupyter_cms
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


# Test resources not included
%bcond_with     test
Name:           jupyter-jupyter_cms
Version:        0.7.0
Release:        0
Summary:        Content management extension for Jupyter Notebook
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-incubator/contentmanagement
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_cms/jupyter_cms-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook >= 4.2.0
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Whoosh >= 2.7.0
BuildRequires:  python3-scandir
BuildRequires:  python3-setuptools
Requires:       jupyter-ipython >= 4.1.0
Requires:       jupyter-jupyter_core
Requires:       jupyter-nbconvert >= 5.0.0
Requires:       jupyter-notebook >= 4.2.0
Requires:       python3-Whoosh >= 2.7.0
Requires(post): jupyter-notebook
Requires(post): python3-Whoosh >= 2.7.0
Requires(preun): jupyter-notebook
Requires(preun): python3-Whoosh >= 2.7.0
Provides:       python3-jupyter_cms = %{version}
Obsoletes:      python3-jupyter_cms <= %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  jupyter-ipython >= 4.1.0
BuildRequires:  jupyter-jupyter_core
BuildRequires:  jupyter-nbconvert >= 5.0.0
BuildRequires:  jupyter-notebook >= 4.2.0
BuildRequires:  python3-Whoosh >= 2.7.0
BuildRequires:  python3-entrypoints >= 0.2.2
%endif

%description
This package adds the following features to Jupyter Notebook:

* Search dialog on file tree, editor, and notebook screens to search over filenames and .ipynb content in the notebook directory
* IPython kernel extension to make notebooks importable, and notebook cells injectable via # <api> and # <help> annotations
* Full-page drag-and-drop upload target
* Pop-over table of contents navigation for notebooks

%prep
%setup -q -n jupyter_cms-%{version}

%build
%python3_build

%install
%python3_install

%{jupyter_nbextension_install jupyter_cms}
%{fdupes %{buildroot}%{python3_sitelib} %{buildroot}%{_jupyter_nbextension_dir}}

%post
%{jupyter_serverextension_enable jupyter_cms}
%{jupyter_nbextension_enable jupyter_cms}

%preun
%{jupyter_serverextension_disable jupyter_cms}
%{jupyter_nbextension_disable jupyter_cms}

%if %{with test}
%check
python3 -m unittest discover -s test
%endif

%files
%license LICENSE.md
%{_bindir}/jupyter-cms
%{_jupyter_nbextension_dir}/jupyter_cms/
%{python3_sitelib}/jupyter_cms-%{version}-py*.egg-info
%{python3_sitelib}/jupyter_cms/

%changelog
