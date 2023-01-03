#
# spec file
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


#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-jupyter-core%{psuffix}
Version:        5.1.1
Release:        0
Summary:        Base package on which Jupyter projects rely
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_core
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_core/jupyter_core-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- use_rpms_paths.patch -- change paths so they are easy to replace at build time
Patch0:         use_rpms_paths.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-platformdirs >= 2.5
Requires:       python-traitlets >= 5.3
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
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
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-core = %{version}}
BuildRequires:  %{python_module pytest-timeout}
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
%autosetup -p1 -n jupyter_core-%{version}
# Set the appropriate hardcoded paths dynamically
sed -i "s|@_datadir_jupyter_@|\"%{_datadir}/jupyter\"|" jupyter_core/paths.py
sed -i "s|@_distconfdir_jupyter_@|\"%{_distconfdir}/jupyter\"|" jupyter_core/paths.py
sed -i "/addopts/ s/--color=yes//" pyproject.toml

%if !%{with test}
%build
%pyproject_wheel
%endif

%if !%{with test}
%install
%pyproject_install
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
# does not work outside venvs: gh#jupyter/jupyter_core#208
donttest="test_jupyter_path_prefer_env or test_jupyter_config_path_prefer_env"
# we changed the xdg path
donttest="$donttest or test_config_dir_linux"
%pytest -k "not ($donttest)"
%endif

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter

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
