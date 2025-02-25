#
# spec file for package suitesparse
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


%ifarch %{arm} aarch64
%define _lto_cflags %{nil}
%endif

%ifarch m68k
%bcond_with openblas
%else
%bcond_without openblas
%endif

Name:           suitesparse
Summary:        A collection of sparse matrix libraries
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Version:        7.8.3
Release:        0
Group:          Development/Libraries/C and C++
URL:            https://people.engr.tamu.edu/davis/suitesparse.html
Source0:        https://github.com/DrTimothyAldenDavis/SuiteSparse/archive/v%{version}.tar.gz#/SuiteSparse-%{version}.tar.gz
Source1:        https://sparse.tamu.edu/files/ssstats.csv

# Add our manually written for-convenience python script that lists all other sources
# This script is basically a modification of the runTests script
# https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/Mongoose/Tests/runTests
Source2:        list-mongoose-test-sources.py
Source3:        README-suse-maintenance.md
# Sources needed for tests, numbered starting from 100
Source100:      https://sparse.tamu.edu/MM/HB/1138_bus.tar.gz
Source101:      https://sparse.tamu.edu/MM/HB/494_bus.tar.gz
Source102:      https://sparse.tamu.edu/MM/HB/662_bus.tar.gz
Source103:      https://sparse.tamu.edu/MM/HB/685_bus.tar.gz
Source104:      https://sparse.tamu.edu/MM/HB/arc130.tar.gz
Source105:      https://sparse.tamu.edu/MM/HB/ash292.tar.gz
Source106:      https://sparse.tamu.edu/MM/HB/ash85.tar.gz
Source107:      https://sparse.tamu.edu/MM/HB/bcspwr01.tar.gz
Source108:      https://sparse.tamu.edu/MM/HB/bcspwr02.tar.gz
Source109:      https://sparse.tamu.edu/MM/HB/bcspwr03.tar.gz
Source110:      https://sparse.tamu.edu/MM/HB/bcspwr09.tar.gz
Source111:      https://sparse.tamu.edu/MM/HB/bcsstk17.tar.gz
Source112:      https://sparse.tamu.edu/MM/HB/bcsstm02.tar.gz
Source113:      https://sparse.tamu.edu/MM/HB/jagmesh7.tar.gz
Source114:      https://sparse.tamu.edu/MM/HB/lnsp3937.tar.gz
Source115:      https://sparse.tamu.edu/MM/HB/lshp3466.tar.gz
Source116:      https://sparse.tamu.edu/MM/HB/sherman1.tar.gz
Source117:      https://sparse.tamu.edu/MM/HB/sstmodel.tar.gz
Source118:      https://sparse.tamu.edu/MM/Boeing/crystm01.tar.gz
Source119:      https://sparse.tamu.edu/MM/Boeing/msc04515.tar.gz
Source120:      https://sparse.tamu.edu/MM/Gset/G42.tar.gz
Source121:      https://sparse.tamu.edu/MM/Nasa/nasa4704.tar.gz
Source122:      https://sparse.tamu.edu/MM/Andrianov/fxm3_6.tar.gz
Source123:      https://sparse.tamu.edu/MM/Andrianov/net25.tar.gz
Source124:      https://sparse.tamu.edu/MM/Oberwolfach/LF10000.tar.gz
Source125:      https://sparse.tamu.edu/MM/Pajek/Erdos992.tar.gz
Source126:      https://sparse.tamu.edu/MM/Pajek/USpowerGrid.tar.gz
Source127:      https://sparse.tamu.edu/MM/Pajek/yeast.tar.gz
Source128:      https://sparse.tamu.edu/MM/Schenk_IBMNA/c-38.tar.gz
Source129:      https://sparse.tamu.edu/MM/Schenk_IBMNA/c-43.tar.gz
Source130:      https://sparse.tamu.edu/MM/Gleich/minnesota.tar.gz
Source131:      https://sparse.tamu.edu/MM/Newman/netscience.tar.gz
Source132:      https://sparse.tamu.edu/MM/AG-Monien/netz4504.tar.gz
Source133:      https://sparse.tamu.edu/MM/DIMACS10/delaunay_n13.tar.gz
Source134:      https://sparse.tamu.edu/MM/DIMACS10/tx2010.tar.gz

