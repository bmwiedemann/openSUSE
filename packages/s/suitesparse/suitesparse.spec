#
# spec file for package suitesparse
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%ifarch m68k riscv64
%bcond_with openblas
%else
%bcond_without openblas
%endif

Name:           suitesparse
Summary:        A collection of sparse matrix libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Version:        5.4.0
Release:        0
Url:            http://faculty.cse.tamu.edu/davis/SuiteSparse/
Source:         http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE build_csparse_shared.patch -- Build CSparse as a shared library
Patch1:         build_csparse_shared.patch
Patch775418:    bnc775418-enable-SuiteSparse_time-symbol.patch
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc >= 4.9
BuildRequires:  gcc-c++ >= 4.9
%endif
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  m4
BuildRequires:  metis-devel
BuildRequires:  tbb-devel
%if %{with openblas}
BuildRequires:  openblas-devel
%endif
%define amdver       2.4.6
%define btfver       1.2.6
%define camdver      2.4.6
%define ccolamdver   2.9.6
%define cholmodver   3.0.13
%define colamdver    2.9.6
%define csparsever   3.2.0
%define cxsparsever  3.2.0
%define graphblasver 2.2.2
%define kluver       1.3.9
%define ldlver       2.2.6
%define mongoosever  2.0.3
%define rbiover      2.2.6
%define spqrver      2.0.9
%define umfpackver   5.7.8
# Your need define even it's just the same as main package
# or the %%build loop will override %%version with umfpack's version.
%define configver    5.4.0
%define csparsemajor %(echo "%{csparsever}" | cut -d "." -f1)
%define amdlib       %(echo "libamd%{amdver}"                  | cut -d "." -f1)
%define btflib       %(echo "libbtf%{btfver}"                  | cut -d "." -f1)
%define camdlib      %(echo "libcamd%{camdver}"                | cut -d "." -f1)
%define ccolamdlib   %(echo "libccolamd%{ccolamdver}"          | cut -d "." -f1)
%define cholmodlib   %(echo "libcholmod%{cholmodver}"          | cut -d "." -f1)
%define colamdlib    %(echo "libcolamd%{colamdver}"            | cut -d "." -f1)
%define csparselib   %(echo "libcsparse%{csparsever}"          | cut -d "." -f1)
%define cxsparselib  %(echo "libcxsparse%{cxsparsever}"        | cut -d "." -f1)
%define graphblaslib %(echo "libgraphblas%{graphblasver}"      | cut -d "." -f1)
%define klulib       %(echo "libklu%{kluver}"                  | cut -d "." -f1)
%define ldllib       %(echo "libldl%{ldlver}"                  | cut -d "." -f1)
%define mongooselib  %(echo "libmongoose%{mongoosever}"        | cut -d "." -f1)
%define rbiolib      %(echo "librbio%{rbiover}"                | cut -d "." -f1)
%define spqrlib      %(echo "libspqr%{spqrver}"                | cut -d "." -f1)
%define umfpacklib   %(echo "libumfpack%{umfpackver}"          | cut -d "." -f1)
%define configlib    %(echo "libsuitesparseconfig%{configver}" | cut -d "." -f1)

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.

