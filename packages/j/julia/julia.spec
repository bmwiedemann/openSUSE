#
# spec file for package julia
#
# Copyright (c) 2025 SUSE LLC
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


%undefine _build_create_debug
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
%global julia_march native

# If not Tumbleweed. Leap 15.6 seems to have trouble with libpthread
%if 0%{?suse_version} < 1600
%global __julia_opts NO_GIT=1 DEPS_GIT=0 BUILD_LLD=1 BUILD_LLDB=1 USE_BINARYBUILDER=0 USE_SYSTEM_CSL=1 USE_SYSTEM_LLVM=0 USE_SYSTEM_LLD=0 OPENBLAS_USE_THREAD=0 OPENBLAS_TARGET_ARCH=NEHALEM OPENBLAS_SYMBOLSUFFIX="%{?__isa_bits}_" OPENBLAS_LIBNAMESUFFIX="%{?__isa_bits}_" OPENBLAS_CFLAGS="${CFLAGS}" LIBBLAS=-lopenblas64_ LIBBLASNAME=libopenblas64_ LIBLAPACK=-lopenblas64_ LIBLAPACKNAME=libopenblas64_ SUITESPARSE_LIB="-lumfpack64_ -lcholmod64_ -lamd64_ -lcamd64_ -lcolamd64_ -lspqr64_" USE_SYSTEM_LIBUNWIND=0 USE_SYSTEM_PCRE=0 USE_SYSTEM_BLAS=0 USE_SYSTEM_LAPACK=0 USE_SYSTEM_LIBBLASTRAMPOLINE=1 USE_SYSTEM_GMP=0 USE_SYSTEM_MPFR=0 USE_SYSTEM_LIBSUITESPARSE=0 USE_SYSTEM_SUITESPARSE=0 USE_INTEL_JITEVENTS=0 USE_SYSTEM_LIBWHICH=1 USE_SYSTEM_DSFMT=0 USE_SYSTEM_LIBUV=0 USE_SYSTEM_UTF8PROC=1 USE_SYSTEM_LIBGIT2=0 USE_SYSTEM_LIBSSH2=0 USE_SYSTEM_MBEDTLS=0 USE_SYSTEM_CURL=1 USE_SYSTEM_PATCHELF=1 USE_SYSTEM_ZLIB=1 USE_SYSTEM_P7ZIP=1 USE_SYSTEM_OPENLIBM=1 USE_BLAS64=1 JLDFLAGS="$LDFLAGS" USE_BINARYBUILDER_BLASTRAMPOLINE=0 USE_BINARYBUILDER_CURL=0 USE_BINARYBUILDER_DSFMT=0 USE_BINARYBUILDER_GMP=0 USE_BINARYBUILDER_LIBGIT2=0 USE_BINARYBUILDER_LIBSSH2=0 USE_BINARYBUILDER_LIBSUITESPARSE=0 USE_BINARYBUILDER_LIBTRACYCLIENT=0 USE_BINARYBUILDER_LIBUNWIND=0 USE_BINARYBUILDER_LIBUV=0 USE_BINARYBUILDER_LLVM=0 USE_BINARYBUILDER_MBEDTLS=0 USE_BINARYBUILDER_MPFR=0 USE_BINARYBUILDER_OPENBLAS=0 USE_BINARYBUILDER_OPENLIBM=0 USE_BINARYBUILDER_P7ZIP=0 USE_BINARYBUILDER_PCRE=0 USE_BINARYBUILDER_ZLIB=0 VERBOSE=0
%else
%global __julia_opts NO_GIT=1 DEPS_GIT=0 BUILD_LLD=1 BUILD_LLDB=1 USE_BINARYBUILDER=0 USE_SYSTEM_CSL=1 USE_SYSTEM_LLVM=0 USE_SYSTEM_LLD=0 OPENBLAS_SYMBOLSUFFIX="%{?__isa_bits}_" OPENBLAS_LIBNAMESUFFIX="%{?__isa_bits}_" OPENBLAS_CFLAGS="${CFLAGS}" LIBBLAS=-lopenblas64_ LIBBLASNAME=libopenblas64_ LIBLAPACK=-lopenblas64_ LIBLAPACKNAME=libopenblas64_ SUITESPARSE_LIB="-lumfpack64_ -lcholmod64_ -lamd64_ -lcamd64_ -lcolamd64_ -lspqr64_" USE_SYSTEM_LIBUNWIND=0 USE_SYSTEM_PCRE=0 USE_SYSTEM_BLAS=0 USE_SYSTEM_LAPACK=0 USE_SYSTEM_LIBBLASTRAMPOLINE=1 USE_SYSTEM_GMP=0 USE_SYSTEM_MPFR=0 USE_SYSTEM_LIBSUITESPARSE=0 USE_SYSTEM_SUITESPARSE=0 USE_INTEL_JITEVENTS=0 USE_SYSTEM_LIBWHICH=1 USE_SYSTEM_DSFMT=0 USE_SYSTEM_LIBUV=0 USE_SYSTEM_UTF8PROC=1 USE_SYSTEM_LIBGIT2=0 USE_SYSTEM_LIBSSH2=0 USE_SYSTEM_MBEDTLS=0 USE_SYSTEM_CURL=1 USE_SYSTEM_PATCHELF=1 USE_SYSTEM_ZLIB=1 USE_SYSTEM_P7ZIP=1 USE_SYSTEM_OPENLIBM=1 USE_BLAS64=1 JLDFLAGS="$LDFLAGS" USE_BINARYBUILDER_BLASTRAMPOLINE=0 USE_BINARYBUILDER_CURL=0 USE_BINARYBUILDER_DSFMT=0 USE_BINARYBUILDER_GMP=0 USE_BINARYBUILDER_LIBGIT2=0 USE_BINARYBUILDER_LIBSSH2=0 USE_BINARYBUILDER_LIBSUITESPARSE=0 USE_BINARYBUILDER_LIBTRACYCLIENT=0 USE_BINARYBUILDER_LIBUNWIND=0 USE_BINARYBUILDER_LIBUV=0 USE_BINARYBUILDER_LLVM=0 USE_BINARYBUILDER_MBEDTLS=0 USE_BINARYBUILDER_MPFR=0 USE_BINARYBUILDER_OPENBLAS=0 USE_BINARYBUILDER_OPENLIBM=0 USE_BINARYBUILDER_P7ZIP=0 USE_BINARYBUILDER_PCRE=0 USE_BINARYBUILDER_ZLIB=0 VERBOSE=0
%endif

