#
# spec file for package xdm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define _dminitdir /usr/lib/X11/displaymanagers
%if 0%{?suse_version} > 1230
%define with_systemd 1
%else
%define with_systemd 0
%endif
%if 0%{?suse_version} < 01210
%define dm_fallbacks 1
%else
%define dm_fallbacks 0
%endif
%if !%with_systemd
%define _unitdir %{_prefix}/lib/systemd/system
%endif
Name:           xdm
Version:        1.1.12
Release:        0
Summary:        X Display Manager
License:        MIT
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        xdm.tar.bz2
Source2:        HOWTO.xdm
Source3:        xdm-fallbacks.tar.bz2
Source4:        display-manager.service
Source5:        xsession.desktop
Patch1:         xdm-tolerant-hostname-changes.diff
# PATCH-FEATURE-OPENSUSE xdm-with-update-alternative.patch dimstar@opensuse.org -- Choice of default DM by means of u-a
Patch2:         xdm-with-update-alternative.patch
# needed for patch0, patch2, patch3, patch4
Patch3:         n_Allow-the-greeter-to-set-the-input-fields-bg-color.patch
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
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
%if 0%{?suse_version} > 1320
BuildRequires:  firewall-macros
%endif
Requires:       /sbin/pidof
%if 0%{?with_systemd}
Requires:       %fillup_prereq
%else
Requires:       insserv-compat
%endif
Requires:       logrotate
Requires:       sessreg
Requires:       xconsole
Requires:       xinit
Requires:       xli
Requires:       xmessage
Requires:       xrdb
Requires:       xset
Requires:       xsetroot
Recommends:     dbus-1-x11
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
%if !%with_systemd
Patch0:         xdm-consolekit.diff
%endif
%if 0%{?suse_version} >= 01140 && 0%{?suse_version} < 1320
# Needed to create the man page symlink to init.d
BuildRequires:  aaa_base-extras
%endif
%if !%with_systemd
BuildRequires:  ConsoleKit-devel
Requires:       ConsoleKit
%else
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%endif
%if 0%{?suse_version} > 1320
Requires:       xterm-bin
%else
Requires:       xterm
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
%if !%with_systemd
%patch0 -p1
%endif
pushd xdm
%patch1 -p1
popd
# Special note: patch 2 is applied in install section; tagging it here for the source validator only
#patch2 -p1
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
make %{?_smp_mflags}

%install
%make_install
# Not used anymore by SuSE
rm %{buildroot}%{_sysconfdir}/X11/xdm/{GiveConsole,TakeConsole,Xsetup_0}

pushd %{buildroot}
# SuSE default XDM configuration
tar xf %{SOURCE1}
%if 0%{?suse_version} > 1320
rm    etc/sysconfig/SuSEfirewall2.d/services/xdmcp
rmdir etc/sysconfig/SuSEfirewall2.d/services
rmdir etc/sysconfig/SuSEfirewall2.d
rmdir etc/sysconfig
%else
rm    usr/lib/firewalld/services/x11.xml
rmdir usr/lib/firewalld/services
rmdir usr/lib/firewalld
%endif
%if 0%{?suse_version} >= 1330
patch -p1 < %{PATCH2}
rm -f usr/lib/X11/display-manager.orig
%endif
%if "%{_fillupdir}" != "/var/adm/fillup-templates"
  mkdir -p %{buildroot}$(dirname %{_fillupdir})
  mv %{buildroot}/var/adm/fillup-templates \
     %{buildroot}$(dirname %{_fillupdir})
%endif

%if %dm_fallbacks
tar xf %{SOURCE3}
%endif
%ifarch s390 s390x
sed -i -e "s+DISPLAYMANAGER_REMOTE_ACCESS=.*+DISPLAYMANAGER_REMOTE_ACCESS=\"yes\"+g" \
       -e "s+DISPLAYMANAGER_STARTS_XSERVER=.*+DISPLAYMANAGER_STARTS_XSERVER=\"no\"+g" \
    %{buildroot}%{_fillupdir}/sysconfig.displaymanager
%endif
popd

# Correct location (FHS-2.1)
ln -s %{_localstatedir}/lib/xdm/authdir %{buildroot}%{_sysconfdir}/X11/xdm/authdir
# bnc#223734
rm %{buildroot}%{_libdir}/X11/xdm/libXdmGreet.la
# for FHS compliance (bnc#21857)
mv %{buildroot}%{_libdir}/X11/xdm/chooser %{buildroot}%{_bindir}
# fdo#35868 (closed INVALID, but because of above fix, we want it)
ln -s xdm.8%{?ext_man} %{buildroot}%{_mandir}/man8/chooser.8%{?ext_man}
install -D %{SOURCE5} -m 0644 %{buildroot}%{_datadir}/xsessions/xsession.desktop
%if 0%{?suse_version} < 1315
# missing manual page
mkdir -p %{buildroot}%{_mandir}/man8
ln -s ../man7/init.d.7%{?ext_man} %{buildroot}%{_mandir}/man8/rcxdm.8%{?ext_man}
ln -sf %{_sysconfdir}/init.d/xdm %{buildroot}%{_sbindir}/rcxdm
%else
rm -f %{buildroot}%{_sbindir}/rcxdm
install -D %{SOURCE4} -m 0444 %{buildroot}%{_unitdir}/display-manager.service
ln -sf service %{buildroot}%{_sbindir}/rcdisplay-manager
cat > %{buildroot}%{_sbindir}/rcxdm <<-'EOF'
	#!/bin/bash
	exec -a rcdisplay-manager %{_sbindir}/rcdisplay-manager ${1+"$@"}
	EOF
