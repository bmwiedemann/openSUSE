#
# spec file for package llvm
#
# Copyright (c) 2024 SUSE LLC
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


%define _sonum 19

%ifarch aarch64 ppc64 ppc64le %{ix86} x86_64
%global has_openmp 1
%endif

%ifarch aarch64 x86_64
%define has_lldb 1
%if %{suse_version} > 1600
%define has_lldb_python 1
%endif
%endif

# obsolete_llvm_versioned() prefix postfix
# Obsolete packages <prefix>X or <prefix>X-<postfix> with X being a set of older versions.
%define obsolete_llvm_versioned() \
Obsoletes:      %{1}10%{?2:-%{2}} \
Obsoletes:      %{1}11%{?2:-%{2}} \
Obsoletes:      %{1}12%{?2:-%{2}} \
Obsoletes:      %{1}13%{?2:-%{2}} \
Obsoletes:      %{1}14%{?2:-%{2}} \
Obsoletes:      %{1}15%{?2:-%{2}} \
Obsoletes:      %{1}16%{?2:-%{2}} \
Obsoletes:      %{1}17%{?2:-%{2}} \
Obsoletes:      %{1}18%{?2:-%{2}} \
Obsoletes:      %{1}7%{?2:-%{2}} \
Obsoletes:      %{1}8%{?2:-%{2}} \
Obsoletes:      %{1}9%{?2:-%{2}}

Name:           llvm
Version:        %{_sonum}
Release:        0
Summary:        Low Level Virtual Machine
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Group:          Development/Languages/Other
URL:            https://www.llvm.org/
# This file documents the process for updating llvm
Source0:        README.packaging
Requires:       llvm%{_sonum}
Suggests:       %{name}-doc

%description
LLVM is a compiler infrastructure designed for compile-time,
link-time, runtime, and idle-time optimization of programs from
arbitrary programming languages.

The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.

This package is a dummy package that depends on the version of
llvm that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package devel
Summary:        Header Files for LLVM
Group:          Development/Libraries/C and C++
Requires:       llvm%{_sonum}-devel
Provides:       llvm-LTO-devel = %{version}
Obsoletes:      llvm-LTO-devel < %{version}
%if 0%{?has_openmp}
Requires:       libomp-devel
%endif
Requires:       llvm-gold
Requires:       llvm-polly-devel
%obsolete_llvm_versioned llvm devel
%obsolete_llvm_versioned llvm LTO-devel

%description devel
This package contains library and header files needed to develop
new native programs that use the LLVM infrastructure.

This package is a dummy package that depends on the version of
llvm-devel that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package doc
Summary:        Documentation for LLVM
Group:          Documentation/HTML
Requires:       %{name} = %{version}
Requires:       llvm%{_sonum}-doc
%obsolete_llvm_versioned llvm doc

%description doc
This package contains documentation for the LLVM infrastructure.

This package is a dummy package that depends on the version of
llvm-doc that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package -n clang
Summary:        CLANG frontend for LLVM
Group:          Development/Languages/C and C++
URL:            https://clang.llvm.org/
Requires:       clang%{_sonum}
Provides:       llvm-clang = %{version}
Obsoletes:      llvm-clang < %{version}
Provides:       llvm-emacs-plugins
Suggests:       clang-doc

%description -n clang
This package contains the clang (C language) frontend for LLVM.

This package is a dummy package that depends on the version of
clang that openSUSE currently supports.  Packages that
don't require a specific Clang version should depend on this.

%package -n clang-devel
Summary:        CLANG frontend for LLVM (devel package)
Group:          Development/Libraries/C and C++
Requires:       clang%{_sonum}-devel
Provides:       llvm-clang-devel = %{version}
Obsoletes:      llvm-clang-devel < %{version}
Provides:       clang-devel-static = %{version}
Obsoletes:      clang-devel-static < %{version}
%obsolete_llvm_versioned clang devel

%description -n clang-devel
This package contains the clang (C language) frontend for LLVM.
(development files)

This package is a dummy package that depends on the version of
clang-devel that openSUSE currently supports.  Packages that
don't require a specific Clang version should depend on this.

%package -n clang-doc
Summary:        Documentation for Clang
Group:          Documentation/HTML
Requires:       clang = %{version}
Requires:       clang%{_sonum}-doc
%obsolete_llvm_versioned clang doc

%description -n clang-doc
This package contains documentation for the Clang compiler.

This package is a dummy package that depends on the version of
clang-doc that openSUSE currently supports.  Packages that
don't require a specific Clang version should depend on this.

%package gold
Summary:        Gold linker plugin for LLVM
Group:          Development/Tools/Building
Requires:       llvm%{_sonum}-gold
%obsolete_llvm_versioned llvm gold

%description gold
This package contains the Gold linker plugin for LLVM.

