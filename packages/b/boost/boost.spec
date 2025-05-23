#
# spec file for package boost
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


#
%global flavor @BUILD_FLAVOR@%{nil}

%define ver 1.88.0
%define _ver 1_88_0
%define file_version %_ver
%define lib_appendix %_ver
%define docs_version 1.56.0
%define short_version 1_56
%define pname boost
%bcond_with    build_docs
%bcond_without package_pdf
%bcond_without build_quickbook
%bcond_with    boost_devel
%bcond_with ringdisabled

%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif

%define package_name boost%{library_version}
%define my_docdir %{_docdir}/boost%{library_version}

# We can't have these inside the "@BUILD_FLAVOR@" because then quilt
# can't understand the spec file. If only @BUILD_FLAVOR@ was a normal macro....
%define build_base 1
%define name_suffix %{nil}

%if "%{flavor}" == "%nil"
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "base"
%define build_base 1
%define name_suffix -base
%bcond_with python3
%bcond_with mpi
%endif

%if "%{flavor}" == "extra"
%define build_base 0
%define name_suffix -extra
%bcond_without python3
%ifnarch %{arm} %ix86
# OpenMPI 5 has no support for 32bit architectures
%bcond_without mpi
%endif
%endif

%define base_name boost%{?name_suffix}

Name:           %{base_name}
Version:        1.88.0
Release:        0
%define library_version 1_88_0
Summary:        Boost C++ Libraries
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://www.boost.org
Source0:        https://archives.boost.io/release/%{version}/source/boost_%{_ver}.tar.bz2
Source1:        boost-rpmlintrc
Source3:        https://downloads.sourceforge.net/project/boost/boost-docs/1.56.0/boost_1_56_pdf.tar.bz2
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
Patch15:        boost-1.57.0-python-abi_letters.patch
Patch16:        boost-1.55.0-python-test-PyImport_AppendInittab.patch
Patch17:        python_mpi.patch
Patch18:        dynamic_linking.patch
Patch20:        python_library_name.patch
Patch21:        boost-remove-cmakedir.patch
Patch25:        boost-no-exception.patch
%{?suse_build_hwcaps_libs}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libbz2-devel
BuildRequires:  libexpat-devel
BuildRequires:  libicu-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(zlib)
%if ! %{build_base}
BuildRequires:  dos2unix
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
%endif
%if %{with build_docs}
BuildRequires:  docbook
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt-tools
BuildRequires:  texlive-latex
%endif
%endif
%if %{with mpi}
BuildRequires:  openmpi-macros-devel
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
Conflicts:      libboost_headers1_66_0-devel
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
Requires:       libboost_url%{library_version}-devel
Requires:       libboost_wave%{library_version}-devel
Requires:       libstdc++-devel
Conflicts:      boost-devel-impl
Provides:       boost-devel-impl = %{version}
Requires:       libboost_context%{library_version}-devel
Requires:       libboost_coroutine%{library_version}-devel
Requires:       libboost_fiber%{library_version}-devel
%if %{with mpi}
Requires:       libboost_graph_parallel%{library_version}-devel
Requires:       libboost_mpi%{library_version}-devel
%endif
%if %{with python3}
Requires:       libboost_python-py3-%{library_version}-devel
%endif

%description -n %{package_name}-devel
This package contains all that is needed to develop/compile
applications that use the Boost C++ libraries. For documentation see
the documentation packages (html, man or pdf).

%package     -n %{package_name}-python3
Summary:        Boost.MPI Python 3.x serialization library
Group:          System/Libraries
Requires:       %{package_name}

%description -n %{package_name}-python3
This package contains the Boost.MPI Python 3.x serialization
interface.

%package     -n boost%{library_version}-jam
Summary:        A Boost Make Replacement
Group:          Development/Tools/Building
Conflicts:      boost_1_66-jam
Obsoletes:      boost-jam-impl < %{version}
Obsoletes:      boost_1_66-jam
Provides:       boost_1_66-jam = %{version}
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
Conflicts:      libboost_atomic1_66_0-devel
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
Conflicts:      libboost_container1_66_0-devel
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
Conflicts:      libboost_context1_66_0-devel
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
Conflicts:      libboost_contract1_66_0-devel
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
Conflicts:      libboost_coroutine1_66_0-devel
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
Conflicts:      libboost_date_time1_66_0-devel
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
Conflicts:      libboost_fiber1_66_0-devel
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
Requires:       libboost_atomic%{library_version}-devel = %{version}
Requires:       libboost_filesystem%{library_version} = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_system%{library_version}-devel = %{version}
Requires:       libstdc++-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_filesystem-devel-impl
Conflicts:      libboost_filesystem1_66_0-devel
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
Conflicts:      libboost_graph1_66_0-devel
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
Requires:       libboost_random%{library_version}-devel = %{version}
Requires:       libboost_regex%{library_version}-devel = %{version}
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(libzstd)
Requires:       pkgconfig(zlib)
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_iostreams-devel-impl
Conflicts:      libboost_iostreams1_66_0-devel
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
Requires:       libboost_random%{library_version}-devel = %{version}
Requires:       libboost_regex%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_log-devel-impl
Conflicts:      libboost_log1_66_0-devel
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
Conflicts:      libboost_math1_66_0-devel
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
Conflicts:      libboost_mpi1_66_0-devel
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
Conflicts:      libboost_graph_parallel1_66_0-devel
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
Conflicts:      boost-nowide-devel-impl
Provides:       boost-nowide-devel-impl = %{version}
Requires:       libboost_nowide%{library_version} = %{version}

