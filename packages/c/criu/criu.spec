#
# spec file for package criu
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


%if 0%{?suse_version} >= 1330
%define use_asciidoctor 1
%define make_options USE_ASCIIDOCTOR=1
%endif

# Build criu with nftables default support if available
%if "%{?default_firewall_backend}" == "nftables"
    %define prefer_nftables 1
%else
    %define prefer_nftables 0
%endif

# currently broken with LTO, resulting in segfaults (bsc#1203854)
%define _lto_cflags %{nil}

%ifarch x86_64 aarch64
%define with_amdgpu_plugin 1
%else
%define with_amdgpu_plugin 0
%endif

%define proto_c_ver %(protoc-c --version | head -1 | awk '{print $2}')

Name:           criu
Version:        4.0
Release:        0
Summary:        Checkpoint/Restore In Userspace Tools
License:        GPL-2.0-only
Group:          System/Console
URL:            https://criu.org/
Source0:        http://github.com/checkpoint-restore/criu/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# To be generated; we keep a static one for building without pip
Source1:        crit.py
Patch101:       criu-py-install-fix.diff
Patch102:       0002-Fix-build-with-nftables-installed-in-different-direc.patch
Patch104:       plugin-dir-path.patch
Patch105:       criu-ns-python3-shebang.patch
Patch106:       vdso-handle-vvar_vclock-vma-s.patch
Patch201:       0001-cr_options-switch-networking-default-backend-to-nfta.patch
BuildRequires:  libcap-devel
%if %{with_amdgpu_plugin}
BuildRequires:  libdrm-devel
%endif
BuildRequires:  libgnutls-devel
BuildRequires:  libnet-devel
BuildRequires:  libnl3-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
BuildRequires:  nftables-devel
%endif
%if 0%{?use_asciidoctor}
BuildRequires:  rubygem(asciidoctor)
%else
BuildRequires:  asciidoc
BuildRequires:  xmlto
%endif
Requires:       python3-ipaddr
Requires:       python3-protobuf
ExclusiveArch:  x86_64 aarch64 ppc64le armv7l armv7hl s390x
%if 0%{?suse_version} > 1320
BuildRequires:  libbsd-devel
%endif

%description
Checkpoint/Restore In Userspace, or CRIU, is a software tool for Linux
operating system. Using this tool, you can freeze a running application
(or part of it) and checkpoint it to a hard drive as a collection of
files. You can then use the files to restore and run the application from
the point it was frozen at.

%if %{with_amdgpu_plugin}
%package plugin-amdgpu
Summary:        AMDGPU plugin for CRIU
License:        GPL-2.0-only
Group:          System/Console
Requires:       %{name} = %{version}

%description plugin-amdgpu
This package contains the AMDGPU ROCm support plugin for CRIU.
%endif

%package plugin-cuda
Summary:        CUDA plugin for CRIU
License:        GPL-2.0-only
Group:          System/Console
Requires:       %{name} = %{version}

%description plugin-cuda
This package contains the CUDA support plugin for CRIU.

%package -n libcriu2
Summary:        Library for CRIU
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n libcriu2
This package contains the library for CRIU, Checkpoint/Restore In
Userspace Tools.

%package -n libcompel1
Summary:        Compel library for CRIU
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n libcompel1
This package contains the compel library for CRIU to execute a parasite code.

%package devel
Summary:        Include Files and Libraries mandatory for Development
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcompel1 = %{version}
Requires:       libcriu2 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications with CRIU library.

%prep
%setup -q
%autopatch -M 200 -p1

%if %{prefer_nftables}
# build with default nftables support on envs
# where nftables is the default firewall backend
# https://github.com/containers/podman/issues/24799
%patch -P201 -p1
%endif

# workaround for Leap 15.x
%if 0%{?suse_version} < 1600
sed -i -e's/\(^.*-mshstk\)/# \1/' criu/pie/Makefile
%endif

# default off
echo "BINFMT_MISC_VIRTUALIZED" > .config

%build
export CFLAGS="%{optflags}"
%ifarch %arm
export CFLAGS="$CFLAGS -Wno-error=deprecated"
%endif
# WERROR=0 is needed for avoiding warning due to doubly _GNU_SOURCE defines
make V=1 %{?_smp_mflags} %{?make_options} WERROR=0 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir}

%install
%make_install V=1 %{?make_options} WERROR=0 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir}
install -c -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/crit

# remove static libs
rm -f %{buildroot}%{_libdir}/lib*.a \
      %{buildroot}%{_libexecdir}/compel/*.a

# remove stable files
rm -f %{buildroot}%{_includedir}/compel/plugins/std/asm/.gitignore
# for compatiblity
ln -s criu %{buildroot}%{_sbindir}/crtools
ln -s criu.8 %{buildroot}%{_mandir}/man8/crtools.8

%if ! %{with_amdgpu_plugin}
rm -f %{buildroot}%{_mandir}/man1/criu-amdgpu-plugin.1
%endif

%post -n libcriu2 -p /sbin/ldconfig
%postun -n libcriu2 -p /sbin/ldconfig
%post -n libcompel1 -p /sbin/ldconfig
%postun -n libcompel1 -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_sbindir}/criu
%{_sbindir}/criu-ns
%{_sbindir}/crtools
%{_bindir}/compel
%{_bindir}/crit
%{_mandir}/man1/compel.1%{?ext_man}
%{_mandir}/man1/crit.1%{?ext_man}
%{_mandir}/man1/criu-ns.1%{?ext_man}
%{_mandir}/man8/criu.8%{?ext_man}
%{_mandir}/man8/crtools.8%{?ext_man}
%{_libexecdir}/criu
%{_libexecdir}/compel
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/crit
%{python3_sitelib}/pycriu

%if %{with_amdgpu_plugin}
%files plugin-amdgpu
%doc plugins/amdgpu/README.md
%{_mandir}/man1/criu-amdgpu-plugin.1%{?ext_man}
%dir %{_libdir}/criu
%{_libdir}/criu/amdgpu_plugin.so
%endif

%files plugin-cuda
%doc plugins/cuda/README.md
%dir %{_libdir}/criu
%{_libdir}/criu/cuda_plugin.so

%files -n libcriu2
%{_libdir}/libcriu.so.*

%files -n libcompel1
%{_libdir}/libcompel.so.*

%files devel
%{_includedir}/criu
%{_includedir}/compel
%{_libdir}/libcriu.so
%{_libdir}/libcompel.so
%{_libdir}/pkgconfig/*.pc

%changelog