%package devel
Summary:        Development headers for SuiteSparse
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} < 1500
Requires:       gcc7-c++
%else
Requires:       gcc-c++ >= 4.9
%endif
Requires:       %{amdlib}       = %{amdver}
Requires:       %{btflib}       = %{btfver}
Requires:       %{camdlib}      = %{camdver}
Requires:       %{ccolamdlib}   = %{ccolamdver}
Requires:       %{cholmodlib}   = %{cholmodver}
Requires:       %{colamdlib}    = %{colamdver}
Requires:       %{configlib}    = %{configver}
Requires:       %{configlib}    = %{version}
Requires:       %{csparselib}   = %{csparsever}
Requires:       %{cxsparselib}  = %{cxsparsever}
Requires:       %{graphblaslib} = %{graphblasver}
Requires:       %{klulib}       = %{kluver}
Requires:       %{ldllib}       = %{ldlver}
Requires:       %{mongooselib}  = %{mongoosever}
Requires:       %{rbiolib}      = %{rbiover}
Requires:       %{spqrlib}      = %{spqrver}
Requires:       %{umfpacklib}   = %{umfpackver}
Requires:       metis-devel
%if %{with openblas}
Requires:       openblas-devel
%else
Requires:       lapack-devel
%endif
Requires:       tbb-devel
# make sure developers can find these packages
Provides:       SuiteSparse_config         = %{version}
Obsoletes:      SuiteSparse_config         < %{version}
Provides:       amd-devel                  = %{amdver}
Obsoletes:      amd-devel                  < %{amdver}
Provides:       suitesparse-common-devel   = %{version}
Obsoletes:      suitesparse-common-devel   < %{version}
Provides:       umfpack-devel              = %{umfpackver}
Obsoletes:      umfpack-devel              < %{umfpackver}
Provides:       libamd-devel               = %{amdver}
Obsoletes:      libamd-devel               < %{amdver}
Provides:       libbtf-devel               = %{btfver}
Obsoletes:      libbtf-devel               < %{btfver}
Provides:       libcamd-devel              = %{camdver}
Obsoletes:      libcamd-devel              < %{camdver}
Provides:       libccolamd-devel           = %{ccolamdver}
Obsoletes:      libccolamd-devel           < %{ccolamdver}
Provides:       libcholmod-devel           = %{cholmodver}
Obsoletes:      libcholmod-devel           < %{cholmodver}
Provides:       libcolamd-devel            = %{colamdver}
Obsoletes:      libcolamd-devel            < %{colamdver}
Provides:       libcsparse-devel           = %{csparsever}
Obsoletes:      libcsparse-devel           < %{csparsever}
Provides:       libcxsparse-devel          = %{cxsparsever}
Obsoletes:      libcxsparse-devel          < %{cxsparsever}
Provides:       libgraphblas-devel         = %{umfpackver}
Obsoletes:      libgraphblas-devel         < %{umfpackver}
Provides:       libklu-devel               = %{kluver}
Obsoletes:      libklu-devel               < %{kluver}
Provides:       libldl-devel               = %{ldlver}
Obsoletes:      libldl-devel               < %{ldlver}
Provides:       libmongoose-devel          = %{mongoosever}
Obsoletes:      libmongoose-devel          < %{mongoosever}
Provides:       librbio-devel              = %{rbiover}
Obsoletes:      librbio-devel              < %{rbiover}
Provides:       libspqr-devel              = %{spqrver}
Obsoletes:      libspqr-devel              < %{spqrver}
Provides:       libumfpack-devel           = %{umfpackver}
Obsoletes:      libumfpack-devel           < %{umfpackver}
Provides:       libsuitesparseconfig-devel = %{configver}
Obsoletes:      libsuitesparseconfig-devel < %{configver}
Provides:       UFconfig-devel             = %{configver}
Obsoletes:      UFconfig-devel             < %{configver}

%description devel
suitesparse is a collection of libraries for computations involving
sparse matrices.

The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.

%package devel-static
Summary:        Static version of SuiteSparse libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
The suitesparse-static package contains the statically linkable
version of the suitesparse libraries.

%package -n %{amdlib}
Version:        %{amdver}
Release:        0
Summary:        Symmetric Approximate Minimum Degree
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libamd-%{amdver}" | tr . _) = %{version}
Obsoletes:      %(echo "libamd-%{amdver}" | tr . _) < %{version}

%description -n %{amdlib}
AMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting). There are versions in both C and Fortran. A MATLAB
interface is provided.

Note that this software has nothing to do with AMD the company.

AMD is part of the SuiteSparse sparse matrix suite.

%package -n libamd-doc
Summary:        Documentation for libamd
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other

%description -n libamd-doc
Documentation for libamd.

%package -n %{btflib}
Version:        %{btfver}
Release:        0
Summary:        Permutation to Block Triangular Form
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libbtf-%{btfver}" | tr . _) = %{version}
Obsoletes:      %(echo "libbtf-%{btfver}" | tr . _) < %{version}

%description -n %{btflib}
BTF permutes an unsymmetric matrix (square or rectangular) into its
block upper triangular form (more precisely, it computes a Dulmage-
Mendelsohn decomposition).

BTF is part of the SuiteSparse sparse matrix suite.

%package -n %{camdlib}
Version:        %{camdver}
Release:        0
Summary:        Symmetric Approximate Minimum Degree
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libcamd-%{camdver}" | tr . _) = %{version}
Obsoletes:      %(echo "libcamd-%{camdver}" | tr . _) < %{version}

%description -n %{camdlib}
CAMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting). There are versions in both C and Fortran. A MATLAB
interface is provided.

CAMD is part of the SuiteSparse sparse matrix suite.

%package -n libcamd-doc
Summary:        Documentation for libcamd
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other

