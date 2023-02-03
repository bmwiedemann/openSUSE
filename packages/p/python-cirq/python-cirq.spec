#
# spec file for package python-cirq
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


%define plainpython python
%define cirqmodules core aqt google ionq pasqal web rigetti
Name:           python-cirq
Version:        1.1.0
Release:        0
Summary:        Library for writing quantum circuits
License:        Apache-2.0
URL:            https://github.com/quantumlib/Cirq
Source:         https://github.com/quantumlib/Cirq/archive/v%{version}.tar.gz#/Cirq-%{version}.tar.gz
# PATCH-FIX-UPSTREAM cirq-pr5991-np1.24.patch gh#quantumlib/Cirq#5991
Patch0:         cirq-pr5991-np1.24.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION cirq-core
BuildRequires:  %{python_module duet >= 0.2}
BuildRequires:  %{python_module matplotlib >= 3.0}
BuildRequires:  %{python_module networkx >= 2.4}
BuildRequires:  %{python_module numpy >= 1.16}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sortedcontainers >= 2.0}
BuildRequires:  %{python_module sympy}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
# SECTION cirq-aqt, cirq-ionq, cirq-pasqal
BuildRequires:  %{python_module requests >= 2.18}
# /SECTION
# SECTION cirq-google
BuildRequires:  %{python_module google-api-core >= 1.14.0}
BuildRequires:  %{python_module proto-plus >= 1.20.0}
BuildRequires:  %{python_module protobuf >= 3.12.0}
# google-api-core[grpc]
BuildRequires:  %{python_module grpcio}
# /SECTION
BuildRequires:  %{python_module pyquil >= 3.2.0}
# SECTION cirq-core[contrib]
BuildRequires:  %{python_module autoray}
BuildRequires:  %{python_module PyLaTeX >= 1.3.0}
BuildRequires:  %{python_module numba >= 0.53}
BuildRequires:  %{python_module opt-einsum}
BuildRequires:  %{python_module ply >= 3.6}
BuildRequires:  %{python_module quimb}
# /SECTION
# SECTION test
BuildRequires:  %{python_module flynt >= 0.60}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module freezegun >= 0.3.15}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
#/SECTION
Requires:       %plainpython(abi) = %python_version
Requires:       python-cirq-aqt
Requires:       python-cirq-core
Requires:       python-cirq-google
Requires:       python-cirq-ionq
Requires:       python-cirq-pasqal
Requires:       python-cirq-rigetti
Requires:       python-cirq-web
# quimb does not support 32 bit arch.
ExcludeArch:    %ix86 %arm ppc
BuildArch:      noarch
%python_subpackages

%description
Cirq is a software library for writing, manipulating, and optimizing
quantum circuits and then running them against quantum computers and
simulators.

This metapackage requires all circ subpackages

%package core
Summary:        Cirq quantum algorithms for NISQ devices
Requires:       python-duet >= 0.2.0
Requires:       python-matplotlib >= 3.0
Requires:       python-networkx >= 2.4
Requires:       python-numpy >= 1.16
Requires:       python-pandas
Requires:       python-scipy
Requires:       python-sortedcontainers >= 2.0
Requires:       python-sympy
Requires:       python-tqdm
Requires:       python-typing_extensions

%description core
Cirq is a Python library for writing, manipulating, and optimizing quantum
circuits and running them against quantum computers and simulators.

This module contains everything you'd need to write quantum algorithms for NISQ devices and run them on the built-in Cirq simulators.
In order to run algorithms on a given quantum hardware platform, you'll have to install the right cirq module as well.

%package core-contrib
Summary:        Cirq quantum algorithms for NISQ devices
Requires:       python-PyLaTeX >= 1.3.0
Requires:       python-autoray
Requires:       python-cirq-core = %{version}
Requires:       python-numba >= 0.53
Requires:       python-opt-einsum
Requires:       python-ply >= 3.6
Requires:       python-quimb

%description core-contrib
The cirq-core[contrib] extra

%package aqt
Summary:        Cirq quantum algorithms on AQT quantum computers
Requires:       python-cirq-core = %{version}
Requires:       python-requests >= 2.18