# This patch is to keep our test sources since upstream has to likely update
# their sources for tests. This is not a fix for upstream but to adapt with
# how open build service works since it disallows network connections during
# the build.
Patch1:         keep-mongoose-test-sources.patch
BuildRequires:  cmake >= 3.22
BuildRequires:  fdupes
BuildRequires:  gcc >= 4.9
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gcc-fortran
BuildRequires:  gmp-devel
BuildRequires:  lapack-devel
BuildRequires:  make
BuildRequires:  memory-constraints
BuildRequires:  metis-devel
BuildRequires:  mpfr-devel
BuildRequires:  tbb-devel
BuildRequires:  valgrind
%if %{with openblas}
BuildRequires:  openblas-devel
%else
BuildRequires:  blas-devel
%endif
%define amd_sover                  3
%define btf_sover                  2
%define camd_sover                 3
%define ccolamd_sover              3
%define cholmod_sover              5
%define colamd_sover               3
%define config_sover               7
%define csparse_sover              4
%define cxsparse_sover             4
%define graphblas_sover            9
%define klu_sover                  2
%define ldl_sover                  3
%define lagraph_sover              1
%define lagraphx_sover             1
%define paru_sover                 1
%define mongoose_sover             3
%define suitesparse_mongoose_sover 3
%define rbio_sover                 4
%define sliplu_sover               1
%define spex_sover                 3
%define spqr_sover                 4
%define umfpack_sover              6
%define klu_cholmod_sover          2
%define amdlib                     libamd%{amd_sover}
%define btflib                     libbtf%{btf_sover}
%define camdlib                    libcamd%{camd_sover}
%define ccolamdlib                 libccolamd%{ccolamd_sover}
%define cholmodlib                 libcholmod%{cholmod_sover}
%define colamdlib                  libcolamd%{colamd_sover}
%define configlib                  libsuitesparseconfig%{config_sover}
%define csparselib                 libcsparse%{csparse_sover}
%define cxsparselib                libcxsparse%{cxsparse_sover}
%define graphblaslib               libgraphblas%{graphblas_sover}
%define suitesparse_mongooselib    libsuitesparse_mongoose%{suitesparse_mongoose_sover}
%define parulib                    libparu%{paru_sover}
%define lagraphlib                 liblagraph%{lagraph_sover}
%define lagraphxlib                liblagraphx%{lagraphx_sover}
%define klulib                     libklu%{klu_sover}
%define ldllib                     libldl%{ldl_sover}
%define mongooselib                libmongoose%{mongoose_sover}
%define rbiolib                    librbio%{rbio_sover}
%define spexlib                    libspex%{spex_sover}
%define spqrlib                    libspqr%{spqr_sover}
%define umfpacklib                 libumfpack%{umfpack_sover}
%define klu_cholmodlib             libklu_cholmod%{klu_cholmod_sover}
%{?suse_build_hwcaps_libs}

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.

