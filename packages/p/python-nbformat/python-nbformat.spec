#
# spec file for package python-nbformat
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
%define doc_ver 5.0.4
Name:           python-nbformat
Version:        5.0.6
Release:        0
Summary:        The Jupyter Notebook format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/nbformat
Source:         https://files.pythonhosted.org/packages/source/n/nbformat/nbformat-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-nbformat = %{version}
Requires:       python-ipython_genutils
Requires:       python-jsonschema > 2.5.0
Requires:       python-jupyter_core
Requires:       python-traitlets >= 4.1
Provides:       python-jupyter_nbformat = %{version}
Obsoletes:      python-jupyter_nbformat < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jsonschema > 2.5.0}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets >= 4.1}
# /SECTION
%python_subpackages

%description
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.

This package provides the python interface.

%package     -n jupyter-nbformat
Summary:        The Jupyter Notebook format
Group:          Development/Languages/Python
Requires:       jupyter-jupyter_core
Requires:       python3-nbformat = %{version}
Conflicts:      python3-jupyter_nbformat < 5.0
Provides:       jupyter-nbformat-doc = %{version}
Obsoletes:      jupyter-nbformat-doc < %{version}

%description -n jupyter-nbformat
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.

This package provides the jupyter components.

%prep
%setup -q -n nbformat-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%fdupes %{buildroot}%{_docdir}/jupyter-nbformat/

%check
%pytest -k "not TestNotary and not SQLiteSignatureStoreTests"

%files %{python_files}
%license COPYING.md
%doc README.md
%{python_sitelib}/nbformat-%{version}-py*.egg-info
%{python_sitelib}/nbformat/

%files -n jupyter-nbformat
%license COPYING.md

%changelog
