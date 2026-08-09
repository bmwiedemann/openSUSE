#
# spec file for package python-pybase64
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


%{?sle15_python_module_pythons}
Name:           python-pybase64
Version:        1.5.0
Release:        0
Summary:        Fast Base64 encoding/decoding
License:        BSD-2-Clause
URL:            https://github.com/mayeut/pybase64
Source:         https://files.pythonhosted.org/packages/source/p/pybase64/pybase64-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
# Upstream pyproject.toml: requires = ["setuptools>=77"]. The floor matters:
# PEP 639 License-Expression metadata, which the test suite asserts on, is
# only emitted from setuptools 77 onwards.
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
pybase64 provides a fast Base64 implementation for Python using the SIMD
(Single Instruction, Multiple Data) accelerated libbase64 C library. It
exposes drop-in replacements for the standard library base64 encode and
decode functions and ships a command line tool.

%prep
%autosetup -p1 -n pybase64-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pybase64
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The PyPI sdist ships tests/ but omits the tests/utils.py helper, which lives
# only in the git tree, so tests/test_pybase64.py and tests/test_benchmark.py
# cannot even be imported - both start with "from . import utils".
# test_main.py and test_packaging.py are self-contained and do run; test_sbom
# is deselected because it asserts a CycloneDX SBOM that only the official
# PyPI wheels carry.
%pytest_arch tests/test_main.py tests/test_packaging.py -m "not pypi_distribution"
# The functional test module is the one that cannot run, so also exercise the
# built C extension with a round trip.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -c "import pybase64; assert pybase64.b64decode(pybase64.b64encode(b'hello world')) == b'hello world'"

%post
%python_install_alternative pybase64

%postun
%python_uninstall_alternative pybase64

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/pybase64
%{python_sitearch}/pybase64
%{python_sitearch}/pybase64-%{version}.dist-info

%changelog
