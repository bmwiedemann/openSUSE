#
# spec file for package cdemu-daemon
#
# Copyright (c) 2021 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           cdemu-daemon
Version:        3.2.5
Release:        0
Summary:        Device daemon for cdemu, a virtual CD-ROM device emulator
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://cdemu.sourceforge.io/about/daemon/

#Git-Clone:	https://github.com/cdemu/cdemu
Source:         https://downloads.sf.net/cdemu/%name-%version.tar.xz
Source2:        60-vhba.rules
Source3:        cdemu-daemon.sysconfig
BuildRequires:  cmake >= 2.8.5
BuildRequires:  intltool >= 0.21
BuildRequires:  pkg-config >= 0.16
BuildRequires:  pkgconfig(ao) >= 0.8.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.30
BuildRequires:  pkgconfig(glib-2.0) >= 2.30
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.30
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30
BuildRequires:  pkgconfig(gthread-2.0) >= 2.30
BuildRequires:  pkgconfig(libmirage) >= 3.2.0
Requires(pre):  %fillup_prereq
Requires:       vhba-kmp
Recommends:     %name-lang

%lang_package

%description
cdemu-daemon receives SCSI commands from kernel module thorugh the
VHBA module and processes them, passing the requested data back to
the kernel. The daemon implements the actual virtual device; one
instance per each device registered by kernel module. It uses
libmirage for the image access (e.g. sector reading).

The daemon registers itself on D-BUS's system or session bus
(depending on the options passed to it) where it exposes an interface
that can be used by clients to control it.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR:PATH="%_libexecdir"
%cmake_build

%install
b="%buildroot"
%cmake_install
mkdir -p "$b/%_sbindir" "$b/%_fillupdir" \
	"$b/%_prefix/lib/udev/rules.d"
install -pm0644 "%{S:2}" "$b/%_prefix/lib/udev/rules.d/60-vhba.rules"
install -pm0644 "%{S:3}" "$b/%_fillupdir/sysconfig.cdemu-daemon"
%find_lang %name

%post
%fillup_only

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/cdemu-daemon
%_mandir/man8/cdemu-daemon.8*
%_fillupdir/sysconfig.cdemu-daemon
%_prefix/lib/udev/

%changelog
