#
# spec file for package guix
#
# Copyright (c) 2022 SUSE LLC
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


%define guile	guile-2.0.9.tar.xz
%define guix_builder_group	guixbuild
Name:           guix
Version:        1.3.0
Release:        0
Summary:        GNU Package manager
License:        GPL-3.0-only
Group:          System/Packages
URL:            http://www.gnu.org/software/guix/
Source0:        https://ftp.gnu.org/gnu/guix/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/guix/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
# source file renamed - this would lead to 3 same file names
# http://alpha.gnu.org/gnu/guix/bootstrap/i686-linux/20131110/%%{guile}
Source3:        i686-linux-%{guile}
# http://alpha.gnu.org/gnu/guix/bootstrap/x86_64-linux/20131110/%%{guile}
Source4:        x86_64-linux-%{guile}
# http://alpha.gnu.org/gnu/guix/bootstrap/mips64el-linux/20131110/%%{guile}
Source5:        mips64el-linux-%{guile}
# http://alpha.gnu.org/gnu/guix/bootstrap/armhf-linux/20150101/guile-2.0.11.tar.xz
Source6:        armhf-linux-guile-2.0.11.tar.xz
Source10:       guix-rpmlintrc
Source11:       armhf-linux-guile-2.0.11.tar.xz.sig
# http://alpha.gnu.org/gnu/guix/bootstrap/aarch64-linux/20170217/guile-2.0.14.tar.xz
Source12:       aarch64-linux-guile-2.0.14.tar.xz
Source13:       aarch64-linux-guile-2.0.14.tar.xz.sig
Source20:       run_guix_daemon.sh
Source21:       run_guix_publish.sh
BuildRequires:  gcc-c++
BuildRequires:  gnutls-guile
BuildRequires:  guile-charting
BuildRequires:  guile-devel >= 2.2
BuildRequires:  guile-gcrypt
BuildRequires:  guile-git
BuildRequires:  guile-json
BuildRequires:  guile-lzlib
BuildRequires:  guile-sqlite3
BuildRequires:  guile-ssh-devel
BuildRequires:  guile-zlib
# this is actually just to make guile-git working
BuildRequires:  libgcrypt-devel
BuildRequires:  libgit2-devel
BuildRequires:  pkgconfig
BuildRequires:  shepherd
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(sqlite3)
Requires:       gnutls-guile
Requires:       guile
Requires:       guile-gcrypt
Requires:       guile-git
Requires:       guile-json
Requires:       guile-lzlib
Requires:       guile-sqlite3
Requires:       guile-ssh-devel
Requires:       guile-zlib
Requires:       gzip
Requires:       libgcrypt-devel
Requires:       libguile-ssh14
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64 armv7hl aarch64
Provides:       %{_libexecdir}/guix/guile

%description
Purely functional package manager and a distribution thereof.
It offers transactional upgrades, roll-backs, unprivileged package management.
As a GNU distribution it contains only free software.

%prep
%setup -q
# install service file to _unitdir
sed -i 's@\$(libdir)/systemd/system@%{_unitdir}@' Makefile.in
mkdir -p gnu/packages/bootstrap/{i686,x86_64,mips64el,armhf,aarch64}-linux
cp %{SOURCE3} gnu/packages/bootstrap/i686-linux/%{guile}
cp %{SOURCE4} gnu/packages/bootstrap/x86_64-linux/%{guile}
cp %{SOURCE5} gnu/packages/bootstrap/mips64el-linux/%{guile}
cp %{SOURCE6} gnu/packages/bootstrap/armhf-linux/guile-2.0.11.tar.xz
cp %{SOURCE12} gnu/packages/bootstrap/aarch64-linux/guile-2.0.14.tar.xz

%build
export GUILE_WARN_DEPRECATED
%configure \
	   --disable-silent-rules \
     --with-bash-completion-dir=%{_datadir}/bash-completion/completions
# guile 2.2.6 core dumps while build guix with more then 3 threads. See https://issues.guix.gnu.org/issue/36811
# building in parallel makes build results nondeterministic (boo#1170378)
make

%install
%make_install
%find_lang %{name}
%find_lang guix-packages
rm %{buildroot}%{_infodir}/dir
install -d -m 0755 %{buildroot}/gnu
install -d -m 0755 %{buildroot}/gnu/store
# only systemd is used, so upstart or sysv init files are not needed
rm -rvf %{buildroot}%{_libdir}/upstart %{buildroot}%{_sysconfdir}/init.d/guix-daemon %{buildroot}%{_sysconfdir}/openrc
install -m 0755 -t %{buildroot}%{_bindir} %{SOURCE20}
install -m 0755 -t %{buildroot}%{_bindir} %{SOURCE21}
sed -i 's@^ExecStart=.*@ExecStart=/usr/bin/run_guix_daemon.sh@' %{buildroot}%{_unitdir}/guix-daemon.service
sed -i 's@^ExecStart=.*@ExecStart=/usr/bin/run_guix_publish.sh@' %{buildroot}%{_unitdir}/guix-publish.service

%pre
%{_sbindir}/groupadd -r %{guix_builder_group} >/dev/null 2>/dev/null || :
for i in `seq 1 5`; do
    %{_sbindir}/useradd -r -o -g %{guix_builder_group} -G %{guix_builder_group} \
        -u $((60+$i)) -c "Guix builder $i" -s /sbin/nologin \
        -d %{_localstatedir}/empty guix-builder$i 2> /dev/null || :
done
%service_add_pre guix-daemon.service
%service_add_pre guix-publish.service

%preun
%service_del_preun guix-daemon.service
%service_del_preun guix-publish.service

%post
%install_info --info-dir=%{_infodir} %{_infodir}/guix.info.gz
%service_add_post guix-daemon.service
%service_add_post guix-publish.service
# Authorize official keys of Guix build farm to enable binary substitutes
for key in %{_datadir}/guix/*.pub; do
    guix archive --authorize < "$key"
done

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/guix.info.gz
%service_del_postun guix-daemon.service
%service_del_postun guix-publish.service

%files -f %{name}.lang -f guix-packages.lang
%defattr(-,root,root)
%license COPYING
%doc README NEWS
%{_bindir}/*guix*
%{_datadir}/bash-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/guix.fish
%{_datadir}/guile
%{_datadir}/guix
%dir %{_datadir}/selinux
%{_datadir}/selinux/guix-daemon.cil
%{_datadir}/zsh
%{_infodir}/guix*
%{_infodir}/images
%{_libdir}/guile/*
# Guile wrapper shipped by Guix to silence locale warnings
%dir %{_libexecdir}/guix
%{_libexecdir}/guix/guile
%{_mandir}/man1/guix*
%{_unitdir}/guix*.service
%{_unitdir}/gnu-store.mount
%attr(755,root,root) %dir /gnu
%attr(775,root,%{guix_builder_group}) %dir /gnu/store

%changelog
