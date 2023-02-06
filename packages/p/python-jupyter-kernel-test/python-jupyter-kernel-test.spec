#
# spec file for package python-jupyter-kernel-test
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


Name:           python-jupyter-kernel-test
Version:        0.5.0
Release:        0
Summary:        A tool for testing Jupyter kernels
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_kernel_test
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_kernel_test/jupyter_kernel_test-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonschema
Requires:       python-jupyter_client >= 6.1.13
Provides:       python-jupyter_kernel_test = %{version}-%{release}
Obsoletes:      python-jupyter_kernel_test < %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module jupyter_client >= 6.1.13}
# /SECTION
%python_subpackages

%description
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol.

%prep
%setup -q -n jupyter_kernel_test-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyter_kernel_test
%{python_sitelib}/jupyter_kernel_test-%{version}*-info

%changelog
