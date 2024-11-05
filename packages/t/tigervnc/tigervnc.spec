#
# spec file for package tigervnc
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


%define vncgroup vnc
%define vncuser vnc
%define tlskey  %{_sysconfdir}/vnc/tls.key
%define tlscert %{_sysconfdir}/vnc/tls.cert
%if 0%{?suse_version} >= 1500
%define use_firewalld 1
%else
%define use_firewalld 0
%endif
%define use_update_alternative 0%{?suse_version} >= 1315 && 0%{?suse_version} < 1600
%define with_rc_service_symlink 0%{?suse_version} && 0%{?suse_version} < 1600
%if 0%{?suse_version} < 1550
%define _pam_vendordir %{_sysconfdir}/pam.d
%endif
Name:           tigervnc
Version:        1.14.1
Release:        0
Summary:        An implementation of VNC
License:        GPL-2.0-only AND MIT
Group:          System/X11/Servers/XF86_4
URL:            https://tigervnc.org/
Source0:        https://github.com/TigerVNC/tigervnc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        10-libvnc.conf
Source2:        vnc-server.susefirewall
Source3:        vnc-httpd.susefirewall
Source4:        vnc.reg
Source5:        vncpasswd.arg
Source6:        vnc.pam
Source7:        with-vnc-key.sh
Source8:        index.vnc
Source9:        x11vnc
Source10:       xvnc@.service.in
Source11:       xvnc.socket
Source12:       xvnc-novnc.socket
Source13:       tigervnc.firewalld
Source14:       tigervnc-https.firewalld
Source15:       xvnc.target
Source16:       xvnc-novnc.service.in
Source17:       vnc.sysusers
Patch1:         u_tigervnc-Ignore-epipe-on-write.patch
Patch2:         u_tigervnc-Build-libXvnc-as-separate-library.patch
Patch3:         u_tigervnc-Add-autoaccept-parameter.patch
Patch4:         n_tigervnc-Date-time.patch
%if %use_update_alternative
Patch5:         n_tigervnc-Correct-path-in-desktop-file.patch
%endif
Patch6:         n_tigervnc-Vncserver.patch
Patch7:         n_tigervnc-Dont-sign-java-client.patch
# The "--date" option was added into jar in OpenJDK 17
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
Patch8:         n_tigervnc-reproducible-jar-mtime.patch
%endif
Provides:       tightvnc = 1.5.0
Obsoletes:      tightvnc < 1.5.0
Provides:       vnc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  fltk-devel >= 1.3.3
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8.0
BuildRequires:  jpackage-utils
BuildRequires:  libjpeg-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  xorg-x11-server-sdk >= 21.1.11
BuildRequires:  xorg-x11-server-source >= 21.1.11
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
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
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
BuildRequires:  pkgconfig(gnutls) >= 3.6.0
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
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.14
BuildRequires:  pkgconfig(xproto)  >= 7.0.17
BuildRequires:  pkgconfig(xtrans) >= 1.2.2
BuildRequires:  pkgconfig(zlib)
%if %use_update_alternative
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%description
TigerVNC is an implementation of VNC (Virtual Network Computing), a
client/server application that allows users to launch and interact
with graphical applications on remote machines. TigerVNC is capable
of running 3D and video applications. TigerVNC also provides
extensions for advanced authentication methods and TLS encryption.

%package -n xorg-x11-Xvnc
Summary:        TigerVNC implementation of Xvnc
Group:          System/X11/Servers/XF86_4
Requires(pre):  group(shadow)
%sysusers_requires
Requires(post): /bin/awk
Requires(post): systemd
%if %{use_firewalld}
BuildRequires:  firewall-macros
%endif
# Needed to generate certificates
Requires:       windowmanager
Requires:       /usr/bin/dbus-launch
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
Provides:       tightvnc = 1.5.0
Obsoletes:      tightvnc < 1.5.0
Provides:       xorg-x11-Xvnc:/usr/lib/vnc/with-vnc-key.sh
Conflicts:      patterns-wsl-tmpfiles

%description -n xorg-x11-Xvnc
This is the TigerVNC implementation of Xvnc.

%package -n xorg-x11-Xvnc-module
Summary:        VNC module for X server
#%%{x11_abi_extension_req}
Group:          System/X11/Servers/XF86_4
Requires:       xorg-x11-Xvnc

%description -n xorg-x11-Xvnc-module
This module allows to share content of X server's screen over VNC.
It is loaded into X server as a module if enable in X server's
configuration.

%package -n xorg-x11-Xvnc-novnc
Summary:        NoVNC service for Xvnc
Group:          System/X11/Servers/XF86_4
Requires:       novnc
Requires:       python3-websockify
Requires:       xorg-x11-Xvnc
BuildArch:      noarch
%{?systemd_requires}