# List all bundled libraries.
%global _privatelibs lib(ssh.*|pcre.*|dSFMT.*|gmp.*|mpfr.*|git.*|mbed.*|nghttp.*||LLVM-.*|unwind*|ccalltest|llvmcalltest|uv|openblas.*|lapack.*|sys|julia.*|amd|btf|camd|ccolamd|cholmod|colamd|cxsparse|graphblas|klu|klu_cholmod|lagraph|lagraphx|ldl|paru|rbio|spex|spqr|suitesparse_mongoose|suitesparseconfig|umfpack)\\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%define libjulia_sover_major 1
%define libjulia_sover_minor 10
%define _julia_llvm_version 15.0.7-10

%if "@BUILD_FLAVOR@%{nil}" == "compat"
%define compat_mode  1
%else
%define compat_mode  0
%endif

%if 0%{?compat_mode}
%define libname              libjulia-compat%{libjulia_sover_major}_%{libjulia_sover_minor}
%else
%define libname              libjulia%{libjulia_sover_major}_%{libjulia_sover_minor}
%endif

# LTO currently makes building blastrampoline and Julia itself fail
# It is not enabled upstream anyway
%global _lto_cflags %nil
Version:        1.10.5
Release:        0
URL:            http://julialang.org/
Source0:        https://github.com/JuliaLang/julia/releases/download/v%{version}/julia-%{version}-full.tar.gz
Source1:        https://github.com/JuliaLang/julia/releases/download/v%{version}/julia-%{version}-full.tar.gz.asc
Source2:        https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/keys/pgp/3673DF529D9049477F76B37566E3C7DC03D6E495.asc?ref_type=heads#/julia.keyring
Source3:        https://www.unicode.org/Public/13.0.0/ucd/UnicodeData.txt
Source4:        julia-rpmlintrc
Source5:        https://github.com/JuliaBinaryWrappers/CompilerSupportLibraries_jll.jl/releases/download/CompilerSupportLibraries-v1.1.1+0/CompilerSupportLibraries.v1.1.1.x86_64-linux-gnu-libgfortran5.tar.gz#/CompilerSupportLibraries.v1.1.1+0.x86_64-linux-gnu-libgfortran5.tar.gz
Source6:        https://github.com/JuliaBinaryWrappers/LibUV_jll.jl/releases/download/LibUV-v2.0.1+14/LibUV.v2.0.1.x86_64-linux-gnu.tar.gz#/LibUV.v2.0.1+14.x86_64-linux-gnu.tar.gz
Source7:        https://github.com/JuliaBinaryWrappers/LibUnwind_jll.jl/releases/download/LibUnwind-v1.5.0+5/LibUnwind.v1.5.0.x86_64-linux-gnu.tar.gz#/LibUnwind.v1.5.0+5.x86_64-linux-gnu.tar.gz
Source8:        https://github.com/JuliaBinaryWrappers/OpenLibm_jll.jl/releases/download/OpenLibm-v0.8.1+2/OpenLibm.v0.8.1.x86_64-linux-gnu.tar.gz#/OpenLibm.v0.8.1+2.x86_64-linux-gnu.tar.gz
Source9:        https://github.com/JuliaBinaryWrappers/dSFMT_jll.jl/releases/download/dSFMT-v2.2.4+4/dSFMT.v2.2.4.x86_64-linux-gnu.tar.gz#/dSFMT.v2.2.4+4.x86_64-linux-gnu.tar.gz
Source10:       https://github.com/JuliaBinaryWrappers/libLLVM_jll.jl/releases/download/libLLVM-v15.0.7+10/libLLVM.v15.0.7.x86_64-linux-gnu-cxx11-llvm_version+15.tar.gz#/libLLVM.v15.0.7+10.x86_64-linux-gnu-cxx11-llvm_version+15.tar.gz
Source11:       https://github.com/JuliaBinaryWrappers/LLD_jll.jl/releases/download/LLD-v15.0.7+10/LLD.v15.0.7.x86_64-linux-gnu-cxx11-llvm_version+15.tar.gz#/LLD.v15.0.7+10.x86_64-linux-gnu-cxx11-llvm_version+15.tar.gz
Source12:       https://github.com/JuliaBinaryWrappers/PCRE2_jll.jl/releases/download/PCRE2-v10.42.0+1/PCRE2.v10.42.0.x86_64-linux-gnu.tar.gz#/PCRE2.v10.42.0+1.x86_64-linux-gnu.tar.gz
Source13:       https://github.com/JuliaBinaryWrappers/OpenBLAS_jll.jl/releases/download/OpenBLAS-v0.3.23+4/OpenBLAS.v0.3.23.x86_64-linux-gnu-libgfortran5.tar.gz#/OpenBLAS.v0.3.23+4.x86_64-linux-gnu-libgfortran5.tar.gz
Source14:       https://github.com/JuliaBinaryWrappers/GMP_jll.jl/releases/download/GMP-v6.2.1+6/GMP.v6.2.1.x86_64-linux-gnu-cxx11.tar.gz#/GMP.v6.2.1+6.x86_64-linux-gnu-cxx11.tar.gz
Source15:       https://github.com/JuliaBinaryWrappers/MbedTLS_jll.jl/releases/download/MbedTLS-v2.28.2+1/MbedTLS.v2.28.2.x86_64-linux-gnu.tar.gz#/MbedTLS.v2.28.2+1.x86_64-linux-gnu.tar.gz
Source16:       https://github.com/JuliaBinaryWrappers/LibSSH2_jll.jl/releases/download/LibSSH2-v1.11.0+1/LibSSH2.v1.11.0.x86_64-linux-gnu.tar.gz#/LibSSH2.v1.11.0+1.x86_64-linux-gnu.tar.gz
Source17:       https://github.com/JuliaBinaryWrappers/nghttp2_jll.jl/releases/download/nghttp2-v1.52.0+1/nghttp2.v1.52.0.x86_64-linux-gnu.tar.gz#/nghttp2.v1.52.0+1.x86_64-linux-gnu.tar.gz
Source18:       https://github.com/JuliaBinaryWrappers/LibCURL_jll.jl/releases/download/LibCURL-v8.4.0+0/LibCURL.v8.4.0.x86_64-linux-gnu.tar.gz#/LibCURL.v8.4.0+0.x86_64-linux-gnu.tar.gz
Source19:       https://github.com/JuliaBinaryWrappers/LibGit2_jll.jl/releases/download/LibGit2-v1.6.4+0/LibGit2.v1.6.4.x86_64-linux-gnu.tar.gz#/LibGit2.v1.6.4+0.x86_64-linux-gnu.tar.gz
Source20:       https://github.com/JuliaBinaryWrappers/MPFR_jll.jl/releases/download/MPFR-v4.2.0+1/MPFR.v4.2.0.x86_64-linux-gnu.tar.gz#/MPFR.v4.2.0+1.x86_64-linux-gnu.tar.gz
Source21:       https://github.com/JuliaBinaryWrappers/SuiteSparse_jll.jl/releases/download/SuiteSparse-v7.2.1+1/SuiteSparse.v7.2.1.x86_64-linux-gnu.tar.gz#/SuiteSparse.v7.2.1+1.x86_64-linux-gnu.tar.gz
Source22:       https://github.com/JuliaBinaryWrappers/Zlib_jll.jl/releases/download/Zlib-v1.2.13+1/Zlib.v1.2.13.x86_64-linux-gnu.tar.gz#/Zlib.v1.2.13+1.x86_64-linux-gnu.tar.gz
Source23:       https://github.com/JuliaBinaryWrappers/p7zip_jll.jl/releases/download/p7zip-v17.4.0+2/p7zip.v17.4.0.x86_64-linux-gnu.tar.gz#/p7zip.v17.4.0+2.x86_64-linux-gnu.tar.gz
Source24:       https://github.com/JuliaBinaryWrappers/libblastrampoline_jll.jl/releases/download/libblastrampoline-v5.11.0+0/libblastrampoline.v5.11.0.x86_64-linux-gnu.tar.gz#/libblastrampoline.v5.11.0+0.x86_64-linux-gnu.tar.gz

