#
# spec file for package jupyter-matlab-kernel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without  test
Name:           jupyter-matlab-kernel
Version:        0.16.7
Release:        0
Summary:        Matlab kernel for Jupyter
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/Calysto/matlab_kernel
Source:         https://files.pythonhosted.org/packages/source/m/matlab-kernel/matlab_kernel-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jupyter-jupyter_client >= 4.4.0
BuildRequires:  python-rpm-macros
BuildRequires:  python3-certifi
BuildRequires:  python3-setuptools
BuildRequires:  python3-wurlitzer
Requires:       jupyter-ipython >= 4.0.0
Requires:       jupyter-jupyter_client >= 4.4.0
Requires:       jupyter-metakernel >= 0.20.8
Requires:       python3-wurlitzer
Suggests:       python-backports.tempfile
Suggests:       python-certifi
Provides:       python-jupyter_matlab_kernel = %{version}
Obsoletes:      python-jupyter_matlab_kernel < %{version}
Provides:       python-matlab-kernel = %{version}
BuildArch:      noarch

%description
A Matlab kernel for Jupyter. The Matlab kernel is based on
MetaKernel, which means it features a standard set of magics.

%prep
%setup -q -n matlab_kernel-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_jupyter_kernel_dir}

# Tests require MATLAB installed
# %%check
# %%pytest

%files
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/matlab_kernel-%{version}-py*.egg-info
%{python3_sitelib}/matlab_kernel/
%{_jupyter_kernel_dir}/matlab

%changelog
