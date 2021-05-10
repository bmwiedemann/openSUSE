#
# spec file for package open-vm-tools
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


# vgauth is enabled for openSUSE Factory, Leap 42.1, SLES12SP1 and later releases (which include xml-security-c and xerces-c)
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 0120100
%bcond_without vgauth
%else
%bcond_with vgauth
%endif

# vmblock-fuse.service requires systemd >= 228 which is in openSUSE Factory, SLES12SP2 and Leap 42.2 (see bsc#985773)
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 0120200
    %bcond_without vmblockfuseservice
%else
    %bcond_with vmblockfuseservice
%endif

# exclude AMD PCnet32 LANCE pci.id from Supplements list [bnc#397554]
%define __find_supplements sh -c '/usr/lib/rpm/find-supplements %{name} | grep -v pci:v00001022d00002000'

# X modules are lower prio upstream and once in a while fail. Offer an easy way to enable/disable them.
%define with_X 1

Name:           open-vm-tools
%define subname open-vm-tools
%define tarname open-vm-tools
%define bldnum  17337674
Version:        11.2.5
Release:        0
Summary:        Open Virtual Machine Tools
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only
Group:          System/Emulators/PC
URL:            https://github.com/vmware/open-vm-tools
Source:         %{tarname}-%{version}-%{bldnum}.tar.gz
Source1:        vmtoolsd
Source2:        vmtoolsd.service
Source3:        vmware-user-autostart.desktop
Source5:        vmware-user-autostart-wrapper
Source6:        open-vm-tools-modprobe.conf
Source7:        tools.conf
Source8:        vgauthd.service
Source9:        vmblock-fuse.service
# PATCH-FIX-UPSTREAM open-vm-tools-glib-2.67.patch dimstar@opensuse.org -- Fix build with glib 2.67, https://github.com/vmware/open-vm-tools/issues/500
Patch100:       open-vm-tools-glib-2.67.patch
Patch101:       open-vm-tools-pollGtk.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
# don't use pkgconfig(gtk+-2.0) so we can build on SLE
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gtk3-devel
BuildRequires:  gtkmm3-devel
BuildRequires:  libdnet-devel
BuildRequires:  libicu-devel
BuildRequires:  libmspack-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre-devel
BuildRequires:  procps-devel
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
BuildRequires:  glibc >= 2.27
BuildRequires:  libtirpc-devel
BuildRequires:  rpcgen
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0) >= 2.21.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
%else
BuildRequires:  glibc >= 2.12
BuildRequires:  xorg-x11-devel
%endif
%if %{with vgauth}
# vgauth requires xml2, xerces-c, and xml-security-c/xmlsec1
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig(xerces-c)

# Use xmlsec1 instead of xml-security-c where available.
# If using xmlsec1, also need to use libxmlsec1-openssl1
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 0120300
BuildRequires:  pkgconfig(xmlsec1)
Requires:       libxmlsec1-openssl1 >= 1.2.28
%else
# Leap 42.1 and 42.2 supports xmlsec1 and libxmlsec1-openssl1 but 12 SP1 and
# SP2 do not.
%if 0%{?is_opensuse} && 0%{?sle_version} >= 0120100
BuildRequires:  pkgconfig(xmlsec1)
Requires:       libxmlsec1-openssl1
%else
BuildRequires:  xml-security-c-devel
%define         arg_xmlsecurity --enable-xmlsecurity
%endif
%endif

%else
# not using vgauth
%define arg_xmlsecurity --without-xmlsecurity
%define arg_xerces --without-xerces
%endif
# vmhgfs is always built so fuse is no longer optional
BuildRequires:  fuse-devel
BuildRequires:  pkgconfig(udev)
%if 0%( pkg-config --exists 'udev > 190' && echo '1' ) == 01
%define _udevrulesdir /usr/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif
Requires:       libvmtools0 = %{version}-%{release}
Requires:       net-tools
Requires:       tar
Requires:       which
# open-vm-tools >= 10.0.0 do not require open-vm-tools-deploypkg
# provided by VMware. That functionality is now available as part
# of open-vm-tools package itself.
Obsoletes:      open-vm-tools-deploypkg <= 10.0.5
Supplements:    modalias(pci:v000015ADd*sv*sd*bc*sc*i*)
ExclusiveArch:  %ix86 x86_64 aarch64
#Upstream patches
Patch0:         pam-vmtoolsd.patch

%if 0%{?suse_version} >= 1500
%systemd_ordering
%else
%systemd_requires
%endif