Source25:       https://github.com/JuliaBinaryWrappers/CompilerSupportLibraries_jll.jl/releases/download/CompilerSupportLibraries-v1.1.1+0/CompilerSupportLibraries.v1.1.1.aarch64-linux-gnu-libgfortran5.tar.gz#/CompilerSupportLibraries.v1.1.1+0.aarch64-linux-gnu-libgfortran5.tar.gz
Source26:       https://github.com/JuliaBinaryWrappers/LibUV_jll.jl/releases/download/LibUV-v2.0.1+14/LibUV.v2.0.1.aarch64-linux-gnu.tar.gz#/LibUV.v2.0.1+14.aarch64-linux-gnu.tar.gz
Source27:       https://github.com/JuliaBinaryWrappers/LibUnwind_jll.jl/releases/download/LibUnwind-v1.5.0+5/LibUnwind.v1.5.0.aarch64-linux-gnu.tar.gz#/LibUnwind.v1.5.0+5.aarch64-linux-gnu.tar.gz
Source28:       https://github.com/JuliaBinaryWrappers/OpenLibm_jll.jl/releases/download/OpenLibm-v0.8.1+2/OpenLibm.v0.8.1.aarch64-linux-gnu.tar.gz#/OpenLibm.v0.8.1+2.aarch64-linux-gnu.tar.gz
Source29:       https://github.com/JuliaBinaryWrappers/dSFMT_jll.jl/releases/download/dSFMT-v2.2.4+4/dSFMT.v2.2.4.aarch64-linux-gnu.tar.gz#/dSFMT.v2.2.4+4.aarch64-linux-gnu.tar.gz
Source30:       https://github.com/JuliaBinaryWrappers/libLLVM_jll.jl/releases/download/libLLVM-v15.0.7+10/libLLVM.v15.0.7.aarch64-linux-gnu-cxx11-llvm_version+15.tar.gz#/libLLVM.v15.0.7+10.aarch64-linux-gnu-cxx11-llvm_version+15.tar.gz
Source31:       https://github.com/JuliaBinaryWrappers/LLD_jll.jl/releases/download/LLD-v15.0.7+10/LLD.v15.0.7.aarch64-linux-gnu-cxx11-llvm_version+15.tar.gz#/LLD.v15.0.7+10.aarch64-linux-gnu-cxx11-llvm_version+15.tar.gz
Source32:       https://github.com/JuliaBinaryWrappers/PCRE2_jll.jl/releases/download/PCRE2-v10.42.0+1/PCRE2.v10.42.0.aarch64-linux-gnu.tar.gz#/PCRE2.v10.42.0+1.aarch64-linux-gnu.tar.gz
Source33:       https://github.com/JuliaBinaryWrappers/OpenBLAS_jll.jl/releases/download/OpenBLAS-v0.3.23+4/OpenBLAS.v0.3.23.aarch64-linux-gnu-libgfortran5.tar.gz#/OpenBLAS.v0.3.23+4.aarch64-linux-gnu-libgfortran5.tar.gz
Source34:       https://github.com/JuliaBinaryWrappers/GMP_jll.jl/releases/download/GMP-v6.2.1+6/GMP.v6.2.1.aarch64-linux-gnu-cxx11.tar.gz#/GMP.v6.2.1+6.aarch64-linux-gnu-cxx11.tar.gz
Source35:       https://github.com/JuliaBinaryWrappers/MbedTLS_jll.jl/releases/download/MbedTLS-v2.28.2+1/MbedTLS.v2.28.2.aarch64-linux-gnu.tar.gz#/MbedTLS.v2.28.2+1.aarch64-linux-gnu.tar.gz
Source36:       https://github.com/JuliaBinaryWrappers/LibSSH2_jll.jl/releases/download/LibSSH2-v1.11.0+1/LibSSH2.v1.11.0.aarch64-linux-gnu.tar.gz#/LibSSH2.v1.11.0+1.aarch64-linux-gnu.tar.gz
Source37:       https://github.com/JuliaBinaryWrappers/nghttp2_jll.jl/releases/download/nghttp2-v1.52.0+1/nghttp2.v1.52.0.aarch64-linux-gnu.tar.gz#/nghttp2.v1.52.0+1.aarch64-linux-gnu.tar.gz
Source38:       https://github.com/JuliaBinaryWrappers/LibCURL_jll.jl/releases/download/LibCURL-v8.4.0+0/LibCURL.v8.4.0.aarch64-linux-gnu.tar.gz#/LibCURL.v8.4.0+0.aarch64-linux-gnu.tar.gz
Source39:       https://github.com/JuliaBinaryWrappers/LibGit2_jll.jl/releases/download/LibGit2-v1.6.4+0/LibGit2.v1.6.4.aarch64-linux-gnu.tar.gz#/LibGit2.v1.6.4+0.aarch64-linux-gnu.tar.gz
Source40:       https://github.com/JuliaBinaryWrappers/MPFR_jll.jl/releases/download/MPFR-v4.2.0+1/MPFR.v4.2.0.aarch64-linux-gnu.tar.gz#/MPFR.v4.2.0+1.aarch64-linux-gnu.tar.gz
Source41:       https://github.com/JuliaBinaryWrappers/SuiteSparse_jll.jl/releases/download/SuiteSparse-v7.2.1+1/SuiteSparse.v7.2.1.aarch64-linux-gnu.tar.gz#/SuiteSparse.v7.2.1+1.aarch64-linux-gnu.tar.gz
Source42:       https://github.com/JuliaBinaryWrappers/Zlib_jll.jl/releases/download/Zlib-v1.2.13+1/Zlib.v1.2.13.aarch64-linux-gnu.tar.gz#/Zlib.v1.2.13+1.aarch64-linux-gnu.tar.gz
Source43:       https://github.com/JuliaBinaryWrappers/p7zip_jll.jl/releases/download/p7zip-v17.4.0+2/p7zip.v17.4.0.aarch64-linux-gnu.tar.gz#/p7zip.v17.4.0+2.aarch64-linux-gnu.tar.gz
Source44:       https://github.com/JuliaBinaryWrappers/libblastrampoline_jll.jl/releases/download/libblastrampoline-v5.11.0+0/libblastrampoline.v5.11.0.aarch64-linux-gnu.tar.gz#/libblastrampoline.v5.11.0+0.aarch64-linux-gnu.tar.gz

