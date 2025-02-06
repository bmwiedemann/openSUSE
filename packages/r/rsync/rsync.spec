#
# spec file for package rsync
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


%if 0%{?suse_version} >= 1550
%bcond_without xxhash
%else
%bcond_with xxhash
%endif

%if 0%{?suse_version} < 1550
%bcond_without gcc11
%else
%bcond_with gcc11
%endif

%if 0%{?suse_version} < 1600
%bcond_without slp
%else
%bcond_with slp
%endif

Name:           rsync
Version:        3.4.1
Release:        0
Summary:        Versatile tool for fast incremental file transfer
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://rsync.samba.org/
Source:         https://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
Source1:        https://rsync.samba.org/ftp/rsync/src/rsync-patches-%{version}.tar.gz
Source2:        logrotate.rsync
Source3:        rsyncd.socket
Source4:        rsyncd.rc
Source5:        rsyncd.conf
Source6:        rsyncd.secrets
Source8:        rsyncd.service
Source9:        rsyncd@.service
Source10:       https://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz.asc
Source11:       https://rsync.samba.org/ftp/rsync/src/rsync-patches-%{version}.tar.gz.asc
Source12:       %{name}.keyring
Source13:       rsyncd
Patch0:         rsync-no-libattr.patch
Patch2:         rsync-usr-etc.patch
Patch3:         rsync-run-dir.patch
# https://github.com/RsyncProject/rsync/pull/639
Patch5:         rsyncd-return-from-list-command-with-0.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  libacl-devel
BuildRequires:  liblz4-devel
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
%if %{with xxhash}
BuildRequires:  pkgconfig(libxxhash) >= 0.8.0
%endif
%if %{with gcc11}
BuildRequires:  gcc11-c++
%endif
%if %{with slp}
BuildRequires:  openslp-devel
%endif
BuildRequires:  pkgconfig(openssl)
Requires(post): grep
Requires(post): sed
Recommends:     logrotate

%description
Rsync is a fast and extraordinarily versatile file  copying  tool. It can copy
locally, to/from another host over any remote shell, or to/from a remote rsync
daemon. It offers a large number of options that control every aspect of its
behavior and permit very flexible specification of the set of files to be
copied. It is famous for its delta-transfer algorithm, which reduces the amount
of data sent over the network by sending only the differences between the
source files and the existing files in the destination. Rsync is widely used
for backups and mirroring and as an improved copy command for everyday use.

%prep
%setup -q -b 1
rm -f zlib/*.h zlib/*.c

%if %{with slp}
patch -p1 < patches/slp.diff
%endif

%autopatch -p1

%build
autoreconf -fiv
%if %{with gcc11}
export CC=gcc-11
export CXX=g++-11
%endif
export CFLAGS="%{optflags} -fPIC -DPIC -fPIE"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,relro,-z,now -fPIE -pie"
%configure \
  --with-included-popt=no \
  --with-included-zlib=no \
  --disable-debug \
%if 0%{?suse_version} > 1500
  --with-rsyncd-distconf=%{_distconfdir}/rsyncd.conf \
%endif
%if !%{with xxhash}
  --disable-xxhash\
%endif
%ifarch x86_64
  --enable-roll-simd \
%endif
%if %{with slp}
  --enable-slp \
%endif
  --enable-acl-support \
  --enable-xattr-support
%make_build reconfigure
%make_build

%check
chmod +x support/*
%make_build check
chmod -x support/*

%install
%make_install
rm -f %{buildroot}%{_sbindir}/rsyncd
install -d %{buildroot}%{_sysconfdir}/init.d
install -d %{buildroot}%{_sysconfdir}/xinetd.d
install -d %{buildroot}%{_sbindir}
install -m 755 %{SOURCE13} %{buildroot}%{_sbindir}/rsyncd
install -m 755 support/rsyncstats %{buildroot}%{_bindir}
%if 0%{?suse_version} > 1500
install -d %{buildroot}%{_distconfdir}/logrotate.d
install -m 644 %{SOURCE2} %{buildroot}%{_distconfdir}/logrotate.d/rsync
install -m 644 %{SOURCE5} %{buildroot}%{_distconfdir}/rsyncd.conf
install -m 600 %{SOURCE6} %{buildroot}%{_distconfdir}/rsyncd.secrets
echo "# This is a template only. Create your own entries in /etc/rsyncd.secrets" >>%{buildroot}%{_distconfdir}/rsyncd.secrets
echo
%else
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/rsync
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/rsyncd.conf
install -m 600 %{SOURCE6} %{buildroot}%{_sysconfdir}/rsyncd.secrets
%endif
install -D -m 0644 %{SOURCE9} %{buildroot}%{_unitdir}/rsyncd@.service
install -D -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/rsyncd.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/rsyncd.socket
%if 0%{?suse_version} < 1600
ln -sf service %{buildroot}%{_sbindir}/rcrsyncd
%endif
chmod -x support/*

%pre
%service_add_pre rsyncd.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/rsync rsyncd.conf rsyncd.secrets; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/rsync rsyncd.conf rsyncd.secrets; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%preun
%service_del_preun rsyncd.service

%post
%service_add_post rsyncd.service

%postun
%service_del_postun rsyncd.service

%files
%license COPYING
%doc NEWS.md README.md tech_report.tex support/
%{_unitdir}/rsyncd@.service
%{_unitdir}/rsyncd.service
%{_unitdir}/rsyncd.socket
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/rsync
%{_distconfdir}/rsyncd.conf
%{_distconfdir}/rsyncd.secrets
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/rsync
%config(noreplace) %{_sysconfdir}/rsyncd.conf
%config(noreplace) %{_sysconfdir}/rsyncd.secrets
%endif
%if 0%{?suse_version} < 1600
%{_sbindir}/rcrsyncd
%endif
%{_sbindir}/rsyncd
%{_bindir}/rsyncstats
%{_bindir}/rsync
%{_bindir}/rsync-ssl
%{_mandir}/man1/rsync.1%{?ext_man}
%{_mandir}/man1/rsync-ssl.1%{?ext_man}
%{_mandir}/man5/rsyncd.conf.5%{?ext_man}

%changelog
