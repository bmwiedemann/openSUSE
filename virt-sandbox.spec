#
# spec file for package virt-sandbox
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


%define libvirt_version 1.0.2
%define sover 1_0-5

Name:           virt-sandbox
Version:        0.8.0
Release:        1%{?dist}%{?extra_release}
Url:            http://libvirt.org/
Summary:        Libvirt application sandbox framework
License:        LGPL-2.0-or-later
Group:          System/Management
Source0:        ftp://libvirt.org/libvirt/sandbox/libvirt-sandbox-%{version}.tar.gz
Source1:        %{name}.rpmlintrc

# Patches pending upstream review
Patch100:       no-unmount-for-lxc-machines.patch

# Need to go upstream

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  glibc-devel-static
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libvirt-glib-devel >= 0.2.1
BuildRequires:  perl
%if 0%{?suse_version} >= 1500
BuildRequires:  libtirpc-devel
BuildRequires:  rpcgen
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  xz-static-devel
%endif
BuildRequires:  zlib-devel-static
Requires:       python3-rpm
# For virsh lxc-enter-namespace command
Requires:       libvirt-client >= %{libvirt_version}
Requires:       python3-gobject
Requires:       systemd >= 198
# Requires: libselinux-python
Requires:       cron
Requires:       libvirt-sandbox-%{sover} = %{version}-%{release}

%package -n libvirt-sandbox-%{sover}
Summary:        Libvirt application sandbox framework libraries
# So we get the full libvirtd daemon, not just client libs
Group:          Development/Libraries/C and C++
Requires:       libvirt-daemon-lxc >= %{libvirt_version}
Requires:       libvirt-daemon-qemu >= %{libvirt_version}

%package -n typelib-1_0-LibvirtSandbox-1_0
Summary:        GLib and GObject mapping of libvirt-sandbox - gi-bindings
Group:          System/Libraries

%package -n libvirt-sandbox-devel
Summary:        Libvirt application sandbox framework development files
Group:          Development/Libraries/C and C++
Requires:       libvirt-sandbox-%{sover} = %{version}-%{release}

%description
This package provides a command for running applications within
a sandbox using libvirt.

%description -n libvirt-sandbox-%{sover}
This package provides a framework for building application sandboxes
using libvirt.

%description -n libvirt-sandbox-devel
This package provides development header files and libraries for
the libvirt sandbox

%description -n typelib-1_0-LibvirtSandbox-1_0
This package provides Gnome-introspection bindings for building
applications within a sandbox using libvirt.

%prep
%setup -q -n libvirt-sandbox-%{version}
%patch100 -p1

%build
# We may have a more recent version of automake when building
# than the one used to autoconfigure the project for the distribution
# Just make sure the files are sync'ed with our version

autoreconf -f -i
%configure --enable-introspection --disable-static
make V=1 %{?_smp_mflags}

%install
chmod a-x examples/*.py examples/*.pl examples/*.js
%make_install
rm -f %{buildroot}/%{_libdir}/*.a
rm -f %{buildroot}/%{_libdir}/*.la

%find_lang libvirt-sandbox

%post -n libvirt-sandbox-%{sover} -p /sbin/ldconfig
%postun -n libvirt-sandbox-%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/virt-sandbox
%{_mandir}/man1/virt-sandbox.1*

%files -n libvirt-sandbox-%{sover} -f libvirt-sandbox.lang
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog NEWS
%license COPYING
%dir %{_sysconfdir}/libvirt-sandbox
%dir %{_sysconfdir}/libvirt-sandbox/scratch
%config %{_sysconfdir}/libvirt-sandbox/scratch/README
%{_libexecdir}/libvirt-sandbox-init-common
%{_libexecdir}/libvirt-sandbox-init-lxc
%{_libexecdir}/libvirt-sandbox-init-qemu
%{_libdir}/libvirt-sandbox-1.0.so.*

%files -n typelib-1_0-LibvirtSandbox-1_0
%defattr(-,root,root,-)
%{_libdir}/girepository-1.0/LibvirtSandbox-1.0.typelib

%files -n libvirt-sandbox-devel
%defattr(-,root,root,-)
%doc examples/virt-sandbox.pl
%doc examples/virt-sandbox.py
%doc examples/virt-sandbox.js
%doc examples/virt-sandbox-mkinitrd.py
%{_libdir}/libvirt-sandbox-1.0.so
%{_libdir}/pkgconfig/libvirt-sandbox-1.0.pc
%dir %{_includedir}/libvirt-sandbox-1.0
%dir %{_includedir}/libvirt-sandbox-1.0/libvirt-sandbox
%{_includedir}/libvirt-sandbox-1.0/libvirt-sandbox/libvirt-sandbox.h
%{_includedir}/libvirt-sandbox-1.0/libvirt-sandbox/libvirt-sandbox-*.h
%{_datadir}/gir-1.0/LibvirtSandbox-1.0.gir
%{_datadir}/gtk-doc/html/Libvirt-sandbox

%changelog