Source45:       https://github.com/JuliaBinaryWrappers/CompilerSupportLibraries_jll.jl/releases/download/CompilerSupportLibraries-v1.1.1+0/CompilerSupportLibraries.v1.1.1.powerpc64le-linux-gnu-libgfortran5.tar.gz#/CompilerSupportLibraries.v1.1.1+0.powerpc64le-linux-gnu-libgfortran5.tar.gz
Source46:       https://github.com/JuliaBinaryWrappers/LibUV_jll.jl/releases/download/LibUV-v2.0.1+14/LibUV.v2.0.1.powerpc64le-linux-gnu.tar.gz#/LibUV.v2.0.1+14.powerpc64le-linux-gnu.tar.gz
Source47:       https://github.com/JuliaBinaryWrappers/LibUnwind_jll.jl/releases/download/LibUnwind-v1.5.0+5/LibUnwind.v1.5.0.powerpc64le-linux-gnu.tar.gz#/LibUnwind.v1.5.0+5.powerpc64le-linux-gnu.tar.gz
Source48:       https://github.com/JuliaBinaryWrappers/OpenLibm_jll.jl/releases/download/OpenLibm-v0.8.1+2/OpenLibm.v0.8.1.powerpc64le-linux-gnu.tar.gz#/OpenLibm.v0.8.1+2.powerpc64le-linux-gnu.tar.gz
Source49:       https://github.com/JuliaBinaryWrappers/dSFMT_jll.jl/releases/download/dSFMT-v2.2.4+4/dSFMT.v2.2.4.powerpc64le-linux-gnu.tar.gz#/dSFMT.v2.2.4+4.powerpc64le-linux-gnu.tar.gz
Source50:       https://github.com/JuliaBinaryWrappers/libLLVM_jll.jl/releases/download/libLLVM-v15.0.7+10/libLLVM.v15.0.7.powerpc64le-linux-gnu-cxx11-llvm_version+15.tar.gz#/libLLVM.v15.0.7+10.powerpc64le-linux-gnu-cxx11-llvm_version+15.tar.gz
Source51:       https://github.com/JuliaBinaryWrappers/LLD_jll.jl/releases/download/LLD-v15.0.7+10/LLD.v15.0.7.powerpc64le-linux-gnu-cxx11-llvm_version+15.tar.gz#/LLD.v15.0.7+10.powerpc64le-linux-gnu-cxx11-llvm_version+15.tar.gz
Source52:       https://github.com/JuliaBinaryWrappers/PCRE2_jll.jl/releases/download/PCRE2-v10.42.0+1/PCRE2.v10.42.0.powerpc64le-linux-gnu.tar.gz#/PCRE2.v10.42.0+1.powerpc64le-linux-gnu.tar.gz
Source53:       https://github.com/JuliaBinaryWrappers/OpenBLAS_jll.jl/releases/download/OpenBLAS-v0.3.23+4/OpenBLAS.v0.3.23.powerpc64le-linux-gnu-libgfortran5.tar.gz#/OpenBLAS.v0.3.23+4.powerpc64le-linux-gnu-libgfortran5.tar.gz
Source54:       https://github.com/JuliaBinaryWrappers/GMP_jll.jl/releases/download/GMP-v6.2.1+6/GMP.v6.2.1.powerpc64le-linux-gnu-cxx11.tar.gz#/GMP.v6.2.1+6.powerpc64le-linux-gnu-cxx11.tar.gz
Source55:       https://github.com/JuliaBinaryWrappers/MbedTLS_jll.jl/releases/download/MbedTLS-v2.28.2+1/MbedTLS.v2.28.2.powerpc64le-linux-gnu.tar.gz#/MbedTLS.v2.28.2+1.powerpc64le-linux-gnu.tar.gz
Source56:       https://github.com/JuliaBinaryWrappers/LibSSH2_jll.jl/releases/download/LibSSH2-v1.11.0+1/LibSSH2.v1.11.0.powerpc64le-linux-gnu.tar.gz#/LibSSH2.v1.11.0+1.powerpc64le-linux-gnu.tar.gz
Source57:       https://github.com/JuliaBinaryWrappers/nghttp2_jll.jl/releases/download/nghttp2-v1.52.0+1/nghttp2.v1.52.0.powerpc64le-linux-gnu.tar.gz#/nghttp2.v1.52.0+1.powerpc64le-linux-gnu.tar.gz
Source58:       https://github.com/JuliaBinaryWrappers/LibCURL_jll.jl/releases/download/LibCURL-v8.4.0+0/LibCURL.v8.4.0.powerpc64le-linux-gnu.tar.gz#/LibCURL.v8.4.0+0.powerpc64le-linux-gnu.tar.gz
Source59:       https://github.com/JuliaBinaryWrappers/LibGit2_jll.jl/releases/download/LibGit2-v1.6.4+0/LibGit2.v1.6.4.powerpc64le-linux-gnu.tar.gz#/LibGit2.v1.6.4+0.powerpc64le-linux-gnu.tar.gz
Source60:       https://github.com/JuliaBinaryWrappers/MPFR_jll.jl/releases/download/MPFR-v4.2.0+1/MPFR.v4.2.0.powerpc64le-linux-gnu.tar.gz#/MPFR.v4.2.0+1.powerpc64le-linux-gnu.tar.gz
Source61:       https://github.com/JuliaBinaryWrappers/SuiteSparse_jll.jl/releases/download/SuiteSparse-v7.2.1+1/SuiteSparse.v7.2.1.powerpc64le-linux-gnu.tar.gz#/SuiteSparse.v7.2.1+1.powerpc64le-linux-gnu.tar.gz
Source62:       https://github.com/JuliaBinaryWrappers/Zlib_jll.jl/releases/download/Zlib-v1.2.13+1/Zlib.v1.2.13.powerpc64le-linux-gnu.tar.gz#/Zlib.v1.2.13+1.powerpc64le-linux-gnu.tar.gz
Source63:       https://github.com/JuliaBinaryWrappers/p7zip_jll.jl/releases/download/p7zip-v17.4.0+2/p7zip.v17.4.0.powerpc64le-linux-gnu.tar.gz#/p7zip.v17.4.0+2.powerpc64le-linux-gnu.tar.gz
Source64:       https://github.com/JuliaBinaryWrappers/libblastrampoline_jll.jl/releases/download/libblastrampoline-v5.11.0+0/libblastrampoline.v5.11.0.powerpc64le-linux-gnu.tar.gz#/libblastrampoline.v5.11.0+0.powerpc64le-linux-gnu.tar.gz

