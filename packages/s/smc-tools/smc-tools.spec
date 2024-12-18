#
# spec file for package smc-tools
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


Name:           smc-tools
Version:        1.8.4
Release:        0
Summary:        Shared Memory Communication via RDMA
License:        EPL-1.0
Group:          System/Kernel
URL:            https://www.ibm.com/developerworks/linux/linux390/smc-tools.html
Source:         https://github.com/ibm-s390-linux/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
### Source:     https://github.com/ibm-s390-linux/smc-tools/releases/tag/1.8.3.tar.gz

BuildRequires:  bash-completion-devel
BuildRequires:  libnl3-devel
PreReq:         permissions

%description
Shared Memory Communication via RDMA (SMC) is a socket over RDMA
communication protocol that allows existing TCP socket applications to
transparently benefit from RDMA when exchanging data via an RDMA over
Converged Ethernet (RoCE) network.

The tools provided in this package allow existing TCP applications
to use a RoCE network without needing to make changes in them.

%package completion
Summary:        Bash completion for smc-tools
Group:          System/Kernel

Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description completion
This package contains the files to enable command completion for the
smc-tools package when running a bash shell.

%prep
%autosetup -p1

%build
# The next two lines are to get around the Makefile not adding
# its own values to CFLAGS if it is already set. This is needed
# so that we can specify the optflags macro to pull in our own
# parameters.
MYCFLAGS=$(grep ^CFLAGS Makefile | head -n1 | cut -f2 -d=)
MYCFLAGS+=" $(pkg-config --silence-errors --cflags libnl-genl-3.0)"
%make_build CFLAGS="${MYCFLAGS} %{optflags}"

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
%license LICENSE
%doc README.md
%{_bindir}/smc_dbg
%{_bindir}/smc_pnet
%{_bindir}/smc_run
%{_bindir}/smcd
%{_bindir}/smcr
%ifarch s390 s390x
%{_bindir}/smc_chk
%{_bindir}/smc_rnics
%endif
%{_bindir}/smcss
%{_libdir}/libsmc-preload.so
%{_mandir}/man7/af_smc.7%{?ext_man}
%{_mandir}/man8/smc_pnet.8%{?ext_man}
%ifarch s390 s390x
%{_mandir}/man8/smc_rnics.8%{?ext_man}
%{_mandir}/man8/smc_chk.8%{?ext_man}
%endif
%{_mandir}/man8/smcd.8%{?ext_man}
%{_mandir}/man8/smcd-device.8%{?ext_man}
%{_mandir}/man8/smcd-info.8%{?ext_man}
%{_mandir}/man8/smcd-linkgroup.8%{?ext_man}
%{_mandir}/man8/smcd-seid.8%{?ext_man}
%{_mandir}/man8/smcd-stats.8%{?ext_man}
%{_mandir}/man8/smcd-ueid.8%{?ext_man}
%{_mandir}/man8/smcr.8%{?ext_man}
%{_mandir}/man8/smcr-device.8%{?ext_man}
%{_mandir}/man8/smcr-info.8%{?ext_man}
%{_mandir}/man8/smcr-linkgroup.8%{?ext_man}
%{_mandir}/man8/smcr-stats.8%{?ext_man}
%{_mandir}/man8/smcr-ueid.8%{?ext_man}
%{_mandir}/man8/smc_run.8%{?ext_man}
%{_mandir}/man8/smcss.8%{?ext_man}

%files completion
%{_datadir}/bash-completion/completions/smc*

%changelog
