#
# spec file for package python-rpyc
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
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-rpyc%{psuffix}
Version:        6.0.1
Release:        0
Summary:        Remote Python Call (RPyC), a RPC library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tomerfiliba/rpyc
Source:         https://github.com/tomerfiliba/rpyc/archive/%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-plumbum >= 1.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module plumbum >= 1.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rpyc = %{version}}
BuildRequires:  gcc-c++
%endif
%python_subpackages

%description
RPyC (pronounced like "are-pie-see"), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls,
clustering, and distributed-computing.  RPyC makes use of
object-proxying, a technique that employs python's dynamic nature, to
overcome the physical boundaries between processes and computers, so
that remote objects can be manipulated as if they were local.

%prep
%setup -q -n rpyc-%{version}
# Replace hashbangs
sed -i -e "s|env python|python%{python_bin_suffix}|" rpyc/cli/rpyc_classic.py rpyc/cli/rpyc_registry.py

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mv %{buildroot}%{_bindir}/rpyc_classic.py %{buildroot}%{_bindir}/rpyc_classic
mv %{buildroot}%{_bindir}/rpyc_registry.py %{buildroot}%{_bindir}/rpyc_registry

%python_clone -a %{buildroot}%{_bindir}/rpyc_classic
%python_clone -a %{buildroot}%{_bindir}/rpyc_registry
%endif

%if %{with test}
%check
export PYTEST_ADDOPTS="--import-mode=importlib" PYTHONPATH="."
pushd tests
donttest="TestDeploy or TestUdpRegistry"
# Fails with python 3.11
donttest+=" or test_gdb"
%pytest -k "not ($donttest)"
popd
%endif

%if !%{with test}
%post
%{python_install_alternative rpyc_classic rpyc_registry}

%postun
%python_uninstall_alternative rpyc_classic

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/rpyc_classic
%python_alternative %{_bindir}/rpyc_registry
%{python_sitelib}/rpyc
%{python_sitelib}/rpyc-%{version}.dist-info
%endif

%changelog
