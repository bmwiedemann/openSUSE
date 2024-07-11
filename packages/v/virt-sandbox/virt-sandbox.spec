#
# spec file for package virt-sandbox
#
# Copyright (c) 2023 SUSE LLC
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


%define so_version 1_0-5

Name:           virt-sandbox
Version:        0.8.0
Release:        0
URL:            http://libvirt.org/
Summary:        Libvirt application sandbox framework
License:        LGPL-2.0-or-later
Source0:        https://libvirt.org/sources/sandbox/libvirt-sandbox-%version.tar.gz
Source1:        %name.rpmlintrc

# Patches pending upstream review
Patch100:       no-unmount-for-lxc-machines.patch

# SUSE patches
Patch200:       PIE.patch
Patch300:       virt-sandbox.patch

# Need to go upstream

BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libvirt-glib-1.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rpcgen
# For virsh lxc-enter-namespace command
Requires:       libvirt-client
Requires:       python3-gobject
Requires:       libvirt-sandbox-%so_version = %version-%release

%package -n libvirt-sandbox-%so_version
Summary:        Libvirt application sandbox framework libraries
# So we get the full libvirtd daemon, not just client libs
Requires:       libvirt-daemon-lxc
Requires:       libvirt-daemon-qemu

%package -n typelib-1_0-LibvirtSandbox-1_0
Summary:        GLib and GObject mapping of libvirt-sandbox - gi-bindings

%package -n libvirt-sandbox-devel
Summary:        Libvirt application sandbox framework development files
Requires:       libvirt-sandbox-%so_version = %version-%release

%description
The %name package provides an API for building application
sandboxes using libvirt. Sandboxes can be based on either container
or machine based virtualization technology. Also included is a simple
command line tool for launching sandboxes for arbitrary commands.

%description -n libvirt-sandbox-%so_version
This package provides a framework for building application sandboxes
using libvirt.

%description -n libvirt-sandbox-devel
This package provides development header files and libraries for
the libvirt sandbox

%description -n typelib-1_0-LibvirtSandbox-1_0
This package provides Gnome-introspection bindings for building
applications within a sandbox using libvirt.

%prep
%autosetup -p1 -n libvirt-sandbox-%version

%build
CFLAGS='%optflags -Wno-deprecated-declarations'
autoreconf -f -i
%configure --enable-introspection --disable-static
%make_build

%install
chmod a-x examples/*.py examples/*.pl examples/*.js
%make_install
rm -f %buildroot/%_libdir/*.a
rm -f %buildroot/%_libdir/*.la

%find_lang libvirt-sandbox

%post -n libvirt-sandbox-%so_version -p /sbin/ldconfig
%postun -n libvirt-sandbox-%so_version -p /sbin/ldconfig

%files
%_bindir/virt-sandbox
%_mandir/man1/virt-sandbox.1*

%files -n libvirt-sandbox-%so_version -f libvirt-sandbox.lang
%doc NEWS
%license COPYING
%dir %_sysconfdir/libvirt-sandbox
%dir %_sysconfdir/libvirt-sandbox/scratch
%config %_sysconfdir/libvirt-sandbox/scratch/README
%_libexecdir/libvirt-sandbox-init-common
%_libexecdir/libvirt-sandbox-init-lxc
%_libexecdir/libvirt-sandbox-init-qemu
%_libdir/libvirt-sandbox-1.0.so.*

%files -n typelib-1_0-LibvirtSandbox-1_0
%_libdir/girepository-1.0/LibvirtSandbox-1.0.typelib

%files -n libvirt-sandbox-devel
%doc examples/virt-sandbox.pl
%doc examples/virt-sandbox.py
%doc examples/virt-sandbox.js
%doc examples/virt-sandbox-mkinitrd.py
%_libdir/libvirt-sandbox-1.0.so
%_libdir/pkgconfig/libvirt-sandbox-1.0.pc
%dir %_includedir/libvirt-sandbox-1.0
%dir %_includedir/libvirt-sandbox-1.0/libvirt-sandbox
%_includedir/libvirt-sandbox-1.0/libvirt-sandbox/libvirt-sandbox.h
%_includedir/libvirt-sandbox-1.0/libvirt-sandbox/libvirt-sandbox-*.h
%_datadir/gir-1.0/LibvirtSandbox-1.0.gir
%_datadir/gtk-doc/html/Libvirt-sandbox

%changelog
