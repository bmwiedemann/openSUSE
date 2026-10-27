#
# spec file for package wasi-libcxx
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


%global llvm_major 23
%global wasi_sysroot %{_datadir}/wasi-sysroot
%global wasi_target wasm32-wasip1

Name:           wasi-libcxx
Version:        23.1.2
Release:        0
Summary:        WASI version of libc++/libc++abi for WebAssembly
License:        Apache-2.0 WITH LLVM-exception
Group:          Development/Languages/Other
URL:            https://libcxx.llvm.org/
# Subset of llvm-project, created via _service (LLVM only ships the full monorepo tarball)
Source0:        llvm-runtimes-subset-%{version}.tar.xz
Source100:      %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM https://github.com/llvm/llvm-project/pull/186054 (from wasi-sdk)
Patch0:         llvm-pr-186054.patch
# PATCH-FIX-UPSTREAM from wasi-sdk: only include IBM locale API on z/OS
Patch1:         llvm-undo-part-of-194317.patch
BuildRequires:  clang%{llvm_major}
BuildRequires:  cmake >= 3.20
BuildRequires:  fdupes
BuildRequires:  lld%{llvm_major}
BuildRequires:  llvm%{llvm_major}
BuildRequires:  ninja
BuildRequires:  python3-base
BuildRequires:  wasi-libc
Requires:       wasi-libc
BuildArch:      noarch

%description
WASI version of libc++/libc++abi for WebAssembly (%{wasi_target}),
to be used with clang --target=%{wasi_target} --sysroot=%{wasi_sysroot}.

%prep
%autosetup -p1 -n llvm-runtimes-subset-%{version}

%build
# Host flags (stack protector, branch protection, ...) don't apply to wasm.
unset CFLAGS CXXFLAGS LDFLAGS

# Flags follow wasi-sdk's cmake/wasi-sdk-sysroot.cmake (libcxx part).
# wasm32-wasip1 only, no -threads/LTO/exceptions variants
cmake -G Ninja -S runtimes -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER=clang-%{llvm_major} \
    -DCMAKE_CXX_COMPILER=clang++-%{llvm_major} \
    -DCMAKE_AR=%{_bindir}/llvm-ar-%{llvm_major} \
    -DCMAKE_RANLIB=%{_bindir}/llvm-ranlib-%{llvm_major} \
    -DCMAKE_C_COMPILER_TARGET=%{wasi_target} \
    -DCMAKE_CXX_COMPILER_TARGET=%{wasi_target} \
    -DCMAKE_C_COMPILER_WORKS=ON \
    -DCMAKE_CXX_COMPILER_WORKS=ON \
    -DCMAKE_SYSTEM_NAME=WASI \
    -DCMAKE_SYSTEM_VERSION=1 \
    -DCMAKE_SYSTEM_PROCESSOR=wasm32 \
    -DCMAKE_SYSROOT=%{wasi_sysroot} \
    -DCMAKE_C_FLAGS="-fno-exceptions" \
    -DCMAKE_CXX_FLAGS="-fno-exceptions" \
    -DCMAKE_C_LINKER_DEPFILE_SUPPORTED=OFF \
    -DCMAKE_CXX_LINKER_DEPFILE_SUPPORTED=OFF \
    -DCMAKE_INSTALL_PREFIX=%{wasi_sysroot} \
    -DCMAKE_INSTALL_INCLUDEDIR=include/%{wasi_target} \
    -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi" \
    -DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_INCLUDE_DOCS=OFF \
    -DLLVM_COMPILER_CHECKED=ON \
    -DUNIX=ON \
    -DLIBCXX_ENABLE_SHARED=OFF \
    -DLIBCXX_ENABLE_STATIC=ON \
    -DLIBCXX_ENABLE_EXCEPTIONS=OFF \
    -DLIBCXX_ENABLE_THREADS=ON \
    -DLIBCXX_HAS_PTHREAD_API=ON \
    -DLIBCXX_HAS_EXTERNAL_THREAD_API=OFF \
    -DLIBCXX_HAS_WIN32_THREAD_API=OFF \
    -DLIBCXX_ENABLE_FILESYSTEM=ON \
    -DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=OFF \
    -DLIBCXX_CXX_ABI=libcxxabi \
    -DLIBCXX_HAS_MUSL_LIBC=OFF \
    -DLIBCXX_ABI_VERSION=2 \
    -DLIBCXX_INSTALL_MODULES=OFF \
    -DLIBCXX_INCLUDE_TESTS=OFF \
    -DLIBCXX_INCLUDE_BENCHMARKS=OFF \
    -DLIBCXX_LIBDIR_SUFFIX=/%{wasi_target} \
    -DLIBCXXABI_ENABLE_SHARED=OFF \
    -DLIBCXXABI_ENABLE_STATIC=ON \
    -DLIBCXXABI_ENABLE_EXCEPTIONS=OFF \
    -DLIBCXXABI_SILENT_TERMINATE=ON \
    -DLIBCXXABI_ENABLE_THREADS=ON \
    -DLIBCXXABI_HAS_PTHREAD_API=ON \
    -DLIBCXXABI_HAS_EXTERNAL_THREAD_API=OFF \
    -DLIBCXXABI_HAS_WIN32_THREAD_API=OFF \
    -DLIBCXXABI_USE_LLVM_UNWINDER=OFF \
    -DLIBCXXABI_INCLUDE_TESTS=OFF \
    -DLIBCXXABI_LIBDIR_SUFFIX=/%{wasi_target}
ninja -v -C build %{?_smp_mflags}

%install
DESTDIR=%{buildroot} ninja -C build install
# clang only looks at include/<target>/c++/v1 if include/c++/v1 exists too.
mkdir -p %{buildroot}%{wasi_sysroot}/include/c++/v1
%fdupes %{buildroot}%{wasi_sysroot}
# OBS uses system strip and ar, which both can't handle wasm-files
export NO_BRP_AR=true
export NO_BRP_STRIP_DEBUG=true

%check
# Built without exceptions: nothing may reference the C++ exception runtime.
if llvm-nm-%{llvm_major} -u %{buildroot}%{wasi_sysroot}/lib/%{wasi_target}/libc++*.a \
     | grep -qE '__cxa_(throw|begin_catch|allocate_exception)'; then
    echo "ERROR: libc++ built with exceptions enabled"; exit 1
fi

%files
%license libcxx/LICENSE.TXT
%dir %{wasi_sysroot}/include/c++
%dir %{wasi_sysroot}/include/c++/v1
%{wasi_sysroot}/include/%{wasi_target}/c++/
%{wasi_sysroot}/lib/%{wasi_target}/libc++*.a

%changelog
