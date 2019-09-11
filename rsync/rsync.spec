#
# spec file for package rsync
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rsync
Version:        3.1.3
Release:        0
Summary:        Versatile tool for fast incremental file transfer
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
Url:            http://rsync.samba.org/
Source:         http://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz
Source1:        http://rsync.samba.org/ftp/rsync/src/rsync-patches-%{version}.tar.gz
Source2:        logrotate.rsync
Source3:        rsyncd.socket
Source4:        rsyncd.rc
Source5:        rsyncd.conf
Source6:        rsyncd.secrets
Source8:        rsyncd.service
Source9:        rsyncd@.service
Source10:       http://rsync.samba.org/ftp/rsync/src/rsync-%{version}.tar.gz.asc
Source11:       http://rsync.samba.org/ftp/rsync/src/rsync-patches-%{version}.tar.gz.asc
Source12:       %{name}.keyring
Patch0:         rsync-no-libattr.patch
#PATCH-FIX-SUSE boo#922710 slp
Patch1:         rsync-add_back_use_slp_directive.patch
Patch2:         rsync-both-compressions.patch
#PATCH-FIX-UPSTREAM bsc#1062063 rsync doesn't stop on errors
Patch4:         rsync-send_error_to_sender.patch
Patch5:         rsync-avoid-uploading-after-error.patch
#PATCH-FIX-UPSTREAM bsc#1108562 file contents cause rsync to fail
Patch6:         rsync-fix-prealloc-to-keep-file-size-0-when-possible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libacl-devel
BuildRequires:  openslp-devel
BuildRequires:  popt-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
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
rm -f zlib/*.h
patch -p1 < patches/acls.diff
patch -p1 < patches/xattrs.diff
patch -p1 < patches/slp.diff
%patch1 -p1
# fate#312479
patch -p1 < patches/time-limit.diff
%patch0 -p1
%patch2 -p1
%patch4
%patch5
%patch6 -p1

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fPIC -DPIC -fPIE"
export LDFLAGS="-Wl,-z,relro,-z,now -pie"
%configure \
  --with-included-popt=no \
  --with-included-zlib=no \
  --disable-debug \
  --enable-slp \
  --enable-acl-support \
  --enable-xattr-support
make %{?_smp_mflags} reconfigure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
rm -f %{buildroot}%{_sbindir}/rsyncd
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}%{_sysconfdir}/init.d
install -d %{buildroot}%{_sysconfdir}/xinetd.d
install -d %{buildroot}%{_prefix}/sbin
ln -sf ../bin/rsync %{buildroot}%{_sbindir}/rsyncd
install -m 755 support/rsyncstats %{buildroot}%{_prefix}/bin
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/rsync
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/rsyncd.conf
install -m 600 %{SOURCE6} %{buildroot}%{_sysconfdir}/rsyncd.secrets
install -D -m 0644 %{SOURCE9} %{buildroot}%{_unitdir}/rsyncd@.service
install -D -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/rsyncd.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/rsyncd.socket
ln -sf service %{buildroot}%{_sbindir}/rcrsyncd

%pre
%service_add_pre rsyncd.service

%preun
%service_del_preun rsyncd.service

%post
%service_add_post rsyncd.service

%postun
%service_del_postun rsyncd.service

%files
%{_unitdir}/rsyncd@.service
%{_unitdir}/rsyncd.service
%{_unitdir}/rsyncd.socket
%config(noreplace) %{_sysconfdir}/rsyncd.conf
%config(noreplace) %{_sysconfdir}/rsyncd.secrets
%config(noreplace) %{_sysconfdir}/logrotate.d/rsync
%{_sbindir}/rcrsyncd
%{_sbindir}/rsyncd
%{_bindir}/rsyncstats
%{_bindir}/rsync
%{_mandir}/man1/rsync.1%{ext_man}
%{_mandir}/man5/rsyncd.conf.5%{ext_man}
%license COPYING
%doc NEWS README tech_report.tex

%changelog
