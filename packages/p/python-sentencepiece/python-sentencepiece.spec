#
# spec file for package python-sentencepiece
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
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-sentencepiece
Version:        0.2.2
Release:        0
Summary:        Unsupervised text tokenizer and detokenizer
License:        Apache-2.0
URL:            https://github.com/google/sentencepiece
Source:         https://files.pythonhosted.org/packages/source/s/sentencepiece/sentencepiece-%{version}.tar.gz
# PATCH-FIX-OPENSUSE sentencepiece-use-bundled-abseil.patch -- build the bundled abseil-cpp directly instead of FetchContent git-cloning it (no network in build env)
Patch0:         sentencepiece-use-bundled-abseil.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11 >= 2.12}
BuildRequires:  %{python_module pybind11-common-devel}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
SentencePiece is an unsupervised text tokenizer and detokenizer mainly for
Neural Network-based text generation systems where the vocabulary size is
predetermined prior to the neural model training. SentencePiece implements
subword units (e.g. byte-pair-encoding and unigram language model) with the
extension of direct training from raw sentences.

This package provides the Python bindings for SentencePiece.

%prep
%autosetup -p1 -n sentencepiece-%{version}

%build
# The setup builds the bundled SentencePiece C++ library (with its vendored
# abseil-cpp and protobuf-lite) via cmake and statically links it into the
# _sentencepiece pybind11 extension; no system sentencepiece is required.
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Run the upstream test suite; its deps (pytest, numpy, protobuf) are all in
# Factory. Exclude gen_stubs/clean manual tests that need extra tooling.
%pytest_arch test/sentencepiece_test.py test/numpy_test.py

%files %{python_files}
%license sentencepiece/LICENSE
%doc README.md
%{python_sitearch}/sentencepiece/
%{python_sitearch}/sentencepiece-%{version}.dist-info/

%changelog
