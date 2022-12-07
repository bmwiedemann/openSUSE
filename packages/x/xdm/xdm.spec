#
# spec file for package xdm
#
# Copyright (c) 2022 SUSE LLC
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


%define _dminitdir %{_prefix}/lib/X11/displaymanagers
%if 0%{?suse_version} >= 1550
%define UsrEtcMove 1
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           xdm
Version:        1.1.14
Release:        0
Summary:        X Display Manager
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        xdm.tar.bz2
Source2:        HOWTO.xdm
Source4:        display-manager.service
Source5:        xsession.desktop
Patch1:         xdm-tolerant-hostname-changes.diff
Patch2:         xdm-tarball.patch
Patch3:         n_Allow-the-greeter-to-set-the-input-fields-bg-color.patch
Patch4:         xinit-UsrEtcMove.patch
BuildRequires:  firewall-macros
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.4
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtrans)
Requires:       %fillup_prereq
Requires:       /sbin/startproc
Requires:       logrotate
Requires:       sessreg
Requires:       xconsole
Requires:       xinit
Requires:       xli
Requires:       xmessage
Requires:       xrdb
Requires:       xset
Requires:       xsetroot
Requires:       xterm-bin
Recommends:     dbus-1-x11
Recommends:     xdmbgrd
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
%{?systemd_requires}
%if 0%{?suse_version} >= 1550
Requires:       %{_bindir}/pidof
%else
Requires:       /sbin/pidof
%endif

%description
Xdm manages a collection of X displays, which may be on the local host
or remote servers.

%package xsession
Summary:        User/System Xsession Desktop File
Group:          System/X11/Utilities
Requires:       xdm
Enhances:       xdm

%description xsession
This package contains the System desktop file which will cause
the execution of a user provided $HOME/.xsession script or pick
the system wide DM default set in %{_sysconfdir}/sysconfig/displaymanager.

%prep
%setup -q
cp %{SOURCE2} .
pushd xdm
%patch1 -p1
popd
# reverse apply (boo#1130321)
%patch3 -p1 -R

%build
# needed for patch0
autoreconf -fi
%configure \
        --disable-static \
        --with-pam \
        --with-xdmconfigdir=%{_sysconfdir}/X11/xdm \
        --with-xdmscriptdir=%{_sysconfdir}/X11/xdm \
	--with-systemdsystemunitdir=no
%make_build

%install
%make_install
# Not used anymore by SuSE
rm %{buildroot}%{_sysconfdir}/X11/xdm/{GiveConsole,TakeConsole,Xsetup_0}

