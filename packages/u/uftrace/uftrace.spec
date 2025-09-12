#
# spec file for package uftrace
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

Name:           uftrace
Summary:        A function call graph tracer for C, C++, Rust and Python programs
Group:          Development/Tools/Debuggers
Version:        0.18.1
Release:        1
License:        GPL-2.0-only
URL:            https://github.com/namhyung/uftrace
Source0:        https://github.com/namhyung/uftrace/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch:    s390x ppc ppc64 ppc64le

%ifarch x86_64
BuildRequires:  pandoc
%endif

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  bash-completion

BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(libtraceevent)

%description
uftrace is a function call graph tracer for C, C++, Rust and Python programs.
It hooks into the entry and exit of each function, recording timestamps as well as the function's arguments and return values. uftrace is capable of tracing both user and kernel functions, as well as library functions and system events providing an integrated execution flow in a single timeline.
Initially, uftrace only supported function tracing with compiler support. However, it now allows users to trace function calls without recompilation by analyzing instructions in each function prologue and dynamically and selectively patching those instructions.
Users can also write and run scripts for each function entry and exit using python/luajit APIs to create custom tools for their specific purposes.
uftrace offers various filters to reduce the amount of trace data and provides visualization using Chrome trace viewer and flame graph or call-graph diagrams for graphviz and mermaid, allowing for a big picture view of the execution flow.
It was heavily inspired by the ftrace framework of the Linux kernel and the name uftrace stems from the combination of user and ftrace.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir}/uftrace
%make_build

%install
# use SUSE bash-completion path and drop exec bit from uftrace.py
%make_install completiondir=%{_datadir}/bash-completion/completions
chmod -x %{buildroot}%{_libdir}/uftrace/uftrace.py

%check
set -e
pushd %_builddir
%{name}-%{version}/uftrace --version
popd

%files
%license COPYING
%doc README* NEWS
%{_bindir}/uftrace
%dir %{_libdir}/uftrace
%{_libdir}/uftrace/libmcount*.so
%{_libdir}/uftrace/uftrace_python.so
%{_libdir}/uftrace/uftrace.py
%{_datadir}/bash-completion/completions/uftrace
%ifarch x86_64
%{_mandir}/man1/uftrace*.1*
%endif

%changelog
