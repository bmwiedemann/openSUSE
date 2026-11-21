#
# spec file for package python-sentencepiece
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
Name:           python-sentencepiece
Version:        0.2.3
Release:        0
Summary:        Unsupervised text tokenizer and detokenizer
License:        Apache-2.0
URL:            https://github.com/google/sentencepiece
Source:         https://files.pythonhosted.org/packages/source/s/sentencepiece/sentencepiece-%{version}.tar.gz
Source1:        https://github.com/abseil/abseil-cpp/archive/refs/tags/20260817.0.tar.gz#/abseil-cpp-20260817.0.tar.gz
# PATCH-FIX-OPENSUSE sentencepiece-system-flatc.patch -- generate the lite schema header with the system flatc instead of FetchContent git-cloning flatbuffers (no network in build env)
Patch0:         sentencepiece-system-flatc.patch
# PATCH-FIX-OPENSUSE sentencepiece-link-system-protobuf-lite.patch -- link the system protobuf-lite (SPM_PROTOBUF_PROVIDER=package), which leaves no static lib in the prebuilt tree for setup.py to find
Patch1:         sentencepiece-link-system-protobuf-lite.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11 >= 2.13}
BuildRequires:  %{python_module pybind11-common-devel}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(flatbuffers)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
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
# Stage vendored abseil-cpp (upstream pin) in a sibling build dir: cmake
# FetchContent has no network on the build workers, and the wheel build
# moves a ./build dir aside, so the prebuilt tree must live outside it.
mkdir -p ../build/_deps
tar -xzf %{SOURCE1} -C ../build/_deps
rm -rf ../build/_deps/abseil-cpp-src
mv ../build/_deps/abseil-cpp-*/ ../build/_deps/abseil-cpp-src

%build
# Prebuild the C++ lib for setup.py (build_bundled.sh would git-clone deps);
# vendored abseil-cpp (upstream pin), system protobuf/flatc (same versions).
# The tree lives in ../build, which setup.py checks before ./build.
cmake -S sentencepiece -B ../build \
  -DCMAKE_BUILD_TYPE=Release \
  -DSPM_ABSL_PROVIDER=module \
  "-DFETCHCONTENT_SOURCE_DIR_ABSEIL-CPP=$PWD/../build/_deps/abseil-cpp-src" \
  -DSPM_PROTOBUF_PROVIDER=package \
  -DSPM_FLATC_EXECUTABLE=%{_bindir}/flatc \
  -DSPM_ENABLE_SHARED=OFF \
  -DSPM_ENABLE_LITE=OFF \
  -DSPM_DISABLE_EMBEDDED_DATA=ON \
  -DCMAKE_INSTALL_PREFIX=$PWD/../build \
  -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
  -DCMAKE_CXX_FLAGS="-fPIC -fvisibility=default -ffunction-sections -fdata-sections"
# Build and install into ../build, where setup.py picks the static libs up.
cmake --build ../build --target install --parallel "$(nproc)"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Run the upstream test suite; its deps (pytest, numpy, protobuf) are all in
# Factory. Exclude gen_stubs/clean manual tests that need extra tooling.
%pytest_arch test/sentencepiece_test.py test/numpy_test.py

%files %python_files
%license sentencepiece/LICENSE
%doc README.md
%{python_sitearch}/sentencepiece/
%{python_sitearch}/sentencepiece-%{version}.dist-info/

%changelog
