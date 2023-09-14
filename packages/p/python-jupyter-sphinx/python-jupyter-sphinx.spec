#
# spec file for package python-jupyter-sphinx
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-jupyter-sphinx
Version:        0.4.0
Release:        0
Summary:        Jupyter Sphinx Extensions
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/jupyter-sphinx
Source:         https://github.com/jupyter/jupyter-sphinx/archive/v%{version}.tar.gz#/jupyter-sphinx-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM jupyter-sphinx-pr226-ipykernel.patch gh#jupyter-widgets/jupyter-sphinx#226
Patch0:         jupyter-sphinx-pr226-ipykernel.patch
# PATCH-FIX-UPSTREAM jupyter-sphinx-pr233-pathlib.patch gh#jupyter-widgets/jupyter-sphinx#233
Patch1:         jupyter-sphinx-pr233-pathlib.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-IPython
Requires:       python-Sphinx >= 2
Requires:       python-ipykernel >= 4.5.1
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-nbconvert >= 5.5
Requires:       python-nbformat
Provides:       python-jupyter_sphinx = %{version}
Obsoletes:      python-jupyter_sphinx < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module IPython}
BuildRequires:  %{python_module Sphinx >= 2}
BuildRequires:  %{python_module Sphinx-latex}
BuildRequires:  %{python_module ipykernel >= 4.5.1}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module nbconvert >= 5.5}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pytest}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-jupyter-sphinx = %{version}
%endif
%python_subpackages

%description
Jupyter Sphinx extensions enable jupyter-specific features in sphinx.

%prep
%autosetup -p1 -n jupyter-sphinx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyter_sphinx-%{version}.dist-info
%{python_sitelib}/jupyter_sphinx/

%changelog