%description
Open Virtual Machine Tools (open-vm-tools) are the open source
implementation of VMware Tools. They are a set of guest operating
system virtualization components that enhance performance and user
experience of virtual machines. As virtualization technology rapidly
becomes mainstream, each virtualization solution provider implements
their own set of tools and utilities to supplement the guest virtual
machine. However, most of the implementations are proprietary and are
tied to a specific virtualization platform.

With the Open Virtual Machine Tools project, we are hoping to solve
this and other related problems. The tools are currently composed of
kernel modules for Linux and user-space programs for all VMware
supported Unix-like guest operating systems. They provide several
useful functions like:

* File transfer between a host and guest

* Improved memory management and network performance under
   virtualization

* General mechanisms and protocols for communication between host and
guests and from guest to guest

%if %{with_X}

%package        desktop
Summary:        User experience components for Open Virtual Machine Tools
Group:          System/Emulators/PC
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-gui < %{version}
Provides:       %{name}-gui = %{version}
Supplements:    packageand(open-vm-tools:xorg-x11-server)
Requires(pre):  permissions

%description    desktop
This package contains only the user-space programs and libraries of
%{name} that are essential for improved user experience of VMware virtual
machines.
%endif

%package        sdmp
Summary:        Service Discovery Plugin
Group:          System Environment/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description      sdmp
Service Discovery Plugin

%package -n libvmtools0
Summary:        Open Virtual Machine Tools - shared library
Group:          System/Libraries

%description -n libvmtools0
This is a shared library used by several Open VM Tools components,
such as vmware-toolbox-cmd and vmtoolsd (and its plugins).

%package -n libvmtools-devel
Summary:        Open Virtual Machine Tools - Development headers
Group:          Development/Libraries/C and C++
Requires:       libvmtools0 = %{version}

%description -n libvmtools-devel
Those are the development headers for libvmtools. They are needed
if you intend to create own plugins for vmtoolsd.

%prep
%setup -q -n %{tarname}-%{version}-%{bldnum}

# fix for an rpmlint warning regarding wrong line feeds
sed -i -e "s/\r//" README
#Upstream patches
%patch0 -p2

# patch not yet coming from upstream, https://github.com/vmware/open-vm-tools/issues/500
%patch100 -p1
%patch101 -p1

%build
%if %{with_X}
    %define arg_x --with-x
%else
    %define arg_x --without-x
%endif

# disable warning unused-but-set-variable which will raise error because of -Werror
# disable warning deprecated-declarations which will raise error because of -Werror
# disable warning sizeof-pointer-memaccess which will raise error because of -Werror
# (this is because of 'g_static_mutex_init' usage which is now deprecated)
export CFLAGS="%{optflags} -Wno-unused-local-typedefs -Wno-unused-but-set-variable -Wno-deprecated-declarations -Wno-sizeof-pointer-memaccess -Wno-cpp -fPIE"
export CXXFLAGS="%{optflags} -Wno-unused-local-typedefs -Wno-unused-but-set-variable -Wno-deprecated-declarations -Wno-sizeof-pointer-memaccess -Wno-cpp -fPIE"
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
export LDFLAGS="-pie -ltirpc"
%else
export LDFLAGS="-pie"
%endif
# Required for version 9.4.0
export CUSTOM_PROCPS_NAME=procps
autoreconf -fi
echo 'HTML_TIMESTAMP=NO' >> docs/api/doxygen.conf
# In the latest official tarballs, configure is not marked executable
chmod 755 configure
%configure \
    --without-kernel-modules \
    --without-root-privileges \
    %{?arg_x} \
    --disable-dependency-tracking \
    --with-gtk3 \
    %{?arg_xmlsecurity} \
    %{?arg_xerces} \
    --with-udev-rules-dir=%{_udevrulesdir} \
    --enable-resolutionkms \
    --enable-servicediscovery \
    --disable-static
make

%install
%make_install

