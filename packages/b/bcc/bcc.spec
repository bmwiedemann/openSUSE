#
# spec file for package bcc
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{?suse_version} > 1500
%ifarch %ix86 x86_64
%{!?with_lua: %global with_lua 1}
%else
%{!?with_lua: %global with_lua 0}
%endif
%else
%{!?with_lua: %global with_lua 0}
%endif

%define libbpf_version 0.3

Name:           bcc
Version:        0.19.0
Release:        0
Summary:        BPF Compiler Collection (BCC)
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/iovisor/bcc
Source:         https://github.com/iovisor/bcc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/libbpf/libbpf/archive/v%{libbpf_version}.tar.gz#/libbpf-%{libbpf_version}.tar.gz
ExcludeArch:    ppc s390
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.7
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libelf-devel
BuildRequires:  llvm-clang-devel >= 3.7.0
BuildRequires:  llvm-devel >= 3.7.0
%if 0%{?suse_version} > 1320
BuildRequires:  clang-devel
BuildRequires:  llvm-gold
%else
BuildRequires:  libstdc++-devel
%endif
%if %{with_lua}
BuildRequires:  luajit-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  python3-base

%description
BCC is a toolkit for creating efficient kernel tracing and manipulation
programs, and includes several useful tools and examples. It makes use
of eBPF (Extended Berkeley Packet Filters), a feature that was first
added to Linux 3.15. Much of what BCC uses requires Linux 4.1 and above.

%package -n libbcc0
Summary:        Shared library from the BPF Compiler Collection
Group:          System/Libraries

%description -n libbcc0
Shared Library from the BPF Compiler Collection.

%package devel
Summary:        Header files for the BPF Compiler Collection
Group:          Development/Languages/C and C++
Requires:       libbcc0 = %{version}

%description devel
Headers and pkg-config build descriptions for developing BCC programs.

%package -n python3-bcc
Summary:        Python3 bindings for the BPF Compiler Collection
Group:          Development/Languages/Python
Requires:       kernel >= 4.1.0
Requires:       kernel-devel >= 4.1.0
Requires:       libbcc0 = %{version}

%description -n python3-bcc
Python 3.x bindings for the BPF Compiler Collection.

%package lua
Summary:        Lua interpreter for the BPF Compiler Collection
Group:          Development/Languages/Other
Requires:       kernel >= 4.1.0
Requires:       kernel-devel >= 4.1.0
Requires:       libbcc0 = %{version}

%description lua
Lua interpreter for the BPF Compiler Collection.

%package examples
Summary:        Examples from the BPF Compiler Collection
Group:          Documentation/Other
Requires:       python3-bcc = %{version}
Requires:       python3-future
Recommends:     python3-pyroute2
Recommends:     python3-netaddr
Recommends:     netperf

%description examples
Python and C examples from the BPF Compiler Collection.

%package tools
Summary:        Tracing tools from the BPF Compiler Collection
# ausyscall from audit is required by syscount.py
Group:          System/Monitoring
Requires:       audit
Requires:       python3-bcc = %{version}
Requires:       python3-future

%description tools
Python tracing scripts from the BPF Compiler Collection.

%package docs
Summary:        BPF Compiler Collection documentation
Group:          Documentation/Other

%description docs
Documentation on how to write programs with the BPF Compiler Collection.

%prep
%setup -q

pushd src/cc/libbpf
tar xf %{SOURCE1} --strip 1
popd

%build
# Prevent the cpp examples from compilation and installation
# Those programs are statically linked and huge in binary size.
sed -i "/add_subdirectory(cpp)/d" examples/CMakeLists.txt

# Remove the lua scripts if bcc-lua is disabled
%if %{with_lua} == 0
sed -i "/add_subdirectory(lua)/d" examples/CMakeLists.txt
%endif

# Install bps to /usr/bin
sed -i "s,share/bcc/introspection,bin," introspection/CMakeLists.txt

export LD_LIBRARY_PATH="%{_builddir}/usr/lib64"
export PATH="%{_builddir}/usr/bin":$PATH

mkdir build
pushd build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" cmake \
	-DPYTHON_CMD=python3 \
	-DREVISION_LAST=%{version} \
	-DREVISION=%{version} \
	-DCMAKE_INSTALL_PREFIX=/usr \
%if 0%{?suse_version} > 1320
	-DENABLE_LLVM_SHARED=1 \
%endif
%if %{with_lua}
	-DLUAJIT_INCLUDE_DIR=`pkg-config --variable=includedir luajit` \
	-DLUAJIT_LIBRARY=%{_libdir}/lib`pkg-config --variable=libname luajit`.so \
	-DENABLE_NO_PIE=OFF \
%endif
%ifarch %arm || %ix86
	-DENABLE_USDT=OFF \
%endif
	..
make %{?_smp_mflags} VERBOSE=1
popd

# Fix up #!-lines.
find tools/ examples/ -type f -exec \
	sed -Ei '1s|^#!/usr/bin/env python3?|#!/usr/bin/python3|' {} +
find tools/ examples/ -type f -exec \
	sed -Ei '1s|^#!/usr/bin/env bcc-lua|#!/usr/bin/bcc-lua|' {} +
find tools/ examples/ -type f -exec \
	sed -i '1s|/bin/python$|/bin/python3|g' {} +

%install
pushd build
%make_install

%if 0%{?suse_version} <= 1500
# Remove bps due to the incomplete support in kernel (bsc#1085403)
rm -f %{buildroot}/%{_bindir}/bps
%endif

popd

# Remove the static libraries
rm -f %{buildroot}/%{_libdir}/libbcc*.a

%post -n libbcc0 -p /sbin/ldconfig

%postun -n libbcc0 -p /sbin/ldconfig

%files -n bcc-devel
%{_libdir}/libbcc.so
%{_libdir}/libbcc_bpf.so
%dir %{_includedir}/bcc/
%{_includedir}/bcc/*
%{_libdir}/pkgconfig/libbcc.pc

%files -n libbcc0
%license LICENSE.txt
%{_libdir}/libbcc.so.*
%{_libdir}/libbcc_bpf.so.*

%files -n python3-bcc
%{python3_sitelib}/bcc*

%if %{with_lua}
%files lua
%{_bindir}/bcc-lua
%endif

%files examples
%dir %{_datadir}/bcc/
%dir %{_datadir}/bcc/examples/
%{_datadir}/bcc/examples/*

%files tools
%dir %{_datadir}/bcc/
%dir %{_datadir}/bcc/tools/
%{_datadir}/bcc/tools/*
%dir %{_datadir}/bcc/man/
%{_datadir}/bcc/man/*
%if 0%{?suse_version} > 1500
%{_bindir}/bps
%endif

%files docs
%doc README.md FAQ.txt
%doc docs/kernel-versions.md docs/reference_guide.md
%doc docs/tutorial_bcc_python_developer.md docs/tutorial.md

%changelog
