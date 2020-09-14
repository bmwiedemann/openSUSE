#
# spec file for package boost
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


%define ver 1.74.0
%define _ver 1_74_0
%define package_version 1_74_0
%define file_version %_ver
%define lib_appendix %_ver
%define docs_version 1.56.0
%define short_version 1_56
%define python3X python38
%define pname boost
%bcond_with    build_docs
%bcond_without package_pdf
%bcond_without build_quickbook
%bcond_with    boost_devel
%bcond_with ringdisabled

%define package_name boost%{library_version}
%define my_docdir %{_docdir}/boost%{library_version}

# We can't have these inside the "@BUILD_FLAVOR@" because then quilt
# can't understand the spec file. If only @BUILD_FLAVOR@ was a normal macro....
%define build_base 1
%define name_suffix %{nil}

%if "@BUILD_FLAVOR@" == "%nil"
ExclusiveArch:  do_not_build
%endif

%if "@BUILD_FLAVOR@" == "base"
%define build_base 1
%define name_suffix -base
%bcond_with hpc
%bcond_with mpi
%endif

%if "@BUILD_FLAVOR@" == "extra"
%define build_base 0
%define name_suffix -extra
%bcond_without python3
%bcond_without mpi
%endif

%if "@BUILD_FLAVOR@" == "gnu-hpc"
%define build_base 1
%define name_suffix hpc
%define compiler_family gnu
%undefine c_f_ver
%bcond_with mpi
%bcond_without hpc
#ExcludeArch:    %%arm s390x i586
ExcludeArch:    s390x %{ix86} ppc64 ppc64le
%endif

%if "@BUILD_FLAVOR@" == "gnu-openmpi2-hpc"
%define build_base 0
%define name_suffix openmpi2_hpc
%define mpi_vers 2
%define compiler_family gnu
%define mpi_flavor openmpi
%undefine c_f_ver
%bcond_without hpc
%bcond_without mpi
%bcond_without python3
%if %{with ringdisabled}
ExclusiveArch:  do-not-build
%else
ExcludeArch:    s390x %{ix86} ppc64 ppc64le
%endif
%endif

%if "@BUILD_FLAVOR@" == "gnu-openmpi3-hpc"
%define build_base 0
%define name_suffix openmpi3_hpc
%define mpi_vers 3
%define compiler_family gnu
%define mpi_flavor openmpi
%undefine c_f_ver
%bcond_without hpc
%bcond_without mpi
%bcond_without python3
%if %{with ringdisabled}
ExclusiveArch:  do-not-build
%else
ExcludeArch:    s390x %{ix86} ppc64 ppc64le
%endif
%endif

%if "@BUILD_FLAVOR@" == "gnu-mvapich2-hpc"
%define build_base 0
%define name_suffix mvapich2_hpc
%define compiler_family gnu
%define mpi_flavor mvapich2
%undefine c_f_ver
%bcond_without hpc
%bcond_without mpi
%bcond_without python3
%if %{with ringdisabled}
ExclusiveArch:  do-not-build
%else
ExcludeArch:    s390x %{ix86} ppc64 ppc64le
%endif
%endif

%if "@BUILD_FLAVOR@" == "gnu-mpich-hpc"
%define build_base 0
%define name_suffix mpich
%define compiler_family gnu
%define mpi_flavor mpich
%undefine c_f_ver
%bcond_without hpc
%bcond_without mpi
%bcond_without python3
%if %{with ringdisabled}
ExclusiveArch:  do-not-build
%else
ExcludeArch:    s390x %{ix86} ppc64 ppc64le
%endif
%endif

