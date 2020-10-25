#
# spec file for package python-cirq
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


%define packagename Cirq
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cirq
Version:        0.9.1
Release:        0
Summary:        Library for writing quantum circuits
License:        Apache-2.0
URL:            https://github.com/quantumlib/Cirq
Source:         https://github.com/quantumlib/Cirq/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module PyLaTeX}
BuildRequires:  %{python_module freezegun >= 0.3.15}
BuildRequires:  %{python_module google-api-core >= 1.14.0}
BuildRequires:  %{python_module matplotlib >= 3.0}
BuildRequires:  %{python_module networkx >= 2.4}
BuildRequires:  %{python_module numpy >= 1.16}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module protobuf >= 3.12.0}
BuildRequires:  %{python_module pyquil}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module quimb}
BuildRequires:  %{python_module requests >= 2.18}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sortedcontainers >= 2.0}
BuildRequires:  %{python_module sympy}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyLaTeX
Requires:       python-freezegun >= 0.3.15
Requires:       python-google-api-core >= 1.14.0
Requires:       python-matplotlib >= 3.0
Requires:       python-networkx >= 2.4
Requires:       python-numpy >= 1.16
Requires:       python-pandas
Requires:       python-ply
Requires:       python-protobuf >= 3.12.0
Requires:       python-pyquil
Requires:       python-quimb
Requires:       python-requests >= 2.18
Requires:       python-scipy
Requires:       python-sortedcontainers >= 2.0
Requires:       python-sympy
Requires:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
Cirq is a software library for writing, manipulating, and optimizing
quantum circuits and then running them against quantum computers and
simulators.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The test failed, but has no effect on package validity. gh#quantumlib/Cirq#3154
%pytest --ignore dev_tools/bash_scripts_test.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*egg-info
%{python_sitelib}/cirq

%changelog
