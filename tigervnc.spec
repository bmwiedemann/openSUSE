#
# spec file for package tigervnc
#
# Copyright (c) 2020 SUSE LLC
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


%define vncgroup vnc
%define vncuser vnc

%define tlskey  %{_sysconfdir}/vnc/tls.key
%define tlscert %{_sysconfdir}/vnc/tls.cert

%define _unitdir %{_prefix}/lib/systemd/system

%if 0%{?suse_version} >= 1500
%define use_firewalld 1
%else
%define use_firewalld 0
%endif

%if 0%{?suse_version} < 1550
%define _distconfdir /etc
%endif

Name:           tigervnc
Version:        1.10.1
Release:        0
Provides:       tightvnc = 1.3.9
Obsoletes:      tightvnc < 1.3.9
Provides:       vnc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  fltk-devel >= 1.3.3
BuildRequires:  gcc-c++
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8.0
BuildRequires:  jpackage-utils
BuildRequires:  libjpeg-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  xorg-x11-server-sdk
BuildRequires:  xorg-x11-server-source
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtst)
# Because of keytool to build java client
BuildRequires:  libXdamage-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  mozilla-nss
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  xorg-x11-libICE-devel
BuildRequires:  xorg-x11-libSM-devel
BuildRequires:  pkgconfig(bigreqsproto) >= 1.1.0
BuildRequires:  pkgconfig(compositeproto) >= 0.4
BuildRequires:  pkgconfig(damageproto) >= 1.1
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fixesproto) >= 4.1
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(inputproto)  >= 1.9.99.902
BuildRequires:  pkgconfig(kbproto) >= 1.0.3
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(pixman-1) >= 0.15.20
BuildRequires:  pkgconfig(presentproto) >= 1.0
BuildRequires:  pkgconfig(randrproto) >= 1.2.99.3
BuildRequires:  pkgconfig(recordproto) >= 1.13.99.1
BuildRequires:  pkgconfig(renderproto) >= 0.11
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto) >= 1.1
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcmiscproto) >= 1.2.0
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.3
BuildRequires:  pkgconfig(xf86driproto) >= 2.1.1
BuildRequires:  pkgconfig(xfont) >= 1.4.2
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.14
BuildRequires:  pkgconfig(xproto)  >= 7.0.17
BuildRequires:  pkgconfig(xtrans) >= 1.2.2
%if 0%{?suse_version} >= 1315
Requires(post):   update-alternatives
Requires(postun): update-alternatives
%endif
URL:            http://tigervnc.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        An implementation of VNC
License:        GPL-2.0-only AND MIT
Group:          System/X11/Servers/XF86_4
Source1:        https://github.com/TigerVNC/tigervnc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source4:        10-libvnc.conf
Source5:        vnc-server.susefirewall
Source6:        vnc-httpd.susefirewall
Source7:        vnc.reg
Source8:        vncpasswd.arg
Source9:        vnc.pam
Source10:       with-vnc-key.sh
Source11:       index.vnc
Source12:       x11vnc
Source13:       xvnc@.service
Source14:       xvnc.socket
Source15:       xvnc-novnc.service
Source16:       xvnc-novnc.socket
Source17:       tigervnc.firewalld
Source18:       tigervnc-https.firewalld
Source19:       xvnc.target

Patch1:         tigervnc-newfbsize.patch
Patch2:         tigervnc-clean-pressed-key-on-exit.patch
Patch3:         u_tigervnc-ignore-epipe-on-write.patch
Patch4:         n_tigervnc-date-time.patch
Patch5:         u_tigervnc-cve-2014-8240.patch
Patch6:         u_tigervnc_update_default_vncxstartup.patch
Patch7:         u_build_libXvnc_as_separate_library.patch
Patch8:         u_tigervnc-add-autoaccept-parameter.patch
Patch9:         u_change-button-layout-in-ServerDialog.patch
Patch10:        n_correct_path_in_desktop_file.patch
Patch11:        U_viewer-reset-ctrl-alt-to-menu-state-on-focus.patch
Patch12:        tigervnc-fix-saving-of-bad-server-certs.patch
Patch13:        u_xorg-server-1.20.7-ddxInputThreadInit.patch
Patch21:        U_0001-Properly-store-certificate-exceptions.patch
Patch22:        U_0002-Properly-store-certificate-exceptions-in-Java-viewer.patch

%description
TigerVNC is an implementation of VNC (Virtual Network Computing), a
client/server application that allows users to launch and interact
with graphical applications on remote machines. TigerVNC is capable
of running 3D and video applications. TigerVNC also provides
extensions for advanced authentication methods and TLS encryption.