%description -n libcamd-doc
Documentation for libcam.

%package -n %{ccolamdlib}
Version:        %{ccolamdver}
Release:        0
Summary:        Constrained Column Approximate Minimum Degree
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libccolamd-%{ccolamdver}" | tr . _) = %{version}
Obsoletes:      %(echo "libccolamd-%{ccolamdver}" | tr . _) < %{version}

%description -n %{ccolamdlib}
CCOLAMD computes an column approximate minimum degree ordering
algorithm, (like COLAMD), but it can also be given a set of ordering
constraints. CCOLAMD is required by the CHOLMOD package.

CCOLAMD is part of the SuiteSparse sparse matrix suite.

%package -n %{cholmodlib}
Version:        %{cholmodver}
Release:        0
Summary:        Supernodal Sparse Cholesky Factorization and Update/Downdate
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Libraries
Provides:       %(echo "libcholmod-%{cholmodver}" | tr . _) = %{version}
Obsoletes:      %(echo "libcholmod-%{cholmodver}" | tr . _) < %{version}
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
Version:        %{colamdver}
Release:        0
Summary:        Column Approximate Minimum Degree
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libcolamd-%{colamdver}" | tr . _) = %{version}
Obsoletes:      %(echo "libcolamd-%{colamdver}" | tr . _) < %{version}

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

%package -n %{csparselib}
Version:        %{csparsever}
Release:        0
Summary:        Instructional Sparse Matrix Package
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libcsparse-%{csparsever}" | tr . _) = %{version}
Obsoletes:      %(echo "libcsparse-%{csparsever}" | tr . _) < %{version}
# AT version 3.1.9, this package was accidentally called libcsparsever-3_1_9
%if "%{csparsever}" == "3.1.9"
Obsoletes:      libcsparsever-3_1_9 = 3.1.9
%endif

%description -n %{csparselib}
CSparse is a small yet feature-rich sparse matrix package written
specifically for a book. The purpose of the package is to demonstrate
a wide range of sparse matrix algorithms in as concise a code as
possible. CSparse is about 2,200 lines long (excluding its MATLAB
interface, demo codes, and test codes), yet it contains algorithms
(either asympotical optimal or fast in practice) for all of the
following functions described below. A MATLAB interface is included.

Note that the LU and Cholesky factorization algorithms are not as
fast as UMFPACK or CHOLMOD. Other functions have comparable
performance as their MATLAB equivalents (some are faster).

