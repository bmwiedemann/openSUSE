#
# spec file for package boost-defaults
#
# Copyright (c) 2022 SUSE LLC
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


%define boost_version 1_81_0
Name:           boost-defaults
Version:        1.81.0
Release:        0
Summary:        Default Boost C++ Libraries
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://www.boost.org
Source1:        README
BuildArch:      noarch

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

%package     -n boost-devel
Summary:        Development headers for Boost
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{boost_version}-devel

%description -n boost-devel
Default version of Boost headers

%package     -n boost-jam
Summary:        A Boost Make Replacement
Group:          Development/Tools/Building
Requires:       boost%{boost_version}-jam

%description -n boost-jam
Boost Jam is a build tool based on FTJam, which in turn is based on
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System.

This package installs the default version of Boost Jam.

%package     -n libboost_headers-devel
Summary:        Development headers for Boost
Group:          Development/Libraries/C and C++
Requires:       libboost_headers%{boost_version}-devel

%description -n libboost_headers-devel
A collection of header-only libraries for Boost. This package
installs the dafault version.

%package     -n libboost_atomic-devel
Summary:        Development headers for Boost.Atomic
Group:          Development/Libraries/C and C++
Requires:       libboost_atomic%{boost_version}-devel

%description -n libboost_atomic-devel
Development support for Boost.Atomic, a library that provides atomic
data types and operations on these data types, as well as memory
ordering constraints required for coordinating multiple threads through
atomic variables.

%package     -n libboost_container-devel
Summary:        Development headers for Boost.Container
Group:          Development/Libraries/C and C++
Requires:       libboost_container%{boost_version}-devel

%description -n libboost_container-devel
Development header files and libraries for Boost.Container.
Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offers advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that don't comply with the latest
C++ standard.

This package installs the default Boost version of the library.

%package     -n libboost_context-devel
Summary:        Development headers for Boost.Context
Group:          Development/Libraries/C and C++
Requires:       libboost_context%{boost_version}-devel

%description -n libboost_context-devel
Development headers and libraries for Boost.Context, a library that
providing cooperative multitasking support.

This package installs the default Boost version of the library.

%package     -n libboost_contract-devel
Summary:        Development headers for Boost.Contract
Group:          Development/Libraries/C and C++
Requires:       libboost_contract%{boost_version}-devel

%description -n libboost_contract-devel
Development headers and libraries for Boost.Contract, a library
that implements Design by Contract or DbC or contract programming.

This package installs the default Boost version of the library.

%package     -n libboost_coroutine-devel
Summary:        Development headers for Boost.Coroutine
Group:          Development/Libraries/C and C++
Requires:       libboost_coroutine%{boost_version}-devel

%description -n libboost_coroutine-devel
This package provides headers for Boost.Coroutine libraries.
Boost.Coroutine2 provides templates for generalized subroutines which
allow suspending and resuming execution at certain locations.

This package installs the default Boost version of the library.

%package     -n libboost_date_time-devel
Summary:        Development headers for Boost.DateTime library
Group:          Development/Libraries/C and C++
Requires:       libboost_date_time%{boost_version}-devel

%description -n libboost_date_time-devel
This package contains development header files and libraries for
Boost.DateTime library.

This package installs the default Boost version of the library.

%package     -n libboost_fiber-devel
Summary:        Development headers for Boost.Fiber library
Group:          Development/Libraries/C and C++
Requires:       libboost_fiber%{boost_version}-devel

%description -n libboost_fiber-devel
This package contains development header files and libraries for
Boost.Fiber library. Boost.Fiber is a cooperative multi-tasking
userland threading library.

This package installs the default Boost version of the library.

%package     -n libboost_filesystem-devel
Summary:        Development headers for Boost.Filesystem library
Group:          Development/Libraries/C and C++
Requires:       libboost_filesystem%{boost_version}-devel

%description -n libboost_filesystem-devel
Development headers for Boost.Filesystem library, a library providing
facilities to manipulate files and directories, and the paths that
identify them.

This package installs the default Boost version of the library.

%package     -n libboost_graph-devel
Summary:        Development headers for Boost.Graph library
Group:          Development/Libraries/C and C++
Requires:       libboost_graph%{boost_version}-devel

%description -n libboost_graph-devel
Development headers for Boost.Graph library. The BGL algorithms consist
of a core set of algorithm patterns and a larger set of graph
algorithms. The core algorithm patterns are Breadth First Search, Depth
First Search, and Uniform Cost Search.

This package installs the default Boost version of the library.

%package     -n libboost_iostreams-devel
Summary:        Development headers for Boost.IOStreans library
Group:          Development/Libraries/C and C++
Requires:       libboost_iostreams%{boost_version}-devel

