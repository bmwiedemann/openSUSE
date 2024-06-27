#
# spec file for package passt
#
# PASST - Plug A Simple Socket Transport
#  for qemu/UNIX domain socket mode
#
# PASTA - Pack A Subtle Tap Abstraction
#  for network namespace/tap device mode
#
# Copyright (c) 2022 Red Hat GmbH
# Author: Stefano Brivio <sbrivio@redhat.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Copyright (c) 2022, Dario Faggioli <dfaggioli@suse.com>
# Copyright (c) 2024, SUSE LLC
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

# We currently have SELinux only on Tumbleweed and in ALP
# but there's no apparmor in ALP
%if 0%{?suse_version} > 1600
# TW
%bcond_without selinux
%bcond_without apparmor
%else
%if 0%{?suse_version} == 1600
# ALP
%bcond_without selinux
%bcond_with apparmor
%else
# Leap & SLE
%bcond_with selinux
%bcond_without apparmor
%endif
%endif

Name:           passt
Version:        20240624.1ee2eca
Release:        0
Summary:        User-mode networking daemons for virtual machines and namespaces
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          System/Daemons
URL:            https://passt.top/
Source:         %{name}-%{version}.tar.zst

BuildRequires:  zstd
BuildRequires:  gcc, make
%if %{with selinux}
BuildRequires:  checkpolicy, selinux-policy-devel
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-targeted)
%endif
%if %{with apparmor}
BuildRequires:  apparmor-abstractions, apparmor-rpm-macros, libapparmor-devel
%endif

%description
passt implements a translation layer between a Layer-2 network interface and
native Layer-4 sockets (TCP, UDP, ICMP/ICMPv6 echo) on a host. It doesn't
require any capabilities or privileges, and it can be used as a simple
replacement for Slirp.

pasta (same binary as passt, different command) offers equivalent functionality,
for network namespaces: traffic is forwarded using a tap interface inside the
namespace, without the need to create further interfaces on the host, hence not
requiring any capabilities or privileges.

%if %{with selinux}
%package    selinux
BuildArch:  noarch
Summary:    SELinux support for passt and pasta
Requires:   %{name} = %{version}-%{release}
Requires:   selinux-policy
Requires(post): %{name}
Requires(post): policycoreutils
Requires(preun): %{name}
Requires(preun): policycoreutils

%description selinux
This package adds SELinux enforcement to passt(1) and pasta(1).
%endif

%prep
%autosetup

%build
%set_build_flags
%make_build VERSION=%{version}-%{release}

%install
%make_install prefix=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} docdir=%{_docdir}/%{name}
%ifarch x86_64
ln -sr %{buildroot}%{_mandir}/man1/passt.1 %{buildroot}%{_mandir}/man1/passt.avx2.1
ln -sr %{buildroot}%{_mandir}/man1/pasta.1 %{buildroot}%{_mandir}/man1/pasta.avx2.1
%endif

%if %{with apparmor}
pushd contrib/apparmor
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d/abstractions
install -m 0644 usr.bin.{passt,pasta} %{buildroot}%{_sysconfdir}/apparmor.d/
install -m 0644 abstractions/{passt,pasta} %{buildroot}%{_sysconfdir}/apparmor.d/abstractions
popd
# apparmor doesn't apply different profiles
# to symlinks, override here with hard links
# https://github.com/containers/buildah/issues/5440
ln -f passt %{buildroot}%{_bindir}/pasta
%ifarch x86_64
ln -f passt.avx2 %{buildroot}%{_bindir}/pasta.avx2
%endif
%endif

%if %{with selinux}
pushd contrib/selinux
make -f %{_datadir}/selinux/devel/Makefile
install -p -m 644 -D passt.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/passt.pp
install -p -m 644 -D passt.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/passt.if
install -p -m 644 -D pasta.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/pasta.pp
popd
%endif

%if %{with apparmor}
%post
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.passt
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.pasta
%endif

%if %{with selinux}
%post selinux
semodule -i %{_datadir}/selinux/packages/%{name}/passt.pp 2>/dev/null || :
semodule -i %{_datadir}/selinux/packages/%{name}/pasta.pp 2>/dev/null || :

%preun selinux
semodule -r passt 2>/dev/null || :
semodule -r pasta 2>/dev/null || :
%endif

%files
%license LICENSES/{GPL-2.0-or-later.txt,BSD-3-Clause.txt}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/demo.sh
%{_bindir}/passt
%{_bindir}/pasta
%{_bindir}/qrap
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions/
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.bin.passt
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.bin.pasta
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/pas*
%endif
%{_mandir}/man1/passt.1*
%{_mandir}/man1/pasta.1*
%{_mandir}/man1/qrap.1*
%ifarch x86_64
%{_bindir}/passt.avx2
%{_mandir}/man1/passt.avx2.1*
%{_bindir}/pasta.avx2
%{_mandir}/man1/pasta.avx2.1*
%endif

%if %{with selinux}
%files selinux
%dir %{_datadir}/selinux/packages/%{name}
%{_datadir}/selinux/packages/%{name}/passt.pp
%{_datadir}/selinux/packages/%{name}/pasta.pp
%dir %{_datadir}/selinux/devel/include/distributed
%{_datadir}/selinux/devel/include/distributed/passt.if
%endif

%changelog
