#
# spec file for package python-jupyter_console
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jupyter_console
Version:        6.4.0
Release:        0
Summary:        Jupyter terminal console
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_console
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_console/jupyter_console-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module prompt_toolkit >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
# /SECTION
Requires:       jupyter-jupyter_console = %{version}
Requires:       python-ipykernel
Requires:       python-ipython
Requires:       python-jupyter-client
Requires:       python-prompt_toolkit >= 2
Requires:       python-pyzmq
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-jupyter-console = %{version}-%{release}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-jupyter_console = %{version}-%{release}
Obsoletes:      jupyter-jupyter_console < %{version}-%{release}
Provides:       jupyter-jupyter_console-doc = %{version}-%{release}
Obsoletes:      jupyter-jupyter_console-doc < %{version}-%{release}
%endif
BuildArch:      noarch
%python_subpackages

%description
A terminal-based console frontend for Jupyter kernels.
This code is based on the single-process IPython terminal.

%prep
%setup -q -n jupyter_console-%{version}
# always build and install with setuptools: it is needed to get the entrypoint gh#jupyter/jupyter_console#222
sed -i '/import sys/ a import setuptools' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-console
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -s --force-flaky --max-runs=10

%post
%python_install_alternative jupyter-console

%postun
%python_uninstall_alternative jupyter-console

%files %{python_files}
%doc CONTRIBUTING.md README.md
%license COPYING.md
%python_alternative %{_bindir}/jupyter-console
%{python_sitelib}/jupyter_console
%{python_sitelib}/jupyter_console-%{version}*-info

%changelog