%package devel
Summary:        Development headers for SuiteSparse
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{amdlib}                  = %{version}
Requires:       %{btflib}                  = %{version}
Requires:       %{camdlib}                 = %{version}
Requires:       %{ccolamdlib}              = %{version}
Requires:       %{cholmodlib}              = %{version}
Requires:       %{colamdlib}               = %{version}
Requires:       %{configlib}               = %{version}
Requires:       %{configlib}               = %{version}
Requires:       %{cxsparselib}             = %{version}
Requires:       %{graphblaslib}            = %{version}
Requires:       %{klu_cholmodlib}          = %{version}
Requires:       %{klu_cholmodlib}          = %{version}
Requires:       %{klulib}                  = %{version}
Requires:       %{lagraphlib}              = %{version}
Requires:       %{lagraphxlib}             = %{version}
Requires:       %{ldllib}                  = %{version}
Requires:       %{parulib}                 = %{version}
Requires:       %{rbiolib}                 = %{version}
Requires:       %{spexlib}                 = %{version}
Requires:       %{spqrlib}                 = %{version}
Requires:       %{suitesparse_mongooselib} = %{version}
Requires:       %{umfpacklib}              = %{version}
Requires:       gcc-c++ >= 4.9
Requires:       metis-devel
%if %{with openblas}
Requires:       openblas-devel
%else
Requires:       blas-devel
%endif
Requires:       tbb-devel

%description devel
suitesparse is a collection of libraries for computations involving
sparse matrices.

The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.

%package -n %{amdlib}
Summary:        Symmetric Approximate Minimum Degree
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{amdlib}
AMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting). There are versions in both C and Fortran. A MATLAB
interface is provided.

Note that this software has nothing to do with AMD the company.

AMD is part of the SuiteSparse sparse matrix suite.

%package -n libamd-doc
Summary:        Documentation for libamd
License:        BSD-3-Clause
Group:          Documentation/Other
BuildArch:      noarch

%description -n libamd-doc
Documentation for libamd.

%package -n %{btflib}
Summary:        Permutation to Block Triangular Form
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{btflib}
BTF permutes an unsymmetric matrix (square or rectangular) into its
block upper triangular form (more precisely, it computes a Dulmage-
Mendelsohn decomposition).

BTF is part of the SuiteSparse sparse matrix suite.

%package -n %{camdlib}
Summary:        Symmetric Approximate Minimum Degree
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{camdlib}
CAMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting). There are versions in both C and Fortran. A MATLAB
interface is provided.

CAMD is part of the SuiteSparse sparse matrix suite.

%package -n libcamd-doc
Summary:        Documentation for libcamd
License:        BSD-3-Clause
Group:          Documentation/Other
BuildArch:      noarch

%description -n libcamd-doc
Documentation for libcam.

%package -n %{ccolamdlib}
Summary:        Constrained Column Approximate Minimum Degree
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{ccolamdlib}
CCOLAMD computes an column approximate minimum degree ordering
algorithm, (like COLAMD), but it can also be given a set of ordering
constraints. CCOLAMD is required by the CHOLMOD package.

CCOLAMD is part of the SuiteSparse sparse matrix suite.

%package -n %{cholmodlib}
Summary:        Supernodal Sparse Cholesky Factorization and Update/Downdate
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Libraries
#bnc746867 cholmod from suitesparse should be GPL-2.0 and/or LGPL-2.0 licensed

%description -n %{cholmodlib}
CHOLMOD is a set of ANSI C routines for sparse Cholesky factorization
and update/downdate. A MATLAB interface is provided.

The performance of CHOLMOD was compared with 10 other codes in a
paper by Nick Gould, Yifan Hu, and Jennifer Scott. see also their raw
data. Comparing BCSLIB-EXT, CHOLMOD, MA57, MUMPS, Oblio, PARDISO,
SPOOLES, SPRSBLKLLT, TAUCS, UMFPACK, and WSMP, on 87 large symmetric
positive definite matrices, they found CHOLMOD to be fastest for 42
of the 87 matrices. Its run time is either fastest or within 10%% of
the fastest for 73 out of 87 matrices. Considering just the larger
matrices, it is either the fastest or within 10%% of the fastest for
40 out of 42 matrices. It uses the least amount of memory (or within
10%% of the least) for 35 of the 42 larger matrices. Jennifer Scott
and Yifan Hu also discuss the design considerations for a sparse
direct code.

CHOLMOD is part of the SuiteSparse sparse matrix suite.

