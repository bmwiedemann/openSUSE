#
# spec file for package criu
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


%if 0%{?suse_version} >= 1330
%define use_asciidoctor 1
%define make_options USE_ASCIIDOCTOR=1
%endif

%ifarch %arm aarch64
%define _lto_cflags %{nil}
%endif

Name:           criu
Version:        3.14
Release:        0
Summary:        Checkpoint/Restore In Userspace Tools
License:        GPL-2.0-only
Group:          System/Console
URL:            https://criu.org/
Source0:        https://download.openvz.org/criu/%{name}-%{version}.tar.bz2
Patch1:         criu-py-install-fix.diff
BuildRequires:  libcap-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libnet-devel
BuildRequires:  libnl3-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-c
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
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
%patch1 -p1
# default off
echo "BINFMT_MISC_VIRTUALIZED" > .config

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
%ifarch %arm
export CFLAGS="$CFLAGS -Wno-error=deprecated"
%endif
make V=1 %{?_smp_mflags} %{?make_options}

%install
%make_install V=1 %{?make_options} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir}
# remove static libs
rm -f %{buildroot}%{_libdir}/lib*.a \
      %{buildroot}%{_libexecdir}/compel/*.a

# remove stable files
rm -f %{buildroot}%{_includedir}/compel/plugins/std/asm/.gitignore
# for compatiblity
ln -s criu %{buildroot}%{_sbindir}/crtools
ln -s criu.8 %{buildroot}%{_mandir}/man8/crtools.8

%post -n libcriu2 -p /sbin/ldconfig
%postun -n libcriu2 -p /sbin/ldconfig
%post -n libcompel1 -p /sbin/ldconfig
%postun -n libcompel1 -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_sbindir}/criu
%{_sbindir}/crtools
%{_bindir}/compel
%{_bindir}/crit
%{_mandir}/man1/compel.1%{?ext_man}
%{_mandir}/man1/crit.1%{?ext_man}
%{_mandir}/man8/criu.8%{?ext_man}
%{_mandir}/man8/crtools.8%{?ext_man}
%{_libexecdir}/criu
%{_libexecdir}/compel
%{python3_sitelib}/crit-*.egg-info
%{python3_sitelib}/pycriu

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
