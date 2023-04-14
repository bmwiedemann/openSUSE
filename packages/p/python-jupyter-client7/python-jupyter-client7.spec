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

Name:           python-jupyter-client7%{psuffix}
Version:        7.4.9
Release:        0
Summary:        Jupyter protocol implementation and client libraries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_client
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_client/jupyter_client-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-entrypoints
Requires:       python-jupyter-core >= 4.9.2
Requires:       python-nest-asyncio >= 1.5.4
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-pyzmq >= 23.0
Requires:       python-tornado >= 6.2
Requires:       python-traitlets
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-jupyter-client = %{version}-%{release}
# Conflict with the python-jupyter-client 8 package
Conflicts:      python-jupyter-client
Provides:       jupyter-jupyter-client = %{version}-%{release}
Obsoletes:      jupyter-jupyter-client < %{version}-%{release}
Provides:       jupyter-jupyter-client7 = %{version}-%{release}
Obsoletes:      jupyter-jupyter-client7 < %{version}-%{release}
Provides:       python-jupyter_client = %{version}-%{release}
Obsoletes:      python-jupyter_client < %{version}-%{release}
Provides:       jupyter-jupyter_client = %{version}-%{release}
Obsoletes:      jupyter-jupyter_client < %{version}-%{release}
Provides:       jupyter-jupyter-client-doc = %{version}-%{release}
Obsoletes:      jupyter-jupyter-client-doc < %{version}-%{release}
BuildArch:      noarch
%if %{with test}
# gh#jupyter/jupyter_client#787
BuildRequires:  %{python_module ipykernel >= 6.13}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module jupyter-client7 = %{version}}
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

%prep
%autosetup -p1 -n jupyter_client-%{version}
sed -i 's/--color=yes//' pyproject.toml

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
pushd jupyter_client/tests
%pytest --force-flaky --max-runs=3 --no-success-flaky-report
popd
%endif

%post
%python_install_alternative jupyter-kernel jupyter-kernelspec jupyter-run

%postun
%python_uninstall_alternative jupyter-kernel

%if !%{with test}
%files %{python_files}
%license COPYING.md
%{python_sitelib}/jupyter_client-%{version}*-info
%{python_sitelib}/jupyter_client/
%python_alternative %{_bindir}/jupyter-kernel
%python_alternative %{_bindir}/jupyter-kernelspec
%python_alternative %{_bindir}/jupyter-run
%endif

%changelog
