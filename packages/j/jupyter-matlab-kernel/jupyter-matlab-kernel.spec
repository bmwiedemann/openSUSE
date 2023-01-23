#
# spec file for package jupyter-matlab-kernel
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


Name:           jupyter-matlab-kernel
Version:        0.17.1
Release:        0
Summary:        Matlab kernel for Jupyter
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/Calysto/matlab_kernel
Source:         https://files.pythonhosted.org/packages/source/m/matlab-kernel/matlab_kernel-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  python3-ipython >= 4.0.0
BuildRequires:  python3-jupyter_client >= 4.4.0
BuildRequires:  python3-metakernel >= 0.23
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-ipython >= 4.0.0
Requires:       python3-jupyter_client >= 4.4.0
Requires:       python3-metakernel >= 0.23
Provides:       python3-jupyter_matlab_kernel = %{version}-%{release}
Obsoletes:      python3-jupyter_matlab_kernel < %{version}-%{release}
Provides:       python3-matlab-kernel = %{version}-%{release}
BuildArch:      noarch

%description
A Matlab kernel for Jupyter. The Matlab kernel is based on
MetaKernel, which means it features a standard set of magics.

%prep
%setup -q -n matlab_kernel-%{version}

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_jupyter_kernel_dir}

# Tests require MATLAB installed
# %%check
# Use from the github repo: test_matlab_kernel.py

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/matlab_kernel-%{version}.dist-info
%{python3_sitelib}/matlab_kernel
%{_jupyter_kernel_dir}/matlab
%{_jupyter_kernel_dir}/matlab_connect

%changelog
