#
# spec file for package python-jupyter-sphinx
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
%define         oldpython python
Name:           python-jupyter-sphinx
Version:        0.2.4
Release:        0
Summary:        Jupyter Sphinx Extensions
License:        BSD-3-Clause
URL:            https://github.com/jupyter-widgets/jupyter-sphinx
Source:         https://github.com/jupyter/jupyter-sphinx/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-IPython
Requires:       python-Sphinx >= 1.8
Requires:       python-ipywidgets >= 7.0.0
Requires:       python-nbconvert >= 5.5
Requires:       python-nbformat
Provides:       python-jupyter_sphinx = %{version}
Obsoletes:      python-jupyter_sphinx < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module IPython}
BuildRequires:  %{python_module Sphinx >= 1.8}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module nbconvert >= 5.5}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module pytest}
# /SECTION
%ifpython3
Provides:       jupyter-jupyter-sphinx = %{version}
%endif
%ifpython2
Provides:       %{oldpython}-jupyter_sphinx = %{version}
Obsoletes:      %{oldpython}-jupyter_sphinx < %{version}
%endif
%python_subpackages

%description
Jupyter Sphinx extensions enable jupyter-specific features in sphinx.

%prep
%setup -q -n jupyter-sphinx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyter_sphinx-%{version}-py*.egg-info
%{python_sitelib}/jupyter_sphinx/

%changelog
