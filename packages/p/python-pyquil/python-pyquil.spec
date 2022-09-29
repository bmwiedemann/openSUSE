#
# spec file for package python-pyquil
#
# Copyright (c) 2022 SUSE LLC
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


%define packagename pyquil
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyquil
Version:        3.3.1
Release:        0
Summary:        A Python library to generate Quantum Instruction Language (Quil) Programs
License:        Apache-2.0
URL:            https://github.com/rigetti/pyquil
Source:         https://github.com/rigetti/pyquil/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module antlr4-python3-runtime >= 4.7.2}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module immutables}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module lark-parser}
BuildRequires:  %{python_module networkx >= 2.0.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qcs-api-client >= 0.20.13}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module respx}
BuildRequires:  %{python_module retry}
BuildRequires:  %{python_module rpcq >= 3.0.0}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module seaborn}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-antlr4-python3-runtime >= 4.7.2
Requires:       python-immutables
Requires:       python-ipython
Requires:       python-lark-parser
Requires:       python-networkx >= 2.0.0
Requires:       python-numpy
Requires:       python-qcs-api-client >= 0.20.13
Requires:       python-requests
Requires:       python-requests-mock
Requires:       python-rpcq >= 3.0.0
Requires:       python-scipy
Requires:       python-seaborn
BuildArch:      noarch
%python_subpackages

%description
A Python library to generate Quantum Instruction Language (Quil) Programs.

%prep
%autosetup -p1 -n %{packagename}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests that need network connection are ignored or skipped.
%pytest --ignore api/_qvm.py --ignore test/unit/test_quantum_computer.py --ignore api/tests/test_compiler.py --ignore test/e2e --ignore test/unit/test_compatibility_v2_operator_estimation.py  --ignore test/unit/test_compatibility_v2_quantum_computer.py --ignore test/unit/test_wavefunction_simulator.py --ignore test/unit/test_compatibility_v2_qvm.py --ignore test/unit/test_reference_wavefunction.py --ignore test/unit/test_qvm.py --ignore test/unit/test_qpu_client.py --ignore test/unit/test_operator_estimation.py --ignore test/unit/test_engagement_manager.py -k 'not (test_quil_to_native_quil or test_local_rb_sequence or test_local_conjugate_request or test_apply_clifford_to_pauli or test_compile_with_quilt_calibrations or test_probabilities)'

%files %{python_files}
%{python_sitelib}/*dist-info
%{python_sitelib}/%{packagename}

%changelog
