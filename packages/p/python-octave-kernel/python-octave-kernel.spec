#
# spec file for package python-octave-kernel
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
%define         skip_python2 1
Name:           python-octave-kernel
Version:        0.32.0
Release:        0
Summary:        A Jupyter kernel for Octave
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/Calysto/octave_kernel
Source:         https://files.pythonhosted.org/packages/source/o/octave-kernel/octave_kernel-%{version}.tar.gz
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-client >= 4.3.0}
BuildRequires:  %{python_module metakernel >= 0.24.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jupyter_kernel_test}
BuildRequires:  octave-cli
# /SECTION
Requires:       jupyter-octave-kernel = %{version}
Requires:       python-ipykernel
Requires:       python-jupyter-client >= 4.3.0
Requires:       python-metakernel >= 0.24.0
Provides:       python-jupyter_octave_kernel = %{version}
Obsoletes:      python-jupyter_octave_kernel < %{version}
Conflicts:      jupyter-octave_kernel < 0.29.0
BuildArch:      noarch

%python_subpackages

%description
A kernel to allow Octave to be used in Jupyter.

This package provides the python interface.

%package     -n jupyter-octave-kernel
Summary:        Interactive plotting package for the Jupyter notebook
Group:          Development/Languages/Python
Requires:       jupyter-notebook
Requires:       python3-octave-kernel = %{version}
Provides:       jupyter-octave_kernel = %{version}
Obsoletes:      jupyter-octave_kernel < %{version}
Conflicts:      python3-jupyter_octave_kernel < 0.29.0

%description -n jupyter-octave-kernel
A kernel to allow Octave to be used in Jupyter.

This package provides the jupyter notebook extension.

%prep
%setup -q -n octave_kernel-%{version}

%build
%python_build

%install
%python_install
sed -i "s|\"python\"|\"python3\"|" %{buildroot}%{_jupyter_kernel_dir}/octave/kernel.json

%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test_octave_kernel.py}

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/octave_kernel/
%{python_sitelib}/octave_kernel-%{version}-py*.egg-info

%files -n jupyter-octave-kernel
%license LICENSE.txt
%{_jupyter_kernel_dir}/octave/

%changelog
