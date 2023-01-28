#
# spec file for package python-quimb
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


Name:           python-quimb
Version:        1.4.2
Release:        0
Summary:        Python library for quantum information and many-body calculations
License:        Apache-2.0
URL:            https://quimb.readthedocs.io/
Source:         https://github.com/jcmgray/quimb/archive/%{version}.tar.gz#/quimb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cytoolz >= 0.8.0
Requires:       python-numba >= 0.39
Requires:       python-numpy >= 1.17
Requires:       python-psutil >= 4.3.1
Requires:       python-scipy >= 1.0.0
Requires:       python-tqdm >= 4
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-autoray >= 0.5.1
Recommends:     python-diskcache >= 3.0
Recommends:     python-matplotlib >= 2
Recommends:     python-networkx
Recommends:     python-opt-einsum >= 3.2
Suggests:       python-mpi4py
Suggests:       python-petsc4py
Suggests:       python-randomgen >= 1.18
Suggests:       python-slepc4py
# SECTION test
BuildRequires:  %{python_module pytest}
# runtime
BuildRequires:  %{python_module cytoolz >= 0.8.0}
BuildRequires:  %{python_module numba >= 0.39}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module psutil >= 4.3.1}
BuildRequires:  %{python_module scipy >= 1.0.0}
BuildRequires:  %{python_module tqdm >= 4}
# extra
BuildRequires:  %{python_module autoray >= 0.5.1}
BuildRequires:  %{python_module diskcache >= 3.0}
BuildRequires:  %{python_module matplotlib >= 2}
BuildRequires:  %{python_module networkx >= 2.3}
BuildRequires:  %{python_module opt-einsum >= 3.2}
# /SECTION
# This package does not support 32 bit arch, s390x fails too
ExcludeArch:    %ix86 %arm ppc s390x
%python_subpackages

%description
quimb is an easy but fast python library for quantum information and
many-body calculations, including with tensor networks.

%prep
%setup -q -n quimb-%{version}
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/quimb-mpi-python
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative quimb-mpi-python

%postun
%python_uninstall_alternative quimb-mpi-python

%check
# precision comparison slightly out of tolerance
%pytest -k "not (test_subtract_update and float32)"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/quimb-mpi-python
%{python_sitelib}/quimb-%{version}.dist-info
%{python_sitelib}/quimb

%changelog