%description -n libboost_iostreams-devel
Boost.IOStreams provides a framework for defining streams, stream
buffers and IO filters

This package installs the default Boost version of the library.

%package     -n libboost_log-devel
Summary:        Development headers for Boost.Log library
Group:          Development/Libraries/C and C++
Requires:       libboost_log%{boost_version}-devel

%description -n libboost_log-devel
Development headers for Boost.Log library which aims to make logging
significantly easier for the application developer. It provides a wide
range of out-of-the-box tools along with public interfaces for extending
the library.

This package installs the default Boost version of the library.

%package     -n libboost_math-devel
Summary:        Development headers for Boost.Math libraries
Group:          Development/Libraries/C and C++
Requires:       libboost_math%{boost_version}-devel

%description -n libboost_math-devel
Development headers for Boost.Math* boost libraries.

This package installs the default Boost version of the library.

%package     -n libboost_mpi-devel
Summary:        Development headers for Boost.MPI library
Group:          Development/Libraries/C and C++
Requires:       libboost_mpi%{boost_version}-devel

%description -n libboost_mpi-devel
Development headers for Boost.MPI boost library

This package installs the default Boost version of the library.

%package     -n libboost_graph_parallel-devel
Summary:        Development headers for Boost.Graph parallel library
Group:          Development/Libraries/C and C++
Requires:       libboost_graph_parallel%{boost_version}-devel

%description -n libboost_graph_parallel-devel
Development headers for Boost.Graph parallel boost library.

This package installs the default Boost version of the library.

%package     -n libboost_mpi_python3-devel
Summary:        Development library for Boost.MPI Python 3.x serialization
Group:          Development/Libraries/C and C++
Requires:       libboost_mpi_python-py3-%{boost_version}-devel

%description -n libboost_mpi_python3-devel
This package contains the Boost.MPI development library for Python 3.x
serialization interface

This package installs the default Boost version of the library.

%package     -n libboost_nowide-devel
Summary:        Development library for Boost.Nowide
Group:          Development/Libraries/C and C++
Requires:       libboost_nowide%{boost_version}-devel

%description -n libboost_nowide-devel
This package contains the Boost.Nowide development library.

This package installs the default Boost version of the library.

%package     -n python3-boost_parallel_mpi
Summary:        Python 3.x bindings for Boost.Parallel.MPI library
Group:          Development/Languages/Python
Requires:       python3-boost_parallel_mpi%{boost_version}

%description -n python3-boost_parallel_mpi
This package contains the Boost.Parallel.MPI bindings for Python 3.x

This package installs the default Boost version of the library.

%package     -n libboost_test-devel
Summary:        Development headers for Boost.Test library
Group:          Development/Libraries/C and C++
Requires:       libboost_test%{boost_version}-devel

%description -n libboost_test-devel
Development headers for Boost.Test library. Boost.Test supports for
simple program testing, full unit testing, and for program execution
monitoring.

This package installs the default Boost version of the library.

%package     -n libboost_program_options-devel
Summary:        Development headers for Boost.ProgramOptions library
Group:          Development/Libraries/C and C++
Requires:       libboost_program_options%{boost_version}-devel

%description -n libboost_program_options-devel
This package contains development headers for Boost.ProgramOptions
library.

This package installs the default Boost version of the library.

%package     -n libboost_python3-devel
Summary:        Development headers for Boost.Python library
Group:          Development/Libraries/C and C++
Requires:       libboost_python-py3-%{boost_version}-devel

%description -n libboost_python3-devel
Development headers for Boost.Python library. This package contains
library for python3 development for boost.

This package installs the default Boost version of the library.

%package     -n libboost_numpy3-devel
Summary:        Development headers for Boost.Python.NumPy library
Group:          Development/Libraries/C and C++
Requires:       libboost_numpy-py3-%{boost_version}-devel

%description -n libboost_numpy3-devel
Development headers for Boost.Python.NumPy library. This package contains
library for python3 development for boost.

This package installs the default Boost version of the library.

%package     -n libboost_serialization-devel
Summary:        Development headers for Boost.Serialization library
Group:          Development/Libraries/C and C++
Requires:       libboost_serialization%{boost_version}-devel

%description -n libboost_serialization-devel
This package contains development headers for Boost.Serialization
library.

This package installs the default Boost version of the library.

%package     -n libboost_stacktrace-devel
Summary:        Development headers for Boost.Stacktrace library
Group:          Development/Libraries/C and C++
Requires:       libboost_stacktrace%{boost_version}-devel

%description -n libboost_stacktrace-devel
This package contains development headers for Boost.Stacktrace library.
Boost.Stacktrace is a simple C++03 library that provide information
about call sequence in a human-readable form.

This package installs the default Boost version of the library.

