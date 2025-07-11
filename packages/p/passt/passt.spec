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

%global selinuxtype targeted
Name:           passt
Version:        20250611.0293c6f
Release:        0
Summary:        User-mode networking daemons for virtual machines and namespaces
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          System/Daemons
URL:            https://passt.top/
Source:         %{name}-%{version}.tar.zst

BuildRequires:  zstd
BuildRequires:  gcc, make
%if %{with selinux}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-targeted)
%endif
%if %{with apparmor}
BuildRequires:  apparmor-abstractions, apparmor-rpm-macros, libapparmor-devel
Requires:       (%{name}-apparmor if apparmor-abstractions)
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

%if %{with apparmor}
%package        apparmor
BuildArch:      noarch
Summary:        Apparmor profiles for passt and pasta
Requires:       %{name} = %{version}-%{release}
Requires:       apparmor-abstractions
Requires(post): apparmor-parser

%description apparmor
This package contains Apparmor profiles for passt and pasta.
%endif

%if %{with selinux}
%package            selinux
BuildArch:          noarch
Summary:            SELinux support for passt and pasta
Requires:           %{name} = %{version}-%{release}
Requires:           selinux-policy
Requires:           container-selinux
Requires(post):     policycoreutils
Requires(post):     container-selinux
Requires(preun):    policycoreutils
BuildRequires:      checkpolicy
BuildRequires:      selinux-policy-devel
Recommends:         selinux-policy-%{selinuxtype}

%description selinux
This package adds SELinux enforcement to passt(1) and pasta(1).
%endif

%prep
%autosetup

%build
%set_build_flags
# The Makefile creates symbolic links for pasta, but we need actual copies for
# SELinux file contexts to work as intended. Same with pasta.avx2 if present.
# Build twice, changing the version string, to avoid duplicate Build-IDs.
# Ran into something similar for apparmor - https://github.com/containers/buildah/issues/5440.
%make_build VERSION=%{version}-%{release}-pasta
%ifarch x86_64
mv -f passt.avx2 pasta.avx2
%make_build passt passt.avx2 VERSION="%{version}-%{release}"
%else
%make_build passt VERSION="%{version}-%{release}"
%endif


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
install -p -m 644 -D passt.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/passt.pp
install -p -m 644 -D passt-repair.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/passt-repair.pp
install -p -m 644 -D pasta.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/pasta.pp
install -p -m 644 -D passt.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/passt.if
popd
%endif

%if %{with apparmor}
%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.passt
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.pasta
%endif

%if %{with selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/passt.pp %{_datadir}/selinux/packages/%{selinuxtype}/passt-repair.pp %{_datadir}/selinux/packages/%{selinuxtype}/pasta.pp

%postun selinux
if [ $1 -eq 0 ]; then
        %selinux_modules_uninstall -s %{selinuxtype} passt pasta passt-repair
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
# %selinux_relabel_post calls fixfiles(8) with the previous file_contexts file
# (see selabel_file(5)) in order to restore only the file contexts which
# actually changed. However, as file_contexts doesn't support %{USERID}
# substitutions, this will not work for specific file contexts that pasta needs
# to have under /run/user. Restore those explicitly.
#
# https://passt.top/passt/commit/?id=e019323538699967c155c29411545223dadfc0f5
restorecon -R /run/user 2>/dev/null
%endif

%files
%license LICENSES/{GPL-2.0-or-later.txt,BSD-3-Clause.txt}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/demo.sh
%{_bindir}/passt
%{_bindir}/pasta
%{_bindir}/qrap
%{_bindir}/passt-repair
%{_mandir}/man1/passt.1*
%{_mandir}/man1/pasta.1*
%{_mandir}/man1/qrap.1*
%{_mandir}/man1/passt-repair.1*
%ifarch x86_64
%{_bindir}/passt.avx2
%{_mandir}/man1/passt.avx2.1*
%{_bindir}/pasta.avx2
%{_mandir}/man1/pasta.avx2.1*
%endif

%if %{with selinux}
%files selinux
%dir %{_datadir}/selinux/packages/%{selinuxtype}
%{_datadir}/selinux/packages/%{selinuxtype}/passt.pp
%{_datadir}/selinux/packages/%{selinuxtype}/pasta.pp
%{_datadir}/selinux/packages/%{selinuxtype}/passt-repair.pp
%dir %{_datadir}/selinux/devel/include/distributed
%{_datadir}/selinux/devel/include/distributed/passt.if
%endif

%if %{with apparmor}
%files apparmor
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions/
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.bin.passt
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.bin.pasta
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/pas*
%endif

%changelog
