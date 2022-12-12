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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-jupyter-client%{psuffix}
Version:        7.3.4
Release:        0
Summary:        Jupyter protocol implementation and client libraries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_client
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_client/jupyter_client-%{version}.tar.gz
# PATCH-FIX-OPENSUSE py3109-compat.patch
Patch0:         py3109-compat.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyter_client = %{version}
Requires:       python-entrypoints
Requires:       python-jupyter-core >= 4.9.2
Requires:       python-nest-asyncio >= 1.5.4
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-pyzmq >= 23.0
Requires:       python-tornado >= 6.0
Requires:       python-traitlets
Provides:       python-jupyter_client = %{version}
Obsoletes:      python-jupyter_client < %{version}
BuildArch:      noarch
%if %{with test}
# gh#jupyter/jupyter_client#787
BuildRequires:  %{python_module ipykernel >= 6.13}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter-client = %{version}}
BuildRequires:  %{python_module pytest-asyncio >= 0.18}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# flaky is not an upstream dep, but for obs flakyness of parallel kernel test
BuildRequires:  %{python_module flaky}
%endif
%python_subpackages

%description
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the jupyter kernelspec entrypoint for installing kernelspecs
for use with Jupyter frontends.

This package provides the python interface.

%package     -n jupyter-jupyter-client
Summary:        Jupyter protocol implementation and client libraries
Group:          Development/Languages/Python
Requires:       python3-jupyter-client = %{version}
Provides:       jupyter-jupyter_client = %{version}
Obsoletes:      jupyter-jupyter_client < %{version}
Provides:       jupyter-jupyter-client-doc = %{version}
Obsoletes:      jupyter-jupyter-client-doc < %{version}

%description -n jupyter-jupyter-client
This package contains the reference implementation of the Jupyter protocol.
It also provides client and kernel management APIs for working with kernels.

It also provides the jupyter kernelspec entrypoint for installing kernelspecs
for use with Jupyter frontends.

This package provides the jupyter components.

%prep
%autosetup -p1 -n jupyter_client-%{version}
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
pushd jupyter_client/tests
%pytest --force-flaky --max-runs=3 --no-success-flaky-report
popd
%endif

%if !%{with test}
%files %{python_files}
%license COPYING.md
%{python_sitelib}/jupyter_client-%{version}*-info
%{python_sitelib}/jupyter_client/

%files -n jupyter-jupyter-client
%license COPYING.md
%doc CONTRIBUTING.md README.md
%{_bindir}/jupyter-kernel
%{_bindir}/jupyter-kernelspec
%{_bindir}/jupyter-run
%endif

%changelog