%package -n xorg-x11-Xvnc
Requires(post): /usr/sbin/useradd
Requires(post): /usr/sbin/groupadd
Requires(post): /bin/awk
Requires(post): systemd
%if %{use_firewalld}
BuildRequires:  firewall-macros
%endif
# Needed to generate certificates
Requires:       windowmanager
Requires:       xauth
Requires:       xinit
Requires:       xkbcomp
Requires:       xkeyboard-config
Requires:       xorg-x11-fonts-core
Requires:       openssl(cli)
# For the with-vnc-key.sh script
Requires:       /bin/hostname
%{?systemd_requires}
%ifnarch s390 s390x
Recommends:     xorg-x11-Xvnc-module
%endif
Provides:       tightvnc = 1.3.9
Provides:       xorg-x11-Xvnc:/usr/lib/vnc/with-vnc-key.sh
Obsoletes:      tightvnc < 1.3.9
Summary:        TigerVNC implementation of Xvnc
Group:          System/X11/Servers/XF86_4

%description -n xorg-x11-Xvnc
This is the TigerVNC implementation of Xvnc.

%ifnarch s390 s390x
%package -n xorg-x11-Xvnc-module
Requires:       xorg-x11-Xvnc
Summary:        VNC module for X server
#%%{x11_abi_extension_req}
Group:          System/X11/Servers/XF86_4

%description -n xorg-x11-Xvnc-module
This module allows to share content of X server's screen over VNC.
It is loaded into X server as a module if enable in X server's
configuration.
%endif

%package -n xorg-x11-Xvnc-novnc
Requires:       novnc
Requires:       python3-websockify
Requires:       xorg-x11-Xvnc
%{?systemd_requires}
Summary:        NoVNC service for Xvnc
Group:          System/X11/Servers/XF86_4
BuildArch:      noarch

%description -n xorg-x11-Xvnc-novnc
A service that starts noVNC linked to Xvnc server.

%package -n xorg-x11-Xvnc-java
BuildArch:      noarch

%{?systemd_requires}
Summary:        VNC viewer in java
Group:          System/X11/Servers/XF86_4

%description -n xorg-x11-Xvnc-java
A VNC client written in java that can be used as standalone application or as
an applet inside web page.

%package -n libXvnc1
Summary:        X extension to control VNC module
Group:          System/Libraries

%description -n libXvnc1
Xvnc extension allows X clients to read and change VNC configuration.

%package -n libXvnc-devel
Summary:        X extension to control VNC module
Group:          Development/Libraries/C and C++
Requires:       libXvnc1 = %version

%description -n libXvnc-devel
Xvnc extension allows X clients to read and change VNC configuration.

%package x11vnc
Summary:        Wrapper that starts x0vncserver
Group:          System/X11/Servers/XF86_4
Requires:       python
Requires:       xorg-x11-Xvnc
Provides:       x11vnc
Conflicts:      x11vnc
BuildArch:      noarch

%description x11vnc
This is a wrapper that looks like x11vnc, but starts x0vncserver instead.
It maps common x11vnc arguments to x0vncserver arguments.

%prep
%setup -T -b1 -q -n tigervnc-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch21 -p1
%patch22 -p1
%patch8 -p1