pushd %{buildroot}
# SuSE default XDM configuration
tar xf %{SOURCE1}
%if 0%{?UsrEtcMove}
patch -p0 < %{PATCH2}
mkdir -p usr%{_sysconfdir}/X11/xdm
mv etc/X11/xdm/* usr%{_sysconfdir}/X11/xdm
# Edited by SUSEConfig.xdm, package a copy
for i in xdm-config Xservers; do
	cp usr%{_sysconfdir}/X11/xdm/$i etc/X11/xdm/$i
done
mkdir -p ./%{_pam_vendordir}
mv etc/pam.d/* ./%{_pam_vendordir}/
%else
patch -p0 < %{PATCH4}
%endif
%if "%{_fillupdir}" != "%{_localstatedir}/adm/fillup-templates"
  mkdir -p %{buildroot}$(dirname %{_fillupdir})
  mv %{buildroot}%{_localstatedir}/adm/fillup-templates \
     %{buildroot}$(dirname %{_fillupdir})
%endif

%ifarch s390 s390x
sed -i -e "s+DISPLAYMANAGER_REMOTE_ACCESS=.*+DISPLAYMANAGER_REMOTE_ACCESS=\"yes\"+g" \
       -e "s+DISPLAYMANAGER_STARTS_XSERVER=.*+DISPLAYMANAGER_STARTS_XSERVER=\"no\"+g" \
    %{buildroot}%{_fillupdir}/sysconfig.displaymanager
%endif
popd

# Correct location (FHS-2.1)
%if 0%{?UsrEtcMove}
ln -s %{_localstatedir}/lib/xdm/authdir %{buildroot}%{_distconfdir}/X11/xdm/authdir
%else
ln -s %{_localstatedir}/lib/xdm/authdir %{buildroot}%{_sysconfdir}/X11/xdm/authdir
%endif
# bnc#223734
rm %{buildroot}%{_libdir}/X11/xdm/libXdmGreet.la
# for FHS compliance (bnc#21857)
mv %{buildroot}%{_libdir}/X11/xdm/chooser %{buildroot}%{_bindir}
# fdo#35868 (closed INVALID, but because of above fix, we want it)
ln -s xdm.8%{?ext_man} %{buildroot}%{_mandir}/man8/chooser.8%{?ext_man}
install -D %{SOURCE5} -m 0644 %{buildroot}%{_datadir}/xsessions/xsession.desktop
rm -f %{buildroot}%{_sbindir}/rcxdm
install -D %{SOURCE4} -m 0444 %{buildroot}%{_unitdir}/display-manager.service
ln -sf service %{buildroot}%{_sbindir}/rcdisplay-manager
cat > %{buildroot}%{_sbindir}/rcxdm <<-'EOF'
	#!/bin/bash
	exec -a rcdisplay-manager %{_sbindir}/rcdisplay-manager ${1+"$@"}
	EOF
chmod 0755 %{buildroot}%{_sbindir}/rcxdm
# prepare for defaul-dm to be chosen by means of update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_prefix}/lib/X11/displaymanagers/default-displaymanager
# Inject a dummy 'console' selection - which used to be choice in /etc/sysconfig/displaymanager
touch %{buildroot}%{_prefix}/lib/X11/displaymanagers/console

%if 0%{?UsrEtcMove}
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/logrotate.d/xdm %{buildroot}%{_distconfdir}/logrotate.d/xdm
%endif

%post
# enable Xorg on s390x with virtio (Redhat PCI ID 1af4:1050) on installation (but not upgrade)
if [ $1 -eq 1 ] ; then
  if [ "$(arch)" = "s390x" ]; then
    if [ -d /dev/dri ]; then
      sed -i -e "s+DISPLAYMANAGER_REMOTE_ACCESS=.*+DISPLAYMANAGER_REMOTE_ACCESS=\"no\"+g" \
             -e "s+DISPLAYMANAGER_STARTS_XSERVER=.*+DISPLAYMANAGER_STARTS_XSERVER=\"yes\"+g" \
          %{_fillupdir}//sysconfig.displaymanager
    fi
  fi
fi
%service_add_post display-manager.service
%{fillup_only -n displaymanager}
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/console 5
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/xdm 10
# get rid of DISPLAYMANAGER in /etc/sysconfig/displaymanager (boo#1125040)
sed -i 's/DISPLAYMANAGER=.*//g' %{_sysconfdir}/sysconfig/displaymanager
%firewalld_reload

%pre
%service_add_pre display-manager.service

%postun
# Do not restart DM on update (bnc#886641)
%if 0%{?suse_version} >= 1550
%service_del_postun_without_restart display-manager.service
%else
%service_del_postun -n display-manager.service
%endif
[ -f %{_prefix}/lib/X11/displaymanagers/console ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_prefix}/lib/X11/displaymanagers/console
[ -f %{_prefix}/lib/X11/displaymanagers/xdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_prefix}/lib/X11/displaymanagers/xdm

%preun
%service_del_preun display-manager.service

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%doc HOWTO.xdm
%dir %{_dminitdir}
%{_dminitdir}/xdm
%{_dminitdir}/console
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%if 0%{?UsrEtcMove}
%dir %{_distconfdir}/X11
%{_distconfdir}/X11/xdm/
%endif
%config %{_sysconfdir}/X11/xdm/
%if 0%{?UsrEtcMove}
%dir %{_distconfdir}/X11/xdm/scripts
%else
%dir %{_sysconfdir}/X11/xdm/scripts
%endif
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/x11.xml
%{_unitdir}/display-manager.service
%{_prefix}/lib/X11/display-manager
%if 0%{?UsrEtcMove}
%{_distconfdir}/logrotate.d/xdm
%else
%config %{_sysconfdir}/logrotate.d/xdm
%endif
%if 0%{?UsrEtcMove}
%{_pam_vendordir}/xdm
%{_pam_vendordir}/xdm-np
%else
%config(noreplace) %{_sysconfdir}/pam.d/xdm
%config(noreplace) %{_sysconfdir}/pam.d/xdm-np
%endif
%dir %{_localstatedir}/lib/xdm/
%{_fillupdir}/sysconfig.displaymanager
%{_localstatedir}/lib/xdm/authdir/
%ghost %{_localstatedir}/log/xdm.errors
%{_bindir}/chooser
%{_bindir}/xdm
%{_sbindir}/rcxdm
%{_sbindir}/rcdisplay-manager
%{_libdir}/X11/xdm/
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Chooser
%{_mandir}/man8/chooser.8%{?ext_man}
%{_mandir}/man8/xdm.8%{?ext_man}
%ifnarch %{ix86}
%dir %{_libdir}/X11
%endif

%files xsession
%{_datadir}/xsessions/xsession.desktop

%changelog