# Python NumPy library is only available on Leap 42.1 OpenSUSE onward
# and is not availble in SLE
%if 0%{?suse_version} >= 1330 || 0%{?is_opensuse}
%bcond_without python_numpy
%else
%bcond_with python_numpy
%endif
# context hasn't been ported to most architectures yet
%ifarch %{ix86} x86_64 %{arm} aarch64 mips ppc ppc64 ppc64le riscv64 s390x
%bcond_without build_context
%else
%bcond_with build_context
%endif
%if %{with hpc}
# needed by the hpc tools
%{hpc_init -c %compiler_family %{?with_mpi:-m %mpi_flavor} %{?c_f_ver:-v %{c_f_ver}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}
%define package_prefix %{hpc_prefix}
%define package_libdir %{hpc_libdir}
%define package_bindir %{hpc_bindir}
%define package_includedir %{hpc_includedir}
%define base_name %{hpc_package_name %_ver}
%define package_name %{hpc_package_name %_ver}
%define package_python3_sitearch %{_hpc_python_sysconfig_path /usr/bin/python3 platlib %{?hpc_prefix}}
%else
%define package_prefix %{_prefix}
%define package_bindir %{_bindir}
%define package_libdir %{_libdir}
%define package_includedir %{_includedir}
%define base_name boost%{name_suffix}
%define package_python3_sitearch %python3_sitearch
%endif

# needs newer *default* GCC to compile runtime
%if %{with build_context} && 0%{?suse_version} > 1320
%bcond_without boost_fiber
%else
%bcond_with boost_fiber
%endif

Name:           %{base_name}
Version:        1.74.0
Release:        0
%define library_version 1_74_0

Summary:        Boost C++ Libraries
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            http://www.boost.org
Source0:        https://dl.bintray.com/boostorg/release/%{version}/source/boost_%{library_version}.tar.bz2
Source1:        boost-rpmlintrc
Source3:        http://downloads.sourceforge.net/project/boost/boost-docs/1.56.0/boost_1_56_pdf.tar.bz2
Source4:        existing_extra_docs
Source10:       exception.objdump
Source11:       __init__.py
Source100:      baselibs.conf
Source101:      symbol_diff.sh
Source102:      README.boost-devel
Patch1:         boost-thread.patch
Patch2:         boost-no_type_punning.patch
Patch4:         boost-pool_check_overflow.patch
Patch5:         boost-strict_aliasing.patch
Patch6:         boost-use_std_xml_catalog.patch
Patch7:         boost-rpmoptflags-only.patch
Patch9:         boost-aarch64-flags.patch
Patch10:        boost-disable-pch-on-aarch64.patch
Patch15:        boost-1.57.0-python-abi_letters.patch
Patch16:        boost-1.55.0-python-test-PyImport_AppendInittab.patch
Patch17:        python_mpi.patch
Patch18:        dynamic_linking.patch
Patch20:        python_library_name.patch
Patch21:        boost-remove-cmakedir.patch
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  libbz2-devel
BuildRequires:  libexpat-devel
BuildRequires:  libicu-devel
BuildRequires:  zlib-devel
%if %{with boost_fiber}
BuildRequires:  gcc-c++ > 5
%else
BuildRequires:  gcc-c++
%endif
%if ! %{build_base}
BuildRequires:  dos2unix
%if %{with python3}
BuildRequires:  python3-devel
%if %{with python_numpy}
BuildRequires:  python3-numpy-devel
%endif
%endif
%if %{with build_docs}
BuildRequires:  docbook
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt-tools
BuildRequires:  texlive-latex
%endif
%endif
%if %{with hpc}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  python3
BuildRequires:  suse-hpc
%hpc_requires
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
Requires:       %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc
%endif
%else
%if %{with mpi}
BuildRequires:  openmpi-macros-devel
%endif
%endif

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries that work well with the C++ Standard Library.
One goal is to establish "existing practice" and provide reference
implementations so that the Boost libraries are suitable for eventual
standardization. Some of the libraries have already been proposed for
inclusion in the C++ Standards Committee's upcoming C++ Standard
Library Technical Report.

Although Boost was begun by members of the C++ Standards Committee
Library Working Group, membership has expanded to include nearly two
thousand members of the C++ community at large.

%package     -n libboost_headers%{library_version}-devel
Summary:        Development headers for Boost
Group:          Development/Libraries/C and C++
Requires:       boost-license%{library_version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_headers-devel < %{version}
Conflicts:      libboost_headers-devel-impl
Provides:       libboost_headers-devel-impl = %{version}

%description -n libboost_headers%{library_version}-devel
A collection of header-only libraries for Boost.

%package     -n boost-license%{library_version}
Summary:        Boost License
Group:          Development/Libraries/C and C++
Provides:       boost-license = %{version}-%{release}
BuildArch:      noarch

%description -n boost-license%{library_version}
This package contains the license boost is provided under.

%package -n     %{package_name}-devel
Summary:        Development package for Boost C++
Group:          Development/Libraries/C and C++
%if %{with hpc}
Requires:       %{package_name}
%else
Requires:       libboost_atomic%{library_version}-devel
Requires:       libboost_chrono%{library_version}-devel
Requires:       libboost_container%{library_version}-devel
Requires:       libboost_date_time%{library_version}-devel
Requires:       libboost_filesystem%{library_version}-devel
Requires:       libboost_graph%{library_version}-devel
Requires:       libboost_iostreams%{library_version}-devel
Requires:       libboost_locale%{library_version}-devel
Requires:       libboost_log%{library_version}-devel
Requires:       libboost_math%{library_version}-devel
Requires:       libboost_nowide%{library_version}-devel
Requires:       libboost_program_options%{library_version}-devel
Requires:       libboost_random%{library_version}-devel
Requires:       libboost_regex%{library_version}-devel
Requires:       libboost_serialization%{library_version}-devel
Requires:       libboost_system%{library_version}-devel
Requires:       libboost_test%{library_version}-devel
Requires:       libboost_thread%{library_version}-devel
Requires:       libboost_timer%{library_version}-devel
Requires:       libboost_type_erasure%{library_version}-devel
Requires:       libboost_wave%{library_version}-devel
Requires:       libstdc++-devel
Conflicts:      boost-devel-impl
Provides:       boost-devel-impl = %{version}
%if %{with build_context}
Requires:       libboost_context%{library_version}-devel
Requires:       libboost_coroutine%{library_version}-devel
%endif
%if %{with boost_fiber}
Requires:       libboost_fiber%{library_version}-devel
%endif
%if %{with mpi}
Requires:       libboost_graph_parallel%{library_version}-devel
Requires:       libboost_mpi%{library_version}-devel
%endif
%if %{with python3}
Requires:       libboost_python-py3-%{library_version}-devel
%endif
%endif
%description -n %{package_name}-devel
This package contains all that is needed to develop/compile
applications that use the Boost C++ libraries. For documentation see
the documentation packages (html, man or pdf).

%if %{with hpc}
%package     -n %{package_name}-python3
Summary:        Boost.MPI Python 3.x serialization library
Group:          System/Libraries
Requires:       %{package_name}

%description -n %{package_name}-python3
This package contains the Boost.MPI Python 3.x serialization
inteface.
%endif

%package     -n boost%{library_version}-jam
Summary:        A Boost Make Replacement
Group:          Development/Tools/Building
Conflicts:      boost-jam-impl
Provides:       boost-jam-impl = %{version}

%description -n boost%{library_version}-jam
Boost Jam is a build tool based on FTJam, which in turn is based on
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System.

%package      -n %{package_name}-doc-html
Summary:        HTML documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description  -n %{package_name}-doc-html
This package contains the documentation of the boost dynamic libraries
in HTML format.

%package        doc-man
Summary:        Man documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description    doc-man
This package contains the documentation of the boost dynamic libraries
as man pages.

%package      -n %{package_name}-doc-pdf
Summary:        PDF documentation for the Boost C++ Libraries
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description  -n %{package_name}-doc-pdf
This package contains the documentation of the boost dynamic libraries
in PDF format.

%package     -n libboost_atomic%{library_version}
Summary:        Boost.Atomic runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_atomic%{library_version}
Run-Time support for Boost.Atomic, a library that provides atomic data types
and operations on these data types, as well as memory ordering constraints
required for coordinating multiple threads through atomic variables.

%package     -n libboost_atomic%{library_version}-devel
Summary:        Development headers for Boost.Atomic
Group:          Development/Libraries/C and C++
Requires:       libboost_atomic%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_atomic-devel-impl
Provides:       libboost_atomic-devel-impl = %{version}

%description -n libboost_atomic%{library_version}-devel
Development support for Boost.Atomic, a library that provides atomic
data types and operations on these data types, as well as memory
ordering constraints required for coordinating multiple threads through
atomic variables.

%package     -n libboost_container%{library_version}
Summary:        Boost.Container runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_container%{library_version}
This package contains the Boost.Container runtime library.

%package     -n libboost_container%{library_version}-devel
Summary:        Development headers for Boost.Container
Group:          Development/Libraries/C and C++
Requires:       libboost_container%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_container-devel-impl
Provides:       libboost_container-devel-impl = %{version}

%description -n libboost_container%{library_version}-devel
Development header files and libraries for Boost.Container.
Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offers advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that don't comply with the latest
C++ standard.

%package     -n libboost_context%{library_version}
Summary:        Boost.Context runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_context%{library_version}
Runtime support for Boost.Context, a library that providing cooperative
multitasking support.

%package     -n libboost_context%{library_version}-devel
Summary:        Development headers for Boost.Context
Group:          Development/Libraries/C and C++
Requires:       libboost_context%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_context-devel-impl
Provides:       libboost_context-devel-impl = %{version}

%description -n libboost_context%{library_version}-devel
Development headers and libraries for Boost.Context, a library that
providing cooperative multitasking support.

%package     -n libboost_contract%{library_version}
Summary:        Boost.Contract runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_contract%{library_version}
Runtime support for Boost.Contract, a library that implements
Design by Contract or DbC or contract programming.

%package     -n libboost_contract%{library_version}-devel
Summary:        Development headers for Boost.Contract
Group:          Development/Libraries/C and C++
Requires:       libboost_contract%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_system%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      libboost_contract-devel-impl
Provides:       libboost_contract-devel-impl = %{version}

%description -n libboost_contract%{library_version}-devel
Development headers and libraries for Boost.Contract, a library
that implements Design by Contract or DbC or contract programming.

%package     -n libboost_coroutine%{library_version}
Summary:        Boost::Coroutine runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_coroutine%{library_version}
This package contains the Boost Coroutine runtime library.

%package     -n libboost_coroutine%{library_version}-devel
Summary:        Development headers for Boost.Coroutine
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_context%{library_version}-devel = %{version}
Requires:       libboost_coroutine%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_coroutine-devel-impl
Provides:       libboost_coroutine-devel-impl = %{version}

%description -n libboost_coroutine%{library_version}-devel
This package provides headers for Boost.Coroutine libraries.
Boost.Coroutine2 provides templates for generalized subroutines which
allow suspending and resuming execution at certain locations.

%package     -n libboost_date_time%{library_version}
Summary:        Boost.DateTime runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_date_time%{library_version}
This package contains the Boost Date.DateTime runtime libraries.

%package     -n libboost_date_time%{library_version}-devel
Summary:        Development headers for Boost.DateTime library
Group:          Development/Libraries/C and C++
Requires:       libboost_date_time%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_date_time-devel-impl
Provides:       libboost_date_time-devel-impl = %{version}

%description -n libboost_date_time%{library_version}-devel
This package contains development header files and libraries for
Boost.DateTime library.

%package     -n libboost_fiber%{library_version}
Summary:        Boost.Fiber runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_fiber%{library_version}
This package contains Boost.Fiber runtime library.

%package     -n libboost_fiber%{library_version}-devel
Summary:        Development headers for Boost.Fiber library
Group:          Development/Libraries/C and C++
Requires:       libboost_context%{library_version}-devel = %{version}
Requires:       libboost_fiber%{library_version} = %{version}
Requires:       libboost_filesystem%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_fiber-devel-impl
Provides:       libboost_fiber-devel-impl = %{version}

%description -n libboost_fiber%{library_version}-devel
This package contains development header files and libraries for
Boost.Fiber library. Boost.Fiber is a cooperative multi-tasking
userland threading library.

%package     -n libboost_filesystem%{library_version}
Summary:        Boost.Filesystem Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_filesystem%{library_version}
This package contains the Boost.Filesystem library.

%package     -n libboost_filesystem%{library_version}-devel
Summary:        Development headers for Boost.Filesystem library
Group:          Development/Libraries/C and C++
Requires:       libboost_filesystem%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_filesystem-devel-impl
Provides:       libboost_filesystem-devel-impl = %{version}

%description -n libboost_filesystem%{library_version}-devel
Development headers for Boost.Filesystem library, a library providing
facilities to manipulate files and directories, and the paths that
identify them.

%package     -n libboost_graph%{library_version}
Summary:        Boost.Graph runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_graph%{library_version}
This package contains the Boost.Graph runtime library.

%package     -n libboost_graph%{library_version}-devel
Summary:        Development headers for Boost.Graph library
Group:          Development/Libraries/C and C++
Requires:       libboost_graph%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_regex%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_graph-devel-impl
Provides:       libboost_graph-devel-impl = %{version}

%description -n libboost_graph%{library_version}-devel
Development headers for Boost.Graph library. The BGL algorithms consist
of a core set of algorithm patterns and a larger set of graph
algorithms. The core algorithm patterns are Breadth First Search, Depth
First Search, and Uniform Cost Search.

%package     -n libboost_iostreams%{library_version}
Summary:        Boost.IOStreams Runtime Libraries
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_iostreams%{library_version}
This package contains the Boost.IOStreams Runtime libraries.

%package     -n libboost_iostreams%{library_version}-devel
Summary:        Development headers for Boost.IOStreans library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_iostreams%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_iostreams-devel-impl
Provides:       libboost_iostreams-devel-impl = %{version}

%description -n libboost_iostreams%{library_version}-devel
Boost.IOStreams provides a framework for defining streams, stream
buffers and IO filters

%package     -n libboost_log%{library_version}
Summary:        Boost.Log runtime Run-Time library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_log%{library_version}
This package contains runtime library for Boost.Log.

%package     -n libboost_log%{library_version}-devel
Summary:        Development headers for Boost.Log library
Group:          Development/Libraries/C and C++
Requires:       libboost_atomic%{library_version}-devel = %{version}
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_date_time%{library_version}-devel = %{version}
Requires:       libboost_filesystem%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_log%{library_version} = %{version}
Requires:       libboost_regex%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_log-devel-impl
Provides:       libboost_log-devel-impl = %{version}

%description -n libboost_log%{library_version}-devel
Development headers for Boost.Log library which aims to make logging
significantly easier for the application developer. It provides a wide
range of out-of-the-box tools along with public interfaces for extending
the library.

%package     -n libboost_math%{library_version}
Summary:        Boost.Math runtime libraries
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_math%{library_version}
This package contains the Boost.Math Runtime libraries.

%package     -n libboost_math%{library_version}-devel
Summary:        Development headers for Boost.Math libraries
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_math%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_math-devel-impl
Provides:       libboost_math-devel-impl = %{version}

%description -n libboost_math%{library_version}-devel
Development headers for Boost.Math* boost libraries.

%package     -n libboost_mpi%{library_version}
Summary:        Boost.MPI runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_mpi%{library_version}
This package contains the Boost.MPI runtime library.

%package     -n libboost_mpi%{library_version}-devel
Summary:        Development headers for Boost.MPI library
Group:          Development/Libraries/C and C++
%if %{with mpi}
%{?openmpi_devel_requires}
%endif
Requires:       libboost_graph%{library_version}-devel
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_mpi%{library_version} = %{version}
Requires:       libboost_serialization%{library_version}-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_mpi-devel-impl
Provides:       libboost_mpi-devel-impl = %{version}
%if %{with python3}
Requires:       libboost_python-py3-%{library_version}-devel
%endif

%description -n libboost_mpi%{library_version}-devel
Development headers for Boost.MPI boost library

%package     -n libboost_graph_parallel%{library_version}
Summary:        Boost.Graph.Distributed runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_graph_parallel%{library_version}
This package contains the Boost.Graph parallel runtime library

%package     -n libboost_graph_parallel%{library_version}-devel
Summary:        Development headers for Boost.Graph parallel library
Group:          Development/Libraries/C and C++
Requires:       libboost_graph_parallel%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_mpi%{library_version}-devel = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_graph_parallel-devel-impl
Provides:       libboost_graph_parallel-devel-impl = %{version}

%description -n libboost_graph_parallel%{library_version}-devel
Development headers for Boost.Graph parallel boost library.

%package     -n libboost_nowide%{library_version}
Summary:        Boost.Nowide runtime libraries
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_nowide%{library_version}
This package contains the Boost.Math Runtime libraries.

%package     -n libboost_nowide%{library_version}-devel
Summary:        Development headers for Boost.Nowide libraries
Group:          Development/Libraries/C and C++
Provides:       boost-nowide-devel = 10.0.2.1
Obsoletes:      boost-nowide-devel < 10.0.2.1

%description -n libboost_nowide%{library_version}-devel
Development headers for Boost.Nowide* boost libraries.

%package     -n libboost_mpi_%{python3X}-py3-%{library_version}
Summary:        Boost.MPI Python 3.x serialization library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_mpi_%{python3X}-py3-%{library_version}
This package contains the Boost.MPI Python 3.x serialization
inteface.

%package     -n libboost_mpi_%{python3X}-py3-%{library_version}-devel
Summary:        Development library for Boost.MPI Python 3.x serialization
Group:          Development/Libraries/C and C++
Requires:       libboost_mpi%{library_version}-devel = %{version}
Requires:       libboost_mpi_%{python3X}-py3-%{library_version} = %{version}
Requires:       libboost_python-py3-%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_mpi_python3-devel-impl
Provides:       libboost_mpi_python3-devel-impl = %{version}

%description -n libboost_mpi_%{python3X}-py3-%{library_version}-devel
This package contains the Boost.MPI development library for Python 3.x
serialization interface

%package     -n python3-boost_parallel_mpi%{library_version}
Summary:        Python 3.x bindings for Boost.Parallel.MPI library
Group:          Development/Languages/Python
Conflicts:      python3-boost_parallel_mpi-impl
Provides:       python3-boost_parallel_mpi-impl = %{version}

%description -n python3-boost_parallel_mpi%{library_version}
This package contains the Boost.Parallel.MPI bindings for Python 3.x

%package    -n libboost_test%{library_version}
Summary:        Boost.Test runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_test%{library_version}
This package contains the BoosttTest runtime library.

%package     -n libboost_test%{library_version}-devel
Summary:        Development headers for Boost.Test library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_test%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_test-devel-impl
Provides:       libboost_test-devel-impl = %{version}

%description -n libboost_test%{library_version}-devel
Development headers for Boost.Test library. Boost.Test supports for
simple program testing, full unit testing, and for program execution
monitoring.

%package     -n libboost_program_options%{library_version}
Summary:        Boost.ProgramOptions runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_program_options%{library_version}
This package contains the Boost.ProgramOptions runtime library.

%package     -n libboost_program_options%{library_version}-devel
Summary:        Development headers for Boost.ProgramOptions library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_program_options%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_program_options-devel-impl
Provides:       libboost_program_options-devel-impl = %{version}

%description -n libboost_program_options%{library_version}-devel
This package contains development headers for Boost.ProgramOptions
library.

%package     -n libboost_python-py3-%{library_version}
Summary:        Boost.Python runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description    -n libboost_python-py3-%{library_version}
This package contains the Boost.Python runtime libraries for python3
bindings.

%package     -n libboost_python-py3-%{library_version}-devel
Summary:        Development headers for Boost.Python library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_python-py3-%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_python3-devel-impl
Provides:       libboost_python3-devel-impl = %{version}

%description -n libboost_python-py3-%{library_version}-devel
Development headers for Boost.Python library. This package contains
library for python3 development for boost.

%package     -n libboost_numpy-py3-%{library_version}
Summary:        Boost.Python.NumPy runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description    -n libboost_numpy-py3-%{library_version}
This package contains the Boost.Python.NumPy runtime libraries for python3
bindings.

%package     -n libboost_numpy-py3-%{library_version}-devel
Summary:        Development headers for Boost.Python.NumPy library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_numpy-py3-%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_numpy3-devel-impl
Provides:       libboost_numpy3-devel-impl = %{version}

%description -n libboost_numpy-py3-%{library_version}-devel
Development headers for Boost.Python.NumPy library. This package contains
library for python3 development for boost.

%package     -n libboost_serialization%{library_version}
Summary:        Boost.Serialization runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_serialization%{library_version}
This package contains the Boost.Serialization runtime library.

%package     -n libboost_serialization%{library_version}-devel
Summary:        Development headers for Boost.Serialization library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_serialization%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_serialization-devel-impl
Provides:       libboost_serialization-devel-impl = %{version}

%description -n libboost_serialization%{library_version}-devel
This package contains development headers for Boost.Serialization
library.

%package     -n libboost_stacktrace%{library_version}
Summary:        Boost.Stacktrace runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_stacktrace%{library_version}
This package contains the Boost.Stacktrace runtime library.

%package     -n libboost_stacktrace%{library_version}-devel
Summary:        Development headers for Boost.Stacktrace library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_stacktrace%{library_version} = %{version}
Conflicts:      libboost_stacktrace-devel-impl
Provides:       libboost_stacktrace-devel-impl = %{version}

%description -n libboost_stacktrace%{library_version}-devel
This package contains development headers for Boost.Stacktrace library.
Boost.Stacktrace is a simple C++03 library that provide information
about call sequence in a human-readable form.

%package     -n libboost_system%{library_version}
Summary:        Boost.System runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_system%{library_version}
This package contains the Boost.System stub library.

%package     -n libboost_system%{library_version}-devel
Summary:        Development headers for Boost.System library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_system%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_system-devel-impl
Provides:       libboost_system-devel-impl = %{version}

%description -n libboost_system%{library_version}-devel
This package contained Boost.System development library. It is no
longer required as the library is headers only.

%package     -n libboost_thread%{library_version}
Summary:        Boost.Thread runtime libraries
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_thread%{library_version}
This package contains the Boost.Thread runtime library.

%package     -n libboost_thread%{library_version}-devel
Summary:        Development headers for Boost.Thread library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_date_time%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_thread-devel-impl
Provides:       libboost_thread-devel-impl = %{version}

%description -n libboost_thread%{library_version}-devel
This package contains development headers for Boost.Thread library.

%package     -n libboost_wave%{library_version}
Summary:        Boost.Wave runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_wave%{library_version}
This package contains the Boost::Wave runtime library.

%package     -n libboost_wave%{library_version}-devel
Summary:        Development headers for Boost.Wave library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_date_time%{library_version}-devel = %{version}
Requires:       libboost_filesystem%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_serialization%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version}-devel = %{version}
Requires:       libboost_wave%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_wave-devel-impl
Provides:       libboost_wave-devel-impl = %{version}

%description -n libboost_wave%{library_version}-devel
This package contains development headers for Boost.Wave library.

%package     -n libboost_regex%{library_version}
Summary:        Boost.Regex runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_regex%{library_version}
This package contains the Boost.Regex runtime library.

%package     -n libboost_regex%{library_version}-devel
Summary:        Development headers for Boost.Regex library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_regex%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_regex-devel-impl
Provides:       libboost_regex-devel-impl = %{version}

%description -n libboost_regex%{library_version}-devel
This package contains development headers for Boost.Regex library.

%package     -n libboost_random%{library_version}
Summary:        Boost.Random runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_random%{library_version}
This package contains the Boost.Random runtime library.

%package     -n libboost_random%{library_version}-devel
Summary:        Development headers for Boost.Random library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_random%{library_version} = %{version}
Requires:       libboost_system%{library_version}-devel = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_random-devel-impl
Provides:       libboost_random-devel-impl = %{version}

%description -n libboost_random%{library_version}-devel
This package contains Boost.Random development headers.

%package     -n libboost_chrono%{library_version}
Summary:        The Boost::Chrono runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_chrono%{library_version}
This package contains the Boost::Chrono runtime library.

%package     -n libboost_chrono%{library_version}-devel
Summary:        Development headers for Boost.Chrono library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_chrono-devel-impl
Provides:       libboost_chrono-devel-impl = %{version}

%description -n libboost_chrono%{library_version}-devel
This package contains Boost.Chrono development headers.

%package     -n libboost_locale%{library_version}
Summary:        Boost::Locale runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_locale%{library_version}
This package contains Boost::Locale runtime library.

%package     -n libboost_locale%{library_version}-devel
Summary:        Development headers for Boost.Locale library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_locale%{library_version} = %{version}
Requires:       libboost_system%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version}-devel = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_locale-devel-impl
Provides:       libboost_locale-devel-impl = %{version}