Documentation is very terse in the code; it is fully documented in
the book. Some indication of how to call the C functions in CSparse
is given by the CSparse/MATLAB/*.m help files.

CSparse is part of the SuiteSparse sparse matrix suite.

%package -n %{cxsparselib}
Version:        %{cxsparsever}
Release:        0
Summary:        An extended version of CSparse
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libcxsparse-%{cxsparsever}"   | tr . _) = %{version}
Obsoletes:      %(echo "libcxsparse-%{cxsparsever}"   | tr . _) < %{version}

%description -n %{cxsparselib}
CXSparse is an extended version of CSparse, with support for double
or complex matrices, with int or long integers.

CXSparse is part of the SuiteSparse sparse matrix suite.

%package -n %{graphblaslib}
Version:        %{graphblasver}
Release:        0
Summary:        An implementation of the GraphBLAS standard
License:        Apache-2.0
Group:          System/Libraries
Provides:       %(echo "libgraphblas-%{graphblasver}" | tr . _) = %{version}
Obsoletes:      %(echo "libgraphblas-%{graphblasver}" | tr . _) < %{version}

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
Version:        %{kluver}
Release:        0
Summary:        Sparse LU Factorization, for Circuit Simulation
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libklu-%{kluver}" | tr . _) = %{version}
Obsoletes:      %(echo "libklu-%{kluver}" | tr . _) < %{version}

%description -n %{klulib}
KLU is a sparse LU factorization algorithm well-suited for use in
circuit simulation. It was highlighted in the May 2007 issue of SIAM
News, Sparse Matrix Algorithm Drives SPICE Performance Gains. It is
the "fast sparse-matrix solver" mentioned in the article.

KLU is part of the SuiteSparse sparse matrix suite.

%package -n libklu-doc
Summary:        Documentation for libklu
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other

%description -n libklu-doc
Documentation for libklu.

%package -n %{ldllib}
Version:        %{ldlver}
Release:        0
Summary:        A Simple LDL^T Factorization
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %(echo "libldl-%{ldlver}" | tr . _) = %{version}
Obsoletes:      %(echo "libldl-%{ldlver}" | tr . _) < %{version}

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
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other

%description -n libldl-doc
Documentation for libldl.

%package -n %{mongooselib}
Version:        %{mongoosever}
Release:        0
Summary:        Graph partitioning library
License:        GPL-3.0-only
Group:          System/Libraries
Provides:       %(echo "libldl-%{mongoosever}" | tr . _) = %{version}
Obsoletes:      %(echo "libldl-%{mongoosever}" | tr . _) < %{version}

%description -n %{mongooselib}
Mongoose is a graph partitioning library. Currently, Mongoose only
supports edge partitioning.

mongoose is part of the SuiteSparse sparse matrix suite.

%package -n libmongoose-doc
Summary:        Documentation for libmongoose
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other

%description -n libmongoose-doc
Documentation for libmongoose.

%package -n %{rbiolib}
Version:        %{rbiover}
Release:        0
Summary:        MATLAB Toolbox for Reading/Writing Sparse Matrices
License:        GPL-2.0-or-later
Group:          System/Libraries
Provides:       %(echo "librbio-%{rbiover}" | tr . _) = %{version}
Obsoletes:      %(echo "librbio-%{rbiover}" | tr . _) < %{version}

%description -n %{rbiolib}
RBio is a MATLAB toolbox for reading/writing sparse matrices in the
Rutherford/Boeing format, and for reading/writing problems in the UF
Sparse Matrix Collection from/to a set of files in a directory.
Version 2.0+ is written in C.

RBio is part of the SuiteSparse sparse matrix suite.

%package -n %{spqrlib}
Version:        %{spqrver}
Release:        0
Summary:        Multifrontal Sparse QR
License:        GPL-2.0-or-later
Group:          System/Libraries
Provides:       %(echo "libspqr-%{spqrver}" | tr . _) = %{version}
Obsoletes:      %(echo "libspqr-%{spqrver}" | tr . _) < %{version}

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
Version:        %{umfpackver}
Release:        0
Summary:        Sparse Multifrontal LU Factorization
License:        GPL-2.0-or-later
Group:          System/Libraries
Provides:       %(echo "libumfpack-%{umfpackver}" | tr . _) = %{version}
Obsoletes:      %(echo "libumfpack-%{umfpackver}" | tr . _) < %{version}

%description -n %{umfpacklib}
UMFPACK is a set of routines for solving unsymmetric sparse linear
systems, Ax=b, using the Unsymmetric MultiFrontal method. Written in
ANSI/ISO C, with a MATLAB (Version 6.0 and later) interface. Appears
as a built-in routine (for lu, backslash, and forward slash) in M
ATLAB. Includes a MATLAB interface, a C-callable interface, and a
Fortran-callable interface. Note that "UMFPACK" is pronounced in two
syllables, "Umph Pack". It is not "You Em Ef Pack".

UMFPACK is part of the SuiteSparse sparse matrix suite.

%package -n %{configlib}
Version:        %{configver}
Release:        0
Summary:        Common configurations for all packages in SuiteSparse
License:        GPL-2.0-or-later
Group:          System/Libraries
Provides:       libufconfig = %{configver}
Obsoletes:      libufconfig < %{configver}
Provides:       libUFconfig = %{configver}
Obsoletes:      libUFconfig < %{configver}
Provides:       %(echo "libsuitesparseconfig%{configver}" | tr . _) = %{version}
Obsoletes:      %(echo "libsuitesparseconfig%{configver}" | tr . _) < %{version}

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
%setup -q -n SuiteSparse
%patch1 -p1
sed 's/^CHOLMOD_CONFIG =.*/CHOLMOD_CONFIG = -DNPARTITION/' -i SuiteSparse_config/SuiteSparse_config.mk
%if %{without openblas}
sed 's/-lopenblas/-lblas/' -i SuiteSparse_config/SuiteSparse_config.mk
%endif

sed -i "s:^SO_VERSION = _:SO_VERSION = %{csparsemajor}:" CSparse/Lib/Makefile
sed -i "s:^VERSION = _:VERSION = %{csparsever}:" CSparse/Lib/Makefile

cat CSparse/Lib/Makefile

mv SPQR/Doc/README.txt SPQR/Doc/README_2.txt

