#
# spec file for package smc-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# aarch64 and ppc64le don't support 32bit applications, so there's no
# gcc-32bit package that can be installed
%ifarch s390x x86_64
%define have_32bit 1
BuildRequires:  gcc-32bit
%endif

# While repos other than Factory have 32bit for s390x, Factory does not
%if 0%{?suse_version} == 1550
%ifarch s390x
%define have_32bit 0
%endif
%endif

Name:           smc-tools
Version:        1.1.0
Release:        0
Summary:        Shared Memory Communication via RDMA
License:        EPL-1.0
Group:          System/Kernel
URL:            https://www.ibm.com/developerworks/linux/linux390/smc-tools.html
Source:         %{name}-%{version}.tar.gz
Source1:        smc-tools-rpmlintrc

BuildRequires:  libnl3-devel
PreReq:         permissions

%description
Shared Memory Communication via RDMA (SMC) is a socket over RDMA
communication protocol that allows existing TCP socket applications to
transparently benefit from RDMA when exchanging data via an RDMA over
Converged Ethernet (RoCE) network.

The tools provided in this package allow existing TCP applications
to use a RoCE network without needing to make changes in them.

%prep
%setup -q

%build
MYCFLAGS=$(grep ^CFLAGS Makefile | cut -f2 -d=)
make %{?_smp_mflags} V=1 CFLAGS="${MYCFLAGS} %{optflags}"

%install
%make_install V=1

%ifarch s390 %{ix86}
rm -Rf "%{buildroot}%{_prefix}/lib64"
%endif

%verifyscript
%verify_permissions -e %{_prefix}/lib/libsmc-preload.so
%verify_permissions -e %{_libdir}/libsmc-preload.so

%post
%set_permissions %{_prefix}/lib/libsmc-preload.so
%set_permissions %{_libdir}/libsmc-preload.so

%files
%defattr(-,root,root)
%license LICENSE
%doc README.smctools
%{_bindir}/smc_pnet
%{_bindir}/smc_run
%{_bindir}/smcss
%{_libdir}/libsmc-preload.so
%if 0%{?have_32bit}
%{_prefix}/lib/libsmc-preload.so
%endif
%{_mandir}/man7/af_smc.7%{?ext_man}
%{_mandir}/man8/smc_pnet.8%{?ext_man}
%{_mandir}/man8/smc_run.8%{?ext_man}
%{_mandir}/man8/smcss.8%{?ext_man}

%changelog