%description -n libboost_locale%{library_version}-devel
This package contains development headers for Boost.Locale library.

%package     -n libboost_timer%{library_version}
Summary:        Boost.Timer runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_timer%{library_version}
This package contains Boost.Timer runtime library.

%package     -n libboost_timer%{library_version}-devel
Summary:        Development headers for Boost.Timer library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_timer%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_timer-devel-impl
Provides:       libboost_timer-devel-impl = %{version}

%description -n libboost_timer%{library_version}-devel
This package contains development headers for Boost.Timer library.

%package     -n libboost_type_erasure%{library_version}
Summary:        Boost.TypeErasure runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_type_erasure%{library_version}
This package contains Boost::TypeErasure runtime library.

%package     -n libboost_type_erasure%{library_version}-devel
Summary:        Development headers for Boost.TypeErasure library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_system%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version}-devel = %{version}
Requires:       libboost_type_erasure%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_type_erasure-devel-impl
Provides:       libboost_type_erasure-devel-impl = %{version}

%description -n libboost_type_erasure%{library_version}-devel
This package contains development headers for Boost.TypeErasure library.

%package -n %{package_name}-quickbook
Summary:        Documentation tool geared towards C++
Group:          Development/Tools/Doc Generators
Requires:       boost-license%{library_version}
Conflicts:      quickbook
Provides:       quickbook = %{version}

