#
# spec file for package python-nbformat
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define doc_ver 5.2.0
%bcond_without libalternatives
Name:           python-nbformat
Version:        5.6.1
Release:        0
Summary:        The Jupyter Notebook format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/nbformat
# PyPI sdist has only some schema tests, get the full test suite from GitHub sources
Source:         https://github.com/jupyter/nbformat/archive/%{version}.tar.gz#/nbformat-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch_nodejs_version}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros >= 20210929
Requires:       jupyter-nbformat = %{version}
Requires:       python-fastjsonschema
Requires:       python-jsonschema > 2.6
Requires:       python-jupyter_core
Requires:       python-traitlets >= 5.1
Provides:       python-jupyter_nbformat = %{version}
Obsoletes:      python-jupyter_nbformat < %{version}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module fastjsonschema}
BuildRequires:  %{python_module jsonschema > 2.6}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module pep440}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets >= 5.1}
BuildRequires:  %{pythons}
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
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-trust
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%fdupes %{buildroot}%{_docdir}/jupyter-nbformat/

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-trust

%post
%python_install_alternative jupyter-trust

%postun
%python_uninstall_alternative jupyter-trust

%files %{python_files}
%license COPYING.md
%doc README.md
%python_alternative jupyter-trust
%{python_sitelib}/nbformat/
%{python_sitelib}/nbformat-%{version}.dist-info/

%files -n jupyter-nbformat
%license COPYING.md

%changelog