%package -n %{colamdlib}
Summary:        Column Approximate Minimum Degree
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{colamdlib}
The COLAMD column approximate minimum degree ordering algorithm
computes a permutation vector P such that the LU factorization of
A (:,P) tends to be sparser than that of A. The Cholesky
factorization of (A (:,P))'*(A (:,P)) will also tend to be sparser
than that of A'*A. SYMAMD is a symmetric minimum degree ordering
method based on COLAMD, available as a MATLAB-callable function. It
constructs a matrix M such that M'*M has the same pattern as A, and
then uses COLAMD to compute a column ordering of M. Colamd and symamd
tend to be faster and generate better orderings than their MATLAB
counterparts, colmmd and symmmd.

COLAMD is part of the SuiteSparse sparse matrix suite.

%package -n %{cxsparselib}
Summary:        An extended version of CSparse
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{cxsparselib}
CXSparse is an extended version of CSparse, with support for double
or complex matrices, with int or long integers.

CXSparse is part of the SuiteSparse sparse matrix suite.

%package -n %{graphblaslib}
Summary:        An implementation of the GraphBLAS standard
License:        Apache-2.0
Group:          System/Libraries

%description -n %{graphblaslib}
GraphBLAS is an full implementation of the GraphBLAS standard,
which defines a set of sparse matrix operations on an extended algebra of
semirings using an almost unlimited variety of operators and types.  When
applied to sparse adjacency matrices, these algebraic operations are equivalent
to computations on graphs.  GraphBLAS provides a powerful and expressive
framework for creating graph algorithms based on the elegant mathematics of
sparse matrix operations on a semiring.

GraphBLAS is part of the SuiteSparse sparse matrix suite.

%package -n %{klulib}
Summary:        Sparse LU Factorization, for Circuit Simulation
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{klulib}
KLU is a sparse LU factorization algorithm well-suited for use in
circuit simulation. It was highlighted in the May 2007 issue of SIAM
News, Sparse Matrix Algorithm Drives SPICE Performance Gains. It is
the "fast sparse-matrix solver" mentioned in the article.

KLU is part of the SuiteSparse sparse matrix suite.

%package -n libklu-doc
Summary:        Documentation for libklu
License:        LGPL-2.1-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description -n libklu-doc
Documentation for libklu.

%package -n %{ldllib}
Summary:        A Simple LDL^T Factorization
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{ldllib}
LDL is a set of concise routines for factorizing symmetric positive-
definite sparse matrices, with some applicability to symmetric
indefinite matrices. Its primary purpose is to illustrate much of the
basic theory of sparse matrix algorithms in as concise a code as
possible, including an elegant new method of sparse symmetric
factorization that computes the factorization row-by-row but stores
it column-by-column. The entire symbolic and numeric factorization
consists of a total of only 49 lines of code. The package is written
in C, and includes a MATLAB interface.

LDL is part of the SuiteSparse sparse matrix suite.

%package -n libldl-doc
Summary:        Documentation for libldl
License:        LGPL-2.1-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description -n libldl-doc
Documentation for libldl.

%package -n %{rbiolib}
Summary:        MATLAB Toolbox for Reading/Writing Sparse Matrices
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{rbiolib}
RBio is a MATLAB toolbox for reading/writing sparse matrices in the
Rutherford/Boeing format, and for reading/writing problems in the UF
Sparse Matrix Collection from/to a set of files in a directory.
Version 2.0+ is written in C.

RBio is part of the SuiteSparse sparse matrix suite.

%package -n %{spexlib}
Summary:        SPEX, A SParse EXact Algebra Factorizations
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{spexlib}
SPEX is software package used to solve a sparse systems of linear equations
and replaces SLIP LU.

SPEX Util is a software package containing utility and auxiliary functions for the
SPEX factorizations. Additionally, SPEX Util provides a wrapper class for the GNU
Multiple Precision Arithmetic (GMP) and GNU Multiple Precision Floating Point
Reliable (MPFR) libraries that prevent memory leaks and improve the overall
stability of these external libraries. SPEX Util is written in ANSI C.