chmod 0755 %{buildroot}%{_sbindir}/rcxdm
%endif
%if 0%{?suse_version} >= 1330
# prepare for defaul-dm to be chosen by means of update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}/usr/lib/X11/displaymanagers/default-displaymanager
# Inject a dummy 'console' selection - which used to be choice in /etc/sysconfig/displaymanager
touch %{buildroot}/usr/lib/X11/displaymanagers/console
%endif

%post
%if 0%{?suse_version} < 1315
%{fillup_and_insserv -Y xdm}
%else
%service_add_post display-manager.service
%{fillup_only -n displaymanager}
%endif
%if 0%{?suse_version} >= 1330
%{_sbindir}/update-alternatives --install /usr/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager /usr/lib/X11/displaymanagers/console 5
%{_sbindir}/update-alternatives --install /usr/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager /usr/lib/X11/displaymanagers/xdm 10
# get rid of DISPLAYMANAGER in /etc/sysconfig/displaymanager (boo#1125040)
sed -i 's/DISPLAYMANAGER=.*//g' /etc/sysconfig/displaymanager
%endif
%if 0%{?suse_version} > 1320
%firewalld_reload
%endif

%pre
%if !0%{?suse_version} < 1315
  %service_add_pre display-manager.service
%endif

%postun
%if 0%{?suse_version} < 1315
%{insserv_cleanup}
%else
# Do not restart DM on update (bnc#886641)
%service_del_postun -n display-manager.service
%endif
%if 0%{?suse_version} >= 1330
[ -f /usr/lib/X11/displaymanagers/console ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager /usr/lib/X11/displaymanagers/console
[ -f /usr/lib/X11/displaymanagers/xdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager /usr/lib/X11/displaymanagers/xdm
%endif

%preun
%if !0%{?suse_version} < 1315
  %service_del_preun display-manager.service
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README.md
%doc HOWTO.xdm
%dir %{_dminitdir}
%{_dminitdir}/xdm
%if 0%{?suse_version} >= 1330
%{_dminitdir}/console
/usr/lib/X11/displaymanagers/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%endif
%if %dm_fallbacks
%{_dminitdir}/entrance.fallback
%{_dminitdir}/gdm.fallback
%{_dminitdir}/kdm.fallback
%{_dminitdir}/lxdm.fallback
%{_dminitdir}/slim.fallback
%{_dminitdir}/wdm.fallback
%endif
%config %{_sysconfdir}/X11/xdm/
%dir %{_sysconfdir}/X11/xdm/scripts
%if 0%{?suse_version} > 1320
%dir /usr/lib/firewalld
%dir /usr/lib/firewalld/services
/usr/lib/firewalld/services/x11.xml
%else
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/xdmcp
%endif
%if 0%{?suse_version} < 1315
%{_sysconfdir}/init.d/xdm
%exclude /usr/lib/X11/display-manager
%else
%exclude %{_sysconfdir}/init.d/xdm
%{_unitdir}/display-manager.service
/usr/lib/X11/display-manager
%endif
%config %{_sysconfdir}/logrotate.d/xdm
%config(noreplace) %{_sysconfdir}/pam.d/xdm
%config(noreplace) %{_sysconfdir}/pam.d/xdm-np
%dir %{_localstatedir}/lib/xdm/
%{_fillupdir}/sysconfig.displaymanager
%{_localstatedir}/lib/xdm/authdir/
%ghost %{_localstatedir}/log/xdm.errors
%{_bindir}/chooser
%{_bindir}/xdm
%{_sbindir}/rcxdm
%if 0%{?suse_version} >= 1315
%{_sbindir}/rcdisplay-manager
%endif
%{_libdir}/X11/xdm/
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Chooser
%{_mandir}/man8/chooser.8%{?ext_man}
%{_mandir}/man8/xdm.8%{?ext_man}
%if 0%{?suse_version} < 1315
%{_mandir}/man8/rcxdm.8%{?ext_man}
%endif
%ifnarch %ix86
%dir %{_libdir}/X11
%endif

%files xsession
%dir %{_datadir}/xsessions
%{_datadir}/xsessions/xsession.desktop

%changelog