Source100:      gmp-6.2.1-arm64-invert_limb.patch

# PATCH-FIX-OPENSUSE julia-env-script-interpreter.patch ronisbr@gmail.com -- Change script interpreted to avoid errors in rpmlint.
Patch1:         julia-env-script-interpreter.patch
# PATCH-FIX-OPENSUSE disable-doc-gen-in-makefile.patch -- this patch ACTUALLY DISABLES the offline builds 😉
Patch2:         disable-doc-gen-in-makefile.patch
# PATCH-FIX-OPENSUSE -- Despite having no network, build looks for UnicodeData.txt (now Source3). Disabled with this patch.
Patch3:         disable-download-of-unicode-for-doc-gen.patch
# Based on https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/julia-libunwind-1.6.patch?ref_type=heads -- System libunwind compatibility
# Patch4:         julia-libunwind-1.9.patch
# Based of https://gitlab.archlinux.org/archlinux/packaging/packages/julia/-/raw/main/julia-libcholmod-cuda.patch?ref_type=heads -- we don't have NVIDIA or any CUDA platform by default
Patch5:         julia-remove-libcholmod_cuda.patch
# PATCH-FIX-OPENSUSE -- julia hardcodes looking for the libraries
Patch6:         openlibm.patch
# PATCH-FIX-OPENSUSE -- Julia packages e.g. LibCURL_jll.jl uses dlopen for libraries
Patch7:         julia-hardcoded-libs.patch
# PATCH-FIX-OPENSUSE -- A bug in MPFR which they describe in their INSTALL file. So we have to assist the mpfr.mk that julia uses.
Patch8:         mpfr-looking-for-gmp-fix.patch
Patch10:        apply-gmp-arm64-invert_limb.patch

BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  ca-certificates
BuildRequires:  clang
BuildRequires:  cmake >= 3.22
BuildRequires:  dos2unix
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel >= 3.3.4
BuildRequires:  gcc-fortran
BuildRequires:  git
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl) >= 1.1.1
BuildRequires:  pkgconfig(zlib)

# Additional dependencies for libgit2
BuildRequires:  fdupes
BuildRequires:  gpg2
BuildRequires:  libexpat-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-Error
BuildRequires:  perl-MailTools
BuildRequires:  python3-base
BuildRequires:  xz

# These lists the supposedly dependencies that are now bundled
# BuildRequires:  lapack-devel >= 3.5.0
# BuildRequires:  lld15
# BuildRequires:  llvm15-devel
# BuildRequires:  libcholmod5
# BuildRequires:  libuv-devel
# BuildRequires:  libopenblas_openmp-devel >= 0.3.5
# BuildRequires:  openblas-common-devel
# BuildRequires:  blas-devel
# BuildRequires:  suitesparse-devel >= 7.2.1
# BuildRequires:  libgit2-devel
BuildConflicts: gmp-devel
BuildConflicts: mpfr-devel
# BuildRequires:  dSFMT-devel
# BuildRequires:  libssh2-devel >= 1.9.0
BuildRequires:  libnghttp2-devel
# BuildRequires:  mbedtls-devel
# BuildRequires:  pcre2-devel >= 10.31

BuildRequires:  fipscheck
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libblastrampoline-devel
# BuildRequires:  libunwind-devel >= 1.3.1
BuildRequires:  libwhich
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  memory-constraints
BuildRequires:  metis-devel
BuildRequires:  ncurses-devel
BuildRequires:  openlibm-devel
BuildRequires:  openspecfun-devel
# I am not sure how or why they're different in Leap and Tumbleweed
%if 0%{?suse_version} > 1600
BuildRequires:  p7zip
%else
BuildRequires:  p7zip-full
%endif
BuildRequires:  patchelf >= 0.9
BuildRequires:  perl
BuildRequires:  readline-devel
BuildRequires:  tbb-devel
BuildRequires:  update-desktop-files
BuildRequires:  utf8proc-devel
BuildRequires:  valgrind
BuildRequires:  valgrind-devel

# Additional Build Requirements needed by LLVM15
BuildRequires:  binutils-devel >= 2.21.90
BuildRequires:  ccache
BuildRequires:  fdupes
BuildRequires:  libstdc++-devel
BuildRequires:  libvmmalloc-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

Requires:       ca-certificates
Requires:       p7zip >= 16
Requires:       readline

# Libraries used by CompilerSupportLibraries_jll, blastrampoline,
# nghttp2_jll but not detected as they are dlopen()ed but not linked to
%if 0%{?__isa_bits} == 64
BuildRequires:  libgcc_s1
BuildRequires:  libgfortran5
Requires:       libgcc_s.so.1()(64bit)
Requires:       libgfortran.so.5()(64bit)
Requires:       libgomp.so.1()(64bit)
%else
BuildRequires:  libgcc_s1
BuildRequires:  libgfortran5
Requires:       libgcc_s.so.1
Requires:       libgfortran.so.5
Requires:       libgomp.so.1
%endif

# Same as the previous comment. But the difference
# is that we applied julia-hardcoded-libs.patch
Requires:       openlibm-devel
Requires:       libblastrampoline-devel
# Requires:       libgit2-devel
# Requires:       libnghttp2-devel
# Requires:       libssh2-devel
# Requires:       mbedtls-devel
# Requires:       suitesparse-devel

# Julia requires the devel package as well
# specifically libjulia.so
%if 0%{?compat_mode}
Requires:       julia-compat-devel = %{version}
%else
Requires:       julia-devel = %{version}
%endif