SPEX operates on matrices stored in any of the following 15 combinations of matrix formats and entry data-types

SPEX and SPEX Utils are part of the SuiteSparse sparse matrix suite.

%package -n     libspex-doc
Summary:        SPEX, A SParse EXact Algebra Factorizations
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description -n libspex-doc
Documentation for libspex.

SPEX is software package used to solve a sparse systems of linear equations
and replaces SLIP LU.

SPEX Util is a software package containing utility and auxiliary functions for the
SPEX factorizations. Additionally, SPEX Util provides a wrapper class for the GNU
Multiple Precision Arithmetic (GMP) and GNU Multiple Precision Floating Point
Reliable (MPFR) libraries that prevent memory leaks and improve the overall
stability of these external libraries. SPEX Util is written in ANSI C.

%package -n %{spqrlib}
Summary:        Multifrontal Sparse QR
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{spqrlib}
SuiteSparseQR is an implementation of the multifrontal sparse QR
factorization method. Parallelism is exploited both in the BLAS and
across different frontal matrices using Intel's Threading Building
Blocks, a shared-memory programming model for modern multicore
architectures. It can obtain a substantial fraction of the
theoretical peak performance of a multicore computer. The package is
written in C++ with user interfaces for MATLAB, C, and C++.

SuiteSparseQR is part of the SuiteSparse sparse matrix suite.

%package -n %{umfpacklib}
Summary:        Sparse Multifrontal LU Factorization
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{umfpacklib}
UMFPACK is a set of routines for solving unsymmetric sparse linear
systems, Ax=b, using the Unsymmetric MultiFrontal method. Written in
ANSI/ISO C, with a MATLAB (Version 6.0 and later) interface. Appears
as a built-in routine (for lu, backslash, and forward slash) in M
ATLAB. Includes a MATLAB interface, a C-callable interface, and a
Fortran-callable interface. Note that "UMFPACK" is pronounced in two
syllables, "Umph Pack". It is not "You Em Ef Pack".

UMFPACK is part of the SuiteSparse sparse matrix suite.

%package -n libumfpack-doc
Summary:        Documentation for libumfpack
License:        GPL-2.0-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description -n libumfpack-doc
Documentation for libumfpack.

%package -n %{klu_cholmodlib}
Summary:        Helpers for GPU accelerated runtimes
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{klu_cholmodlib}
This package provides the helper functions for the GPU for
SuiteSparse..

KLU x CHOLMOD is part of the SuiteSparse sparse matrix suite.

%package -n %{lagraphlib}
Summary:        Community effort collection of algorithms on top of GraphBLAS
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{lagraphlib}
This package provides a collection of graph algorithms built on top of GraphBLAS.

LAGraph is part of the SuiteSparse sparse matrix suite.

%package -n %{lagraphxlib}
Summary:        Community effort collection of algorithms on top of GraphBLAS
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{lagraphxlib}
This package provides an extended collection of graph algorithms built on top of GraphBLAS.

LAGraphX is part of the SuiteSparse sparse matrix suite.

%package -n %{suitesparse_mongooselib}
Summary:        Graph partitioning library
License:        GPL-3.0-only
Group:          System/Libraries

%description -n %{suitesparse_mongooselib}
Mongoose is a graph partitioning library. Currently, Mongoose only
supports edge partitioning.

mongoose is part of the SuiteSparse sparse matrix suite.

%package -n libsuitesparse_mongoose-doc
Summary:        Documentation for libsuitesparse_mongoose
License:        GPL-3.0-only
Group:          Documentation/Other
BuildArch:      noarch

%description -n libsuitesparse_mongoose-doc
Documentation for libsuitesparse_mongoose.

Mongoose is a graph partitioning library. Currently, Mongoose only
supports edge partitioning.

mongoose is part of the SuiteSparse sparse matrix suite.

%package -n     suitesparse_mongoose
Summary:        Binary executable for suitesparse mongoose
License:        GPL-3.0-only

