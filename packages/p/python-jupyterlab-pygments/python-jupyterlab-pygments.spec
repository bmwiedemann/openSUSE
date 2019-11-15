#
# spec file for package python-jupyterlab-pygments
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyterlab-pygments
Version:        0.1.0
Release:        0
License:        BSD-3-Clause
Summary:        Pygments theme for jupyterlab
Url:            https://github.com/jupyterlab/jupyterlab_pygments
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab-pygments/jupyterlab_pygments-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygments >= 2.4.1
BuildArch:      noarch

%python_subpackages

%description
This package contains a syntax coloring theme for pygments making use
of the JupyterLab CSS variables.

%prep
%setup -q -n jupyterlab_pygments-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