Requires(post): %{_sbindir}/update-alternatives
Requires(post): /sbin/ldconfig
Requires(postun): %{_sbindir}/update-alternatives
Requires(postun): /sbin/ldconfig

Recommends:     curl
Recommends:     git
Recommends:     openssh-clients
# Recommends:     gmp-devel
# Recommends:     libcurl-devel
# Recommends:     mpfr-devel
# Recommends:     openspecfun-devel
# Recommends:     pcre2-devel
# Recommends:     suitesparse-devel

%if 0%{?compat_mode} == 0
Name:           julia
%else
Name:           julia-compat
%endif
%if 0%{?compat_mode} == 0
Summary:        High-level, high-performance dynamic programming language
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT AND Zlib
Group:          Development/Languages/Other
%else
Summary:        High-level, high-performance dynamic programming language (without CPU optim.)
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT AND Zlib
Group:          Development/Languages/Other
%endif
%if 0%{?compat_mode}
Conflicts:      julia
Provides:       julia = %{version}
%endif
Obsoletes:      %{name} < %{version}

# NOTICE: Enabled for now
# Let's not be optimistic towards 32 bit support and other architectures
# openSUSE or Julia cannot guarantee to support, shall we? Only choose
# Tier1 architectures
# libquadmath is disabled in the aarch64 build of gcc. so we cannot
# include that as exclusive arches for now.
# %%if 0%%{?compat_mode}
# ExclusiveArch:  x86_64 x86_64_v3
# %%else
# ExclusiveArch:  x86_64 x86_64_v3 aarch64
# %%endif
%{?suse_build_hwcaps_libs}

%description
Julia is a high-level, high-performance dynamic programming language for
technical computing, with syntax that is familiar to users of other technical
computing environments. It provides a sophisticated compiler, distributed
parallel execution, numerical accuracy, and an extensive mathematical function
library. The library, largely written in Julia itself, also integrates mature,
best-of-breed C and Fortran libraries for linear algebra, random number
generation, signal processing, and string processing.

This package is experimental and by no means supported by upstream. To use
upstream sources, you can use the alternative called juliaup.

%package        devel
Summary:        Julia development, debugging and testing files
Group:          Development/Languages/Other
Requires:       %{libname} = %{version}
%if 0%{?compat_mode}
Conflicts:      julia-devel
Provides:       julia-devel = %{version}
%endif
Obsoletes:      %{name}-devel < %{version}

%description    devel
Contains library symbolic links and header files for developing applications
linking to the Julia library, in particular embedding it, as well as tests and a
debugging version of Julia. This package is normally not needed when programming
in the Julia language, but rather for embedding Julia into external programs or
debugging Julia itself.

%package -n     %{libname}
Summary:        Julia shared object libraries
Group:          System/Libraries
%if 0%{?compat_mode}
Conflicts:      libjulia%{libjulia_sover_major}_%{libjulia_sover_minor}
Provides:       libjulia%{libjulia_sover_major}_%{libjulia_sover_minor} = %{version}
%endif
Obsoletes:      %{libname} < %{version}

%description -n %{libname}
Contains library files for interacting with Julia through C interfaces.

%prep
%autosetup -p1 -n julia-%{version}

# Copy https://www.unicode.org/Public/13.0.0/ucd/UnicodeData.txt to deps/srccache
cp -v %{SOURCE3} deps/srccache/UnicodeData-13.0.0.txt

# All bundled sources. Full.tar.gz is not full.tar.gz now eh?
cp -v %{SOURCE5}  deps/srccache/
cp -v %{SOURCE6}  deps/srccache/
cp -v %{SOURCE7}  deps/srccache/
cp -v %{SOURCE8}  deps/srccache/
cp -v %{SOURCE9}  deps/srccache/
cp -v %{SOURCE10} deps/srccache/
cp -v %{SOURCE11} deps/srccache/
cp -v %{SOURCE12} deps/srccache/
cp -v %{SOURCE13} deps/srccache/
cp -v %{SOURCE14} deps/srccache/
cp -v %{SOURCE15} deps/srccache/
cp -v %{SOURCE16} deps/srccache/
cp -v %{SOURCE17} deps/srccache/
cp -v %{SOURCE18} deps/srccache/
cp -v %{SOURCE19} deps/srccache/
cp -v %{SOURCE20} deps/srccache/
cp -v %{SOURCE21} deps/srccache/
cp -v %{SOURCE22} deps/srccache/
cp -v %{SOURCE23} deps/srccache/
cp -v %{SOURCE24} deps/srccache/
cp -v %{SOURCE25} deps/srccache/
cp -v %{SOURCE25} deps/srccache/
cp -v %{SOURCE26} deps/srccache/
cp -v %{SOURCE27} deps/srccache/
cp -v %{SOURCE28} deps/srccache/
cp -v %{SOURCE29} deps/srccache/
cp -v %{SOURCE30} deps/srccache/
cp -v %{SOURCE31} deps/srccache/
cp -v %{SOURCE32} deps/srccache/
cp -v %{SOURCE33} deps/srccache/
cp -v %{SOURCE34} deps/srccache/
cp -v %{SOURCE35} deps/srccache/
cp -v %{SOURCE36} deps/srccache/
cp -v %{SOURCE37} deps/srccache/
cp -v %{SOURCE38} deps/srccache/
cp -v %{SOURCE39} deps/srccache/
cp -v %{SOURCE40} deps/srccache/
cp -v %{SOURCE41} deps/srccache/
cp -v %{SOURCE42} deps/srccache/
cp -v %{SOURCE43} deps/srccache/
cp -v %{SOURCE44} deps/srccache/

cp -v %{SOURCE100} deps/patches/

# JLDOWNLOAD SHOULD BE DISABLED IF WE HAVE THE FULL TARBALL (NOT USEFUL FOR OPENSUSE)
echo "true" | tee deps/tools/jldownload

# JLCHECKSUM SHOULD BE DISABLED IF WE HAVE THE SOURCES (NOT USEFUL FOR OPENSUSE)
echo "true" | tee deps/tools/jlchecksum

%build
export CC=clang
export CXX=clang++
export CFLAGS="%{optflags} -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration"
export CXXFLAGS="%{optflags} -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration"

# Needed when USE_SYSTEM_CSL=1
# https://github.com/JuliaLang/julia/issues/39637
unlink %{_builddir}/%{buildsubdir}/build/usr/lib || true
mkdir -p %{_builddir}/%{buildsubdir}/build/%{_libdir}/
%if 0%{?suse_version} > 1600
ln -sf %{_libdir}/libgcc_s.so.1 %{_builddir}/%{buildsubdir}/build/%{_libdir}/libgcc_s.so.1
%else
ln -sf /%{_lib}/libgcc_s.so.1 %{_builddir}/%{buildsubdir}/build/%{_libdir}/libgcc_s.so.1
%endif

