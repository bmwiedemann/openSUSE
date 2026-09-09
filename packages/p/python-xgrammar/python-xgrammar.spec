#
# spec file for package python-xgrammar
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.//
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-xgrammar
Version:        0.2.6
Release:        0
Summary:        Efficient, Flexible and Portable Structured Generation
License:        Apache-2.0
URL:            https://xgrammar.mlc.ai/
# https://github.com/mlc-ai/xgrammar
# PyPI sdist ships the 3rdparty sources the C++ build needs.
Source:         https://files.pythonhosted.org/packages/source/x/xgrammar/xgrammar-%{version}.tar.gz
BuildRequires:  %{python_module apache-tvm-ffi >= 0.1.10}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module scikit-build-core >= 0.10.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module torch >= 1.10.0}
BuildRequires:  %{python_module transformers >= 4.38.0}
BuildRequires:  %{python_module typing_extensions >= 4.9.0}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# numpy only Recommends an OpenBLAS runtime; pull one explicitly so torch/numpy
# import during %%check (Recommends are not installed in the build root).
BuildRequires:  libopenblas_pthreads0
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
# triton is a Linux x86_64 PyPI dep for the CUDA bitmask kernel only; CPU
# auto-selects the bundled CPU backend. python-triton is not in Factory.
Requires:       python-apache-tvm-ffi >= 0.1.10
Requires:       python-numpy
Requires:       python-pydantic
Requires:       python-torch >= 1.10.0
Requires:       python-transformers >= 4.38.0
Requires:       python-typing_extensions >= 4.9.0
%python_subpackages

%description
XGrammar is an open-source library for efficient, flexible, and portable
structured generation. It provides a fast engine for constrained decoding
of large language models against grammars such as JSON schemas, regular
expressions and context-free grammars.

%prep
%autosetup -p1 -n xgrammar-%{version}

%build
export CMAKE_GENERATOR=Ninja
%pyproject_wheel

%install
%pyproject_install
%{python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/xgrammar}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The upstream pytest suite downloads tokenizer models from HuggingFace, so it
# is not runnable in the build root. Importing xgrammar loads the compiled
# tvm_ffi binding first (exercising that the C++ extension builds, loads and
# links against apache-tvm-ffi correctly) before importing the public API.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B -c "import xgrammar; from xgrammar import Grammar, GrammarCompiler, CompiledGrammar"

%files %{python_files}
%license LICENSE NOTICE
%doc README.md
%{python_sitearch}/xgrammar
%{python_sitearch}/xgrammar-%{version}.dist-info

%changelog