%description -n xorg-x11-Xvnc-novnc
A service that starts noVNC linked to Xvnc server.

%package -n xorg-x11-Xvnc-java
Summary:        VNC viewer in java
Group:          System/X11/Servers/XF86_4
BuildArch:      noarch
%{?systemd_requires}

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
Requires:       xorg-x11-Xvnc
Conflicts:      x11vnc
Provides:       x11vnc
BuildArch:      noarch

%description x11vnc
This is a wrapper that looks like x11vnc, but starts x0vncserver instead.
It maps common x11vnc arguments to x0vncserver arguments.

%prep
%autosetup -p1

cp -r %{_prefix}/src/xserver/* unix/xserver/
pushd unix/xserver
patch -p1 < ../xserver21.patch
popd

%build
%sysusers_generate_pre %{SOURCE17} xorg-x11-Xvnc vnc.conf
export CXXFLAGS="%optflags"
export CFLAGS="%optflags"
sed "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE10} > xvnc@.service
sed "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE16} > xvnc-novnc.service
# Build all tigervnc
cmake -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_libexecdir} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo .
%make_build

# Build Xvnc server
pushd unix/xserver
autoreconf -fi
%configure \
        --disable-xorg --disable-xnest --disable-xvfb \
        --disable-xwin --disable-xephyr --disable-kdrive \
        --disable-static --disable-xinerama \
        --with-xkb-path="%{_datadir}/X11/xkb" \
        --with-xkb-output="%{_sharedstatedir}/xkb/compiled" \
        --enable-glx --enable-dri \
%ifnarch s390 s390x
	--enable-dri2 \
%endif
        --disable-config-hal \
        --disable-config-udev \
        --without-dtrace \
        --disable-unit-tests \
        --disable-devel-docs \
        --with-fontrootdir=%{_datadir}/fonts \
        --disable-selective-werror
%make_build V=1
popd

# Build java client
pushd java
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} .
%make_build
popd

%install

%make_install

%if %use_update_alternative
mv %{buildroot}%{_bindir}/vncviewer %{buildroot}%{_bindir}/vncviewer-tigervnc
mv %{buildroot}%{_datadir}/man/man1/vncviewer.1 %{buildroot}%{_datadir}/man/man1/vncviewer-tigervnc.1
%endif

pushd unix/xserver
%make_install
popd

pushd java
mkdir -p %{buildroot}%{_datadir}/vnc/classes
install -m755 VncViewer.jar %{buildroot}%{_datadir}/vnc/classes
popd

%ifnarch s390x
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/X11/xorg.conf.d/10-libvnc.conf
%endif

%if %{use_firewalld}
install -D -m 644 %{SOURCE13} %{buildroot}%{_prefix}/lib/firewalld/services/tigervnc.xml
install -D -m 644 %{SOURCE14} %{buildroot}%{_prefix}/lib/firewalld/services/tigervnc-https.xml
%else
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/vnc-server
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/vnc-httpd
%endif

# only package as %%doc (boo#1173045)
cp %{SOURCE4} .
install -D -m 755 %{SOURCE5} %{buildroot}%{_bindir}/vncpasswd.arg
install -D -m 644 %{SOURCE6} %{buildroot}%{_pam_vendordir}/vnc
%if 0%{?suse_version} >= 1550
mv %{buildroot}%{_sysconfdir}/pam.d/tigervnc %{buildroot}%{_pam_vendordir}
%endif
install -D -m 644 %{SOURCE8} %{buildroot}%{_datadir}/vnc/classes
%if %use_update_alternative
ln -s -f %{_sysconfdir}/alternatives/vncviewer %{buildroot}%{_bindir}/vncviewer
ln -s -f %{_sysconfdir}/alternatives/vncviewer.1.gz %{buildroot}%{_mandir}/man1/vncviewer.1.gz
%endif

%if %with_rc_service_symlink
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcxvnc
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcxvnc-novnc
%endif

mkdir -p %{buildroot}%{_sysconfdir}/vnc

mkdir -p %{buildroot}%{_libexecdir}/vnc
install -D -m 755 %{SOURCE7} %{buildroot}%{_libexecdir}/vnc

install -D -m 755 %{SOURCE9} %{buildroot}%{_bindir}/x11vnc

install -D xvnc@.service -m 0444 %{buildroot}%{_unitdir}/xvnc@.service
install -D %{SOURCE11} -m 0444 %{buildroot}%{_unitdir}/xvnc.socket
install -D %{SOURCE12} -m 0444 %{buildroot}%{_unitdir}/xvnc-novnc.socket
install -D %{SOURCE15} -m 0444 %{buildroot}%{_unitdir}/xvnc.target
install -D xvnc-novnc.service -m 0444 %{buildroot}%{_unitdir}/xvnc-novnc.service

install -Dm0644 %{SOURCE17} %{buildroot}%{_sysusersdir}/vnc.conf

rm -rf %{buildroot}%{_datadir}/doc/tigervnc*

%find_lang '%{name}'
%python3_fix_shebang

%if %use_update_alternative
%post
%_sbindir/update-alternatives \
    --install %{_bindir}/vncviewer vncviewer %{_bindir}/vncviewer-tigervnc 20 \
    --slave %{_mandir}/man1/vncviewer.1.gz  vncviewer.1.gz  %{_mandir}/man1/vncviewer-tigervnc.1.gz
%endif

%if %use_update_alternative
%postun
if [ "$1" = 0 ] ; then
   "%{_sbindir}/update-alternatives" --remove vncviewer %{_bindir}/vncviewer-tigervnc
fi
%endif

%pre -n xorg-x11-Xvnc -f xorg-x11-Xvnc.pre
%service_add_pre xvnc.socket xvnc.target
%if 0%{?suse_version} >= 1550
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/vnc pam.d/tigervnc ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans -n xorg-x11-Xvnc
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/vnc pam.d/tigervnc ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post -n xorg-x11-Xvnc
%service_add_post xvnc.socket xvnc.target

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
%service_del_preun xvnc.socket xvnc.target

%postun -n xorg-x11-Xvnc
%service_del_postun xvnc.socket xvnc.target

%pre -n xorg-x11-Xvnc-novnc
%service_add_pre xvnc-novnc.service xvnc-novnc.socket

%post -n xorg-x11-Xvnc-novnc
%service_add_post xvnc-novnc.service xvnc-novnc.socket

%preun -n xorg-x11-Xvnc-novnc
%service_del_preun xvnc-novnc.service xvnc-novnc.socket

%postun -n xorg-x11-Xvnc-novnc
%service_del_postun xvnc-novnc.service xvnc-novnc.socket

%post -n libXvnc1 -p /sbin/ldconfig
%postun -n libXvnc1 -p /sbin/ldconfig

%files -f %{name}.lang
%license LICENCE.TXT
%doc README.rst
%if %use_update_alternative
%ghost %{_bindir}/vncviewer
%{_bindir}/vncviewer-tigervnc
%ghost %{_mandir}/man1/vncviewer.1.gz
%{_mandir}/man1/vncviewer-tigervnc.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/vncviewer
%ghost %{_sysconfdir}/alternatives/vncviewer.1.gz
%else
%{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1%{?ext_man}
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
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps

%{_datadir}/icons/hicolor/*/apps/tigervnc.png
%{_datadir}/icons/hicolor/scalable/apps/tigervnc.svg

