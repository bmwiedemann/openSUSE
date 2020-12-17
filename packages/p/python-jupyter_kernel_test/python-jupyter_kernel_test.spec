#
# spec file for package python-jupyter_kernel_test
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
%define mname jupyter_kernel_test
Name:           python-%{mname}
Version:        0.3
Release:        0
Summary:        Machinery for testing Jupyter kernels via the messaging protocol
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter_kernel_test
Source:         %{url}/archive/%{version}.tar.gz#/%{mname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#github.com/jupyter/jupyter_kernel_test#37 -- use jsonschema to validate messages, removes nose
Patch0:         %{url}/pull/37.patch#/%{mname}-pr37-usejsonschema.patch
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-flit
Requires:       python-jsonschema
Requires:       python-jupyter_client
Requires:       python-traitlets
Provides:       python-jupyter-kernel-test = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipykernel}
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
Provides:       jupyter-jupyter_kernel_test = %{version}-%{release}
%endif
%python_subpackages

%description
jupyter_kernel_test is a tool for testing Jupyter kernels.
It tests kernels for successful code execution and
conformance with the Jupyter Messaging Protocol
(currently 5.0).

%prep
%autosetup -p1 -n %{mname}-%{version}

%build
python3 -m flit.tomlify
%pyproject_wheel

%install
%pyproject_install

%check
%pyunittest test_ipykernel.py -v
# test_irkernel.py: no jupyter R kernel package on openSUSE yet (R-IRkernel)

%files %{python_files}
%license COPYING.md
%doc README.rst
%{python_sitelib}/%{mname}
%{python_sitelib}/%{mname}-%{version}*-info

%changelog