# I am not sure why Julia cannot find also libgfortran5.so on Leap...
ln -sf %{_libdir}/libgfortran.so.5 %{_builddir}/%{buildsubdir}/build/%{_libdir}/libgfortran.so.5

# Idk how it can't find libblastrampoline?
ln -sf %{_libdir}/libblastrampoline.so %{_builddir}/%{buildsubdir}/build/%{_libdir}/libblastrampoline.so

export LD_LIBRARY_PATH="%{_builddir}/%{buildsubdir}/build/usr/lib:%{_builddir}/%{buildsubdir}/build%{_libdir}:/usr/lib64:/usr/lib"

# Based on fedora specfile
# Work around bug that prompts zlib to be downloaded even when not used
# https://github.com/JuliaLang/julia/pull/42524/files#r734972945
# sed "s/ \$(build_prefix)\\/manifest\\/zlib//" -i deps/llvm.mk

%if 0%{?suse_version} > 1600
RELEASE_BANNER="openSUSE Tumbleweed - Built on $(date -u)"
%else
SLE_VERSION="$(echo %{sle_version} | sed -E 's|^(15)0([0-9])00|\1.\2|m')"
RELEASE_BANNER="openSUSE Leap ${SLE_VERSION} - Built on $(date -u)"
%endif
make %{?_smp_mflags} \
                     MARCH="%{julia_march}" \
%ifarch x86_64 || x86_64_v3
                     JULIA_CPU_TARGET="generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1);x86_64-v4,-rdrnd,base(1)" \
%endif
%ifarch i686
                     JULIA_CPU_TARGET="pentium4" \
%endif
%ifarch armv7l
                     JULIA_CPU_TARGET="armv7-a;armv7-a,neon;armv7-a,neon,vfp4" \
%endif
%ifarch aarch64
                     JULIA_CPU_TARGET="generic;cortex-a57;thunderx2t99;carmel,clone_all" \
%endif
%ifarch pp64le
                     JULIA_CPU_TARGET="pwr8" \
%endif
                     build_prefix="%{_builddir}/%{buildsubdir}/build%{_prefix}" \
                     build_libdir="%{_builddir}/%{buildsubdir}/build%{_libdir}" \
                     prefix="%{_prefix}" \
                     bindir="%{_bindir}" \
                     libdir="%{_libdir}" \
                     libexecdir="%{_libexecdir}" \
                     datarootdir="%{_datarootdir}" \
                     includedir="%{_includedir}" \
                     sysconfdir="%{_sysconfdir}" \
                     %{__julia_opts} \
%if 0%{?suse_version} > 1600
                     TAGGED_RELEASE_BANNER="${RELEASE_BANNER}" \
%else
                     TAGGED_RELEASE_BANNER="${RELEASE_BANNER}" \
%endif
                     release

