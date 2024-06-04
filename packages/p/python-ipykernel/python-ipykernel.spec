#
# spec file for package python-ipykernel
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-ipykernel
Version:        6.29.4
Release:        0
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/ipykernel
Source:         https://files.pythonhosted.org/packages/source/i/ipykernel/ipykernel-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#ipython/ipykernel#1242
Patch0:         ignore-ipython-deprecationwarning.patch
Provides:       python-jupyter_ipykernel = %{version}
Obsoletes:      python-jupyter_ipykernel < %{version}
Provides:       %{python_module ipykernel-doc = %{version}}
Obsoletes:      %{python_module ipykernel-doc < %{version}}
Provides:       %{python_module jupyter_ipykernel-doc = %{version}}
Obsoletes:      %{python_module jupyter_ipykernel-doc < %{version}}
Provides:       %{python_module jupyter-ipykernel-doc = %{version}}
Obsoletes:      %{python_module jupyter-ipykernel-doc < %{version}}
BuildArch:      noarch
# SECTION build-system
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling >= 1.4}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION dependencies
BuildRequires:  %{python_module comm >= 0.1.1}
BuildRequires:  %{python_module debugpy >= 1.6.5}
BuildRequires:  %{python_module ipython >= 7.23.1}
BuildRequires:  %{python_module jupyter-client >= 6.1.12}
BuildRequires:  %{python_module matplotlib-inline >= 0.1}
BuildRequires:  %{python_module nest-asyncio}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyzmq >= 24}
BuildRequires:  %{python_module tornado >= 6.1}
BuildRequires:  %{python_module traitlets >= 5.1.0}
BuildRequires:  %{python_module jupyter-core >= 5.1 or (%python-jupyter-core >= 4.12 with %python-jupyter-core < 5.0)}
Requires:       jupyter-jupyter-client >= 6.1.12
Requires:       python-comm >= 0.1.1
Requires:       python-debugpy >= 1.6.5
Requires:       python-ipython >= 7.23.1
Requires:       python-jupyter-client >= 6.1.12
Requires:       python-matplotlib-inline >= 0.1
Requires:       python-nest-asyncio
Requires:       python-packaging
Requires:       python-psutil
Requires:       python-pyzmq >= 24
Requires:       python-tornado >= 6.1
Requires:       python-traitlets >= 5.4.0
Requires:       (python-jupyter-core >= 5.1 or (python-jupyter-core >= 4.12 with python-jupyter-core < 5.0))
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.23.5}
BuildRequires:  %{python_module pytest-timeout}
# we don't want ipyparallel and its dependencies in Ring1, see below
#BuildRequires:  #{python_module ipyparallel}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-ipykernel = %{version}-%{release}
Obsoletes:      jupyter-ipykernel < %{version}-%{release}
%endif
%python_subpackages

%description
This package provides the IPython kernel for Jupyter.

%prep
%autosetup -p1 -n ipykernel-%{version}
sed -i -e 's/, "--color=yes"//' pyproject.toml
sed -i -e '/ignore:.* current event loop:DeprecationWarning/ a \  "ignore:pytest-asyncio detected an unclosed event loop:DeprecationWarning",' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install

# use the symlink for the default python3 flavor, which was installed during the install but used python3.X name
# from the primary flavor.
sed -i "s|$(readlink -f python3)|python3|" %{buildroot}%{_jupyter_kernel_dir}/python3/kernel.json
%{python_expand # install kernelspecs for each flavor
PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m ipykernel install \
    --prefix=%{buildroot}%{_prefix} \
    --name python%{$python_bin_suffix} \
    --display-name 'Python %{$python_bin_suffix} (ipykernel)'
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%fdupes  %{buildroot}%{_jupyter_kernel_dir}

%check
# fails in obs setups
ignoretests="--ignore tests/test_debugger.py"
# flaky obs timeouts
donttest="test_init_ipc_socket"
# we don't want ipyparallel and its dependencies in Ring1
ignoretests="$ignoretests --ignore tests/test_pickleutil.py"
donttest="$donttest or test_do_apply"
%pytest -k "not ($donttest)" $ignoretests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ipykernel
%{python_sitelib}/ipykernel_launcher.py
%{python_sitelib}/ipykernel-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/ipykernel_launcher*.pyc
%{_jupyter_kernel_dir}/python%{python_bin_suffix}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
%{_jupyter_kernel_dir}/python3
%endif

%changelog
