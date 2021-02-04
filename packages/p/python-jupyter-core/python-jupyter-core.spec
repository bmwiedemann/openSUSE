#
# spec file for package python-jupyter-core
#
# Copyright (c) 2021 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-jupyter-core%{psuffix}
Version:        4.7.1
Release:        0
Summary:        Base package on which Jupyter projects rely
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_core
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_core/jupyter_core-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- use_rpms_paths.patch -- change paths so they are easy to replace at build time
Patch0:         use_rpms_paths.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traitlets}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  python-rpm-macros
Requires:       python-traitlets
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-ipython
Provides:       python-jupyter_core = %{version}-%{release}
Obsoletes:      python-jupyter_core < %{version}-%{release}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-jupyter-core = %{version}-%{release}
Obsoletes:      jupyter-jupyter-core < %{version}-%{release}
Provides:       jupyter-jupyter_core = %{version}-%{release}
Obsoletes:      jupyter-jupyter_core < %{version}-%{release}
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects. It doesn't do much on its own.

There is no reason to install this package on its own.  It will be pulled in
as a dependency by packages that require it.

%prep
%setup -q -n jupyter_core-%{version}
%patch0 -p1
# Set the appropriate hardcoded paths dynamically
sed -i "s|\"_datadir_jupyter_\"|\"%{_datadir}/jupyter\"|" jupyter_core/paths.py
sed -i "s|\"_sysconfdir_jupyter_\"|\"%{_sysconfdir}/jupyter\"|" jupyter_core/paths.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/jupyter
%python_clone -a %{buildroot}%{_bindir}/jupyter-migrate
%python_clone -a %{buildroot}%{_bindir}/jupyter-troubleshoot
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/jupyter_core/troubleshoot.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/jupyter_core/troubleshoot.py
}
%python_compileall
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
pushd jupyter_core/tests
# test_jupyter_path_prefer_env does not work outside venvs: gh#jupyter/jupyter_core#208
%pytest -k "not test_jupyter_path_prefer_env"
popd
%endif

%post
%python_install_alternative jupyter jupyter-migrate jupyter-troubleshoot

%postun
%python_uninstall_alternative jupyter

%if !%{with test}
%files %{python_files}
%license COPYING.md
%python_alternative %{_bindir}/jupyter
%python_alternative %{_bindir}/jupyter-migrate
%python_alternative %{_bindir}/jupyter-troubleshoot
%{python_sitelib}/jupyter.py*
%pycache_only %{python_sitelib}/__pycache__/jupyter.*.py*
%{python_sitelib}/jupyter_core/
%{python_sitelib}/jupyter_core-%{version}*-info
%endif

%changelog