%description -n %{package_name}-quickbook
QuickBook is a WikiWiki style documentation tool geared towards C++
documentation using simple rules and markup for simple formatting
tasks.

%if %{with hpc}
%{hpc_master_package}
%{hpc_master_package devel}
%if %{with python3}
%{hpc_master_package python3}
%endif
%endif

%prep
%setup -q -n boost_%{library_version} -b 3
#everything in the tarball has the executable flag set ...
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +
%patch1 -p1
%patch2
%patch4
%patch5
%patch6 -p1
%patch7
%patch9 -p1
%patch10 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch20 -p1
%patch21 -p1

%build
find . -type f -exec chmod u+w {} +

# General case
cat << EOF >user-config.jam
import os ;
local RPM_OPT_FLAGS = [ os.environ RPM_OPT_FLAGS ] ;
using gcc : : : <compileflags>\$(RPM_OPT_FLAGS) ;
project user-config ;
EOF

%if %{build_base}
cat << \EOF >.build
export LIBRARIES_FLAGS="--without-mpi --without-python"
%if ! %{with build_context}
# coroutine depends on context
LIBRARIES_FLAGS+=" --without-context --without-coroutine"
%endif

%if ! %{with boost_fiber}
LIBRARIES_FLAGS+=" --without-fiber"
%endif
EOF

%else

# Since boost build system is broken and incable of handling multiple python versions,
# we need to build boost piece by piece. First time to build all the non-python bits,
# then we build MPI and/or PYTHON modules for two python versions we need.
# MPI builds a python module.
cat << \EOF >.build
export PY_LIBRARIES_FLAGS="--with-python"
%if %{with mpi}
PY_LIBRARIES_FLAGS+=" --with-mpi"
%endif