# Remove exec bit from config files
chmod a-x %{buildroot}%{_sysconfdir}/pam.d/*

# Remove unnecessary files from packaging
find %{buildroot}%{_libdir} -name '*.la' -delete
rm -fr %{buildroot}%{_defaultdocdir}
rm -fr %{buildroot}/usr/share/doc/open-vm-tools/api
rm -f docs/api/build/html/FreeSans.ttf

# install systemd init scripts and symlinks
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/vmtoolsd.service
ln -sf service %{buildroot}%{_sbindir}/rcvmtoolsd
%if %{with vmblockfuseservice}
install -p -m 644 -D %{SOURCE9} %{buildroot}%{_unitdir}/vmblock-fuse.service
ln -sf service %{buildroot}%{_sbindir}/rcvmblock-fuse
%endif
%if %{with vgauth}
install -p -m 644 -D %{SOURCE8} %{buildroot}%{_unitdir}/vgauthd.service
ln -sf service %{buildroot}%{_sbindir}/rcvgauthd
mkdir -p %{buildroot}%{_var}/lib/vmware
%else
# if vgauth is not enabled, it must be removed from vmtoolsd.service
sed -i '/vgauth/d' %{buildroot}%{_unitdir}/vmtoolsd.service
%endif

%if %{with_X}
# vmware-user is started by vmware-user-suid-wrapper by xdg-autostart
# unfortunately, vmware-user-suid-wrapper does not wait for it's block device
# to appear. For this reason we have now a vmware-user-autostart-wrapper
# which checks for /proc/fs/vmblock/dev to appear and then starts vmware-user-suid-wrapper
install -D -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/vmware-user-autostart-wrapper
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/xdg/autostart/vmware-user-autostart.desktop

# Install the default tools.conf
install -D -m 0644 %{S:7} %{buildroot}%{_sysconfdir}/vmware-tools/tools.conf
# Remove the 'disable-perl-mon=1' setting if procps is available
sed -i '/openSUSE/,+2d' %{buildroot}%{_sysconfdir}/vmware-tools/tools.conf

# We have our own 'safe' autostart wrapper, which checks for modules to start in autologin mode...
# Thus we drop the 'original' autostartup
rm %{buildroot}%{_sysconfdir}/xdg/autostart/vmware-user.desktop

# handle the .destop files for translations
%suse_update_desktop_file vmware-user-autostart
%endif

# modprobe configuration for vmnics - only include if before SLE-12
%if 0%{?suse_version} < 1315
install -D -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/modprobe.d/50-vmnics.conf
%endif

# fix a link pointing to the buildroot for mount.vmhgfs
rm %{buildroot}/sbin/mount.vmhgfs
%if !0%{?usrmerged}
ln -s ..%{_sbindir}/mount.vmhgfs %{buildroot}/sbin/mount.vmhgfs
%endif

%pre
%service_add_pre vmtoolsd.service

%post
/sbin/ldconfig
%service_add_post vmtoolsd.service

%if %{with_X}

%verifyscript desktop
%verify_permissions -e /usr/bin/vmware-user-suid-wrapper

%if %{with vmblockfuseservice}
%pre desktop
%service_add_pre vmblock-fuse.service
%endif

%post desktop
%set_permissions /usr/bin/vmware-user-suid-wrapper
%if %{with vmblockfuseservice}
%service_add_post vmblock-fuse.service
%endif
/sbin/ldconfig

%preun desktop
%if %{with vmblockfuseservice}
%service_del_preun vmblock-fuse.service
%endif

%postun desktop
%if %{with vmblockfuseservice}
%service_del_postun vmblock-fuse.service
%endif
/sbin/ldconfig

%endif

%post sdmp
systemctl try-restart vmtoolsd.service || :

%preun
%service_del_preun vmtoolsd.service
%if %{with vgauth}
%service_del_preun vgauthd.service
%endif
# Tell VMware that open-vm-tools is being uninstalled
if [ "$1" = "0" -a \
 -e %{_bindir}/vmware-checkvm -a \
 -e %{_bindir}/vmware-rpctool ] && \
 %{_bindir}/vmware-checkvm > /dev/null 2>&1; then
 %{_bindir}/vmware-rpctool 'tools.set.version 0' > /dev/null 2>&1 || true
fi

%postun
%service_del_postun vmtoolsd.service
%if %{with vgauth}
%service_del_postun vgauthd.service
%endif
/sbin/ldconfig

%postun sdmp
# restart tools without plugin
systemctl try-restart vmtoolsd.service || :

%post -n libvmtools0 -p /sbin/ldconfig

%postun -n libvmtools0 -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 0120300
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%else
%doc AUTHORS COPYING ChangeLog NEWS README
%endif

%{_bindir}/vmtoolsd
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/common
%dir %{_libdir}/%{name}/plugins/vmsvc
%{_libdir}/%{name}/plugins/vmsvc/libdeployPkgPlugin.so
%{_libdir}/%{name}/plugins/vmsvc/libguestInfo.so
%{_libdir}/%{name}/plugins/vmsvc/libpowerOps.so
%{_libdir}/%{name}/plugins/vmsvc/libresolutionKMS.so
%{_libdir}/%{name}/plugins/vmsvc/libtimeSync.so
%{_libdir}/%{name}/plugins/vmsvc/libvmbackup.so
%{_libdir}/%{name}/plugins/vmsvc/libappInfo.so
%{_libdir}/%{name}/plugins/common/libhgfsServer.so
%{_libdir}/%{name}/plugins/common/libvix.so
%{_bindir}/vmhgfs-fuse
%{_bindir}/vmware-checkvm
%{_bindir}/vmware-hgfsclient
%{_bindir}/vmware-namespace-cmd
%{_bindir}/vmware-rpctool
%{_bindir}/vmware-toolbox-cmd
%{_bindir}/vmware-xferlogs
%{_bindir}/vm-support
%{_sbindir}/mount.vmhgfs
%if !0%{?usrmerged}
/sbin/mount.vmhgfs
%endif
%config(noreplace) %{_sysconfdir}/pam.d/vmtoolsd
%dir %{_sysconfdir}/vmware-tools
%dir %{_sysconfdir}/vmware-tools/scripts
%dir %{_sysconfdir}/vmware-tools/scripts/vmware
%{_sysconfdir}/vmware-tools/poweroff-vm-default
%{_sysconfdir}/vmware-tools/poweron-vm-default
%{_sysconfdir}/vmware-tools/resume-vm-default
%{_sysconfdir}/vmware-tools/scripts/vmware/network
%{_sysconfdir}/vmware-tools/statechange.subr
%{_sysconfdir}/vmware-tools/suspend-vm-default
%{_udevrulesdir}/99-vmware-scsi-udev.rules
%config(noreplace) %{_sysconfdir}/vmware-tools/tools.conf
%config(noreplace) %{_sysconfdir}/vmware-tools/tools.conf.example
%if 0%{?suse_version} < 1315
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/modprobe.d/50-vmnics.conf
%endif
%if %{with vgauth}
%dir %{_var}/lib/vmware
%{_bindir}/VGAuthService
%{_bindir}/vmware-vgauth-cmd
%{_bindir}/vmware-vgauth-smoketest
%dir %{_sysconfdir}/vmware-tools/vgauth
%dir %{_sysconfdir}/vmware-tools/vgauth/schemas
%config(noreplace) %{_sysconfdir}/vmware-tools/vgauth.conf
%config(noreplace) %{_sysconfdir}/vmware-tools/vgauth/schemas/*
%endif
%{_datadir}/%{name}/
%{_unitdir}/vmtoolsd.service
%if %{with vgauth}
%{_unitdir}/vgauthd.service
%{_sbindir}/rcvgauthd
%endif
%{_sbindir}/rcvmtoolsd
%exclude %{_libdir}/*.so

%if %{with_X}

%files desktop
%defattr(-, root, root)
%config %{_sysconfdir}/xdg/autostart/vmware-user-autostart.desktop
%verify(not mode) %attr(0755, root, root) %{_bindir}/vmware-user-suid-wrapper
%{_libdir}/%{name}/plugins/vmusr/
%{_bindir}/vmware-user
%{_bindir}/vmware-user-autostart-wrapper
%{_bindir}/vmware-vmblock-fuse
%if %{with vmblockfuseservice}
%{_unitdir}/vmblock-fuse.service
%{_sbindir}/rcvmblock-fuse
%endif

%endif

%files sdmp
%dir %{_libdir}/%{name}/serviceDiscovery/
%dir %{_libdir}/%{name}/serviceDiscovery/scripts/
%{_libdir}/%{name}/plugins/vmsvc/libserviceDiscovery.so
%{_libdir}/%{name}/serviceDiscovery/scripts/get-connection-info.sh
%{_libdir}/%{name}/serviceDiscovery/scripts/get-listening-process-info.sh
%{_libdir}/%{name}/serviceDiscovery/scripts/get-listening-process-perf-metrics.sh
%{_libdir}/%{name}/serviceDiscovery/scripts/get-versions.sh

%files -n libvmtools0
%defattr(-, root, root)
%{_libdir}/libvmtools.so.*
%{_libdir}/libguestlib.so.*
%{_libdir}/libhgfs.so.*
%{_libdir}/libDeployPkg.so.*
%if %{with vgauth}
%{_libdir}/libvgauth.so.*
%endif

%files -n libvmtools-devel
%defattr(-,root,root)
%doc docs/api/build/*
%{_includedir}/vmGuestLib
%{_libdir}/*.so
%{_libdir}/pkgconfig/vmguestlib.pc
%{_includedir}/libDeployPkg
%{_libdir}/pkgconfig/libDeployPkg.pc

%changelog