%description -n libboost_nowide%{library_version}-devel
Development headers for Boost.Nowide* boost libraries.

%package     -n libboost_mpi_python-py3-%{library_version}
Summary:        Boost.MPI Python 3.x serialization library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_mpi_python-py3-%{library_version}
This package contains the Boost.MPI Python 3.x serialization
interface.

%package     -n libboost_mpi_python-py3-%{library_version}-devel
Summary:        Development library for Boost.MPI Python 3.x serialization
Group:          Development/Libraries/C and C++
Requires:       libboost_mpi%{library_version}-devel = %{version}
Requires:       libboost_mpi_python-py3-%{library_version} = %{version}
Requires:       libboost_python-py3-%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_mpi_python-py3-1_66_0-devel
Conflicts:      libboost_mpi_python3-devel-impl
Provides:       libboost_mpi_python3-devel-impl = %{version}

%description -n libboost_mpi_python-py3-%{library_version}-devel
This package contains the Boost.MPI development library for Python 3.x
serialization interface

%package     -n python3-boost_parallel_mpi%{library_version}
Summary:        Python 3.x bindings for Boost.Parallel.MPI library
Group:          Development/Languages/Python
Conflicts:      python3-boost_parallel_mpi-impl
Conflicts:      python3-boost_parallel_mpi1_66_0
Provides:       python3-boost_parallel_mpi-impl = %{version}

%description -n python3-boost_parallel_mpi%{library_version}
This package contains the Boost.Parallel.MPI bindings for Python 3.x

%package    -n libboost_test%{library_version}
Summary:        Boost.Test runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_test%{library_version}
This package contains the Boost.Test runtime library.

%package     -n libboost_test%{library_version}-devel
Summary:        Development headers for Boost.Test library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_test%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_test-devel-impl
Conflicts:      libboost_test1_66_0-devel
Provides:       libboost_test-devel-impl = %{version}

%description -n libboost_test%{library_version}-devel
Development headers for Boost.Test library. Boost.Test supports for
simple program testing, full unit testing, and for program execution
monitoring.

%package     -n libboost_process%{library_version}
Summary:        Boost.Process runtime library
Group:          System/Libraries/C and C++
Requires:       boost-license%{library_version}

%description -n libboost_process%{library_version}
This package contains the Boost.Process runtime library.

%package     -n libboost_process%{library_version}-devel
Summary:        Development headers for Boost.Process library
Group:          Development/Libraries/C and C++
Requires:       libboost_context%{library_version}-devel = %{version}
Requires:       libboost_date_time%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_process%{library_version} = %{version}
Conflicts:      boost-devel < 1.88
Conflicts:      libboost_process-devel-impl
Provides:       libboost_process-devel-impl = %{version}

%description -n libboost_process%{library_version}-devel
This package contains development headers for Boost.Process
library.

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
Conflicts:      libboost_program_options1_66_0-devel
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
Requires:       libboost_container%{library_version}-devel = %{version}
Requires:       libboost_graph%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_python-py3-%{library_version} = %{version}
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_python-py3-1_66_0-devel
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
Conflicts:      libboost_numpy-py3-1_66_0-devel
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
Conflicts:      libboost_serialization1_66_0-devel
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
Conflicts:      libboost_stacktrace1_66_0-devel
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
Conflicts:      libboost_system1_66_0-devel
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
Conflicts:      libboost_thread1_66_0-devel
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
Conflicts:      libboost_wave1_66_0-devel
Provides:       libboost_wave-devel-impl = %{version}

%description -n libboost_wave%{library_version}-devel
This package contains development headers for Boost.Wave library.

%package     -n libboost_url%{library_version}
Summary:        Boost.URL runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_url%{library_version}
This package contains the Boost::URL runtime library.

%package     -n libboost_url%{library_version}-devel
Summary:        Development headers for Boost.URL library
Group:          Development/Libraries/C and C++
Provides:       libboost_url-devel-impl = %{version}

