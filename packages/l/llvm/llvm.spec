#
# spec file for package llvm
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


%define _sonum 9
%ifarch x86_64
%define has_lldb 1
# python3-lldb%{_sonum} is only built with these distributions (see llvm%{_sonum} package)
%if 0%{?suse_version} > 1320
%define has_lldb_python 1
%endif
%endif
Name:           llvm
Version:        9.0.0
Release:        0
Summary:        Low Level Virtual Machine
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Group:          Development/Languages/Other
URL:            https://www.llvm.org/
# This file documents the process for updating llvm
Source0:        README.packaging
Source101:      baselibs.conf
# Avoid multiple providers error
BuildRequires:  clang%{_sonum} = %{version}
BuildRequires:  clang%{_sonum}-checker = %{version}
BuildRequires:  clang%{_sonum}-devel = %{version}
BuildRequires:  llvm%{_sonum} = %{version}
BuildRequires:  llvm%{_sonum}-LTO-devel = %{version}
BuildRequires:  llvm%{_sonum}-devel = %{version}
BuildRequires:  llvm%{_sonum}-emacs-plugins = %{version}
BuildRequires:  llvm%{_sonum}-gold = %{version}
BuildRequires:  llvm%{_sonum}-vim-plugins = %{version}
Requires:       llvm%{_sonum} = %{version}
%if 0%{?has_lldb}
BuildRequires:  lldb%{_sonum} = %{version}
BuildRequires:  lldb%{_sonum}-devel = %{version}
%endif
%if 0%{?has_lldb_python}
BuildRequires:  python3-lldb%{_sonum} = %{version}
%endif
Recommends:     %{name}-doc
# Mirrors ExcludeArch in llvm%{_sonum}
ExcludeArch:    s390

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
Requires:       llvm%{_sonum}-devel = %{version}
Requires:       llvm-gold

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
Requires:       llvm%{_sonum}-doc = %{version}

%description doc
This package contains documentation for the LLVM infrastructure.

This package is a dummy package that depends on the version of
llvm-doc that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package -n clang
Summary:        CLANG frontend for LLVM
Group:          Development/Languages/C and C++
Url:            https://clang.llvm.org/
Requires:       clang%{_sonum} = %{version}
Recommends:     clang-doc
Provides:       llvm-clang = %{version}
Obsoletes:      llvm-clang < %{version}

%description -n clang
This package contains the clang (C language) frontend for LLVM.

This package is a dummy package that depends on the version of
clang that openSUSE currently supports.  Packages that
don't require a specific Clang version should depend on this.

%package -n clang-checker
Summary:        Static code analyzer for CLANG
Group:          Development/Languages/C and C++
Url:            https://clang-analyzer.llvm.org/
Requires:       clang%{_sonum}-checker = %{version}
Provides:       llvm-clang-checker = %{version}
Obsoletes:      llvm-clang-checker < %{version}

%description -n clang-checker
This package contains scan-build and scan-view, command line
static code analyzers for CLANG.

This package is a dummy package that depends on the version of
clang-checker that openSUSE currently supports.  Packages that
don't require a specific Clang version should depend on this.

%package -n clang-devel
Summary:        CLANG frontend for LLVM (devel package)
Group:          Development/Libraries/C and C++
Requires:       clang%{_sonum}-devel = %{version}
Provides:       llvm-clang-devel = %{version}
Obsoletes:      llvm-clang-devel < %{version}
Provides:       clang-devel-static = %{version}
Obsoletes:      clang-devel-static < %{version}

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
Requires:       clang%{_sonum}-doc = %{version}

%description -n clang-doc
This package contains documentation for the Clang compiler.

This package is a dummy package that depends on the version of
clang-doc that openSUSE currently supports.  Packages that
don't require a specific Clang version should depend on this.

%package LTO-devel
Summary:        Link-time optimizer for LLVM (devel package)
Group:          Development/Libraries/C and C++
Requires:       llvm%{_sonum}-LTO-devel = %{version}

%description LTO-devel
This package contains the link-time optimizer for LLVM.
(development files)

This package is a dummy package that depends on the version of
llvm-LTO-devel that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package gold
Summary:        Gold linker plugin for LLVM
Group:          Development/Tools/Building
Requires:       llvm%{_sonum}-gold = %{version}

%description gold
This package contains the Gold linker plugin for LLVM.

This package is a dummy package that depends on the version of
llvm-gold that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package        vim-plugins
Summary:        Vim plugins for LLVM
Group:          Productivity/Text/Editors
Requires:       llvm%{_sonum}-vim-plugins = %{version}
Supplements:    packageand(llvm:vim)
BuildArch:      noarch

%description    vim-plugins
This package contains vim plugins for LLVM like syntax highlighting.

This package is a dummy package that depends on the version of
llvm-vim-plugins that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package        emacs-plugins
Summary:        Emacs plugins for LLVM
Group:          Productivity/Text/Editors
Requires:       llvm%{_sonum}-emacs-plugins = %{version}
Supplements:    packageand(llvm:emacs)
BuildArch:      noarch

%description    emacs-plugins
This package contains Emacs plugins for LLVM like syntax highlighting.

This package is a dummy package that depends on the version of
llvm-emacs-plugins that openSUSE currently supports.  Packages that
don't require a specific LLVM version should depend on this.

%package -n lldb
Summary:        Software debugger built using LLVM libraries
Group:          Development/Tools/Debuggers
Url:            https://lldb.llvm.org/
Requires:       lldb%{_sonum} = %{version}
Recommends:     python3-lldb

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
Requires:       lldb%{_sonum}-devel = %{version}

%description -n lldb-devel
This package contains the development files for LLDB.

This package is a dummy package that depends on the version of
lldb-devel that openSUSE currently supports.  Packages that
don't require a specific LLDB version should depend on this.

%package -n python3-lldb
Summary:        Python bindings for liblldb
Group:          Development/Libraries/Python
Requires:       python3-lldb%{_sonum} = %{version}

%description -n python3-lldb
This package contains the Python bindings to clang (C language) frontend for LLVM.

This package is a dummy package that depends on the version of
python3-lldb that openSUSE currently supports.  Packages that
don't require a specific LLDB version should depend on this.

%package -n lld
Summary:        Linker for Clang/LLVM
Group:          Development/Tools/Building
Url:            https://lld.llvm.org/
Requires:       lld%{_sonum} = %{version}

%description -n lld
LLD is a linker from the LLVM project. That is a drop-in replacement for
system linkers and runs much faster than them. It also provides features that
are useful for toolchain developers.

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

%files -n clang-checker
%doc README

%files gold
%doc README

%files devel
%doc README

%files -n clang-devel
%doc README

%files LTO-devel
%doc README

%files emacs-plugins
%doc README

%files vim-plugins
%doc README

%if 0%{?has_lldb}
%files -n lldb
%doc README

%files -n lldb-devel
%doc README

%endif

%if 0%{?has_lldb_python}
%files -n python3-lldb
%doc README

%endif

%files -n lld
%doc README

%changelog
