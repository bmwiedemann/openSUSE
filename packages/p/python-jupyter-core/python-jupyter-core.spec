#
# spec file for package python-jupyter-core
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
%define         oldpython python
Name:           python-jupyter-core
Version:        4.6.1
Release:        0
Summary:        Base package on which Jupyter projects rely
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_core
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_core/jupyter_core-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- use_rpms_paths.patch -- change paths so they are easy to replace at build time
Patch0:         use_rpms_paths.patch
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traitlets}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyter_core = %{version}
Requires:       python-ipython_genutils
Requires:       python-traitlets
Recommends:     python-ipython
Provides:       python-jupyter_core = %{version}
Obsoletes:      python-jupyter_core < %{version}
%ifpython2
Provides:       %{oldpython}-jupyter_core = %{version}
Obsoletes:      %{oldpython}-jupyter_core < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects. It doesn't do much on its own.

There is no reason to install this package on its own.  It will be pulled in
as a dependency by packages that require it.

This package provides the python interface.

%package     -n jupyter-jupyter-core
Summary:        Base package on which Jupyter projects rely
Group:          Development/Languages/Python
Requires:       python3-jupyter_core = %{version}
Requires:       jupyter-notebook-filesystem
Provides:       jupyter-jupyter_core = %{version}
Obsoletes:      jupyter-jupyter_core < %{version}

%description -n jupyter-jupyter-core
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects. It doesn't do much on its own.

There is no reason to install this package on its own.  It will be pulled in
as a dependency by packages that require it.

This package provides the jupyter components.

%prep
%setup -q -n jupyter_core-%{version}
%patch0 -p1
# Set the appropriate paths dynamically
sed -i "s|\"%{_datadir}/jupyter\"|\"%{_datadir}/jupyter\"|" jupyter_core/paths.py
sed -i "s|\"%{_sysconfdir}/jupyter\"|\"%{_sysconfdir}/jupyter\"|" jupyter_core/paths.py
sed -i "s|(sys\.prefix, 'share', 'jupyter')|('%{_datadir}', 'jupyter')|" jupyter_core/paths.py
sed -i "s|(sys\.prefix, 'etc', 'jupyter')|('%{_sysconfdir}', 'jupyter')|" jupyter_core/paths.py

%build
%python_build

%install
%python_install

%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/jupyter_core/troubleshoot.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/jupyter_core/troubleshoot.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/jupyter_core/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/jupyter_core/
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%license COPYING.md
%{python_sitelib}/jupyter.py*
%pycache_only %{python_sitelib}/__pycache__/jupyter.*.py*
%{python_sitelib}/jupyter_core/
%{python_sitelib}/jupyter_core-%{version}-*.egg-info

%files -n jupyter-jupyter-core
%license COPYING.md
%doc CONTRIBUTING.md README.md
%{_bindir}/jupyter
%{_bindir}/jupyter-migrate
%{_bindir}/jupyter-troubleshoot

%changelog
