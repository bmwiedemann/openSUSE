#
# spec file for package python-nbinteract
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
Name:           python-nbinteract
Version:        0.2.5
Release:        0
Summary:        Python package to export interactive HTML pages from Jupyter Notebooks
License:        BSD-3-Clause
URL:            https://github.com/SamLau95/nbinteract
Source:         https://github.com/SamLau95/nbinteract/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-nbinteract = %{version}
Requires:       python-Jinja2 >= 2.10
Requires:       python-bqplot >= 0.10
Requires:       python-docopt >= 0.6.2
Requires:       python-ipython >= 6
Requires:       python-ipywidgets >= 7
Requires:       python-nbconvert >= 5.3
Requires:       python-nbformat >= 4.4.0
Requires:       python-numpy >= 1
Requires:       python-toolz >= 0.8
Requires:       python-traitlets >= 4.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module bqplot >= 0.10}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module coveralls}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module ipython >= 6}
BuildRequires:  %{python_module ipywidgets >= 7}
BuildRequires:  %{python_module nbconvert >= 5.3}
BuildRequires:  %{python_module nbformat >= 4.4.0}
BuildRequires:  %{python_module numpy >= 1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toolz >= 0.8}
BuildRequires:  %{python_module traitlets >= 4.3}
# /SECTION
%python_subpackages

%description
NBinteract is a Python package that creates interactive webpages from Jupyter
notebooks. NBinteract also has built-in support for interactive plotting.
These interactions are driven by data, not callbacks, allowing authors to focus
on the logic of their programs.

This package provides the python interface.

%package     -n jupyter-nbinteract
Summary:        Python package to export interactive HTML pages from Jupyter Notebooks
Requires:       jupyter-ipython >= 6
Requires:       jupyter-ipywidgets >= 7
Requires:       jupyter-nbconvert >= 5.3
Requires:       jupyter-nbformat >= 4.4.0
Requires:       jupyter-notebook
Requires:       python3-nbinteract = %{version}

%description -n jupyter-nbinteract
NBinteract is a Python package that creates interactive webpages from Jupyter
notebooks. NBinteract also has built-in support for interactive plotting.
These interactions are driven by data, not callbacks, allowing authors to focus
on the logic of their programs.

This package provides the command-line interface.

%prep
%setup -q -n nbinteract-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/nbinteract*

%files -n jupyter-nbinteract
%license LICENSE.txt
%{_bindir}/nbinteract

%changelog