# Dummy entry to make sure we don't build everything
export LIBRARIES_FLAGS="--with-system"

# Dummy entry replaced with real libraries, if we build something
%if %{with mpi}
LIBRARIES_FLAGS=" --with-graph_parallel"
%endif

EOF

%if %{with mpi}
# Set PATH, MANPATH and LD_LIBRARY_PATH for mpi
%if %{with hpc}
module load gnu %mpi_flavor
%else
%setup_openmpi
%endif
%endif

# Need specific Boost Jam config files.
#   1. one all "normal" libraries
#   2. one for each python version for for python/mpi libraries
#      use staging directories for MPI/PYTHON combinations.

# General case
# alias boost_python_alias : : <library>/boost/python//boost_python ;
cat << EOF >user-config.jam
EOF
%endif

# bootstrap b2
./bootstrap.sh \
    --prefix=%{package_prefix} --exec-prefix=%{package_bindir} \
    --libdir=%{package_libdir} --includedir=%{package_includedir} \
    --with-toolset=gcc

# Read shared build instructions
. ./.build

%if ! %{build_base}

# Build boost python3 and MPI, installed in python3 staging
%if %{with python3}
cp user-config.jam user-config-py3.jam
# sed -i -e 's#//boost_python#//boost_python3#' ./user-config-py3.jam
%define py3_abiflags %(python3-config --abiflags)
%{?!python3_version: %define python3_version %{py3_ver} }

cat << EOF >> user-config-py3.jam
using python
	: %{python3_version}
	: %{_bindir}/python3
	: %{_includedir}/python%{python3_version}%{py3_abiflags}
	:
	:
	: .%{py3_soflags}
	: %{py3_abiflags}
	;
%if %{with mpi}
using mpi ;
%endif
EOF

./b2 -d+2 -q --user-config=./user-config-py3.jam \
    --build-type=minimal --build-dir=./python3-build \
    --python-buildid=py3 \
    --stagedir=./python3-stage %{?_smp_mflags} \
    $PY_LIBRARIES_FLAGS \
    python=%{python3_version} threading=multi link=shared runtime-link=shared stage
%endif

%if %{with build_docs}
cat << EOF >>user-config.jam
using xsltproc ;

using boostbook
    : %{_datadir}/xml/docbook/stylesheet/nwalsh/current
    : %{_datadir}/xml/docbook/schema/dtd/4.2
    ;

using doxygen ;
EOF
%endif

# needed to get graph_parallel built
%if %{with mpi}
echo 'using mpi ;' >> ./user-config.jam
%endif

%endif

# This is run for both mini and non-mini build
./b2 -d+2 -q --user-config=./user-config.jam \
    --build-type=minimal --build-dir=./build \
    --stagedir=./stage %{?_smp_mflags} \
    $LIBRARIES_FLAGS \
    threading=multi link=shared runtime-link=shared stage

%if ! %{build_base}

# Verify that all symbols built in different stages are interchangeable.
# Can't be too careful!
cp %{SOURCE101} .
chmod +x symbol_diff.sh

# Build documentation
%if ! %{with hpc}
%if %{with build_quickbook}
pushd tools/quickbook
../../b2 --user-config=../../user-config.jam --v2 dist-bin %{?_smp_mflags}
popd
%endif

%if %{with build_docs}
cd doc
./b2 --user-config=../user-config.jam --v2 man %{?_smp_mflags}
%endif
%endif

%endif

%install

# Read shared build instructions
. ./.build

%if ! %{build_base}

%if %{with mpi}
# Set PATH, MANPATH and LD_LIBRARY_PATH for mpi
%if %{with hpc}
module load gnu %mpi_flavor
%else
%setup_openmpi
%endif
%endif

%if %{with python3}
./b2 -d+2 -q --user-config=./user-config-py3.jam \
    --build-type=minimal --build-dir=./python3-build \
    --python-buildid=py3 \
    --prefix=%{buildroot}%{package_prefix} --exec-prefix=%{buildroot}%{package_bindir} \
    --libdir=%{buildroot}%{package_libdir} --includedir=%{buildroot}%{package_includedir} \
    --stagedir=./python3-stage %{?_smp_mflags} \
    $PY_LIBRARIES_FLAGS \
    threading=multi link=shared runtime-link=shared install
%endif

%endif

# Generic install
./b2 -d+2 -q \
     --build-type=minimal --build-dir=./build --stagedir=./stage \
     --prefix=%{buildroot}%{package_prefix} --exec-prefix=%{buildroot}%{package_bindir} \
     --libdir=%{buildroot}%{package_libdir} --includedir=%{buildroot}%{package_includedir} \
     --user-config=./user-config.jam \
     $LIBRARIES_FLAGS \
     threading=multi link=shared runtime-link=shared install

# No python dependencies in the main tree