%description -n   suitesparse_mongoose
Binary executable for suitesparse_mongoose.

Mongoose is a graph partitioning library. Currently, Mongoose only
supports edge partitioning.

mongoose is part of the SuiteSparse sparse matrix suite.

%package -n %{parulib}
Summary:        Multifrontal sparse LU factorization methods
License:        GPL-3.0-only
Group:          System/Libraries

%description -n %{parulib}
ParU is an implementation of the multifrontal sparse LU factorization method.
Parallelis is exploited both in the BLAS and across different frontal matrices
using OpenMP tasking and shared-memory programming model for modern multicore
architectures.

ParU is part of the SuiteSparse sparse matrix suite.

%package -n %{configlib}
Summary:        Common configurations for all packages in SuiteSparse
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %{configlib}
SuiteSparse_config is required by a number of sparse matrix packages,
including SuiteSparseQR, AMD, COLAMD, CCOLAMD, CHOLMOD, KLU, BTF,
LDL, CXSparse, RBio, and UMFPACK. It is not required by CSparse,
which is a stand-alone packages. Mongoose uses SuiteSparse_config,
if available but works also without it.

SuiteSparse_config contains a configuration file for "make"
(SuiteSparse_config.mk) and an include file (SuiteSparse_config.h).
Also included in SuiteSparse_config is a replacement for the
BLAS/LAPACK xerbla routine that does not print a warning message
(helpful if you don't want to link the entire Fortran I/O library
into a C application).

SuiteSparse_config is part of the SuiteSparse sparse matrix suite.

%prep
%autosetup -p1 -n SuiteSparse-%{version}

mv SPQR/Doc/README.txt SPQR/Doc/README_2.txt

# bnc#751746
rm CHOLMOD/Doc/IA3_2014_Workshop_Rennich_Stosic_Davis_preprint.pdf
rm KLU/Doc/palamadai_e.pdf
rm MATLAB_Tools/Factorize/Doc/factorize_article.pdf
rm SPQR/Doc/algo_spqr.pdf
rm SPQR/Doc/qrgpu_paper.pdf
rm SPQR/Doc/spqr.pdf

cp %{SOURCE1} Mongoose/Tests/

%(for src in "$(seq 100 134)"; do tar xvf %{SOURCE$src} --strip-components=1 -C Mongoose/Matrix; tar xvf %{SOURCE$src} --strip-components=1 -C Mongoose/Tests/Matrix; end)

%build
%limit_build -m 1500

%if %{with openblas}
export BLAS=-lopenblas
%else
export BLAS=-lblas
%endif

%ifarch %{arm} aarch64
%define build_ldflags  -latomic -lm
%else
%define build_ldflags -lm
# Better performance with -flto
unset MALLOC_CHECK_
unset MALLOC_PERTURB_
%endif

# GraphBlas demos: avoid writing to root dir
export GRAPHBLAS_CACHE_PATH=$(mktemp -d GraphBlas_JIT_cache_XXX)
#
export CMAKE_OPTIONS='-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
%if %{with openblas}
        -DBLA_VENDOR=OpenBLAS \
%endif
        -DCMAKE_INSTALL_BINDIR:PATH=%{_bindir} \
        -DCMAKE_INSTALL_SBINDIR:PATH=%{_sbindir} \
        -DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_libexecdir} \
        -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
        -DCMAKE_INSTALL_SHAREDSTATEDIR:PATH=%{_sharedstatedir} \
        -DCMAKE_INSTALL_LOCALSTATEDIR:PATH=%{_localstatedir} \
        -DCMAKE_INSTALL_RUNSTATEDIR:PATH=%{_rundir} \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
        -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir} \
        -DCMAKE_INSTALL_DATAROOTDIR:PATH=%{_datadir} \
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_C_FLAGS="${CFLAGS:-%optflags}" \
        -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags}" \
        -DCMAKE_Fortran_FLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" \
        -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
        -DCMAKE_MODULE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed" \
        -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
