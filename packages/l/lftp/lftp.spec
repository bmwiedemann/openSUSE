#
# spec file for package lftp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           lftp
Version:        4.8.4
Release:        0
Summary:        Command Line File Transfer Program
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Ftp/Clients
URL:            http://lftp.yar.ru/
Source:         http://lftp.yar.ru/ftp/%{name}-%{version}.tar.xz
Source2:        http://lav.yar.ru/lav@yars.free.net-gpg-public-key#/%name.keyring
Source3:        http://lftp.yar.ru/ftp/%{name}-%{version}.tar.xz.asc
# PATCH-FEATURE-OPENSUSE lftp-ssl-cipher.patch pgajdos@suse.cz -- use stronger cipher [bnc#857148]
Patch0:         lftp-default-ssl-cipher.patch
# PATCH-FEATURE-OPENSUSE patch1-patch6 psimons@suse.com -- maintained at https://github.com/opensuse/lftp [bsc#1083331]
Patch1:         0001-Add-content-of-the-SUSE-lftp-vi-1.1-archive.patch
Patch2:         0002-Add-content-of-lftp-compat-addfiles.patch.patch
Patch3:         0003-Add-content-of-lftp-completion.patch.patch
Patch4:         0004-Include-config.h-to-detect-gnulib-macros.patch
Patch5:         0005-Add-the-wrapper-code-to-the-Makefile-in-order-to-bui.patch
Patch6:         relax-ssh-password-prompt-recognition.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  update-alternatives
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(zlib)
Requires:       less
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      ftp

%description
LFTP is a reliable shell-like command line FTP client. It can retry
operations and does reget automatically. It can do several transfers
simultaneously in the background. With LFTP, you can start a transfer
in the background and continue browsing that FTP site or another one.
This is all done in one process. Background jobs are completed in nohup
mode if you exit or close the modem connection. LFTP has reput, mirror,
and reverse mirror among its features. Since version 2.0, it also
supports the HTTP protocol. Other features include IPV6 support,
context sensitive completion, output redirection to files or to pipe,
FTP and HTTP proxy support, transfer rate throttling for each
connection and for all connections in sum, job queueing, job execution
at specified times, opie and skey support in the FTP protocol, SSL for
HTTP and FTP, and FXP transfers.

%prep
%setup -q
%autopatch -p1

%build
# It's necessary to update the Autotools build system, because of patches 2-6
# that we apply above.
gettextize --force --copy --no-changelog
autoreconf --install --force
%configure \
   --disable-silent-rules \
   --without-included-regex \
   --disable-static \
   --with-modules \
   --without-gnutls \
   --with-openssl \
   --with-debug \
   --without-profiling \
   --enable-largefile \
   --with-pager=%{_bindir}/less \
   --with-libidn2 \
   --with-expat \
   --disable-rpath
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/ftp %{buildroot}%{_bindir}/ftp
ln -sf %{_sysconfdir}/alternatives/ftp.1.gz %{buildroot}%{_mandir}/man1/ftp.1.gz
%suse_update_desktop_file %{name} -G "FTP client" Network FileTransfer
%find_lang %{name}

%post
/sbin/ldconfig
update-alternatives --install %{_bindir}/ftp ftp %{_bindir}/%{name}_wrapper 5 \
  --slave %{_mandir}/man1/ftp.1.gz ftp.1 %{_mandir}/man1/%{name}.1.gz

%postun
/sbin/ldconfig
if [ "$1" = 0 ] ; then
  update-alternatives --remove ftp %{_bindir}/%{name}_wrapper
fi

%files -f "lftp.lang"
%license COPYING
%doc BUGS ChangeLog FAQ FEATURES README* NEWS THANKS TODO
%ghost %{_sysconfdir}/alternatives/ftp
%ghost %{_sysconfdir}/alternatives/ftp.1.gz
%{_bindir}/ftp
%{_mandir}/man1/ftp.1%{ext_man}
%config %{_sysconfdir}/lftp.conf
%{_bindir}/lftp
%{_bindir}/lftp_wrapper
%{_bindir}/lftpget
%{_datadir}/lftp
%dir %{_libdir}/lftp
%dir %{_libdir}/lftp/%{version}
%{_libdir}/lftp/%{version}/compat-mode.so
%{_libdir}/lftp/%{version}/cmd-mirror.so
%{_libdir}/lftp/%{version}/cmd-sleep.so
%{_libdir}/lftp/%{version}/cmd-torrent.so
%{_libdir}/lftp/%{version}/cmd-edit.so
%{_libdir}/lftp/%{version}/liblftp-network.so
%{_libdir}/lftp/%{version}/liblftp-pty.so
%{_libdir}/lftp/%{version}/proto-file.so
%{_libdir}/lftp/%{version}/proto-fish.so
%{_libdir}/lftp/%{version}/proto-ftp.so
%{_libdir}/lftp/%{version}/proto-http.so
%{_libdir}/lftp/%{version}/proto-sftp.so
%{_libdir}/liblftp-*.so
%{_libdir}/liblftp-*.so.*
%{_mandir}/man1/lftp.1%{ext_man}
%{_mandir}/man1/lftpget.1%{ext_man}
%{_mandir}/man5/lftp.conf.5%{ext_man}
%{_datadir}/applications/lftp.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/lftp-icon.png

%changelog
