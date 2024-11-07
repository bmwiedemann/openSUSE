#
# spec file for package python-jupyter-client
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# python-pytest-jupyter-client is not available on python 313
%define skip_python313 1
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-jupyter-client%{psuffix}
Version:        8.6.3
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
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-pyzmq >= 23.0
Requires:       python-tornado >= 6.2
Requires:       python-traitlets >= 5.3
Requires:       (python-importlib-metadata >= 4.8.3 if python-base < 3.10)
Requires:       (python-jupyter-core >= 5.1 or (python-jupyter-core >= 4.12 with python-jupyter-core < 5.0))
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-jupyter_client = %{version}-%{release}
Obsoletes:      python-jupyter_client < %{version}-%{release}
Provides:       jupyter-jupyter-client = %{version}-%{release}
Obsoletes:      jupyter-jupyter-client < %{version}-%{release}
Provides:       jupyter-jupyter_client = %{version}-%{release}
Obsoletes:      jupyter-jupyter_client < %{version}-%{release}
Provides:       jupyter-jupyter-client-doc = %{version}-%{release}
Obsoletes:      jupyter-jupyter-client-doc < %{version}-%{release}
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

%prep
%autosetup -p1 -n jupyter_client-%{version}
sed -i 's/"--color=yes",//' pyproject.toml

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-kernel
%python_clone -a %{buildroot}%{_bindir}/jupyter-kernelspec
%python_clone -a %{buildroot}%{_bindir}/jupyter-run
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# flaky timeout
donttest="(TestAsyncKernelClient and test_input_request)"
# timeout
donttest+=" or (TestKernelManager and test_stream_on_recv)"
%pytest --force-flaky --max-runs=3 --no-success-flaky-report -k "not ($donttest)"
%endif

%post
%python_install_alternative jupyter-kernel jupyter-kernelspec jupyter-run

%postun
%python_uninstall_alternative jupyter-kernel

%if !%{with test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyter_client-%{version}*-info
%{python_sitelib}/jupyter_client/
%python_alternative %{_bindir}/jupyter-kernel
%python_alternative %{_bindir}/jupyter-kernelspec
%python_alternative %{_bindir}/jupyter-run
%endif

%changelog
