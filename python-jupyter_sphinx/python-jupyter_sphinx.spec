#
# spec file for package python-jupyter_sphinx
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
Name:           python-jupyter_sphinx
Version:        0.2.1
Release:        0
Summary:        Jupyter Sphinx Extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter-widgets/jupyter-sphinx
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_sphinx/jupyter_sphinx-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
Requires:       python-ipywidgets >= 6.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 0.6}
BuildRequires:  %{python_module ipywidgets >= 6.0.0}
# /SECTION
%ifpython3
Provides:       jupyter-jupyter_sphinx = %{version}
%endif
%python_subpackages

%description
Jupyter Sphinx extensions enable jupyter-specific features in sphinx.

%prep
%setup -q -n jupyter_sphinx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jupyter_sphinx-%{version}-py*.egg-info
%{python_sitelib}/jupyter_sphinx/

%changelog
