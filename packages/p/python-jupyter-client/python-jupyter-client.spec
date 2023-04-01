#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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

Name:           python-jupyter-client%{psuffix}
Version:        8.1.0
Release:        0
Summary:        Jupyter protocol implementation and client libraries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_client
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_client/jupyter_client-%{version}.tar.gz
# PATCH-FIX-OPENSUSE jupyter-client-suse-remove-ifconfig-test.patch code@bnavigator.de -- we don't have `ifconfig` and don't need it because we have `ip`
Patch10:        jupyter-client-suse-remove-ifconfig-test.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyter_client = %{version}
Requires:       python-entrypoints
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-pyzmq >= 23.0
Requires:       python-tornado >= 6.2
Requires:       python-traitlets >= 5.3
Requires:       (python-importlib-metadata >= 4.8.3 if python-base < 3.10)
Requires:       (python-jupyter-core >= 5.1 or (python-jupyter-core >= 4.12 with python-jupyter-core < 5.0))
Provides:       python-jupyter_client = %{version}
Obsoletes:      python-jupyter_client < %{version}
BuildArch:      noarch
%if %{with test}
# gh#jupyter/jupyter_client#787
BuildRequires:  %{python_module ipykernel >= 6.14}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter-client = %{version}}
BuildRequires:  %{python_module pytest-jupyter-client >= 0.4.1}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# flaky is not an upstream dep, but for obs flakyness of parallel kernel test
BuildRequires:  %{python_module flaky}
BuildRequires:  iproute2
BuildRequires:  openssh-clients
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
# flaky timeout
donttest="(TestAsyncKernelClient and test_input_request)"
%pytest --force-flaky --max-runs=3 --no-success-flaky-report -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyter_client-%{version}*-info
%{python_sitelib}/jupyter_client/

%files -n jupyter-jupyter-client
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/jupyter-kernel
%{_bindir}/jupyter-kernelspec
%{_bindir}/jupyter-run
%endif

%changelog