%if "%{?_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DBUILD_SHARED_LIBS:BOOL=ON \
        -DBUILD_STATIC_LIBS:BOOL=OFF \
        -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
        -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
        -DCMAKE_MODULES_INSTALL_DIR=%{_libdir}/cmake/%{name} \
        -DSUITESPARSE_DEMOS=ON \
        -DBUILD_TESTING=ON'

export JOBS="%(echo %{?_smp_mflags} | cut -c 3-)"
%make_build library

%install
%make_install

%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%check
# GraphBlas demos: avoid writing to root dir
export GRAPHBLAS_CACHE_PATH=$(mktemp -d GraphBlas_JIT_cache_XXX)
#
# Demos also include checks. These runs demos and their respective test suites.
export JOBS="%(echo %{?_smp_mflags} | cut -c 3-)"
%make_build demos

%ldconfig_scriptlets -n %{amdlib}
%ldconfig_scriptlets -n %{btflib}
%ldconfig_scriptlets -n %{camdlib}
%ldconfig_scriptlets -n %{ccolamdlib}
%ldconfig_scriptlets -n %{cholmodlib}
%ldconfig_scriptlets -n %{colamdlib}
%ldconfig_scriptlets -n %{cxsparselib}
%ldconfig_scriptlets -n %{graphblaslib}
%ldconfig_scriptlets -n %{klulib}
%ldconfig_scriptlets -n %{ldllib}
%ldconfig_scriptlets -n %{suitesparse_mongooselib}
%ldconfig_scriptlets -n %{rbiolib}
%ldconfig_scriptlets -n %{spexlib}
%ldconfig_scriptlets -n %{spqrlib}
%ldconfig_scriptlets -n %{umfpacklib}
%ldconfig_scriptlets -n %{lagraphlib}
%ldconfig_scriptlets -n %{lagraphxlib}
%ldconfig_scriptlets -n %{parulib}
%ldconfig_scriptlets -n %{klu_cholmodlib}
%ldconfig_scriptlets -n %{configlib}

