#
# spec file for package dump
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


Name:           dump
Version:        0.4b49
Release:        0
Summary:        Programs for backing up and restoring ext2/3/4 filesystems
License:        BSD-3-Clause
Group:          Productivity/Archiving/Backup
URL:            http://dump.sourceforge.net
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        ermt.1.in
# PATCH-FIX-SUSE dump-0.4b46-pathnames.patch svalx@svalx.net -- pathnames and
# symlinks configuration for dump and restore
Patch0:         %{name}-0.4b46-pathnames.patch
# PATCH-FIX-UPSTREAM dump-0.4b46-rmt-ermt.patch svalx@svalx.net -- Independent rmt and
# ermt build, change its locations to _bindir
Patch1:         %{name}-0.4b46-rmt-ermt.patch
Patch3:         %{name}-0.4b43-include.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  libbz2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  lzo-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite3-devel
BuildRequires:  zlib-devel
Recommends:     %{name}-rmt = %{version}
Recommends:     mt

%description
The dump package contains both dump and restore.  Dump examines files
in a file system, determines which ones need to be backed up, and
copies those files to a specified disk, tape, or other storage medium.
The restore command performs the inverse function of dump. It can
restore a full backup of a file system.

%package	rmt
Summary:        Provides certain programs with access to remote tape devices
Group:          Productivity/Archiving/Backup
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       rmt

%description	rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup), tar (an archiving program) and cpio.

%prep
%setup -q
cp %{SOURCE1} rmt/
%autopatch -p1

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fcommon"
%configure \
  --disable-silent-rules \
  --enable-sqlite \
  --enable-ermt \
  --enable-rmt=no \
  --with-rmtpath=%{_bindir}
%make_build

%install
%make_install
mv examples/encrypted_rmt .
# Alternatives system
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/rmt %{buildroot}%{_bindir}/rmt
ln -sf %{_sysconfdir}/alternatives/rmt.1%{ext_man} %{buildroot}%{_mandir}/man1/rmt.1%{ext_man}

%post rmt
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/rmt rmt %{_bindir}/ermt 20 \
    --slave %{_mandir}/man1/rmt.1%{ext_man} rmt.1%{ext_man} %{_mandir}/man1/ermt.1%{ext_man}

%postun rmt
if [ ! -f %{_bindir}/ermt ] ; then
   "%{_sbindir}/update-alternatives" --remove rmt %{_bindir}/ermt
fi

%files
%{_sbindir}/dump
%{_sbindir}/restore
%{_mandir}/man8/dump.8%{?ext_man}
%{_mandir}/man8/restore.8%{?ext_man}
%license COPYING
%doc NEWS KNOWNBUGS MAINTAINERS README REPORTING-BUGS
%doc AUTHORS TODO dump.lsm examples

%files rmt
%ghost %{_bindir}/rmt
%{_bindir}/ermt
%ghost %{_mandir}/man1/rmt.1%{ext_man}
%{_mandir}/man1/ermt.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/rmt
%ghost %{_sysconfdir}/alternatives/rmt.1%{ext_man}
%doc encrypted_rmt/README

%changelog
