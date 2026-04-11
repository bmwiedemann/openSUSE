#
# spec file for package python-octave-kernel
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# truncate trailing .0
%define distversion 1.0.3
Name:           python-octave-kernel
Version:        1.0.3
Release:        0
Summary:        A Jupyter kernel for Octave
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Calysto/octave_kernel
Source:         https://files.pythonhosted.org/packages/source/o/octave_kernel/octave_kernel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module hatchling >= 1.5}
BuildRequires:  %{python_module ipykernel >= 6.22.0}
BuildRequires:  %{python_module jupyter-client >= 8.1.0}
BuildRequires:  %{python_module jupyter_kernel_test}
BuildRequires:  %{python_module metakernel >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  octave
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       jupyter-octave-kernel = %{version}
Requires:       octave
Requires:       python-ipykernel >= 6.22.0
Requires:       python-jupyter-client >= 8.1.0
Requires:       python-metakernel >= 1.0
Provides:       python-jupyter_octave_kernel = %{version}-%{release}
Obsoletes:      python-jupyter_octave_kernel < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
A kernel to allow Octave to be used in Jupyter.

This package provides the python interface.

%package     -n jupyter-octave-kernel
Summary:        Interactive plotting package for the Jupyter notebook
Group:          Development/Languages/Python
Requires:       jupyter-notebook
Requires:       python3dist(octave-kernel) = %{distversion}
Suggests:       python3-octave-kernel = %{version}
Conflicts:      python3-jupyter_octave_kernel < 0.29.0
Provides:       jupyter-octave_kernel = %{version}-%{release}
Obsoletes:      jupyter-octave_kernel < %{version}-%{release}

%description -n jupyter-octave-kernel
A kernel to allow Octave to be used in Jupyter.

This package provides the jupyter notebook extension.

%prep
%autosetup -p1 -n octave_kernel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%fdupes %{buildroot}%{_jupyter_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export JUPYTER_PATH=%{buildroot}%{_jupyter_prefix}
# no test_execute_stdout: gh#Calysto/octave_kernel#240 -- octave does not find qt toolkit backed
%pytest test_octave_kernel.py -k "not test_execute_stdout"

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/octave_kernel/
%{python_sitelib}/octave_kernel-%{version}*-info

%files -n jupyter-octave-kernel
%license LICENSE.txt
%{_jupyter_kernel_dir}/octave/

%changelog