cp -r %{_prefix}/src/xserver/* unix/xserver/
pushd unix/xserver
patch -p1 < ../xserver120.patch
popd

%build
export CXXFLAGS="%optflags"
export CFLAGS="%optflags"
# Build all tigervnc
cmake -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_BUILD_TYPE=RelWithDebInfo .
make %{?_smp_mflags}

# Build Xvnc server
pushd unix/xserver
autoreconf -fi
%configure \
        --disable-xorg --disable-xnest --disable-xvfb --disable-dmx \
        --disable-xwin --disable-xephyr --disable-kdrive --with-pic \
        --disable-static --disable-xinerama \
        --with-xkb-path="%{_datadir}/X11/xkb" \
        --with-xkb-output="%{_sharedstatedir}/xkb/compiled" \
        --enable-glx --enable-dri \
%ifnarch s390 s390x
	--enable-dri2 \
%endif
        --disable-config-dbus \
        --disable-config-hal \
        --disable-config-udev \
        --without-dtrace \
        --disable-unit-tests \
        --disable-devel-docs \
        --with-fontrootdir=%{_datadir}/fonts \
        --disable-selective-werror
make %{?_smp_mflags} V=1
popd

# Build java client
pushd java
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DJAVACFLAGS="-encoding utf8 -source 1.6 -target 1.6" .
make %{?_smp_mflags}
popd

%install

%make_install

mv %{buildroot}%{_bindir}/vncviewer %{buildroot}%{_bindir}/vncviewer-tigervnc
mv %{buildroot}%{_datadir}/man/man1/vncviewer.1 %{buildroot}%{_datadir}/man/man1/vncviewer-tigervnc.1

pushd unix/xserver
%make_install
popd

pushd java
mkdir -p %{buildroot}%{_datadir}/vnc/classes
install -m755 VncViewer.jar %{buildroot}%{_datadir}/vnc/classes
popd

%ifnarch s390x
install -D -m 644 %{SOURCE4} %{buildroot}%{_datadir}/X11/xorg.conf.d/10-libvnc.conf
%endif

%if %{use_firewalld}
install -D -m 644 %{SOURCE17} %{buildroot}%{_prefix}/lib/firewalld/services/tigervnc.xml
install -D -m 644 %{SOURCE18} %{buildroot}%{_prefix}/lib/firewalld/services/tigervnc-https.xml
%else
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/vnc-server
install -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/vnc-httpd
%endif

# only package as %doc (boo#1173045)
cp %{SOURCE7} .
install -D -m 755 %{SOURCE8} %{buildroot}%{_bindir}/vncpasswd.arg
install -D -m 644 %{SOURCE9} %{buildroot}%{_distconfdir}/pam.d/vnc
install -D -m 644 %{SOURCE11} %{buildroot}%{_datadir}/vnc/classes
%if 0%{?suse_version} >= 1315
ln -s -f %{_sysconfdir}/alternatives/vncviewer %{buildroot}%{_bindir}/vncviewer
ln -s -f %{_sysconfdir}/alternatives/vncviewer.1.gz %{buildroot}%{_mandir}/man1/vncviewer.1.gz
%endif

mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcxvnc
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcxvnc-novnc

mkdir -p %{buildroot}%{_sysconfdir}/vnc

mkdir -p %{buildroot}%{_libexecdir}/vnc
install -D -m 755 %{SOURCE10} %{buildroot}%{_libexecdir}/vnc

install -D -m 755 %{SOURCE12} %{buildroot}%{_bindir}/x11vnc

install -D %{SOURCE13} -m 0444 %{buildroot}%{_unitdir}/xvnc@.service
install -D %{SOURCE14} -m 0444 %{buildroot}%{_unitdir}/xvnc.socket
install -D %{SOURCE15} -m 0444 %{buildroot}%{_unitdir}/xvnc-novnc.service
install -D %{SOURCE16} -m 0444 %{buildroot}%{_unitdir}/xvnc-novnc.socket
install -D %{SOURCE19} -m 0444 %{buildroot}%{_unitdir}/xvnc.target

rm -rf %{buildroot}%{_datadir}/doc/tigervnc-*

%find_lang '%{name}'

%post
%if 0%{?suse_version} >= 1315
%_sbindir/update-alternatives \
    --install %{_bindir}/vncviewer vncviewer %{_bindir}/vncviewer-tigervnc 20 \
    --slave %{_mandir}/man1/vncviewer.1.gz  vncviewer.1.gz  %{_mandir}/man1/vncviewer-tigervnc.1.gz
%endif

%postun
%if 0%{?suse_version} >= 1315
if [ "$1" = 0 ] ; then
   "%{_sbindir}/update-alternatives" --remove vncviewer %{_bindir}/vncviewer-tigervnc
fi
%endif

%pre -n xorg-x11-Xvnc
%service_add_pre xvnc.socket

getent group %{vncgroup} > /dev/null || groupadd -r %{vncgroup} || :
getent passwd %{vncuser} > /dev/null || useradd -r -g %{vncgroup} -d %{_sharedstatedir}/empty -s /sbin/nologin -c "user for VNC" %{vncuser} || :
# add vnc user to shadow group. (bsc#980326)
# more details about the reasoning in bsc#1162951
usermod -G shadow -a %{vncuser} || :

%post -n xorg-x11-Xvnc
%service_add_post xvnc.socket

%if %{use_firewalld}
%{firewalld_reload}
%endif

# If there is old xinetd configuration file and VNC service was enabled, enable the systemd service too.
# Once we are done, RPM will rename the file to /etc/xinetd.d/vnc.rpmsave, so this won't happen
# during future updates.
if [ -e %{_sysconfdir}/xinetd.d/vnc ] && awk '
  BEGIN { in_vnc1_section = 0 }
  /service.*vnc1/ { in_vnc1_section = 1 }
  in_vnc1_section && /disable\s*=\s*yes/ { exit 1 }
  in_vnc1_section && /}/ { exit 0 }
  ' %{_sysconfdir}/xinetd.d/vnc;
then
  echo "Found old xinetd configuration with enabled VNC service. Enabling xvnc.socket."
  systemctl enable xvnc.socket
fi

%preun -n xorg-x11-Xvnc
%service_del_preun xvnc.socket

%postun -n xorg-x11-Xvnc
%service_del_postun xvnc.socket

%pre -n xorg-x11-Xvnc-novnc
%service_add_pre xvnc-novnc.service
%service_add_pre xvnc-novnc.socket

%post -n xorg-x11-Xvnc-novnc
%service_add_post xvnc-novnc.service
%service_add_post xvnc-novnc.socket

%preun -n xorg-x11-Xvnc-novnc
%service_del_preun xvnc-novnc.service
%service_del_preun xvnc-novnc.socket

%postun -n xorg-x11-Xvnc-novnc
%service_del_postun xvnc-novnc.service
%service_del_postun xvnc-novnc.socket

%post -n libXvnc1 -p /sbin/ldconfig

%postun -n libXvnc1 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%ghost %{_bindir}/vncviewer
%{_bindir}/vncviewer-tigervnc
%doc LICENCE.TXT README.rst
%ghost %{_mandir}/man1/vncviewer.1.gz
%doc %{_mandir}/man1/vncviewer-tigervnc.1.gz
%if 0%{?suse_version} >= 1315
%ghost %{_sysconfdir}/alternatives/vncviewer
%ghost %{_sysconfdir}/alternatives/vncviewer.1.gz
%endif

%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/22x22
%dir %{_datadir}/icons/hicolor/22x22/apps
%dir %{_datadir}/icons/hicolor/24x24
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps

%{_datadir}/icons/hicolor/*/apps/tigervnc.png
%{_datadir}/icons/hicolor/scalable/apps/tigervnc.svg