%description aqt
A Cirq package to simulate and connect to Alpine Quantum Technologies quantum computers

%package ionq
Summary:        Cirq quantum algorithms on IonQ quantum computers
Requires:       python-cirq-core = %{version}
Requires:       python-requests >= 2.18

%description ionq
A Cirq package to simulate and connect to IonQ quantum computers

%package pasqal
Summary:        Cirq quantum algorithms on Pasqal quantum computers
Requires:       python-cirq-core = %{version}
Requires:       python-requests >= 2.18

%description pasqal
A Cirq package to simulate and connect to Pasqal quantum computers

%package google
Summary:        Cirq package for Google Quantum Computing Service1
Requires:       python-cirq-core = %{version}
Requires:       python-google-api-core >= 1.14.0
# google-api-core[grpc]
Requires:       python-grpcio
Requires:       python-protobuf >= 3.13.0

%description google
A Cirq module that provides tools and access to the Google Quantum Computing Service

%package web
Summary:        Web-based 3D visualization tools for Cirq

%description web
Cirq is a Python library for writing, manipulating, and optimizing quantum
circuits and running them against quantum computers and simulators.

This package allows users to take advantage of browser based 3D visualization tools
and features in Cirq. cirq-web also provides a development environment for contributors to create and add
their own visualizations to the module.

%package rigetti
Summary:        Cirq package for Rigetti quantum computers and Quil QVM
Requires:       python-cirq-core = %{version}
Requires:       python-pyquil >= 3.2.0

%description rigetti
Cirq is a Python library for writing, manipulating, and optimizing quantum
circuits and running them against quantum computers and simulators.

This module provides everything you'll need to run Cirq quantum algorithms on Rigetti quantum computers.

%prep
%autosetup -p1 -n Cirq-%{version}

%build
for p in %cirqmodules; do
  pushd cirq-$p
  %pyproject_wheel
  popd
done
%pyproject_wheel

%install
for p in %cirqmodules; do
  cp cirq-$p/dist/*.whl dist/
done
%python_expand cp dist/*.whl build/
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests assume testfiles and import path to be the same, but we test BUILDROOT
donttest="test_json_test_data_coverage"
donttest="$donttest or test_json_and_repr_data"
for p in %cirqmodules; do
  pushd cirq-$p
  %pytest -v -k "not ($donttest)" -n auto
  popd
done

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/cirq-%{version}*-info

%files %{python_files core}
%doc cirq-core/README.rst
%license cirq-core/LICENSE
%{python_sitelib}/cirq
%{python_sitelib}/cirq_core-%{version}*-info

%files %{python_files core-contrib}
%doc cirq-core/README.rst
%license cirq-core/LICENSE

%files %{python_files aqt}
%doc cirq-aqt/README.rst
%license cirq-aqt/LICENSE
%{python_sitelib}/cirq_aqt
%{python_sitelib}/cirq_aqt-%{version}*-info

%files %{python_files ionq}
%doc cirq-ionq/README.rst
%license cirq-ionq/LICENSE
%{python_sitelib}/cirq_ionq
%{python_sitelib}/cirq_ionq-%{version}*-info

%files %{python_files pasqal}
%doc cirq-pasqal/README.rst
%license cirq-pasqal/LICENSE
%{python_sitelib}/cirq_pasqal
%{python_sitelib}/cirq_pasqal-%{version}*-info

%files %{python_files google}
%doc cirq-google/README.rst
%license cirq-google/LICENSE
%{python_sitelib}/cirq_google
%{python_sitelib}/cirq_google-%{version}*-info

%files %{python_files web}
%doc cirq-web/README.rst
%license cirq-web/LICENSE
%{python_sitelib}/cirq_ts
%{python_sitelib}/cirq_web
%{python_sitelib}/cirq_web-%{version}*-info

%files %{python_files rigetti}
%doc cirq-rigetti/README.rst
%license cirq-rigetti/LICENSE
%{python_sitelib}/cirq_rigetti
%{python_sitelib}/cirq_rigetti-%{version}*-info

%changelog
