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
Version:        0.2.5
Release:        0
Summary:        Efficient, Flexible and Portable Structured Generation
License:        Apache-2.0
URL:            https://xgrammar.mlc.ai/
# Upstream stopped publishing an sdist on PyPI; the tarball is generated from
# the git tag via _service because the C++ build needs the 3rdparty submodules.
# https://github.com/mlc-ai/xgrammar
Source:         xgrammar-%{version}.tar.gz
BuildRequires:  %{python_module apache-tvm-ffi >= 0.1.9}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module scikit-build-core}
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
Requires:       python-apache-tvm-ffi >= 0.1.9
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
# The wheel ships internal C++ build artifacts (headers plus the static
# libxgrammar.a) that are not used at runtime by the loadable bindings module;
# drop them so they neither bloat the package nor trip the devel-file/LTO
# rpmlint checks.
%{python_expand find %{buildroot}%{$python_sitearch} -name '*.h' -delete
find %{buildroot}%{$python_sitearch} -name '*.a' -delete
$python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/xgrammar
}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# The upstream pytest suite downloads tokenizer models from HuggingFace, so it
# is not runnable in the build root. Importing xgrammar loads the compiled
# tvm_ffi binding first (exercising that the C++ extension builds, loads and
# links against apache-tvm-ffi correctly) before importing the public API.
#
# TEMPORARY: Factory ships python-transformers 5.14.1 (which caps
# tokenizers<=0.23.0) alongside python-tokenizers 0.23.1, so `import
# transformers` -- reached via xgrammar's tokenizer_info -- raises ImportError
# distro-wide. That import happens *after* the native binding is loaded, so we
# tolerate only that specific ImportError and still assert the C++ extension
# loaded. Drop this guard once the transformers/tokenizers skew is fixed in
# Factory.
cat > smoketest.py <<'PYEOF'
import sys

try:
    import xgrammar
    from xgrammar import Grammar, GrammarCompiler, CompiledGrammar

    assert Grammar is not None
    assert GrammarCompiler is not None
    assert CompiledGrammar is not None
    print("xgrammar smoke test: full import OK")
except ImportError as exc:
    if "tokenizers" not in str(exc) and "transformers" not in str(exc):
        raise
    # xgrammar/__init__ imports load_binding (native xgrammar_bindings) before
    # the transformers-dependent tokenizer_info, so the compiled extension is
    # already loaded even though the top-level import aborted.
    lb = sys.modules.get("xgrammar.load_binding")
    assert lb is not None and getattr(lb, "LIB", None) is not None, (
        "native xgrammar_bindings failed to load"
    )
    print(
        "xgrammar native C++ binding loaded OK; transformers-dependent import "
        "skipped due to Factory transformers<=0.23.0 / tokenizers 0.23.1 skew"
    )
PYEOF
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B smoketest.py

%files %{python_files}
%license LICENSE NOTICE
%doc README.md
%{python_sitearch}/xgrammar
%{python_sitearch}/xgrammar-%{version}.dist-info

%changelog