# This may fix other issues where libLLVM-15jl.so is not properly copied?
if [ "x%{_lib}" != xlib ] ; then
  cp -a %{_builddir}/%{buildsubdir}/build/usr/lib/* %{_builddir}/%{buildsubdir}/build/%{_libdir}
  rm -rf %{_builddir}/%{buildsubdir}/build/usr/lib/
fi

%check
export CC=clang
export CXX=clang++
export CFLAGS="%{optflags} -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration"
export CXXFLAGS="%{optflags} -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration"
# Failures are to be expected if tests are done
# - int.jl not being found. see https://github.com/JuliaLang/julia/pull/53682#issuecomment-1992420825
# - Dates printing inconsistent. see https://github.com/JuliaLang/julia/issues/34655
# - hard-coded libs for non-impactful libraries e.g. zlib or mbedtls. see https://github.com/JuliaLang/julia/pull/38347#discussion_r574819534.
#   understandable if LLVM and other patched libraries but for unpatched ones, i am not sure if it is a strict requirement but reports
#   say mbedtls and similar work just fine.
# I might have to disable the tests for now
export CFLAGS="%{optflags} -Wno-error=implicit-function-declaration"
export CXXFLAGS="%{optflags} -Wno-error=implicit-function-declaration"
export LD_LIBRARY_PATH="%{_builddir}/%{buildsubdir}/build/usr/lib:%{_builddir}/%{buildsubdir}/build%{_libdir}:/usr/lib64:/usr/lib"
pushd %{_builddir}/%{buildsubdir}/test
# DISABLED FOR NOW
# ../julia --check-bounds=yes --startup-file=no ./runtests.jl || true
# Printing the version just for the sake of printing the version
../julia --version
popd

%install
export CC=clang
export CXX=clang++
export CFLAGS="%{optflags} -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration"
export CXXFLAGS="%{optflags} -Wno-error=incompatible-pointer-types -Wno-error=implicit-function-declaration"
export DEPS_GIT=0
export BUILD_LLD=1
export BUILD_LLDB=1
export LD_LIBRARY_PATH="%{_builddir}/%{buildsubdir}/build/usr/lib:%{_builddir}/%{buildsubdir}/build%{_libdir}:/usr/lib64:/usr/lib"
%if 0%{?suse_version} > 1600
RELEASE_BANNER="openSUSE Tumbleweed - Built on $(date -u)"
%else
SLE_VERSION="$(echo %{sle_version} | sed -E 's|^(15)0([0-9])00|\1.\2|m')"
RELEASE_BANNER="openSUSE Leap ${SLE_VERSION} - Built on $(date -u)"
%endif

make install DESTDIR="%{buildroot}" \
             MARCH="%{julia_march}" \
%ifarch x86_64 || x86_64_v3
                     JULIA_CPU_TARGET="generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1);x86_64-v4,-rdrnd,base(1)" \
%endif
%ifarch i686
                     JULIA_CPU_TARGET="pentium4" \
%endif
%ifarch armv7l
                     JULIA_CPU_TARGET="armv7-a;armv7-a,neon;armv7-a,neon,vfp4" \
%endif
%ifarch aarch64
                     JULIA_CPU_TARGET="generic;cortex-a57;thunderx2t99;carmel,clone_all" \
%endif
%ifarch pp64le
                     JULIA_CPU_TARGET="pwr8" \
%endif
             build_prefix="%{_builddir}/%{buildsubdir}/build%{_prefix}" \
             build_libdir="%{_builddir}/%{buildsubdir}/build%{_libdir}" \
             prefix="%{_prefix}" \
             bindir="%{_bindir}" \
             libdir="%{_libdir}" \
             libexecdir="%{_libexecdir}" \
             datarootdir="%{_datarootdir}" \
             includedir="%{_includedir}" \
             sysconfdir="%{_sysconfdir}" \
             %{__julia_opts} \
%if 0%{?suse_version} > 1600
             TAGGED_RELEASE_BANNER="${RELEASE_BANNER}"
%else
             TAGGED_RELEASE_BANNER="${RELEASE_BANNER}"
%endif

# Fix dangling symlinks
ln -sf %{_libdir}/libblastrampoline.so %{buildroot}%{_libdir}/julia/libblastrampoline.so
%if 0%{?suse_version} > 1600
ln -sf %{_libdir}/libgcc_s.so.1        %{buildroot}%{_libdir}/julia/libgcc_s.so.1
%else
ln -sf /%{_lib}/libgcc_s.so.1          %{buildroot}%{_libdir}/julia/libgcc_s.so.1
%endif
ln -sf %{_libdir}/libgfortran.so.5     %{buildroot}%{_libdir}/julia/libgfortran.so.5
ln -sf %{_libdir}/libcurl.so           %{buildroot}%{_libdir}/julia/libcurl.so.4

# GZip man page.
gzip %{buildroot}/%{_mandir}/man1/julia.1

rm -f %{buildroot}%{_libdir}/julia/libuv.a
rm -f %{buildroot}%{_datadir}/julia/base/build.h
rm -f %{buildroot}%{_datadir}/julia/base/Makefile

# Fix documentation directories.
mkdir -p %{buildroot}%{_docdir}/julia
mv -f %{buildroot}%{_datadir}/doc/julia/* %{buildroot}%{_docdir}/julia/
rm -r %{buildroot}%{_datadir}/doc/julia

ln -sfv /var/lib/ca-certificates/ca-bundle.pem %{buildroot}%{_datadir}/julia/cert.pem   # Needed by some julia packages

# Remove execution permission on documentation files.
chmod -x+X -R %{buildroot}%{_docdir}/julia/*

# Prevent find-debuginfo from touching precompiled caches as it
# changes checksums, which invalidates them
chmod -x %{buildroot}%{_datarootdir}/julia/compiled/*/*/*.so

# Install .desktop file and icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -p contrib/julia.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
convert -scale 16x16 -extent 16x16 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert -scale 24x24 -extent 24x24 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
convert -scale 32x32 -extent 32x32 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert -scale 48x48 -extent 48x48 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
convert -scale 256x256 -extent 256x256 -gravity center -background transparent \
    contrib/julia.svg %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

# Remove hidden files and zero-length files and directories from stdlib.
pushd %{buildroot}
find . -name ".codecov.yml" -prune -execdir rm -rf {} \;
find . -name ".git*" -prune -execdir rm -rf {} \;
find . -name ".ci" -prune -execdir rm -rf {} \;
find . -name ".devcontainer" -prune -execdir rm -rf {} \;
find . -name ".travis.yml" -prune -execdir rm -rf {} \;
find . -empty -type d -prune -execdir rm -rf {} \;
find . -empty -type f -prune -execdir rm -rf {} \;
find . -name "*.orig" -prune -execdir rm -rf {} \;
popd

%if 0%{?compat_mode}
rm -rf %{buildroot}%{_docdir}/julia/

# The 'application' object must be only provided by one package
# Alternatively, we could rename the .appdata and .desktop file to have
# both applications show up in a valid way, but that would require the
# -compat appdata to be modified to make the difference clear
rm %{buildroot}%{_datadir}/appdata/julia.appdata.xml
%endif

%suse_update_desktop_file -r julia Science Math

mv %{buildroot}%{_bindir}/julia %{buildroot}%{_bindir}/julia-base
mkdir -p %{buildroot}%{_sysconfdir}/alternatives

if [ "x%{_lib}" != xlib ] ; then
    mkdir -p %{buildroot}%{_prefix}/lib
    ln -sf %{_libdir}/julia %{buildroot}%{_prefix}/lib/julia
fi

ln -sf %{_sysconfdir}/alternatives/julia %{buildroot}%{_bindir}/julia

# Julia has a custom compiled LLVM sofile with a good name. We need
# it to be discoverable in LD_LIBRARY_PATHs
# so it can be dlopened for libLLVM_jll
ln -sf %{_libdir}/julia/libLLVM-15jl.so %{buildroot}%{_libdir}/libLLVM-15jl.so

# Attempt to convert all eol encodings to Unix
find %{buildroot} -type f -execdir dos2unix -k {} \;

# make it executable
chmod +x %{buildroot}%{_datadir}/julia/stdlib/v1.10/SparseArrays/gen/generator.jl

# Remove duplicated files.
%fdupes -s %{buildroot}%{_datadir}/julia

# Remove libtool leftovers
find %{buildroot} -type f -name "*.la" -delete -print

# Set RPATHs for libmpfr.so from julia
patchelf --set-rpath "%{_libdir}/julia:%{_libdir}:%{_prefix}/lib" "%{buildroot}%{_libdir}/julia/libmpfr.so"

%post
%{_sbindir}/update-alternatives --install %{_bindir}/julia \
    julia %{_bindir}/julia-base 5

%postun
if [ ! -f %{_bindir}/julia-base ] ; then
    %{_sbindir}/update-alternatives --remove julia %{_bindir}/julia-base
fi

%ldconfig_scriptlets -n %{libname}

%files
%doc CONTRIBUTING.md NEWS.md README.md
%license LICENSE.md
%ghost %{_bindir}/julia
%ghost %{_sysconfdir}/alternatives/julia
%{_bindir}/julia-base
%dir %{_datadir}/julia
%{_datadir}/julia/base
%{_datadir}/julia/base.cache
%{_datadir}/julia/stdlib
%{_datadir}/julia/compiled*
%{_datadir}/julia/cert.pem
%dir %{_libexecdir}/julia
%{_libexecdir}/julia/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%if !%{?compat_mode}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/julia.appdata.xml
%dir %{_docdir}/julia
%{_docdir}/julia/*
%endif
%{_datadir}/applications/julia.desktop
%{_prefix}/lib/julia
%{_libdir}/julia/
%{_mandir}/man1/julia.1%{?ext_man}
%{_libdir}/libLLVM-15jl.so
%dir %{_sysconfdir}/julia/
%config(noreplace) %{_sysconfdir}/julia/startup.jl

%files devel
%{_datadir}/julia/test/
%{_datadir}/julia/julia-config.jl
%{_includedir}/julia/
%{_libdir}/libjulia.so

%files -n %{libname}
%{_libdir}/libjulia.so.*

%changelog