%files devel
%doc ChangeLog README.md
%license LICENSE.txt
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/cmake/*

%files -n %{amdlib}
%doc AMD/README.txt
%doc AMD/Doc/ChangeLog
%license AMD/Doc/License.txt
%{_libdir}/libamd.so.*

%files -n libamd-doc
%doc AMD/Doc/AMD_UserGuide.pdf

%files -n %{btflib}
%doc BTF/README.txt
%doc BTF/Doc/ChangeLog
%license BTF/Doc/License.txt BTF/Doc/lesser.txt
%{_libdir}/libbtf.so.*

%files -n %{camdlib}
%doc CAMD/README.txt
%doc CAMD/Doc/ChangeLog
%license CAMD/Doc/License.txt
%{_libdir}/libcamd.so.*

%files -n libcamd-doc
%doc CAMD/Doc/CAMD_UserGuide.pdf

%files -n %{ccolamdlib}
%doc CCOLAMD/README.txt
%doc CCOLAMD/Doc/ChangeLog
%license CCOLAMD/Doc/License.txt
%{_libdir}/libccolamd.so.*

%files -n %{cholmodlib}
%doc CHOLMOD/README.txt
%doc CHOLMOD/Doc/CHOLMOD_UserGuide.pdf
%license CHOLMOD/Doc/ChangeLog CHOLMOD/Doc/License.txt
%license CHOLMOD/Cholesky/lesser.txt
%license CHOLMOD/MatrixOps/gpl.txt
%{_libdir}/libcholmod.so.*

%files -n %{colamdlib}
%doc COLAMD/README.txt
%doc COLAMD/Doc/ChangeLog
%license COLAMD/Doc/License.txt
%{_libdir}/libcolamd.so.*

%files -n %{cxsparselib}
%doc CXSparse/README.txt
%doc CXSparse/Doc/ChangeLog
%license CXSparse/Doc/License.txt CXSparse/Doc/lesser.txt
%{_libdir}/libcxsparse.so.*

%files -n %{graphblaslib}
%doc GraphBLAS/README.md
%doc GraphBLAS/Doc/GraphBLAS_UserGuide.pdf
%license GraphBLAS/Doc/ChangeLog GraphBLAS/LICENSE
%{_libdir}/libgraphblas.so.*

%files -n %{klulib}
%doc KLU/README.txt
%doc KLU/Doc/ChangeLog
%license KLU/Doc/License.txt KLU/Doc/lesser.txt
%{_libdir}/libklu.so.*

%files -n libklu-doc
%doc KLU/Doc/KLU_UserGuide.pdf

%files -n %{ldllib}
%doc LDL/README.txt
%doc LDL/Doc/ChangeLog
%license LDL/Doc/License.txt LDL/Doc/lesser.txt
%{_libdir}/libldl.so.*

%files -n libldl-doc
%doc LDL/Doc/ldl_userguide.pdf

%files -n %{suitesparse_mongooselib}
%doc Mongoose/README.md
%license Mongoose/Doc/License.txt
%{_libdir}/libsuitesparse_mongoose.so.*

%files -n libsuitesparse_mongoose-doc
%doc Mongoose/Doc/Mongoose_UserGuide.pdf

%files -n  suitesparse_mongoose
%{_bindir}/suitesparse_mongoose

%files -n %{rbiolib}
%doc RBio/README.txt
%doc RBio/Doc/ChangeLog
%license RBio/Doc/License.txt RBio/Doc/gpl.txt
%{_libdir}/librbio.so.*

%files -n %{spexlib}
%license SPEX/LICENSE.txt
%license SPEX/SPEX_Utilities/License/license.txt  SPEX/SPEX_Utilities/License/GPLv2.txt
%license SPEX/SPEX_Utilities/License/lesserv3.txt SPEX/SPEX_Utilities/License/CONTRIBUTOR-LICENSE.txt
%{_libdir}/libspex.so.*
%{_libdir}/libspexpython.so.*

%files -n libspex-doc
%doc SPEX/README.md
%doc SPEX/Doc/SPEX_UserGuide.pdf

%files -n %{spqrlib}
%doc SPQR/README.txt
%doc SPQR/Doc/spqr_user_guide.pdf SPQR/Doc/ChangeLog SPQR/Doc/README_2.txt
%license SPQR/Doc/License.txt SPQR/Doc/gpl.txt
%{_libdir}/libspqr.so.*

%files -n %{umfpacklib}
%license UMFPACK/Doc/License.txt UMFPACK/Doc/gpl.txt
%{_libdir}/libumfpack.so.*

%files -n libumfpack-doc
%doc UMFPACK/README.txt
%doc UMFPACK/Doc/UMFPACK_QuickStart.pdf UMFPACK/Doc/UMFPACK_UserGuide.pdf UMFPACK/Doc/ChangeLog

%files -n %{lagraphlib}
%doc LAGraph/README.md LAGraph/Acknowledgments.txt
%license LAGraph/LICENSE
%{_libdir}/liblagraph.so.*

%files -n %{lagraphxlib}
%doc LAGraph/README.md LAGraph/Acknowledgments.txt
%license LAGraph/LICENSE
%{_libdir}/liblagraphx.so.*

%files -n %{parulib}
%doc ParU/README.md
%license ParU/LICENSE.txt
%{_libdir}/libparu.so.*

%files -n %{klu_cholmodlib}
%doc KLU/README.txt
%doc KLU/Doc/ChangeLog
%license KLU/Doc/License.txt KLU/Doc/lesser.txt
%{_libdir}/libklu_cholmod.so.*

%files -n %{configlib}
%doc SuiteSparse_config/README.txt
%license LICENSE.txt
%{_libdir}/libsuitesparseconfig.so.*

%changelog
