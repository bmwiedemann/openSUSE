#
# spec file for package appimaged
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


Name:           appimaged
Version:        10
Release:        0
URL:            http://www.appimage.org
Summary:        Daemon handles (un)registering AppImages with the system
License:        MIT
Group:          System/Daemons
Source0:        AppImageKit-%version.tar.xz
Source1:        appimaged.service
Patch0:         gcc14,patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  inotify-tools-devel
BuildRequires:  libarchive-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz-devel
Requires:       zsync

%description
appimaged is a daemon that handles registering and unregistering AppImages
with the system (e.g., menu entries, icons, MIME types, binary delta updates,
and such).

The package comes also with appimage.validate CLI tool to verify signature
of AppImage files.

%prep
%autosetup -p1 -n AppImageKit-%version
sed -i -e s,^version=.*,version=%version, build.sh

%build
export PATH=$PWD/bin:$PATH
# Upstream squashfuse is not providing a lib, so it gets patched to produce one here
cd squashfuse
patch -p1 < ../squashfuse.patch
export ACLOCAL_FLAGS="-I /usr/share/aclocal"
libtoolize --force
aclocal
autoheader
automake --force-missing --add-missing
autoreconf -fi || true # Errors out, but the following succeeds then?
autoconf
sed -i '/PKG_CHECK_MODULES.*/,/,:./d' configure # https://github.com/vasi/squashfuse/issues/12
./configure --disable-demo --disable-high-level --without-lzo --without-lz4
make
cd ..

CC=gcc
$CC -std=gnu99 -o appimaged -I./squashfuse/ ./getsection.c ./notify.c ./elf.c ./appimaged.c \
  -D_FILE_OFFSET_BITS=64 -DHAVE_LIBARCHIVE3=0 -DVERSION_NUMBER=\"%version\" \
  ./squashfuse/.libs/libsquashfuse.a ./squashfuse/.libs/libfuseprivate.a \
  -Wl,-Bdynamic -linotifytools -larchive \
  -Wl,--as-needed \
  $(pkg-config --cflags --libs glib-2.0) \
  $(pkg-config --cflags --libs gio-2.0) \
  $(pkg-config --cflags --libs cairo) \
  -ldl -lpthread -lz -llzma

# basic tool for validation of downloaded appimage files
$CC -o appimage.validate ./getsection.c ./validate.c -Wl,-Bdynamic -lssl -lcrypto \
  -Wl,--as-needed $(pkg-config --cflags --libs glib-2.0) -lz -ldl

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 appimaged appimage.validate %{buildroot}%{_bindir}

# install systemd per user service
mkdir -p %{buildroot}%{_userunitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_userunitdir}/appimaged.service

%post
%systemd_user_post appimaged.service

%preun
%systemd_user_preun appimaged.service

%postun
%systemd_user_postun appimaged.service

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/appimage.validate
%{_bindir}/appimaged
%{_userunitdir}/appimaged.service

%changelog