%description -n libboost_url%{library_version}-devel
This package contains development headers for Boost.URL library.

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
Requires:       libicu-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_regex-devel-impl
Conflicts:      libboost_regex1_66_0-devel
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
Conflicts:      libboost_random1_66_0-devel
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
Conflicts:      libboost_chrono1_66_0-devel
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
Requires:       libboost_charconv%{library_version}-devel = %{version}
Requires:       libboost_chrono%{library_version}-devel = %{version}
Requires:       libboost_headers%{library_version}-devel = %{version}
Requires:       libboost_locale%{library_version} = %{version}
Requires:       libboost_system%{library_version}-devel = %{version}
Requires:       libboost_thread%{library_version}-devel = %{version}
Requires:       libicu-devel
Conflicts:      boost-devel < 1.63
Conflicts:      libboost_locale-devel-impl
Conflicts:      libboost_locale1_66_0-devel
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
Conflicts:      libboost_timer1_66_0-devel
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
Conflicts:      libboost_type_erasure1_66_0-devel
Provides:       libboost_type_erasure-devel-impl = %{version}

%description -n libboost_type_erasure%{library_version}-devel
This package contains development headers for Boost.TypeErasure library.

%package     -n libboost_json%{library_version}
Summary:        Boost.JSON runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_json%{library_version}
This package contains Boost::JSON runtime library.

%package     -n libboost_json%{library_version}-devel
Summary:        Development headers for Boost.JSON library
Group:          Development/Libraries/C and C++
Requires:       libboost_container%{library_version}-devel = %{version}
Requires:       libboost_json%{library_version} = %{version}
Conflicts:      libboost_json-devel-impl
Provides:       libboost_json-devel-impl = %{version}

%description -n libboost_json%{library_version}-devel
This package contains development headers for Boost.JSON library.

%package     -n libboost_charconv%{library_version}
Summary:        Boost.CharConv runtime library
Group:          System/Libraries
Requires:       boost-license%{library_version}

%description -n libboost_charconv%{library_version}
This package contains Boost::CharConv runtime library.

%package     -n libboost_charconv%{library_version}-devel
Summary:        Development headers for Boost.CharConv library
Group:          Development/Libraries/C and C++
Requires:       libboost_charconv%{library_version} = %{version}
Requires:       libboost_container%{library_version}-devel = %{version}
Conflicts:      libboost_charconv-devel-impl
Provides:       libboost_charconv-devel-impl = %{version}

%description -n libboost_charconv%{library_version}-devel
This package contains development headers for Boost.CharConv library.

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

%prep
%setup -q -n boost_%{library_version} -b 3
#everything in the tarball has the executable flag set ...
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +
%patch -P 1 -p1
%patch -P 2
%patch -P 4
%patch -P 5
%patch -P 6 -p1
%patch -P 7
%patch -P 9 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 25

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
%setup_openmpi
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
    --prefix=%{_prefix} --exec-prefix=%{_bindir} \
    --libdir=%{_libdir} --includedir=%{_includedir} \
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
    --debug-configuration \
    boost.stacktrace.from_exception=off \
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
    --debug-configuration \
    boost.stacktrace.from_exception=off \
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
%if %{with build_quickbook}
pushd tools/quickbook
../../b2 --debug-configuration --user-config=../../user-config.jam --v2 dist-bin %{?_smp_mflags}
popd
%endif

%if %{with build_docs}
cd doc
./b2 --debug-configuration --user-config=../user-config.jam --v2 man %{?_smp_mflags}
%endif

%endif

%install

# Read shared build instructions
. ./.build

%if ! %{build_base}

%if %{with mpi}
# Set PATH, MANPATH and LD_LIBRARY_PATH for mpi
%setup_openmpi
%endif

%if %{with python3}
./b2 -d+2 -q --user-config=./user-config-py3.jam \
    --debug-configuration \
    boost.stacktrace.from_exception=off \
    --build-type=minimal --build-dir=./python3-build \
    --python-buildid=py3 \
    --prefix=%{buildroot}%{_prefix} --exec-prefix=%{buildroot}%{_bindir} \
    --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir} \
    --stagedir=./python3-stage %{?_smp_mflags} \
    $PY_LIBRARIES_FLAGS \
    threading=multi link=shared runtime-link=shared install
%endif

%endif

# Generic install
./b2 -d+2 -q \
     --debug-configuration \
     boost.stacktrace.from_exception=off \
     --build-type=minimal --build-dir=./build --stagedir=./stage \
     --prefix=%{buildroot}%{_prefix} --exec-prefix=%{buildroot}%{_bindir} \
     --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir} \
     --user-config=./user-config.jam \
     $LIBRARIES_FLAGS \
     threading=multi link=shared runtime-link=shared install

# No python dependencies in the main tree