! $(ldd %{buildroot}%{package_libdir}/*.so* | grep python\\.)

%if ! %{build_base}

%if %{with python3}
! $(ldd %{buildroot}%{package_libdir}/*.so* | grep python3-\\.)
ln -s libboost_python-py3.so       %{buildroot}%{package_libdir}/libboost_python3.so
%endif

%if %{with python3}
mkdir -p %{buildroot}%{package_python3_sitearch}/boost/parallel/mpi/
install -m 0644 libs/mpi/build/__init__.py %{buildroot}%{package_python3_sitearch}/boost/parallel/mpi/
install -m 0644 %{SOURCE11} %{buildroot}%{package_python3_sitearch}/boost/parallel
install -m 0644 %{SOURCE11} %{buildroot}%{package_python3_sitearch}/boost
%if ! %{with hpc}
mv %{buildroot}%{_libdir}/boost-python3.8/mpi.%{py3_soflags}.so %{buildroot}%{package_python3_sitearch}/mpi.%{py3_soflags}.so
rmdir %{buildroot}%{_libdir}/boost-python3.8
%endif
%endif

%if ! %{with hpc}
#install doc files
mkdir -p %{buildroot}%{my_docdir}
%if %{with boost_devel}
install -m 0644 %{SOURCE102} %{buildroot}%{my_docdir}
%endif
find libs/ -name \*.htm\* -o -name \*.css -o -name \*.js | xargs dos2unix
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar --files-from=%{SOURCE4} -cf - --files-from=- | tar -C %{buildroot}%{my_docdir} -xf -
rm -rf %{buildroot}%{my_docdir}/boost
#ln -s %%{package_includedir}/boost %%{buildroot}%%{my_docdir}
#ln -s ../LICENSE_1_0.txt %%{buildroot}%%{my_docdir}/libs
find %{buildroot}%{my_docdir} -name \*.py -exec chmod -x {} +
chmod -x ../boost_1_56_pdf/*.pdf

%if %{with build_quickbook}
mkdir -p %{buildroot}%{package_bindir}
install -m 0755 dist/bin/quickbook %{buildroot}%{package_bindir}/quickbook
%endif
%endif
%endif

%if %{build_base} || %{with hpc}
mkdir -p %{buildroot}%{package_bindir}
%if %{without hpc}
install -m 755 b2 %{buildroot}%{package_bindir}/bjam
ln -s bjam %{buildroot}%{package_bindir}/jam
%endif

%if %{build_base}
# Remove exception library, but only if the symbols are not
# actually used. For now, the only symbol that is linked is
# should never be used as it's only available on Windows. So,
# verify that here.
objdump -Ctj .text -Ctj .text %{buildroot}%{package_libdir}/libboost_exception.so | \
  grep '^[0-9a-f]\+[[:space:]]\+g[[:space:]]\+F' | \
  sed -e 's#[0-9a-f]\+[[:space:]]\+g[[:space:]]\+F[[:space:]]\+\.text[[:space:]]\+[0-9a-f]\+[[:space:]]\+##' | \
  diff %{SOURCE10} - || echo "WARNING: libexception symbol change?"
rm %{buildroot}%{package_libdir}/libboost_exception.so
rm %{buildroot}%{package_libdir}/libboost_exception.so.%{version}

# not used or duplicated in boost-extra flavour
rm -r %{buildroot}%{package_libdir}/cmake/boost_stacktrace_{backtrace,windbg}*
rm -r %{buildroot}%{package_libdir}/cmake/boost_exception-*
rm -r %{buildroot}%{package_libdir}/cmake/boost_graph_parallel-%{version}
%endif

%fdupes %{buildroot}%{package_includedir}/boost
mkdir -p %{buildroot}%{my_docdir}
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120200 && !0%{?is_opensuse}
mkdir -p %{buildroot}%{_defaultlicensedir}
%endif
%else
# duplicate from boost-base flavour
rm %{buildroot}%{package_libdir}/cmake/BoostDetectToolset-%{version}.cmake
rm -r %{buildroot}%{package_libdir}/cmake/Boost-%{version}
rm -r %{buildroot}%{package_libdir}/cmake/boost_headers-%{version}
rm -r %{buildroot}%{package_libdir}/cmake/boost_{w,}serialization-%{version}

rm -rf %{buildroot}%{package_libdir}/libboost_numpy.so{,.%{version}}
rm -rf %{buildroot}%{package_libdir}/libboost_mpi_python.so.%{version}
rm -rf %{buildroot}%{package_libdir}/libboost_python.so.%{version}

rm -r %{buildroot}%{package_includedir}/boost
rm %{buildroot}%{package_libdir}/libboost_{w,}serialization*
rmdir --ignore-fail-on-non-empty %{buildroot}%{package_libdir}
%fdupes %{buildroot}%{my_docdir}
%endif

%if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{summary:0}"
module-whatis "URL: %{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
setenv          BOOST_DIR           %{hpc_path}
setenv          BOOST_DIR           %{hpc_libdir}
setenv          BOOST_INC           %{hpc_includedir}
if ([file isdirectory  %{hpc_includedir}]) {
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
}
if ([file isdirectory  %{package_python3_sitearch}]) {
prepend-path    PYTHONPATH          %{package_python3_sitearch}
}

%{hpc_modulefile_add_pkgconfig_path}

EOF
%endif

%if %{build_base}
%post -n libboost_atomic%{library_version} -p /sbin/ldconfig
%post -n libboost_container%{library_version} -p /sbin/ldconfig
%post -n libboost_context%{library_version} -p /sbin/ldconfig
%post -n libboost_contract%{library_version} -p /sbin/ldconfig
%post -n libboost_coroutine%{library_version} -p /sbin/ldconfig
%post -n libboost_date_time%{library_version} -p /sbin/ldconfig
%post -n libboost_fiber%{library_version} -p /sbin/ldconfig
%post -n libboost_filesystem%{library_version} -p /sbin/ldconfig
%post -n libboost_iostreams%{library_version} -p /sbin/ldconfig
%post -n libboost_log%{library_version} -p /sbin/ldconfig
%post -n libboost_test%{library_version} -p /sbin/ldconfig
%post -n libboost_program_options%{library_version} -p /sbin/ldconfig
%post -n libboost_regex%{library_version} -p /sbin/ldconfig
%post -n libboost_serialization%{library_version} -p /sbin/ldconfig
%post -n libboost_thread%{library_version} -p /sbin/ldconfig
%post -n libboost_type_erasure%{library_version} -p /sbin/ldconfig
%post -n libboost_math%{library_version} -p /sbin/ldconfig
%post -n libboost_nowide%{library_version} -p /sbin/ldconfig
%post -n libboost_graph%{library_version} -p /sbin/ldconfig
%post -n libboost_stacktrace%{library_version} -p /sbin/ldconfig
%post -n libboost_system%{library_version} -p /sbin/ldconfig
%post -n libboost_wave%{library_version} -p /sbin/ldconfig
%post -n libboost_random%{library_version} -p /sbin/ldconfig
%post -n libboost_chrono%{library_version} -p /sbin/ldconfig
%post -n libboost_locale%{library_version} -p /sbin/ldconfig
%post -n libboost_timer%{library_version} -p /sbin/ldconfig
%else

%if %{with python3}
%post -n libboost_python-py3-%{library_version} -p /sbin/ldconfig
%if %{with python_numpy}
%post -n libboost_numpy-py3-%{library_version} -p /sbin/ldconfig
%endif
%endif

%if %{with mpi}
%post -n libboost_mpi%{library_version} -p /sbin/ldconfig
%post -n libboost_graph_parallel%{library_version} -p /sbin/ldconfig

%if %{with python3}
%post -n libboost_mpi_%{python3X}-py3-%{library_version} -p /sbin/ldconfig
%endif
%endif

%endif
%if %{with hpc}
%post -n %base_name -p /sbin/ldconfig
%endif

%if %{build_base}
%postun -n libboost_atomic%{library_version} -p /sbin/ldconfig
%postun -n libboost_container%{library_version} -p /sbin/ldconfig
%postun -n libboost_context%{library_version} -p /sbin/ldconfig
%postun -n libboost_contract%{library_version} -p /sbin/ldconfig
%postun -n libboost_coroutine%{library_version} -p /sbin/ldconfig
%postun -n libboost_date_time%{library_version} -p /sbin/ldconfig
%postun -n libboost_fiber%{library_version} -p /sbin/ldconfig
%postun -n libboost_filesystem%{library_version} -p /sbin/ldconfig
%postun -n libboost_iostreams%{library_version} -p /sbin/ldconfig
%postun -n libboost_log%{library_version} -p /sbin/ldconfig
%postun -n libboost_test%{library_version} -p /sbin/ldconfig
%postun -n libboost_program_options%{library_version} -p /sbin/ldconfig
%postun -n libboost_regex%{library_version} -p /sbin/ldconfig
%postun -n libboost_serialization%{library_version} -p /sbin/ldconfig
%postun -n libboost_thread%{library_version} -p /sbin/ldconfig
%postun -n libboost_type_erasure%{library_version} -p /sbin/ldconfig
%postun -n libboost_math%{library_version} -p /sbin/ldconfig
%postun -n libboost_nowide%{library_version} -p /sbin/ldconfig
%postun -n libboost_graph%{library_version} -p /sbin/ldconfig
%postun -n libboost_stacktrace%{library_version} -p /sbin/ldconfig
%postun -n libboost_system%{library_version} -p /sbin/ldconfig
%postun -n libboost_wave%{library_version} -p /sbin/ldconfig
%postun -n libboost_random%{library_version} -p /sbin/ldconfig
%postun -n libboost_chrono%{library_version} -p /sbin/ldconfig
%postun -n libboost_locale%{library_version} -p /sbin/ldconfig
%postun -n libboost_timer%{library_version} -p /sbin/ldconfig
%else

%if %{with python3}
%postun -n libboost_python-py3-%{library_version} -p /sbin/ldconfig
%if %{with python_numpy}
%postun -n libboost_numpy-py3-%{library_version} -p /sbin/ldconfig
%endif
%endif

%if %{with mpi}
%postun -n libboost_mpi%{library_version} -p /sbin/ldconfig
%postun -n libboost_graph_parallel%{library_version} -p /sbin/ldconfig

%if %{with python3}
%postun -n libboost_mpi_%{python3X}-py3-%{library_version} -p /sbin/ldconfig
%endif
%endif

%endif

%if %{with hpc}
%postun -n %{base_name} -p /sbin/ldconfig
%endif

%if %{with hpc}

%files
%hpc_modules_files
%{!?hpc_compiler_family:%dir %{hpc_install_base}}
%dir %{hpc_install_path_base}
%dir %{hpc_install_path}
%package_libdir
%exclude %package_libdir/*.so
%if %{with python3}
%exclude %package_python3_sitearch
%endif

%files -n %{package_name}-devel
%package_includedir
%package_libdir/*.so
%if %{with python3}
%files -n %{package_name}-python3
%package_python3_sitearch
%endif

%else
%if %{build_base}
%files -n boost%{library_version}-jam
%{package_bindir}/bjam
%{package_bindir}/jam

%files -n libboost_atomic%{library_version}
%{package_libdir}/libboost_atomic.so.%{version}

%files -n libboost_atomic%{library_version}-devel
%dir %{package_libdir}/cmake/boost_atomic-%{version}
%{package_libdir}/cmake/boost_atomic-%{version}/*
%{package_libdir}/libboost_atomic.so

%files -n libboost_container%{library_version}
%{package_libdir}/libboost_container.so.%{version}

%files -n libboost_container%{library_version}-devel
%dir %{package_libdir}/cmake/boost_container-%{version}
%{package_libdir}/cmake/boost_container-%{version}/*
%{package_libdir}/libboost_container.so

%if %{with build_context}
%files -n libboost_context%{library_version}
%{package_libdir}/libboost_context.so.%{version}

%files -n libboost_context%{library_version}-devel
%dir %{package_libdir}/cmake/boost_context-%{version}
%{package_libdir}/cmake/boost_context-%{version}/*
%{package_libdir}/libboost_context.so

%files -n libboost_coroutine%{library_version}
%{package_libdir}/libboost_coroutine.so.%{version}

%files -n libboost_coroutine%{library_version}-devel
%dir %{package_libdir}/cmake/boost_coroutine-%{version}
%{package_libdir}/cmake/boost_coroutine-%{version}/*
%{package_libdir}/libboost_coroutine.so

%endif

%files -n libboost_contract%{library_version}
%{package_libdir}/libboost_contract.so.%{version}

%files -n libboost_contract%{library_version}-devel
%dir %{package_libdir}/cmake/boost_contract-%{version}
%{package_libdir}/cmake/boost_contract-%{version}/*
%{package_libdir}/libboost_contract.so

%files -n libboost_date_time%{library_version}
%{package_libdir}/libboost_date_time.so.%{version}

%files -n libboost_date_time%{library_version}-devel
%dir %{package_libdir}/cmake/boost_date_time-%{version}
%{package_libdir}/cmake/boost_date_time-%{version}/*
%{package_libdir}/libboost_date_time.so

%if %{with boost_fiber}
%files -n libboost_fiber%{library_version}
%{package_libdir}/libboost_fiber.so.%{version}

%files -n libboost_fiber%{library_version}-devel
%dir %{package_libdir}/cmake/boost_fiber-%{version}
%dir %{package_libdir}/cmake/boost_fiber_numa-%{version}
%{package_libdir}/cmake/boost_fiber-%{version}/*
%{package_libdir}/cmake/boost_fiber_numa-%{version}/*
%{package_libdir}/libboost_fiber.so

%endif

%files -n libboost_filesystem%{library_version}
%{package_libdir}/libboost_filesystem.so.%{version}

%files -n libboost_filesystem%{library_version}-devel
%dir %{package_libdir}/cmake/boost_filesystem-%{version}
%{package_libdir}/cmake/boost_filesystem-%{version}/*
%{package_libdir}/libboost_filesystem.so

%files -n libboost_graph%{library_version}
%{package_libdir}/libboost_graph.so.%{version}

%files -n libboost_graph%{library_version}-devel
%dir %{package_libdir}/cmake/boost_graph-%{version}
%{package_libdir}/cmake/boost_graph-%{version}/*
%{package_libdir}/libboost_graph.so

%files -n libboost_iostreams%{library_version}
%{package_libdir}/libboost_iostreams.so.%{version}

%files -n libboost_iostreams%{library_version}-devel
%dir %{package_libdir}/cmake/boost_iostreams-%{version}
%{package_libdir}/cmake/boost_iostreams-%{version}/*
%{package_libdir}/libboost_iostreams.so

%files -n libboost_log%{library_version}
%{package_libdir}/libboost_log.so.%{version}
%{package_libdir}/libboost_log_setup.so.%{version}

%files -n libboost_log%{library_version}-devel
%dir %{package_libdir}/cmake/boost_log-%{version}
%dir %{package_libdir}/cmake/boost_log_setup-%{version}
%{package_libdir}/cmake/boost_log-%{version}/*
%{package_libdir}/cmake/boost_log_setup-%{version}/*
%{package_libdir}/libboost_log.so
%{package_libdir}/libboost_log_setup.so

%files -n libboost_math%{library_version}
%{package_libdir}/libboost_math_c99f.so.%{version}
%{package_libdir}/libboost_math_c99l.so.%{version}
%{package_libdir}/libboost_math_c99.so.%{version}
%{package_libdir}/libboost_math_tr1f.so.%{version}
%{package_libdir}/libboost_math_tr1l.so.%{version}
%{package_libdir}/libboost_math_tr1.so.%{version}

%files -n libboost_math%{library_version}-devel
%dir %{package_libdir}/cmake/boost_math_c99*-%{version}
%dir %{package_libdir}/cmake/boost_math_tr1*-%{version}
%{package_libdir}/cmake/boost_math_c99*-%{version}/*
%{package_libdir}/cmake/boost_math_tr1*-%{version}/*
%{package_libdir}/libboost_math_c99f.so
%{package_libdir}/libboost_math_c99l.so
%{package_libdir}/libboost_math_c99.so
%{package_libdir}/libboost_math_tr1f.so
%{package_libdir}/libboost_math_tr1l.so
%{package_libdir}/libboost_math_tr1.so

%files -n libboost_nowide%{library_version}
%{package_libdir}/libboost_nowide.so.%{version}

%files -n libboost_nowide%{library_version}-devel
%dir %{package_libdir}/cmake/boost_nowide-%{version}
%{package_libdir}/cmake/boost_nowide-%{version}/boost_nowide-config.cmake
%{package_libdir}/cmake/boost_nowide-%{version}/boost_nowide-config-version.cmake
%{package_libdir}/cmake/boost_nowide-%{version}/libboost_nowide-variant-shared.cmake
%{package_libdir}/libboost_nowide.so

%files -n libboost_test%{library_version}
%{package_libdir}/libboost_prg_exec_monitor.so.%{version}
%{package_libdir}/libboost_test_exec_monitor.so.%{version}
%{package_libdir}/libboost_unit_test_framework.so.%{version}

%files -n libboost_test%{library_version}-devel
%dir %{package_libdir}/cmake/boost_prg_exec_monitor-%{version}
%dir %{package_libdir}/cmake/boost_test_exec_monitor-%{version}
%dir %{package_libdir}/cmake/boost_unit_test_framework-%{version}
%{package_libdir}/cmake/boost_prg_exec_monitor-%{version}/*
%{package_libdir}/cmake/boost_test_exec_monitor-%{version}/*
%{package_libdir}/cmake/boost_unit_test_framework-%{version}/*
%{package_libdir}/libboost_prg_exec_monitor.so
%{package_libdir}/libboost_test_exec_monitor.so
%{package_libdir}/libboost_unit_test_framework.so

%files -n libboost_program_options%{library_version}
%{package_libdir}/libboost_program_options.so.%{version}

%files -n libboost_program_options%{library_version}-devel
%dir %{package_libdir}/cmake/boost_program_options-%{version}
%{package_libdir}/cmake/boost_program_options-%{version}/*
%{package_libdir}/libboost_program_options.so
%endif

%if ! %{build_base}

%if %{with mpi}
%files -n libboost_mpi%{library_version}
%{package_libdir}/libboost_mpi.so.1*

%files -n libboost_mpi%{library_version}-devel
%dir %{package_libdir}/cmake
%dir %{package_libdir}/cmake/boost_mpi-%{version}
%{package_libdir}/cmake/boost_mpi-%{version}/*
%{package_libdir}/libboost_mpi.so

%files -n libboost_graph_parallel%{library_version}
%{package_libdir}/libboost_graph_parallel.so.1*

%files -n libboost_graph_parallel%{library_version}-devel
%dir %{package_libdir}/cmake
%dir %{package_libdir}/cmake/boost_graph_parallel-%{version}
%{package_libdir}/cmake/boost_graph_parallel-%{version}/*
%{package_libdir}/libboost_graph_parallel.so

%if %{with python3}
%files -n libboost_mpi_%{python3X}-py3-%{library_version}
%{package_libdir}/libboost_mpi_%{python3X}-py3.so.%{version}

%files -n libboost_mpi_%{python3X}-py3-%{library_version}-devel
%dir %{package_libdir}/cmake/boost_mpi_python-%{version}
%{package_libdir}/cmake/boost_mpi_python-%{version}/*
%endif
%{package_libdir}/libboost_mpi_%{python3X}-py3.so

%files -n python3-boost_parallel_mpi%{library_version}
%dir %{package_python3_sitearch}/boost
%dir %{package_python3_sitearch}/boost/parallel
%dir %{package_python3_sitearch}/boost/parallel/mpi
%{package_python3_sitearch}/boost/__init__.py
%{package_python3_sitearch}/boost/parallel/__init__.py
%{package_python3_sitearch}/boost/parallel/mpi/__init__.py
%{package_python3_sitearch}/mpi.%{py3_soflags}.so
%endif

%if %{with python3}
%files -n libboost_python-py3-%{library_version}
%{package_libdir}/libboost_python-py3.so.1*

%files -n libboost_python-py3-%{library_version}-devel
%dir %{package_libdir}/cmake
%dir %{package_libdir}/cmake/boost_python-%{version}
%{package_libdir}/cmake/boost_python-%{version}/*
%{package_libdir}/libboost_python3.so
%{package_libdir}/libboost_python-py3.so

%if %{with python_numpy}
%files -n libboost_numpy-py3-%{library_version}
%{package_libdir}/libboost_numpy-py3.so.1*

%files -n libboost_numpy-py3-%{library_version}-devel
%dir %{package_libdir}/cmake
%dir %{package_libdir}/cmake/boost_numpy-%{version}
%{package_libdir}/cmake/boost_numpy-%{version}/*
%{package_libdir}/libboost_numpy-py3.so

%endif
%endif
%endif

%if %{build_base}
%files -n libboost_serialization%{library_version}
%{package_libdir}/libboost_serialization.so.%{version}
%{package_libdir}/libboost_wserialization.so.%{version}

%files -n libboost_serialization%{library_version}-devel
%dir %{package_libdir}/cmake/boost_serialization-%{version}
%dir %{package_libdir}/cmake/boost_wserialization-%{version}
%{package_libdir}/cmake/boost_serialization-%{version}/*
%{package_libdir}/cmake/boost_wserialization-%{version}/*
%{package_libdir}/libboost_serialization.so
%{package_libdir}/libboost_wserialization.so

%files -n libboost_stacktrace%{library_version}
%{package_libdir}/libboost_stacktrace_addr2line.so.%{version}
%{package_libdir}/libboost_stacktrace_basic.so.%{version}
%{package_libdir}/libboost_stacktrace_noop.so.%{version}

%files -n libboost_stacktrace%{library_version}-devel
%dir %{package_libdir}/cmake/boost_stacktrace_addr2line-%{version}
%dir %{package_libdir}/cmake/boost_stacktrace_basic-%{version}
%dir %{package_libdir}/cmake/boost_stacktrace_noop-%{version}
%{package_libdir}/cmake/boost_stacktrace_addr2line-%{version}/*
%{package_libdir}/cmake/boost_stacktrace_basic-%{version}/*
%{package_libdir}/cmake/boost_stacktrace_noop-%{version}/*
%{package_libdir}/libboost_stacktrace_addr2line.so
%{package_libdir}/libboost_stacktrace_basic.so
%{package_libdir}/libboost_stacktrace_noop.so

%files -n libboost_system%{library_version}
%{package_libdir}/libboost_system.so.%{version}

%files -n libboost_system%{library_version}-devel
%dir %{package_libdir}/cmake/boost_system-%{version}
%{package_libdir}/cmake/boost_system-%{version}/*
%{package_libdir}/libboost_system.so

%files -n libboost_thread%{library_version}
%{package_libdir}/libboost_thread.so.%{version}

%files -n libboost_thread%{library_version}-devel
%dir %{package_libdir}/cmake/boost_thread-%{version}
%{package_libdir}/cmake/boost_thread-%{version}/*
%{package_libdir}/libboost_thread.so

%files -n libboost_wave%{library_version}
%{package_libdir}/libboost_wave.so.%{version}

%files -n libboost_wave%{library_version}-devel
%dir %{package_libdir}/cmake/boost_wave-%{version}
%{package_libdir}/cmake/boost_wave-%{version}/*
%{package_libdir}/libboost_wave.so

%files -n libboost_regex%{library_version}
%{package_libdir}/libboost_regex.so.%{version}

%files -n libboost_regex%{library_version}-devel
%dir %{package_libdir}/cmake/boost_regex-%{version}
%{package_libdir}/cmake/boost_regex-%{version}/*
%{package_libdir}/libboost_regex.so

%files -n libboost_random%{library_version}
%{package_libdir}/libboost_random.so.%{version}

%files -n libboost_random%{library_version}-devel
%dir %{package_libdir}/cmake/boost_random-%{version}
%{package_libdir}/cmake/boost_random-%{version}/*
%{package_libdir}/libboost_random.so

%files -n libboost_chrono%{library_version}
%{package_libdir}/libboost_chrono.so.%{version}

%files -n libboost_chrono%{library_version}-devel
%dir %{package_libdir}/cmake/boost_chrono-%{version}
%{package_libdir}/cmake/boost_chrono-%{version}/*
%{package_libdir}/libboost_chrono.so

%files -n libboost_locale%{library_version}
%{package_libdir}/libboost_locale.so.%{version}

%files -n libboost_locale%{library_version}-devel
%dir %{package_libdir}/cmake/boost_locale-%{version}
%{package_libdir}/cmake/boost_locale-%{version}/*
%{package_libdir}/libboost_locale.so

%files -n libboost_timer%{library_version}
%{package_libdir}/libboost_timer.so.%{version}

%files -n libboost_timer%{library_version}-devel
%dir %{package_libdir}/cmake/boost_timer-%{version}
%{package_libdir}/cmake/boost_timer-%{version}/*
%{package_libdir}/libboost_timer.so

%files -n libboost_type_erasure%{library_version}
%{package_libdir}/libboost_type_erasure.so.%{version}

%files -n libboost_type_erasure%{library_version}-devel
%dir %{package_libdir}/cmake/boost_type_erasure-%{version}
%{package_libdir}/cmake/boost_type_erasure-%{version}/*
%{package_libdir}/libboost_type_erasure.so
%endif

%if ! %{build_base}
%if %{with boost_devel}
%files -n %{package_name}-devel
%dir %{my_docdir}
%{my_docdir}/README.boost-devel
%endif

%files -n %{package_name}-doc-html
%dir %{my_docdir}
%doc %{my_docdir}/*
%if %{with boost_devel}
%exclude %{my_docdir}/README.boost-devel
%endif

%if %{with build_docs}
%files doc-man
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%{_mandir}/man9/*.9%{?ext_man}
%endif

%if %{with package_pdf}
%files -n %{package_name}-doc-pdf
%doc ../boost_1_56_pdf/*.pdf
%endif

%if %{with build_quickbook}
%files -n %{package_name}-quickbook
%{package_bindir}/quickbook
%endif
%endif

%if %{build_base}
%files -n libboost_headers%{library_version}-devel
%dir %{package_libdir}/cmake
%dir %{package_libdir}/cmake/Boost-%{version}
%dir %{package_libdir}/cmake/boost_headers-%{version}
%dir %{package_includedir}/boost
%{package_libdir}/cmake/BoostDetectToolset-%{version}.cmake
%{package_libdir}/cmake/Boost-%{version}/*
%{package_libdir}/cmake/boost_headers-%{version}/*
%{package_includedir}/boost/*

%files -n boost-license%{library_version}
%license LICENSE_1_0.txt
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120200 && !0%{?is_opensuse}
%attr(755,root,root) %dir %{_defaultlicensedir}
%endif

%endif
%endif

%changelog
