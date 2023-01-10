#
# spec file for package gvfs
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


%bcond_without  cdda
Name:           gvfs
Version:        1.50.3
Release:        0
Summary:        Virtual File System functionality for GLib
License:        GPL-3.0-only AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/gvfs
Source0:        https://download.gnome.org/sources/gvfs/1.50/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

### NOTE: Please, keep SLE-only patches at bottom (starting on 1000).
# PATCH-FEATURE-SLE gvfs-nds.patch ksamrat@novell.com -- Provides NDS browsing for nautilus
Patch1000:      gvfs-nds.patch
# PATCH-FEATURE-SLE gvfs-nvvfs.patch ksamrat@novell.com -- Provides gvfs backend for novell nautilus plugin
Patch1001:      gvfs-nvvfs.patch

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libgcrypt-devel >= 1.2.2
BuildRequires:  meson >= 0.50.0
BuildRequires:  openssh
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(avahi-client) >= 0.6
BuildRequires:  pkgconfig(avahi-glib) >= 0.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fuse3) >= 3.0.0
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(goa-1.0) >= 3.17.1
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.33.0
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libgdata) >= 0.18.0
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.0
BuildRequires:  pkgconfig(libimobiledevice-1.0) >= 1.2
BuildRequires:  pkgconfig(libmtp) >= 1.1.12
BuildRequires:  pkgconfig(libnfs) >= 1.9.8
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.21
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.114
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udisks2) >= 1.97
Recommends:     gvfs-backends
Recommends:     gvfs-common
Recommends:     gvfs-fuse
%{glib2_gio_module_requires}
%{?systemd_requires}
%if %{with cdda}
BuildRequires:  pkgconfig(libcdio_paranoia) >= 0.78.2
%endif
%if 0%{?sle_version}
# The library gvfscommon was converted to a private library and is not used outside of gvfs
Obsoletes:      libgvfscommon0 <= %{version}
%endif

%description
gvfs GNOME's userspace virtual filesystem designed to work with the
I/O abstraction of GIO, a library available with GLib. gvfs installs
several modules that are automatically used by applications using the
APIs of libgio. There is also FUSE support that allows applications
not using GIO to access the GVfs filesystems.

%package backend-afc
%define mobile_device_package %(rpm -q --qf "%%{name}" -f $(readlink -f %{_libdir}/libimobiledevice-1.0.so))
Summary:        VFS functionality for GLib -- iPod / iPhone Support
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Supplements:    (gvfs and %{mobile_device_package})

%description backend-afc
This package provides a gvfs backend that supports iPod / iPhone devices.

%package backend-samba
%define smb_client_package %(rpm -q --qf "%%{name}" -f $(readlink -f %{_libdir}/libsmbclient.so))
Summary:        VFS functionality for GLib -- Samba Support
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-backends = %{version}
Supplements:    (gvfs and %{smb_client_package})

%description backend-samba
This package provides a gvfs backend that supports Samba.

%package backends
Summary:        VFS functionality for GLib
License:        GPL-3.0-only AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         permissions
Recommends:     pkexec
Recommends:     udisks2

%description backends
VFS functionality for GLib.
This package contains all necessary backend files and libraries.

%package fuse
Summary:        VFS functionality for GLib
License:        LGPL-2.0-or-later
Group:          System/Filesystems
Requires:       %{name} = %{version}
Requires:       fuse3

%description fuse
gvfs GNOME's userspace virtual filesystem designed to work with the
I/O abstraction of GIO, a library available with GLib. gvfs installs
several modules that are automatically used by applications using the
APIs of libgio.

This package contains FUSE support that allows applications
not using GIO to access the GVfs filesystems.

%package devel
Summary:        Development files for the GNOME Virtual file system
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
gvfs GNOME's userspace virtual filesystem designed to work with the
I/O abstraction of GIO, a library available with GLib. gvfs installs
several modules that are automatically used by applications using the
APIs of libgio.

This subpackage contains libraries and header files for developing
gvfs plugins.

%lang_package

%prep
%setup -q