! $(ldd %{buildroot}%{_libdir}/*.so* | grep python\\.)

%if ! %{build_base}

%if %{with python3}
! $(ldd %{buildroot}%{_libdir}/*.so* | grep python3-\\.)
ln -s libboost_python-py3.so %{buildroot}%{_libdir}/libboost_python3.so
%endif

%if %{with python3} && %{with mpi}
mkdir -p %{buildroot}%{python3_sitearch}/boost/parallel/mpi/
install -m 0644 libs/mpi/build/__init__.py %{buildroot}%{python3_sitearch}/boost/parallel/mpi/
install -m 0644 %{SOURCE11} %{buildroot}%{python3_sitearch}/boost/parallel
install -m 0644 %{SOURCE11} %{buildroot}%{python3_sitearch}/boost
# Boost 1.87 packages a python cmake file in both the mpi-python dir and the mpi directory.
# It should not be in that second one
rm -f %{buildroot}%{_libdir}/cmake/boost_mpi-%{version}/libboost_mpi-variant-shared-py3*.cmake
mv %{buildroot}%{_libdir}/boost-python3.*/mpi.%{py3_soflags}.so %{buildroot}%{python3_sitearch}/mpi.%{py3_soflags}.so
rmdir %{buildroot}%{_libdir}/boost-python3.*
%endif

#install doc files
mkdir -p %{buildroot}%{my_docdir}
%if %{with boost_devel}
install -m 0644 %{SOURCE102} %{buildroot}%{my_docdir}
%endif
find libs/ -name \*.htm\* -o -name \*.css -o -name \*.js | xargs dos2unix
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar --files-from=%{SOURCE4} -cf - --files-from=- | tar -C %{buildroot}%{my_docdir} -xf -
rm -rf %{buildroot}%{my_docdir}/boost
#ln -s %%{_includedir}/boost %%{buildroot}%%{my_docdir}
#ln -s ../LICENSE_1_0.txt %%{buildroot}%%{my_docdir}/libs
find %{buildroot}%{my_docdir} -name \*.py -exec chmod -x {} +
chmod -x ../boost_1_56_pdf/*.pdf

%if %{with build_quickbook}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 dist/bin/quickbook %{buildroot}%{_bindir}/quickbook
%endif
%endif

%if %{build_base}

mkdir -p %{buildroot}%{_bindir}
install -m 755 b2 %{buildroot}%{_bindir}/bjam
ln -s bjam %{buildroot}%{_bindir}/jam

# install boost-build jam files
mkdir -p %{buildroot}%{_datadir}/boost-build/
cp -r tools/build/src/* %{buildroot}%{_datadir}/boost-build/
rm -r %{buildroot}%{_datadir}/boost-build/engine
find %{buildroot}%{_datadir}/boost-build/ -type f \! -name \*.py \! -name \*.jam -delete
find %{buildroot}%{_datadir}/boost-build/ -type f -exec chmod 644 {} +

rm -r %{buildroot}%{_datadir}/boost_predef

# Remove exception library, but only if the symbols are not
# actually used. For now, the only symbol that is linked is
# should never be used as it's only available on Windows. So,
# verify that here.
objdump -Ctj .text -Ctj .text %{buildroot}%{_libdir}/libboost_exception.so | \
  grep '^[0-9a-f]\+[[:space:]]\+g[[:space:]]\+F' | \
  sed -e 's#[0-9a-f]\+[[:space:]]\+g[[:space:]]\+F[[:space:]]\+\.text[[:space:]]\+[0-9a-f]\+[[:space:]]\+##' | \
  diff %{SOURCE10} - || echo "WARNING: libexception symbol change?"
rm %{buildroot}%{_libdir}/libboost_exception.so
rm %{buildroot}%{_libdir}/libboost_exception.so.%{version}

# not used or duplicated in boost-extra flavour
rm -r %{buildroot}%{_libdir}/cmake/boost_exception-*
rm -r %{buildroot}%{_libdir}/cmake/boost_graph_parallel-%{version}

%fdupes %{buildroot}%{_includedir}/boost
mkdir -p %{buildroot}%{my_docdir}
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120200 && !0%{?is_opensuse}
mkdir -p %{buildroot}%{_defaultlicensedir}
%endif
%else
# duplicate from boost-base flavour
rm %{buildroot}%{_libdir}/cmake/BoostDetectToolset-%{version}.cmake
rm -r %{buildroot}%{_libdir}/cmake/Boost-%{version}
rm -r %{buildroot}%{_libdir}/cmake/boost_headers-%{version}
rm -rf %{buildroot}%{_libdir}/cmake/boost_{w,}serialization-%{version}
rm -r %{buildroot}%{_libdir}/cmake/boost_container-%{version}
rm -f %{buildroot}%{_libdir}/libboost_container.so*
rm -r %{buildroot}%{_libdir}/cmake/boost_graph-%{version}
rm -f %{buildroot}%{_libdir}/libboost_graph.so*
# If no library was needed to be built, system was built to avoid building everything.
# If needs to be removed from the extra package in that case
rm -Rf %{buildroot}%{_libdir}/cmake/boost_system-%{version}
rm -Rf %{buildroot}%{_libdir}/libboost_system.so*

rm -r %{buildroot}%{_includedir}/boost
rm -f %{buildroot}%{_libdir}/libboost_{w,}serialization*
rmdir --ignore-fail-on-non-empty %{buildroot}%{_libdir}
%fdupes %{buildroot}%{my_docdir}
%endif

%if %{build_base}
%ldconfig_scriptlets -n libboost_atomic%{library_version}
%ldconfig_scriptlets -n libboost_container%{library_version}
%ldconfig_scriptlets -n libboost_context%{library_version}
%ldconfig_scriptlets -n libboost_contract%{library_version}
%ldconfig_scriptlets -n libboost_coroutine%{library_version}
%ldconfig_scriptlets -n libboost_date_time%{library_version}
%ldconfig_scriptlets -n libboost_fiber%{library_version}
%ldconfig_scriptlets -n libboost_filesystem%{library_version}
%ldconfig_scriptlets -n libboost_iostreams%{library_version}
%ldconfig_scriptlets -n libboost_log%{library_version}
%ldconfig_scriptlets -n libboost_test%{library_version}
%ldconfig_scriptlets -n libboost_process%{library_version}
%ldconfig_scriptlets -n libboost_program_options%{library_version}
%ldconfig_scriptlets -n libboost_regex%{library_version}
%ldconfig_scriptlets -n libboost_serialization%{library_version}
%ldconfig_scriptlets -n libboost_thread%{library_version}
%ldconfig_scriptlets -n libboost_type_erasure%{library_version}
%ldconfig_scriptlets -n libboost_json%{library_version}
%ldconfig_scriptlets -n libboost_charconv%{library_version}
%ldconfig_scriptlets -n libboost_math%{library_version}
%ldconfig_scriptlets -n libboost_nowide%{library_version}
%ldconfig_scriptlets -n libboost_graph%{library_version}
%ldconfig_scriptlets -n libboost_stacktrace%{library_version}
%ldconfig_scriptlets -n libboost_system%{library_version}
%ldconfig_scriptlets -n libboost_wave%{library_version}
%ldconfig_scriptlets -n libboost_url%{library_version}
%ldconfig_scriptlets -n libboost_random%{library_version}
%ldconfig_scriptlets -n libboost_chrono%{library_version}
%ldconfig_scriptlets -n libboost_locale%{library_version}
%ldconfig_scriptlets -n libboost_timer%{library_version}
%else

%if %{with python3}
%ldconfig_scriptlets -n libboost_python-py3-%{library_version}
%ldconfig_scriptlets -n libboost_numpy-py3-%{library_version}
%endif

%if %{with mpi}
%ldconfig_scriptlets -n libboost_mpi%{library_version}
%ldconfig_scriptlets -n libboost_graph_parallel%{library_version}

%if %{with python3}
%ldconfig_scriptlets -n libboost_mpi_python-py3-%{library_version}
%endif
%endif

%endif

%if %{build_base}
%files -n boost%{library_version}-jam
%{_bindir}/bjam
%{_bindir}/jam
%dir %{_datadir}/boost-build
%{_datadir}/boost-build/*

%files -n libboost_atomic%{library_version}
%{_libdir}/libboost_atomic.so.%{version}

%files -n libboost_atomic%{library_version}-devel
%dir %{_libdir}/cmake/boost_atomic-%{version}
%{_libdir}/cmake/boost_atomic-%{version}/*
%{_libdir}/libboost_atomic.so

%files -n libboost_container%{library_version}
%{_libdir}/libboost_container.so.%{version}

%files -n libboost_container%{library_version}-devel
%dir %{_libdir}/cmake/boost_container-%{version}
%{_libdir}/cmake/boost_container-%{version}/*
%{_libdir}/libboost_container.so

%files -n libboost_context%{library_version}
%{_libdir}/libboost_context.so.%{version}

%files -n libboost_context%{library_version}-devel
%dir %{_libdir}/cmake/boost_context-%{version}
%{_libdir}/cmake/boost_context-%{version}/*
%{_libdir}/libboost_context.so

%files -n libboost_coroutine%{library_version}
%{_libdir}/libboost_coroutine.so.%{version}

%files -n libboost_coroutine%{library_version}-devel
%dir %{_libdir}/cmake/boost_coroutine-%{version}
%{_libdir}/cmake/boost_coroutine-%{version}/*
%{_libdir}/libboost_coroutine.so

%files -n libboost_contract%{library_version}
%{_libdir}/libboost_contract.so.%{version}

%files -n libboost_contract%{library_version}-devel
%dir %{_libdir}/cmake/boost_contract-%{version}
%{_libdir}/cmake/boost_contract-%{version}/*
%{_libdir}/libboost_contract.so

%files -n libboost_date_time%{library_version}
%{_libdir}/libboost_date_time.so.%{version}

%files -n libboost_date_time%{library_version}-devel
%dir %{_libdir}/cmake/boost_date_time-%{version}
%{_libdir}/cmake/boost_date_time-%{version}/*
%{_libdir}/libboost_date_time.so

%files -n libboost_fiber%{library_version}
%{_libdir}/libboost_fiber.so.%{version}

%files -n libboost_fiber%{library_version}-devel
%dir %{_libdir}/cmake/boost_fiber-%{version}
%{_libdir}/cmake/boost_fiber-%{version}/*
%{_libdir}/libboost_fiber.so

%files -n libboost_filesystem%{library_version}
%{_libdir}/libboost_filesystem.so.%{version}

%files -n libboost_filesystem%{library_version}-devel
%dir %{_libdir}/cmake/boost_filesystem-%{version}
%{_libdir}/cmake/boost_filesystem-%{version}/*
%{_libdir}/libboost_filesystem.so

%files -n libboost_graph%{library_version}
%{_libdir}/libboost_graph.so.%{version}

%files -n libboost_graph%{library_version}-devel
%dir %{_libdir}/cmake/boost_graph-%{version}
%{_libdir}/cmake/boost_graph-%{version}/*
%{_libdir}/libboost_graph.so

%files -n libboost_iostreams%{library_version}
%{_libdir}/libboost_iostreams.so.%{version}

%files -n libboost_iostreams%{library_version}-devel
%dir %{_libdir}/cmake/boost_iostreams-%{version}
%{_libdir}/cmake/boost_iostreams-%{version}/*
%{_libdir}/libboost_iostreams.so

%files -n libboost_log%{library_version}
%{_libdir}/libboost_log.so.%{version}
%{_libdir}/libboost_log_setup.so.%{version}

%files -n libboost_log%{library_version}-devel
%dir %{_libdir}/cmake/boost_log-%{version}
%dir %{_libdir}/cmake/boost_log_setup-%{version}
%{_libdir}/cmake/boost_log-%{version}/*
%{_libdir}/cmake/boost_log_setup-%{version}/*
%{_libdir}/libboost_log.so
%{_libdir}/libboost_log_setup.so

%files -n libboost_math%{library_version}
%{_libdir}/libboost_math_c99f.so.%{version}
%{_libdir}/libboost_math_c99.so.%{version}
%{_libdir}/libboost_math_tr1f.so.%{version}
%{_libdir}/libboost_math_tr1.so.%{version}
%ifnarch ppc ppc64
%{_libdir}/libboost_math_c99l.so.%{version}
%{_libdir}/libboost_math_tr1l.so.%{version}
%endif

%files -n libboost_math%{library_version}-devel
%dir %{_libdir}/cmake/boost_math-%{version}
%dir %{_libdir}/cmake/boost_math_c99*-%{version}
%dir %{_libdir}/cmake/boost_math_tr1*-%{version}
%{_libdir}/cmake/boost_math-%{version}/*
%{_libdir}/cmake/boost_math_c99*-%{version}/*
%{_libdir}/cmake/boost_math_tr1*-%{version}/*
%{_libdir}/libboost_math_c99f.so
%{_libdir}/libboost_math_c99.so
%{_libdir}/libboost_math_tr1f.so
%{_libdir}/libboost_math_tr1.so
%ifnarch ppc ppc64
%{_libdir}/libboost_math_c99l.so
%{_libdir}/libboost_math_tr1l.so
%endif

%files -n libboost_nowide%{library_version}
%{_libdir}/libboost_nowide.so.%{version}

%files -n libboost_nowide%{library_version}-devel
%dir %{_libdir}/cmake/boost_nowide-%{version}
%{_libdir}/cmake/boost_nowide-%{version}/boost_nowide-config.cmake
%{_libdir}/cmake/boost_nowide-%{version}/boost_nowide-config-version.cmake
%{_libdir}/cmake/boost_nowide-%{version}/libboost_nowide-variant-shared.cmake
%{_libdir}/libboost_nowide.so

%files -n libboost_test%{library_version}
%{_libdir}/libboost_prg_exec_monitor.so.%{version}
%{_libdir}/libboost_test_exec_monitor.so.%{version}
%{_libdir}/libboost_unit_test_framework.so.%{version}

%files -n libboost_test%{library_version}-devel
%dir %{_libdir}/cmake/boost_prg_exec_monitor-%{version}
%dir %{_libdir}/cmake/boost_test_exec_monitor-%{version}
%dir %{_libdir}/cmake/boost_unit_test_framework-%{version}
%{_libdir}/cmake/boost_prg_exec_monitor-%{version}/*
%{_libdir}/cmake/boost_test_exec_monitor-%{version}/*
%{_libdir}/cmake/boost_unit_test_framework-%{version}/*
%{_libdir}/libboost_prg_exec_monitor.so
%{_libdir}/libboost_test_exec_monitor.so
%{_libdir}/libboost_unit_test_framework.so

%files -n libboost_process%{library_version}
%{_libdir}/libboost_process.so.%{version}

%files -n libboost_process%{library_version}-devel
%dir %{_libdir}/cmake/boost_process-%{version}
%{_libdir}/cmake/boost_process-%{version}/*
%{_libdir}/libboost_process.so

%files -n libboost_program_options%{library_version}
%{_libdir}/libboost_program_options.so.%{version}

%files -n libboost_program_options%{library_version}-devel
%dir %{_libdir}/cmake/boost_program_options-%{version}
%{_libdir}/cmake/boost_program_options-%{version}/*
%{_libdir}/libboost_program_options.so
%endif

%if ! %{build_base}

%if %{with mpi}
%files -n libboost_mpi%{library_version}
%{_libdir}/libboost_mpi.so.1*

%files -n libboost_mpi%{library_version}-devel
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/boost_mpi-%{version}
%{_libdir}/cmake/boost_mpi-%{version}/*
%{_libdir}/libboost_mpi.so

%files -n libboost_graph_parallel%{library_version}
%{_libdir}/libboost_graph_parallel.so.1*

%files -n libboost_graph_parallel%{library_version}-devel
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/boost_graph_parallel-%{version}
%{_libdir}/cmake/boost_graph_parallel-%{version}/*
%{_libdir}/libboost_graph_parallel.so

%if %{with python3}
%files -n libboost_mpi_python-py3-%{library_version}
%{_libdir}/libboost_mpi_python-py3.so.%{version}

%files -n libboost_mpi_python-py3-%{library_version}-devel
%dir %{_libdir}/cmake/boost_mpi_python-%{version}
%{_libdir}/cmake/boost_mpi_python-%{version}/*
%endif
%{_libdir}/libboost_mpi_python-py3.so

%files -n python3-boost_parallel_mpi%{library_version}
%dir %{python3_sitearch}/boost
%dir %{python3_sitearch}/boost/parallel
%dir %{python3_sitearch}/boost/parallel/mpi
%{python3_sitearch}/boost/__init__.py
%{python3_sitearch}/boost/parallel/__init__.py
%{python3_sitearch}/boost/parallel/mpi/__init__.py
%{python3_sitearch}/mpi.%{py3_soflags}.so
%endif

%if %{with python3}
%files -n libboost_python-py3-%{library_version}
%{_libdir}/libboost_python-py3.so.1*

%files -n libboost_python-py3-%{library_version}-devel
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/boost_python-%{version}
%{_libdir}/cmake/boost_python-%{version}/*
%{_libdir}/libboost_python3.so
%{_libdir}/libboost_python-py3.so

%files -n libboost_numpy-py3-%{library_version}
%{_libdir}/libboost_numpy-py3.so.1*

%files -n libboost_numpy-py3-%{library_version}-devel
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/boost_numpy-%{version}
%{_libdir}/cmake/boost_numpy-%{version}/*
%{_libdir}/libboost_numpy-py3.so

%endif
%endif

%if %{build_base}
%files -n libboost_serialization%{library_version}
%{_libdir}/libboost_serialization.so.%{version}
%{_libdir}/libboost_wserialization.so.%{version}

%files -n libboost_serialization%{library_version}-devel
%dir %{_libdir}/cmake/boost_serialization-%{version}
%dir %{_libdir}/cmake/boost_wserialization-%{version}
%{_libdir}/cmake/boost_serialization-%{version}/*
%{_libdir}/cmake/boost_wserialization-%{version}/*
%{_libdir}/libboost_serialization.so
%{_libdir}/libboost_wserialization.so

%files -n libboost_stacktrace%{library_version}
%{_libdir}/libboost_stacktrace_addr2line.so.%{version}
%{_libdir}/libboost_stacktrace_basic.so.%{version}
%{_libdir}/libboost_stacktrace_noop.so.%{version}

%files -n libboost_stacktrace%{library_version}-devel
%dir %{_libdir}/cmake/boost_stacktrace_addr2line-%{version}
%dir %{_libdir}/cmake/boost_stacktrace_basic-%{version}
%dir %{_libdir}/cmake/boost_stacktrace_noop-%{version}
%{_libdir}/cmake/boost_stacktrace_addr2line-%{version}/*
%{_libdir}/cmake/boost_stacktrace_basic-%{version}/*
%{_libdir}/cmake/boost_stacktrace_noop-%{version}/*
%{_libdir}/libboost_stacktrace_addr2line.so
%{_libdir}/libboost_stacktrace_basic.so
%{_libdir}/libboost_stacktrace_noop.so

%files -n libboost_system%{library_version}
%{_libdir}/libboost_system.so.%{version}

%files -n libboost_system%{library_version}-devel
%dir %{_libdir}/cmake/boost_system-%{version}
%{_libdir}/cmake/boost_system-%{version}/*
%{_libdir}/libboost_system.so

%files -n libboost_thread%{library_version}
%{_libdir}/libboost_thread.so.%{version}

%files -n libboost_thread%{library_version}-devel
%dir %{_libdir}/cmake/boost_thread-%{version}
%{_libdir}/cmake/boost_thread-%{version}/*
%{_libdir}/libboost_thread.so

%files -n libboost_wave%{library_version}
%{_libdir}/libboost_wave.so.%{version}

%files -n libboost_wave%{library_version}-devel
%dir %{_libdir}/cmake/boost_wave-%{version}
%{_libdir}/cmake/boost_wave-%{version}/*
%{_libdir}/libboost_wave.so

%files -n libboost_url%{library_version}
%{_libdir}/libboost_url.so.%{version}

%files -n libboost_url%{library_version}-devel
%dir %{_libdir}/cmake/boost_url-%{version}
%{_libdir}/cmake/boost_url-%{version}/*
%{_libdir}/libboost_url.so

%files -n libboost_regex%{library_version}
%{_libdir}/libboost_regex.so.%{version}

%files -n libboost_regex%{library_version}-devel
%dir %{_libdir}/cmake/boost_regex-%{version}
%{_libdir}/cmake/boost_regex-%{version}/*
%{_libdir}/libboost_regex.so

%files -n libboost_random%{library_version}
%{_libdir}/libboost_random.so.%{version}

%files -n libboost_random%{library_version}-devel
%dir %{_libdir}/cmake/boost_random-%{version}
%{_libdir}/cmake/boost_random-%{version}/*
%{_libdir}/libboost_random.so

%files -n libboost_chrono%{library_version}
%{_libdir}/libboost_chrono.so.%{version}

%files -n libboost_chrono%{library_version}-devel
%dir %{_libdir}/cmake/boost_chrono-%{version}
%{_libdir}/cmake/boost_chrono-%{version}/*
%{_libdir}/libboost_chrono.so

%files -n libboost_locale%{library_version}
%{_libdir}/libboost_locale.so.%{version}

%files -n libboost_locale%{library_version}-devel
%dir %{_libdir}/cmake/boost_locale-%{version}
%{_libdir}/cmake/boost_locale-%{version}/*
%{_libdir}/libboost_locale.so

%files -n libboost_timer%{library_version}
%{_libdir}/libboost_timer.so.%{version}

%files -n libboost_timer%{library_version}-devel
%dir %{_libdir}/cmake/boost_timer-%{version}
%{_libdir}/cmake/boost_timer-%{version}/*
%{_libdir}/libboost_timer.so

%files -n libboost_type_erasure%{library_version}
%{_libdir}/libboost_type_erasure.so.%{version}

%files -n libboost_type_erasure%{library_version}-devel
%dir %{_libdir}/cmake/boost_type_erasure-%{version}
%{_libdir}/cmake/boost_type_erasure-%{version}/*
%{_libdir}/libboost_type_erasure.so

%files -n libboost_json%{library_version}
%{_libdir}/libboost_json.so.%{version}

%files -n libboost_json%{library_version}-devel
%dir %{_libdir}/cmake/boost_json-%{version}
%{_libdir}/cmake/boost_json-%{version}/*
%{_libdir}/libboost_json.so

%files -n libboost_charconv%{library_version}
%{_libdir}/libboost_charconv.so.%{version}

%files -n libboost_charconv%{library_version}-devel
%dir %{_libdir}/cmake/boost_charconv-%{version}
%{_libdir}/cmake/boost_charconv-%{version}/*
%{_libdir}/libboost_charconv.so

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
%{_bindir}/quickbook
%endif
%endif

%if %{build_base}
%files -n libboost_headers%{library_version}-devel
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/Boost-%{version}
%dir %{_libdir}/cmake/boost_headers-%{version}
%dir %{_includedir}/boost
%{_libdir}/cmake/BoostDetectToolset-%{version}.cmake
%{_libdir}/cmake/Boost-%{version}/*
%{_libdir}/cmake/boost_headers-%{version}/*
%{_includedir}/boost/*

%files -n boost-license%{library_version}
%license LICENSE_1_0.txt
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} <= 120200 && !0%{?is_opensuse}
%attr(755,root,root) %dir %{_defaultlicensedir}
%endif

%endif

%changelog