%package     -n libboost_system-devel
Summary:        Development headers for Boost.System library
Group:          Development/Libraries/C and C++
Requires:       libboost_system%{boost_version}-devel

%description -n libboost_system-devel
This package contains development headers for Boost.System library.

This package installs the default Boost version of the library.

%package     -n libboost_thread-devel
Summary:        Development headers for Boost.Thread library
Group:          Development/Libraries/C and C++
Requires:       libboost_thread%{boost_version}-devel

%description -n libboost_thread-devel
This package contains development headers for Boost.Thread library.

This package installs the default Boost version of the library.

%package     -n libboost_json-devel
Summary:        Development headers for Boost.JSON library
Group:          Development/Libraries/C and C++
Requires:       libboost_json%{boost_version}-devel

%description -n libboost_json-devel
This package contains development headers for Boost.JSON library.

This package installs the default Boost version of the library.

%package     -n libboost_wave-devel
Summary:        Development headers for Boost.Wave library
Group:          Development/Libraries/C and C++
Requires:       libboost_wave%{boost_version}-devel

%description -n libboost_wave-devel
This package contains development headers for Boost.Wave library.

This package installs the default Boost version of the library.

%package     -n libboost_regex-devel
Summary:        Development headers for Boost.Regex library
Group:          Development/Libraries/C and C++
Requires:       libboost_regex%{boost_version}-devel

%description -n libboost_regex-devel
This package contains development headers for Boost.Regex library.

This package installs the default Boost version of the library.

%package     -n libboost_random-devel
Summary:        Development headers for Boost.Random library
Group:          Development/Libraries/C and C++
Requires:       libboost_random%{boost_version}-devel

%description -n libboost_random-devel
This package contains Boost.Random development headers.

This package installs the default Boost version of the library.

%package     -n libboost_chrono-devel
Summary:        Development headers for Boost.Chrono library
Group:          Development/Libraries/C and C++
Requires:       libboost_chrono%{boost_version}-devel

%description -n libboost_chrono-devel
This package contains Boost.Chrono development headers.

This package installs the default Boost version of the library.

%package     -n libboost_locale-devel
Summary:        Development headers for Boost.Locale library
Group:          Development/Libraries/C and C++
Requires:       libboost_locale%{boost_version}-devel

%description -n libboost_locale-devel
This package contains development headers for Boost.Locale library.

This package installs the default Boost version of the library.

%package     -n libboost_timer-devel
Summary:        Development headers for Boost.Timer library
Group:          Development/Libraries/C and C++
Requires:       libboost_timer%{boost_version}-devel

%description -n libboost_timer-devel
This package contains development headers for Boost.Timer library.

This package installs the default Boost version of the library.

%package     -n libboost_type_erasure-devel
Summary:        Development headers for Boost.TypeErasure library
Group:          Development/Libraries/C and C++
Requires:       libboost_type_erasure%{boost_version}-devel

%description -n libboost_type_erasure-devel
This package contains development headers for Boost.TypeErasure library.

This package installs the default Boost version of the library.

%prep

%build
cp %{SOURCE1} .

%install

%files -n boost-devel
%doc README

%files -n boost-jam
%doc README

%files -n libboost_headers-devel
%doc README

%files -n libboost_atomic-devel
%doc README

%files -n libboost_container-devel
%doc README

%files -n libboost_context-devel
%doc README

%files -n libboost_contract-devel
%doc README

%files -n libboost_coroutine-devel
%doc README

%files -n libboost_date_time-devel
%doc README

%files -n libboost_fiber-devel
%doc README

%files -n libboost_filesystem-devel
%doc README

%files -n libboost_graph-devel
%doc README

%files -n libboost_iostreams-devel
%doc README

%files -n libboost_log-devel
%doc README

%files -n libboost_math-devel
%doc README

%files -n libboost_mpi-devel
%doc README

%files -n libboost_graph_parallel-devel
%doc README

%files -n libboost_mpi_python3-devel
%doc README

%files -n libboost_nowide-devel
%doc README

%files -n python3-boost_parallel_mpi
%doc README

%files -n libboost_test-devel
%doc README

%files -n libboost_program_options-devel
%doc README

%files -n libboost_python3-devel
%doc README

%files -n libboost_numpy3-devel
%doc README

%files -n libboost_serialization-devel
%doc README

%files -n libboost_stacktrace-devel
%doc README

%files -n libboost_system-devel
%doc README

%files -n libboost_thread-devel
%doc README

%files -n libboost_wave-devel
%doc README

%files -n libboost_regex-devel
%doc README

%files -n libboost_random-devel
%doc README

%files -n libboost_chrono-devel
%doc README

%files -n libboost_locale-devel
%doc README

%files -n libboost_timer-devel
%doc README

%files -n libboost_type_erasure-devel
%doc README

%changelog