%if 0%{?sle_version}
%patch1000 -p1
%patch1001 -p1
%endif

%build
%meson \
	--libexecdir=%{_libexecdir}/%{name} \
	-Dudisks2=true \
	%{!?with_cdda: -Dcdda=false} \
	-Dman=true \
	-Dsystemduserunitdir=%{_userunitdir} \
	%{nil}
%meson_build

%install
%meson_install
# drop polkit rules files (for wheel group) - boo#1125433
rm -v %{buildroot}%{_datadir}/polkit-1/rules.d/org.gtk.vfs.file-operations.rules
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

# Rename daemon/trashlib/COPYING
mv daemon/trashlib/COPYING daemon/trashlib/COPYING.trashlib

%post
%{glib2_gio_module_post}

%post fuse
%tmpfiles_create %{_tmpfilesdir}/gvfsd-fuse-tmpfiles.conf

%post backends
%set_permissions %{_libexecdir}/%{name}/gvfsd-nfs

%verifyscript backends
%verify_permissions -e %{_libexecdir}/%{name}/gvfsd-nfs

%postun
%{glib2_gio_module_postun}

%files
%license COPYING daemon/trashlib/COPYING.trashlib
%doc NEWS README.md
%doc daemon/org.gtk.vfs.file-operations.rules.in
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/mounts
%dir %{_datadir}/%{name}/remote-volume-monitors
%{_libdir}/gio/modules/*.so
%dir %{_libdir}/gvfs
%{_libdir}/gvfs/libgvfscommon.so
%{_libdir}/gvfs/libgvfsdaemon.so
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gvfsd
%{_datadir}/dbus-1/services/org.gtk.vfs.Daemon.service
%{_libexecdir}/%{name}/gvfsd-metadata
%{_datadir}/dbus-1/services/org.gtk.vfs.Metadata.service
%{_mandir}/man1/gvfsd.1%{?ext_man}
%{_mandir}/man1/gvfsd-metadata.1%{?ext_man}
%{_mandir}/man7/gvfs.7%{?ext_man}
%{_userunitdir}/gvfs-daemon.service
%{_userunitdir}/gvfs-metadata.service

%files fuse
%{_libexecdir}/%{name}/gvfsd-fuse
%{_tmpfilesdir}/gvfsd-fuse-tmpfiles.conf
%{_mandir}/man1/gvfsd-fuse.1%{?ext_man}

%files backend-afc
%{_libexecdir}/%{name}/gvfs-afc-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.AfcVolumeMonitor.service
%{_userunitdir}/gvfs-afc-volume-monitor.service
%{_datadir}/%{name}/remote-volume-monitors/afc.monitor
%{_libexecdir}/%{name}/gvfsd-afc
%{_datadir}/%{name}/mounts/afc.mount

%files backend-samba
%{_libexecdir}/%{name}/gvfsd-smb
%{_datadir}/%{name}/mounts/smb.mount
%{_libexecdir}/%{name}/gvfsd-smb-browse
%{_datadir}/%{name}/mounts/smb-browse.mount
# GSettings schemas & conversion data
# Those schemas are used gvfsd-smb
%{_datadir}/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
%{_datadir}/GConf/gsettings/gvfs-smb.convert

%files backends
%doc monitor/udisks2/what-is-shown.txt
%{_datadir}/dbus-1/services/org.gtk.vfs.UDisks2VolumeMonitor.service
%{_datadir}/%{name}/remote-volume-monitors/udisks2.monitor
%{_libexecdir}/%{name}/gvfs-udisks2-volume-monitor
%{_userunitdir}/gvfs-udisks2-volume-monitor.service
%{_libexecdir}/%{name}/gvfs-gphoto2-volume-monitor
%{_userunitdir}/gvfs-gphoto2-volume-monitor.service
%{_datadir}/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service
%{_datadir}/%{name}/remote-volume-monitors/gphoto2.monitor
%{_libexecdir}/%{name}/gvfsd-admin
%{_datadir}/%{name}/mounts/admin.mount
%{_datadir}/polkit-1/actions/org.gtk.vfs.file-operations.policy
%{_libexecdir}/%{name}/gvfsd-afp
%{_datadir}/%{name}/mounts/afp.mount
%{_libexecdir}/%{name}/gvfsd-afp-browse
%{_datadir}/%{name}/mounts/afp-browse.mount
%{_libexecdir}/%{name}/gvfsd-archive
%{_datadir}/%{name}/mounts/archive.mount
%{_libexecdir}/%{name}/gvfsd-burn
%{_datadir}/%{name}/mounts/burn.mount
%if %{with cdda}
%{_libexecdir}/%{name}/gvfsd-cdda
%{_datadir}/%{name}/mounts/cdda.mount
%endif
%{_libexecdir}/%{name}/gvfsd-computer
%{_datadir}/%{name}/mounts/computer.mount
%{_libexecdir}/%{name}/gvfsd-dav
%{_datadir}/%{name}/mounts/dav.mount
%{_datadir}/%{name}/mounts/dav+sd.mount
%{_libexecdir}/%{name}/gvfsd-dnssd
%{_datadir}/%{name}/mounts/dns-sd.mount
%{_libexecdir}/%{name}/gvfsd-ftp
%{_datadir}/%{name}/mounts/ftp.mount
%{_datadir}/%{name}/mounts/ftps.mount
%{_datadir}/%{name}/mounts/ftpis.mount
%{_libexecdir}/%{name}/gvfsd-google
%{_datadir}/%{name}/mounts/google.mount
%{_libexecdir}/%{name}/gvfsd-gphoto2
%{_datadir}/%{name}/mounts/gphoto2.mount
%{_libexecdir}/%{name}/gvfsd-http
%{_datadir}/%{name}/mounts/http.mount
%{_libexecdir}/%{name}/gvfs-goa-volume-monitor
%{_userunitdir}/gvfs-goa-volume-monitor.service
%{_datadir}/%{name}/remote-volume-monitors/goa.monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.GoaVolumeMonitor.service
%{_libexecdir}/%{name}/gvfsd-localtest
%{_datadir}/%{name}/mounts/localtest.mount
%{_libexecdir}/%{name}/gvfsd-mtp
%{_libexecdir}/%{name}/gvfs-mtp-volume-monitor
%{_userunitdir}/gvfs-mtp-volume-monitor.service
%{_datadir}/%{name}/remote-volume-monitors/mtp.monitor
%{_datadir}/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service
%{_datadir}/%{name}/mounts/mtp.mount
%if 0%{?sle_version}
%{_libexecdir}/%{name}/gvfsd-nds
%{_libexecdir}/%{name}/gvfsd-nvvfs
%{_datadir}/%{name}/mounts/nds.mount
%{_datadir}/%{name}/mounts/nvvfs.mount
%endif
%{_libexecdir}/%{name}/gvfsd-network
%{_datadir}/%{name}/mounts/network.mount
# allow priv ports for mounting nfs. Otherwise the nfs-service requires insecure (boo#1065864)
%verify(not mode caps) %caps(cap_net_bind_service=+ep) %{_libexecdir}/%{name}/gvfsd-nfs
%{_libexecdir}/%{name}/gvfsd-nfs
%{_datadir}/%{name}/mounts/nfs.mount
%{_libexecdir}/%{name}/gvfsd-recent
%{_datadir}/%{name}/mounts/recent.mount
%{_libexecdir}/%{name}/gvfsd-sftp
%{_datadir}/%{name}/mounts/sftp.mount
# gvfsd-trash is GPLv3 because of trashlib.
%{_libexecdir}/%{name}/gvfsd-trash
%{_datadir}/%{name}/mounts/trash.mount
# GSettings schemas & conversion data
# Those schemas are used by gvfsd-network
%{_datadir}/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gvfs-dns-sd.convert

%files devel
%doc CONTRIBUTING.md NEWS.pre-1-2
%{_includedir}/gvfs-client

%files lang -f %{name}.lang

%changelog