%{_datadir}/applications/vncviewer.desktop

%files -n xorg-x11-Xvnc
%doc LICENCE.TXT README.rst vnc.reg
%defattr(-,root,root)

%{_bindir}/Xvnc
%{_bindir}/vncconfig
%{_bindir}/vncpasswd
%{_bindir}/vncpasswd.arg
%{_bindir}/vncserver
%{_bindir}/x0vncserver

%exclude %{_mandir}/man1/Xserver.1*
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/vncconfig.1*
%{_mandir}/man1/vncpasswd.1*
%{_mandir}/man1/vncserver.1*
%{_mandir}/man1/x0vncserver.1*

%{_unitdir}/xvnc@.service
%{_unitdir}/xvnc.socket
%{_unitdir}/xvnc.target
%{_sbindir}/rcxvnc

%exclude %{_sharedstatedir}/xkb/compiled/README.compiled

%if %{use_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/tigervnc.xml
%{_prefix}/lib/firewalld/services/tigervnc-https.xml
%else
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/vnc-server
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/vnc-httpd
%endif

%if 0%{?suse_version} < 1550
%config %{_distconfdir}/pam.d/vnc
%else
%{_distconfdir}/pam.d/vnc
%endif

%dir %attr(0755,%{vncuser},%{vncuser}) %{_sysconfdir}/vnc
%ghost %attr(0600,%{vncuser},%{vncuser}) %config(noreplace) %{tlskey}
%ghost %attr(0644,%{vncuser},%{vncuser}) %config(noreplace) %{tlscert}

%{_libexecdir}/vnc

%ifarch s390 s390x
# These would be in xorg-x11-Xvnc-module, but we don't build that on s390
%exclude %{_libdir}/xorg/protocol.txt
%exclude %{_libdir}/xorg/modules/extensions/libvnc.la
%exclude %{_libdir}/xorg/modules/extensions/libvnc.so
%endif

%ifnarch s390 s390x
%files -n xorg-x11-Xvnc-module
%exclude %{_libdir}/xorg/protocol.txt
%exclude %{_libdir}/xorg/modules/extensions/libvnc.la
%{_libdir}/xorg/modules/extensions/libvnc.so
%{_datadir}/X11/xorg.conf.d/10-libvnc.conf
%endif

%files -n xorg-x11-Xvnc-novnc
%{_unitdir}/xvnc-novnc.service
%{_unitdir}/xvnc-novnc.socket
%{_sbindir}/rcxvnc-novnc

%files -n xorg-x11-Xvnc-java
%doc java/com/tigervnc/vncviewer/README
%{_datadir}/vnc

%files -n libXvnc1
%defattr(-,root,root)
%{_libdir}/libXvnc.so.1*

%files -n libXvnc-devel
%defattr(-,root,root)
%{_libdir}/libXvnc.so
%{_includedir}/X11/extensions/Xvnc.h

%files x11vnc
%defattr(-,root,root)
%{_bindir}/x11vnc

%changelog