This package is a dummy package that depends on the version of
llvm-gold that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package        vim-plugins
Summary:        Vim plugins for LLVM
Group:          Productivity/Text/Editors
Requires:       llvm%{_sonum}-vim-plugins
Supplements:    packageand(llvm:vim)
%obsolete_llvm_versioned llvm vim-plugins
BuildArch:      noarch

%description    vim-plugins
This package contains vim plugins for LLVM like syntax highlighting.

This package is a dummy package that depends on the version of
llvm-vim-plugins that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package opt-viewer
Summary:        Tools for visualising the LLVM optimization records
Group:          Development/Languages/Other
Requires:       llvm%{_sonum}-opt-viewer
%obsolete_llvm_versioned llvm opt-viewer
BuildArch:      noarch

%description opt-viewer
Set of tools for visualising the LLVM optimization records generated
with -fsave-optimization-record. Used for compiler-assisted performance
analysis.

This package is a dummy package that depends on the version of
llvm-opt-viewer that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package -n lldb
Summary:        Software debugger built using LLVM libraries
Group:          Development/Tools/Debuggers
URL:            https://lldb.llvm.org/
Requires:       lldb%{_sonum}
%if 0%{?has_lldb_python}
Recommends:     python3-lldb
%endif

%description -n lldb
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

This package is a dummy package that depends on the version of
lldb that openSUSE currently supports.  Packages that
don't require a specific LLDB version should depend on this.

%package -n lldb-devel
Summary:        Development files for LLDB
Group:          Development/Libraries/C and C++
Requires:       lldb%{_sonum}-devel
%obsolete_llvm_versioned lldb devel

%description -n lldb-devel
This package contains the development files for LLDB.

This package is a dummy package that depends on the version of
lldb-devel that openSUSE currently supports.  Packages that
don't require a specific LLDB version should depend on this.

%package -n python3-clang
Summary:        Python bindings for libclang
Group:          Development/Libraries/Python
Requires:       python3-clang%{_sonum}
%obsolete_llvm_versioned python3-clang
BuildArch:      noarch

%description -n python3-clang
This package contains the Python bindings to clang (C language)
frontend for LLVM.

%package -n python3-lldb
Summary:        Python bindings for liblldb
Group:          Development/Libraries/Python
Requires:       python3-lldb%{_sonum}
%obsolete_llvm_versioned python3-lldb

%description -n python3-lldb
This package contains the Python bindings to clang (C language) frontend for LLVM.

This package is a dummy package that depends on the version of
python3-lldb that openSUSE currently supports.  Packages that
don't require a specific LLDB version should depend on this.

%package -n lld
Summary:        Linker for Clang/LLVM
Group:          Development/Tools/Building
URL:            https://lld.llvm.org/
Requires:       lld%{_sonum}

%description -n lld
LLD is a linker from the LLVM project. That is a drop-in replacement for
system linkers and runs much faster than them. It also provides features that
are useful for toolchain developers.

%package -n libomp-devel
Summary:        MPI plugin for LLVM
Group:          Development/Libraries/C and C++
Requires:       libomp%{_sonum}-devel
%obsolete_llvm_versioned libomp devel

%description -n libomp-devel
This package contains the OpenMP MPI plugin for LLVM.

This package is a dummy package that depends on the version of
libomp-devel that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package polly
Summary:        LLVM Framework for High-Level Loop and Data-Locality Optimizations
Group:          Development/Languages/Other
URL:            https://polly.llvm.org/
Requires:       llvm%{_sonum}-polly
%obsolete_llvm_versioned llvm polly

%description polly
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedra to analyze and optimize the memory access pattern of a
program. Polly can currently perform classical loop transformations, especially
tiling and loop fusion to improve data-locality. It can also exploit OpenMP
level parallelism and expose SIMDization opportunities.

This package is a dummy package that depends on the version of
llvm-polly that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package polly-devel
Summary:        Development files for Polly
Group:          Development/Libraries/C and C++
Requires:       llvm%{_sonum}-polly-devel
Requires:       llvm-polly = %{version}
%obsolete_llvm_versioned llvm polly-devel

%description polly-devel
This package contains the development files for Polly.

This package is a dummy package that depends on the version of
llvm-polly-devel that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%prep
# Not needed

%build
echo "This is a dummy package to provide a dependency on the system compiler." > README

%install
# Not needed

%files
%doc README

%files -n clang
%doc README

%files gold
%doc README

%files devel
%doc README

%files doc
%doc README

%files -n clang-devel
%doc README

%files -n clang-doc
%doc README

%files vim-plugins
%doc README

%files opt-viewer
%doc README

%if 0%{?has_lldb}
%files -n lldb
%doc README

%files -n lldb-devel
%doc README
%endif

%files -n python3-clang
%doc README

%if 0%{?has_lldb_python}
%files -n python3-lldb
%doc README
%endif

%files -n lld
%doc README

%if 0%{?has_openmp}
%files -n libomp-devel
%doc README
%endif

%files polly
%doc README

%files polly-devel
%doc README

%changelog
