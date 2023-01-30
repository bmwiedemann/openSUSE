#
# spec file for package python-pyquil
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


Name:           python-pyquil
Version:        3.3.3
Release:        0
Summary:        A Python library to generate Quantum Instruction Language (Quil) Programs
License:        Apache-2.0
URL:            https://github.com/rigetti/pyquil
Source:         https://github.com/rigetti/pyquil/archive/v%{version}.tar.gz#/pyquil-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module importlib-metadata >= 3.7.3 if %python-base < 3.8}
BuildRequires:  %{python_module lark >= 0.11.1}
BuildRequires:  %{python_module networkx >= 2.5}
BuildRequires:  %{python_module numpy >= 1.21}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module qcs-api-client >= 0.21 with %python-qcs-api-client < 0.22.0}
BuildRequires:  %{python_module retry}
BuildRequires:  %{python_module rpcq >= 3.10.0}
BuildRequires:  %{python_module scipy >= 1.6.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lark >= 0.11.1
Requires:       python-networkx >= 2.5
Requires:       python-numpy >= 1.21
Requires:       python-retry
Requires:       python-rpcq >= 3.10.0
Requires:       python-scipy >= 1.6.1
Requires:       (python-importlib-metadata >= 3.7.3 if python-base < 3.8)
Requires:       (python-qcs-api-client >= 0.21 with python-qcs-api-client < 0.22.0)
Recommends:     python-ipython
# SECTION test
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module pytest >= 6.2.2}
BuildRequires:  %{python_module pytest-freezegun >= 0.4.2}
BuildRequires:  %{python_module pytest-mock >= 3.6.1}
BuildRequires:  %{python_module pytest-rerunfailures >= 9.1.1}
BuildRequires:  %{python_module pytest-timeout >= 1.4.2}
BuildRequires:  %{python_module pytest-xdist >= 2.2.1}
BuildRequires:  %{python_module respx >= 0.20}
# /SECTION

BuildArch:      noarch
%python_subpackages

%description
PyQuil is a Python library for quantum programming using Quil,
the quantum instruction language developed at Rigetti Computing.
PyQuil serves three main functions:
  - Easily generating Quil programs from quantum gates and
    classical operations
  - Compiling and simulating Quil programs using the Quil
    Compiler (quilc) and the Quantum Virtual Machine (QVM)
  - Executing Quil programs on real quantum processors (QPUs)
    using Quantum Cloud Services (QCS)

%prep
%autosetup -p1 -n pyquil-%{version}
echo "# empty module" >> pyquil/quantum_processor/_isa.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# These need a (local) network connection to two docker containers
ignoretests="--ignore api/_qvm.py"
ignoretests="$ignoretests --ignore test/e2e"
ignoretests="$ignoretests --ignore test/unit/test_api.py"
ignoretests="$ignoretests --ignore test/unit/test_compiler.py"
ignoretests="$ignoretests --ignore test/unit/test_compatibility_v2_operator_estimation.py"
ignoretests="$ignoretests --ignore test/unit/test_compatibility_v2_quantum_computer.py"
ignoretests="$ignoretests --ignore test/unit/test_compatibility_v2_qvm.py"
ignoretests="$ignoretests --ignore test/unit/test_operator_estimation.py"
ignoretests="$ignoretests --ignore test/unit/test_quantum_computer.py"
ignoretests="$ignoretests --ignore test/unit/test_qvm.py"
ignoretests="$ignoretests --ignore test/unit/test_reference_wavefunction.py"
ignoretests="$ignoretests --ignore test/unit/test_wavefunction_simulator.py"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # 32-bit precision errors
  donttest="$donttest or (test_wavefunction and test_probabilities)"
  # non-deterministic order
  donttest="$donttest or (test_paulis_with_placeholders and test_get_qubit)"
fi
%pytest -n auto $ignoretests -k "not (dummpyprefix $donttest)"

%files %{python_files}
%{python_sitelib}/pyquil-%{version}.dist-info
%{python_sitelib}/pyquil

%changelog