%{_datadir}/applications/vncviewer.desktop
%{_datadir}/metainfo/org.tigervnc.vncviewer.metainfo.xml

%files -n xorg-x11-Xvnc
%license LICENCE.TXT
%doc README.rst vnc.reg
%doc unix/vncserver/HOWTO.md

%{_bindir}/Xvnc
%{_bindir}/vncconfig
%{_bindir}/vncpasswd
%{_bindir}/vncpasswd.arg
%{_bindir}/x0vncserver
%{_sbindir}/vncsession

%{_libexecdir}/vncserver
%{_libexecdir}/vncsession-start

%exclude %{_mandir}/man1/Xserver.1*
%{_mandir}/man1/Xvnc.1%{?ext_man}
%{_mandir}/man1/vncconfig.1%{?ext_man}
%{_mandir}/man1/vncpasswd.1%{?ext_man}
%{_mandir}/man1/x0vncserver.1%{?ext_man}
%{_mandir}/man8/vncserver.8%{?ext_man}
%{_mandir}/man8/vncsession.8%{?ext_man}

%{_unitdir}/vncserver@.service
%{_unitdir}/xvnc@.service
%{_unitdir}/xvnc.socket
%{_unitdir}/xvnc.target
%{_sysusersdir}/vnc.conf
%if %with_rc_service_symlink
%{_sbindir}/rcxvnc
%endif

%dir %{_sysconfdir}/tigervnc
%config(noreplace) %{_sysconfdir}/tigervnc/vncserver*

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
%config %{_sysconfdir}/pam.d/vnc
%config(noreplace) %{_sysconfdir}/pam.d/tigervnc
%else
%{_pam_vendordir}/vnc
%{_pam_vendordir}/tigervnc
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
%if %with_rc_service_symlink
%{_sbindir}/rcxvnc-novnc
%endif

%files -n xorg-x11-Xvnc-java
%doc java/com/tigervnc/vncviewer/README
%{_datadir}/vnc

%files -n libXvnc1
%{_libdir}/libXvnc.so.1*

%files -n libXvnc-devel
%{_libdir}/libXvnc.so
%{_includedir}/X11/extensions/Xvnc.h

%files x11vnc
%{_bindir}/x11vnc

%changelog