# bnc#751746
rm CHOLMOD/Doc/IA3_2014_Workshop_Rennich_Stosic_Davis_preprint.pdf
rm KLU/Doc/palamadai_e.pdf
rm MATLAB_Tools/Factorize/Doc/factorize_article.pdf
rm SPQR/Doc/algo_spqr.pdf
rm SPQR/Doc/qrgpu_paper.pdf
rm SPQR/Doc/spqr.pdf

# bnc#775418
%patch775418 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%if 0%{?suse_version} < 1500
export CC=gcc-7
export CXX=g++-7
%endif

%if %{with openblas}
blas_lib=-lopenblas
%else
blas_lib=-lblas
%endif

make MY_METIS_LIB="-lmetis" LAPACK="-llapack" BLAS="$blas_lib" TBB="-ltbb" CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" go
chrpath -d lib/*.so.*.*
chrpath -d GraphBLAS/build/*.so
chrpath -d GraphBLAS/build/*.so.*.*
chrpath -d Mongoose/build/lib/*.so
chrpath -d Mongoose/build/lib/*.so.*.*

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_libdir}

cp -Pt %{buildroot}%{_libdir} */Lib/*.a
cp -Pt %{buildroot}%{_libdir} lib/*
cp -Pt %{buildroot}%{_libdir} GraphBLAS/build/*.so
cp -Pt %{buildroot}%{_libdir} GraphBLAS/build/*.so.*
cp -Pt %{buildroot}%{_libdir} Mongoose/build/lib/*.so
cp -Pt %{buildroot}%{_libdir} Mongoose/build/lib/*.so.*
cp -Pt %{buildroot}%{_includedir}/%{name} include/*
cp -Pt %{buildroot}%{_includedir}/%{name} GraphBLAS/Include/*.h
cp -Prt %{buildroot}%{_docdir} share/doc/*

%if 0%{?sle_version} > 120300
cp -Pt %{buildroot}%{_libdir} GraphBLAS/build/*.a
%endif

%check
amd_test_symbol="amd_postorder"
btf_test_symbol="btf_order"
camd_test_symbol="camd_postorder"
ccolamd_test_symbol="ccolamd"
colamd_test_symbol="colamd"
cholmod_test_symbol="cholmod_start"
csparse_test_symbol="cs_sqr"
cxsparse_test_symbol="cs_di_sqr"
klu_test_symbol="klu_solve"
ldl_test_symbol="ldl_symbolic"
rbio_test_symbol="RBread"
spqr_test_symbol="SuiteSparseQR_C_symbolic"
umfpack_test_symbol="umfpack_toc"

mkdir -p linking_test
pushd linking_test

cat > linking_test.c.in << 'EOF'
char @test_symbol@ ();
int main ()
{
    return @test_symbol@ ();
}
EOF

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
for test_library in amd btf camd ccolamd colamd cholmod csparse cxsparse klu ldl rbio spqr umfpack; do
    cp linking_test.c.in linking_test.c
    test_symbol=${test_library}_test_symbol
    sed -i "s|@test_symbol@|${!test_symbol}|" linking_test.c
    cat linking_test.c
    gcc -o linking_test linking_test.c -L%{buildroot}%{_libdir} -l${test_library}
done

popd

%post   -n %{amdlib} -p /sbin/ldconfig
%postun -n %{amdlib} -p /sbin/ldconfig

%post   -n %{btflib} -p /sbin/ldconfig
%postun -n %{btflib} -p /sbin/ldconfig

%post   -n %{camdlib} -p /sbin/ldconfig
%postun -n %{camdlib} -p /sbin/ldconfig

%post   -n %{ccolamdlib} -p /sbin/ldconfig
%postun -n %{ccolamdlib} -p /sbin/ldconfig

%post   -n %{cholmodlib} -p /sbin/ldconfig
%postun -n %{cholmodlib} -p /sbin/ldconfig

%post   -n %{colamdlib} -p /sbin/ldconfig
%postun -n %{colamdlib} -p /sbin/ldconfig

%post   -n %{csparselib} -p /sbin/ldconfig
%postun -n %{csparselib} -p /sbin/ldconfig

%post   -n %{cxsparselib} -p /sbin/ldconfig
%postun -n %{cxsparselib} -p /sbin/ldconfig

%post   -n %{graphblaslib} -p /sbin/ldconfig
%postun -n %{graphblaslib} -p /sbin/ldconfig

%post   -n %{klulib} -p /sbin/ldconfig
%postun -n %{klulib} -p /sbin/ldconfig

%post   -n %{ldllib} -p /sbin/ldconfig
%postun -n %{ldllib} -p /sbin/ldconfig

%post   -n %{mongooselib} -p /sbin/ldconfig
%postun -n %{mongooselib} -p /sbin/ldconfig

%post   -n %{rbiolib} -p /sbin/ldconfig
%postun -n %{rbiolib} -p /sbin/ldconfig

%post   -n %{spqrlib} -p /sbin/ldconfig
%postun -n %{spqrlib} -p /sbin/ldconfig

%post   -n %{umfpacklib} -p /sbin/ldconfig
%postun -n %{umfpacklib} -p /sbin/ldconfig

%post   -n %{configlib} -p /sbin/ldconfig
%postun -n %{configlib} -p /sbin/ldconfig

%files devel
%doc ChangeLog README.txt
%license LICENSE.txt
%{_docdir}/%{name}-%{version}
%{_libdir}/*.so
%{_includedir}/%{name}/

%files devel-static
%doc ChangeLog README.txt
%license LICENSE.txt
%{_libdir}/*.a

%files -n %{amdlib}
%doc AMD/README.txt
%doc AMD/Doc/ChangeLog
%license AMD/Doc/License.txt AMD/Doc/lesser.txt
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
%license CAMD/Doc/License.txt CAMD/Doc/lesser.txt
%{_libdir}/libcamd.so.*

%files -n libcamd-doc
%doc CAMD/Doc/CAMD_UserGuide.pdf

%files -n %{ccolamdlib}
%doc CCOLAMD/README.txt
%doc CCOLAMD/Doc/ChangeLog
%license CCOLAMD/Doc/License.txt CCOLAMD/Doc/lesser.txt
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
%license COLAMD/Doc/License.txt COLAMD/Doc/lesser.txt
%{_libdir}/libcolamd.so.*

%files -n %{csparselib}
%doc CSparse/README.txt
%doc CSparse/Doc/ChangeLog
%license CSparse/Doc/License.txt CSparse/Doc/lesser.txt
%{_libdir}/libcsparse.so.*

%files -n %{cxsparselib}
%doc CXSparse/README.txt
%doc CXSparse/Doc/ChangeLog
%license CXSparse/Doc/License.txt CXSparse/Doc/lesser.txt
%{_libdir}/libcxsparse.so.*

%files -n %{graphblaslib}
%doc GraphBLAS/README.txt
%doc GraphBLAS/Doc/GraphBLAS_UserGuide.pdf
%license GraphBLAS/Doc/ChangeLog GraphBLAS/Doc/License.txt
%{_libdir}/libgraphblas.so.*

%files -n %{klulib}
%doc KLU/README.txt
%doc KLU/Doc/ChangeLog
%license KLU/Doc/License.txt KLU/Doc/lesser.txt
%{_libdir}/libklu.so.*

%files -n libldl-doc
%doc KLU/Doc/KLU_UserGuide.pdf

%files -n %{ldllib}
%doc LDL/README.txt
%doc LDL/Doc/ChangeLog
%license LDL/Doc/License.txt LDL/Doc/lesser.txt
%{_libdir}/libldl.so.*

%files -n libldl-doc
%doc LDL/Doc/ldl_userguide.pdf

%files -n %{mongooselib}
%doc Mongoose/README.md
%license Mongoose/Doc/License.txt
%{_libdir}/libmongoose.so.*

%files -n libmongoose-doc
%doc Mongoose/Doc/Mongoose_UserGuide.pdf

%files -n %{rbiolib}
%doc RBio/README.txt
%doc RBio/Doc/ChangeLog
%license RBio/Doc/License.txt RBio/Doc/gpl.txt
%{_libdir}/librbio.so.*

%files -n %{spqrlib}
%doc SPQR/README.txt
%doc SPQR/Doc/spqr_user_guide.pdf SPQR/Doc/ChangeLog SPQR/Doc/README_2.txt
%license SPQR/Doc/License.txt SPQR/Doc/gpl.txt
%{_libdir}/libspqr.so.*

%files -n %{umfpacklib}
%doc UMFPACK/README.txt
%doc UMFPACK/Doc/UMFPACK_QuickStart.pdf UMFPACK/Doc/UMFPACK_UserGuide.pdf UMFPACK/Doc/ChangeLog
%license UMFPACK/Doc/License.txt UMFPACK/Doc/gpl.txt
%{_libdir}/libumfpack.so.*

%files -n %{configlib}
%doc share/doc/*/SUITESPARSECONFIG_README.txt
%license LICENSE.txt
%{_libdir}/libsuitesparseconfig.so.*

%changelog
