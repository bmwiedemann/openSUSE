#
# spec file for package dpdk
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
# needssslcertforbuild


%define platform generic
%define machine  auto
# This is in sync with <src>/ABI_VERSION
# TODO: automate this sync
%define maj 25
%define min 0
#%%define lname libdpdk-%%{maj}_%%{min}
%define lname libdpdk-%{maj}
#
%if 0%{?sle_version} >= 150600
%global pprefix python311
%{?sle15_python_module_pythons}
%else
%global pythons python3
%global pprefix python3
%endif
# Add option to build without examples
%bcond_without examples
# Add option to build without tools
%bcond_without tools
Name:           dpdk
Version:        24.11.1
Release:        0
Summary:        Set of libraries and drivers for fast packet processing
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only
Group:          System/Libraries
URL:            https://www.dpdk.org/
Source:         https://fast.dpdk.org/rel/dpdk-%{version}.tar.xz
# PATCH-FIX-OPENSUSE PATCH-FEATURE-UPSTREAM
Patch0:         0001-fix-cpu-compatibility.patch
# PATCH-FIX-UPSTREAM - https://bugs.dpdk.org/show_bug.cgi?id=1530
Patch1:         0001-examples-vm_power_manager-add-missing-header.patch
# Fix inline error for < gcc14 (<=SLE16)
Patch2:         0001-always_inline-fix.patch
# Fix reproducable builds https://bugzilla.opensuse.org/show_bug.cgi?id=1244130
Patch3:         0001-dts-generate-random-capture_name-per-call.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pyelftools >= 0.22}
BuildRequires:  %{pythons}
BuildRequires:  binutils
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kernel-syms
BuildRequires:  libfdt-devel
BuildRequires:  meson >= 0.53.2
BuildRequires:  modutils
BuildRequires:  patchelf
BuildRequires:  pesign-obs-integration
BuildRequires:  pkgconfig
BuildRequires:  rdma-core-devel
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(zlib)
Obsoletes:      dpdk-kmp-trace < %{version}
%ifarch aarch64
Provides:       dpdk-thunderx = %{version}-%{release}
Obsoletes:      dpdk-thunderx < %{version}-%{release}
%endif
ExclusiveArch:  aarch64 x86_64 ppc64le
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
# https://bugzilla.opensuse.org/show_bug.cgi?id=1196511
BuildRequires:  pkgconfig(libbpf)
%endif

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package devel
Summary:        Data Plane Development Kit development files
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
%ifarch aarch64
Provides:       dpdk-thunderx-devel = %{version}-%{release}
Obsoletes:      dpdk-thunderx-devel < %{version}-%{release}
%endif

%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package devel-static
Summary:        Data Plane Development Kit static development files
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
%ifarch aarch64
Provides:       dpdk-thunderx-devel-static = %{version}-%{release}
Obsoletes:      dpdk-thunderx-devel-static < %{version}-%{release}
%endif

%description devel-static
This package contains the static library files needed for developing
applications with the Data Plane Development Kit.

%package -n %{lname}
Summary:        Data Plane Development Kit runtime libraries
Group:          Development/Libraries/C and C++
Provides:       %{lname}-any = %{version}

%description -n %{lname}
This package contains the runtime libraries needed for 3rd party application
to use the Data Plane Development Kit.

%package doc
Summary:        Data Plane Development Kit API documentation
Group:          System/Libraries
BuildArch:      noarch
%ifarch aarch64
Provides:       dpdk-thunderx-doc = %{version}-%{release}
Obsoletes:      dpdk-thunderx-doc < %{version}-%{release}
%endif

%description doc
API programming documentation for the Data Plane Development Kit.

%if %{with tools}
%package tools
Summary:        Tools for setting up Data Plane Development Kit environment
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       findutils
Requires:       iproute
Requires:       kmod
Requires:       pciutils
%ifarch aarch64
Provides:       dpdk-thunderx-tools = %{version}-%{release}
Obsoletes:      dpdk-thunderx-tools < %{version}-%{release}
%endif

%description tools
This package contains tools for setting up Data Plane Development Kit environment
%endif

%if %{with examples}
%package examples
Summary:        Data Plane Development Kit example applications
Group:          System/Libraries
BuildRequires:  libvirt-devel
%ifarch aarch64
Provides:       dpdk-thunderx-examples = %{version}-%{release}
Obsoletes:      dpdk-thunderx-examples < %{version}-%{release}
%endif

%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.
%endif

%define sdkdir  %{_datadir}/dpdk
%define docdir  %{_docdir}/dpdk
%define incdir %{_includedir}/dpdk
%define pmddir %{_libdir}/dpdk-pmds-%{maj}.%{min}

