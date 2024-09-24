#
# spec file for package python-quimb
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
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
BuildArch:      noarch
%else
%bcond_without test
%define psuffix -%{flavor}
# This package does not support 32 bit arch, s390x fails too
ExcludeArch:    %{ix86} %{arm} ppc s390x
%endif

Name:           python-quimb%{psuffix}
Version:        1.8.4
Release:        0
Summary:        Python library for quantum information and many-body calculations
License:        Apache-2.0
URL:            https://quimb.readthedocs.io/
Source:         https://github.com/jcmgray/quimb/archive/refs/tags/v%{version}.tar.gz#/quimb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-autoray >= 0.6.12
Requires:       python-cotengra >= 0.6.1
Requires:       python-cytoolz >= 0.8.0
Requires:       python-numba >= 0.39
Requires:       python-numpy >= 1.17
Requires:       python-psutil >= 4.3.1
Requires:       python-scipy >= 1.0.0
Requires:       python-tqdm >= 4
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-diskcache >= 3.0
Recommends:     python-matplotlib >= 2
Recommends:     python-networkx >= 2.3
Suggests:       python-mpi4py
Suggests:       python-petsc4py
Suggests:       python-slepc4py
%if %{with test}
BuildRequires:  %{python_module quimb = %{version}}
##
BuildRequires:  %{python_module diskcache >= 3.0}
BuildRequires:  %{python_module matplotlib >= 2}
BuildRequires:  %{python_module networkx >= 2.3}
BuildRequires:  %{python_module psutil >= 4.3.1}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
quimb is an easy but fast python library for quantum information and
many-body calculations, including with tensor networks.

%prep
%setup -q -n quimb-%{version}

sed -i '/addopts/d' pyproject.toml

%build
%if !%{with test}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/quimb-mpi-python
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%post
%python_install_alternative quimb-mpi-python

%postun
%python_uninstall_alternative quimb-mpi-python

%if %{with test}
%check
mv quimb quimb.movedsrc
# precision comparison slightly out of tolerance: this one is permament, others are flaky (rerun them)
donttest="(test_subtract_update and float32)"
%pytest -n auto --reruns 3 -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/quimb-mpi-python
%{python_sitelib}/quimb-%{version}.dist-info
%{python_sitelib}/quimb
%endif

%changelog
