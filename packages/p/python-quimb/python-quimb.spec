#
# spec file for package python-quimb
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


%define packagename quimb
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-quimb
Version:        1.3.0
Release:        0
Summary:        Python library for quantum information and many-body calculations
License:        Apache-2.0
URL:            https://quimb.readthedocs.io/
Source:         https://github.com/jcmgray/quimb/archive/%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module autoray >= 0.1}
BuildRequires:  %{python_module cytoolz >= 0.8.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module numba >= 0.39}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module opt-einsum >= 2}
BuildRequires:  %{python_module psutil >= 4.3.1}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm >= 4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-autoray >= 0.1
Requires:       python-cytoolz >= 0.8.0
Requires:       python-matplotlib
Requires:       python-networkx
Requires:       python-numba >= 0.39
Requires:       python-numpy >= 1.17
Requires:       python-opt-einsum >= 2
Requires:       python-psutil >= 4.3.1
Requires:       python-scipy >= 1.0.0
Requires:       python-tqdm >= 4
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-mpi4py
Suggests:       python-petsc4py
Suggests:       python-randomgen >= 1.18
Suggests:       python-slepc4py
# This package does not support 32 bit arch.
ExcludeArch:    i586
%python_subpackages

%description
quimb is an easy but fast python library for quantum information and
many-body calculations, including with tensor networks.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/quimb-mpi-python
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative quimb-mpi-python

%postun
%python_uninstall_alternative quimb-mpi-python

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/quimb-mpi-python
%{python_sitelib}/*egg-info
%{python_sitelib}/%{packagename}

%changelog