%prep
%setup -q -n dpdk-stable-%{version}
%autopatch -p1

# Skip not supported examples
sed -i "/performance-thread/d" examples/meson.build

# Verify ABI
[ "$(cat ABI_VERSION)" = "%{maj}.%{min}" ] || exit 1

%build
%define _vpath_builddir "build-%{_target_cpu}-$flavor"

%ifarch x86_64
export CFLAGS="%{optflags} -U_FORTIFY_SOURCE -msse4"
%endif
examples="all"
for flavor in %{flavors_to_build}; do
  %meson --includedir=%{incdir} \
    -Ddefault_library=shared \
    -Denable_docs=true \
    -Db_lto=true \
  %if %{with examples}
    -Dexamples="$examples" \
  %endif
    -Dplatform="%{platform}" \
    -Dcpu_instruction_set=%{machine} \
    -Denable_kmods=true \
    -Denable_driver_sdk=true \
    -Ddrivers_install_subdir=%{pmddir} \
    -Dkernel_dir="%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor"
  %meson_build
  # Make sure examples are only built once
  examples=""
done

%install
examples="%{?with_examples:all}"
for flavor in %{flavors_to_build}; do
    %meson_install
    # Also install the example binaries
    if [ ! -z "$examples" ]; then
        for f in %{_vpath_builddir}/examples/dpdk-*; do
            bn=$(basename "$f")
            if [ -f "$f" ] ; then
                install -Dm 0755 ${f} "%{buildroot}%{_bindir}/${bn/dpdk-/dpdk_example_}"
                patchelf --remove-rpath "%{buildroot}%{_bindir}/${bn/dpdk-/dpdk_example_}"
            fi
        done
    fi
    examples=""
done

# Fix documentation
mkdir -p %{buildroot}%{docdir}
mv %{buildroot}%{_datadir}/doc/dpdk %{buildroot}%{_docdir}
rm -rf %{buildroot}%{docdir}/html/.doctrees
rm -rf %{buildroot}%{docdir}/html/dts/.doctrees
rm %{buildroot}%{docdir}/html/.buildinfo
rm %{buildroot}%{docdir}/html/dts/.buildinfo
rm %{buildroot}%{docdir}/html/dts/.html.d

# Fix man directory
rm -r %{buildroot}%{_mandir}/man3/*

# driver .so files often depend upon the bus drivers for their connect bus,
# e.g. ixgbe depends on librte_bus_pci. This means that the bus drivers need
# to be in the library path, so symlink the drivers from the main lib directory
# Fix broken symlink created by buildtools/symlink-drivers-solibs.sh
for f in %{buildroot}/%{pmddir}/*.so.*; do
    bn=$(basename ${f})
    ln -s %{pmddir}/${bn} %{buildroot}%{_libdir}/${bn}
done

%if ! %{with tools}
# Remove tools if not needed
for tool in dpdk-devbind.py dpdk-pmdinfo.py dpdk-telemetry.py dpdk-hugepages.py; do
  rm -rf "%{buildroot}%{_bindir}/$tool"
done
%else
# Add compatibility symlink
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_bindir}/dpdk-devbind.py %{buildroot}%{_sbindir}/dpdk_nic_bind
%endif

# Fix interpreter
%python3_fix_shebang
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/examples/ipsec-secgw/test/*
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/examples/pipeline/examples/*

# Remove duplicates
%fdupes %{buildroot}/%docdir
%fdupes %{buildroot}/%{sdkdir}/examples

# Fix broken symlink (yes with * in its name)
rm -v "%{buildroot}%{_libdir}/librte_*.so*"

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig
%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%{_bindir}/dpdk-dumpcap
%{_bindir}/dpdk-pdump
%{_bindir}/dpdk-proc-info
%{_bindir}/dpdk-test*
%{_bindir}/dpdk-graph*

%files -n %{lname}
%license license/gpl-2.0.txt license/lgpl-2.1.txt license/bsd-3-clause.txt
%{_libdir}/*.so.*
%dir %{pmddir}
%{pmddir}/*.so.*

%files devel
#BSD
%{incdir}/
%{sdkdir}/
%{pmddir}/*.so
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdpdk*.pc
%if %{with examples}
%exclude %{sdkdir}/examples/
%endif

%files devel-static
#BSD
%{_libdir}/*.a

%files doc
#BSD
%doc %docdir

%if %{with tools}
%files tools
%{_sbindir}/dpdk_nic_bind
%{_bindir}/dpdk-*.py
%endif

%if %{with examples}
%files examples
%{_bindir}/dpdk_example_*
%doc %{sdkdir}/examples
%endif

%changelog
