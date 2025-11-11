#
# spec file for package gdm
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define enable_split_authentication 1

# special hack for SLE15/Leap 15: it does not yet know /usr/etc, and files in /etc should be %%config
%if 0%{?suse_version} >= 1550
  %define _config_norepl %nil
%else
  %define _pam_vendordir %{_sysconfdir}/pam.d
  %define _config_norepl %config(noreplace)
%endif

Name:           gdm
Version:        49.1
Release:        0
Summary:        The GNOME Display Manager
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GDM

Source0:        %{name}-%{version}.tar.zst
Source1:        gdm.pamd
Source2:        gdm-autologin.pamd
Source3:        gdm-launch-environment.pamd
Source4:        gdm-fingerprint.pamd
Source5:        gdm-smartcard.pamd
# gdmflexiserver wrapper, to enable other display managers to abuse the gdmflexiserver namespace (like lightdm)
Source6:        gdmflexiserver-wrapper
# /etc/xinit.d/xdm integration script
Source7:        X11-displaymanager-gdm
# Use tmpfiles to create directories under /var to support transactional updates
Source9:        gdm.tmpfiles
# Use reserveVT.conf to make autologin user session not to select tty1
Source10:       reserveVT.conf
# Use sysusers to create gdm system user
Source11:       gdm.sysusers
# PAM configuration files for SLE15 and older
Source12:       gdm-sle.pamd
Source13:       gdm-autologin-sle.pamd
Source14:       gdm-fingerprint-sle.pamd
Source15:       gdm-smartcard-sle.pamd
# Configuration for pulseaudio
Source20:       default.pa
Source21:       keytable.in
# PATCH-FIX-OPENSUSE  gdm-sysconfig-settings.patch bnc432360 bsc#919723 hpj@novell.com -- Read autologin options from /etc/sysconfig/displaymanager; note that accountsservice has a similar patch (accountsservice-sysconfig.patch)
Patch1:         gdm-sysconfig-settings.patch
# PATCH-FIX-OPENSUSE gdm-suse-xsession.patch vuntz@novell.com -- Use the /etc/X11/xdm/* scripts
Patch2:         gdm-suse-xsession.patch
# PATCH-FIX-OPENSUSE gdm-xauthlocalhostname.patch bnc#538064 vuntz@novell.com -- Set XAUTHLOCALHOSTNAME to current hostname when we authenticate, for local logins, to avoid issues in the session in case the hostname changes later one. See comment 24 in the bug.
Patch4:         gdm-xauthlocalhostname.patch
# PATCH-FIX-OPENSUSE gdm-switch-to-tty1.patch bsc#1113700 xwang@suse.com -- switch to tty1 when stopping gdm service
Patch5:         gdm-switch-to-tty1.patch
# PATCH-FIX-OPENSUSE gdm-initial-setup-hardening.patch boo#1140851, glgo#GNOME/gnome-initial-setup#76 fezhang@suse.com -- Prevent gnome-initial-setup running if any regular user has perviously logged into the system
Patch6:         gdm-initial-setup-hardening.patch
# PATCH-FIX-OPENSUSE gdm-service-keytable.patch bsc#1248831 bsc#1250366 yfjiang@suse.com -- set KEYMAP to XkbLayout for GNOME
Patch10:        gdm-service-keytable.patch

### NOTE: Keep please SLE-only patches at bottom (starting on 1000).
# PATCH-FIX-SLE gdm-disable-gnome-initial-setup.patch bnc#1067976 qzhao@suse.com -- Disable gnome-initial-setup runs before gdm, g-i-s will only serve for CJK people to choose the input-method after login.
Patch1000:      gdm-disable-gnome-initial-setup.patch

BuildRequires:  /usr/bin/dbus-run-session
BuildRequires:  check-devel
# dconf and gnome-session-core are needed for directory ownership
BuildRequires:  dconf
BuildRequires:  fdupes
BuildRequires:  gnome-session-core
BuildRequires:  itstool
BuildRequires:  meson >= 0.57
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  tcpd-devel
BuildRequires:  xorg-x11-server
BuildRequires:  xorg-x11-server-extra
BuildRequires:  pkgconfig(accountsservice) >= 0.6.35
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.56.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.12
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.1
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ply-boot-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{_bindir}/dbus-run-session
Requires:       %{name}-branding = %{version}
Requires:       displaymanager-sysconfig
Requires:       gdmflexiserver
Requires:       gnome-session-core
Requires:       gnome-settings-daemon
Requires:       gnome-shell
# xdm package ships systemd display-manager service and other common scripts
# between display managers (bsc#1084655)
Requires:       (gdm-xdm-integration or gdm-systemd)
Suggests:       gdm-systemd
# whenever xdm is installed, we need to be sure to integrate into it
Requires:       (gdm-xdm-integration if xdm)
Requires(post): dconf
Requires(pre):  group(video)
Recommends:     iso-codes
# accessibility
Recommends:     orca
# smartcard login
Recommends:     pam_pkcs11
DocDir:         %{_defaultdocdir}
%ifnarch s390 s390x
BuildRequires:  pkgconfig(xorg-server)
%endif
%sysusers_requires

%description
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package -n libgdm1
Summary:        Client Library for Communicating with GDM Greeter Server
Group:          System/Libraries
Requires:       %{name}-schema
Recommends:     gdm

%description -n libgdm1
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package -n typelib-1_0-Gdm-1_0
Summary:        Introspection bindings for gdm
Group:          System/Libraries

%description -n typelib-1_0-Gdm-1_0
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

This package provides the GObject Introspection bindings for
communicating with the GDM greeter server.

%package schema
Summary:        Config schema for GDM
Group:          System/Libraries
BuildArch:      noarch

%description schema
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package devel
Summary:        Libraries for GDM -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgdm1 = %{version}
Requires:       typelib-1_0-Gdm-1_0 = %{version}

%description devel
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package branding-upstream
Summary:        The GNOME Display Manager -- Upstream default configuration
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: Provide one file:
#BRAND: /etc/gdm/custom.conf
#BRAND:   Default configuration of gdm

%description branding-upstream
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

This package provides the upstream default configuration for gdm.

%package xdm-integration
Summary:        GDM integration into the xdm wrapper script
Group:          System/GUI/GNOME
Requires:       gdm
Requires:       xdm
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%description xdm-integration
GDM's XDM wrapper integration
By default openSUSE uses xdm which enables the DM based on sysconfig.

%package systemd
Summary:        Systemd gdm.service file
Group:          System/GUI/GNOME
Requires:       gdm
# Upgrade xdm first if installed - to run systemd DM migration
Requires(pre):  (xdm >= 1.1.17 if xdm)
BuildArch:      noarch

%description systemd
GDM's systemd service file.
By default openSUSE uses xdm which enables the DM based on sysconfig.
This package is only needed if the system administrator wishes to use
'systemctl' instead of openSUSE's default 'update-alternatives' method.

%package -n gdmflexiserver
Summary:        Compatibility Wrapper for Display Managers
Group:          System/GUI/GNOME
Suggests:       gdm
BuildArch:      noarch

%description -n gdmflexiserver
The GDMFlexiServer tool interacts with the display manager to
enable fast user switching. This package contains a wrapper that
selects the correct Gdmflexiserver implementation, based on the
running display manager.

%lang_package

%prep
%autosetup -N
### NON-SLE patches start from 0 to 999
%autopatch -p1 -m 1 -M 999

### SLE and Leap only patches start at 1000
%if !0%{?is_opensuse} || 0%{?suse_version} <= 1600
## Use this when there's no need to skip patches.
%autopatch -p1 -m 1000
%endif

%build
%meson \
        --libexecdir=%{_libexecdir}/gdm \
        -Dat-spi-registryd-dir=%{_libexecdir}/at-spi \
        -Dgdm-xsession=true \
        -Dgnome-settings-daemon-dir=%{_libexecdir}/gnome-settings-daemon-3.0 \
        -Dinitial-vt=7 \
        -Dipv6=true \
        -Dpam-mod-dir=%{_pam_moduledir} \
        -Ddbus-sys=%{_datadir}/dbus-1/system.d \
        -Ddistro=generic \
        -Dplymouth=enabled \
        -Drun-dir=/run/gdm \
%if %{enable_split_authentication}
        -Dsplit-authentication=true \
%else
        -Dsplit-authentication=false \
%endif
        -Dudev-dir=%{_udevrulesdir} \
        -Dwayland-support=true \
%if !0%{?is_opensuse}
        -Dx11-support=false \
%endif
        %nil
%meson_build
%sysusers_generate_pre %{SOURCE11} gdm gdm.conf

%install
%meson_install
## Install PAM files.
mkdir -p %{buildroot}%{_pam_vendordir}
# Pam config for the greeter session
cp %{SOURCE3} %{buildroot}%{_pam_vendordir}/gdm-launch-environment
%if 0%{?suse_version} >= 1550
# Generic pam config
cp %{SOURCE1} %{buildroot}%{_pam_vendordir}/gdm
# Pam config for autologin
cp %{SOURCE2} %{buildroot}%{_pam_vendordir}/gdm-autologin
%if %{enable_split_authentication}
# Pam config for fingerprint authentication
cp %{SOURCE4} %{buildroot}%{_pam_vendordir}/gdm-fingerprint
# Pam config for smartcard authentication
cp %{SOURCE5} %{buildroot}%{_pam_vendordir}/gdm-smartcard
%endif
%else
# Generic pam config
cp %{SOURCE12} %{buildroot}%{_pam_vendordir}/gdm
# Pam config for autologin
cp %{SOURCE13} %{buildroot}%{_pam_vendordir}/gdm-autologin
%if %{enable_split_authentication}
# Pam config for fingerprint authentication
cp %{SOURCE14} %{buildroot}%{_pam_vendordir}/gdm-fingerprint
# Pam config for smartcard authentication
cp %{SOURCE15} %{buildroot}%{_pam_vendordir}/gdm-smartcard
%endif
%endif
# The default gdm pam configuration is the one to be used as pam-password too
ln -s gdm %{buildroot}%{_pam_vendordir}/gdm-password
## Install other files
# Install PostLogin script.
mv %{buildroot}%{_sysconfdir}/gdm/PostLogin/Default.sample %{buildroot}%{_sysconfdir}/gdm/PostLogin/Default
# Move gdmflexiserver to libexecdir and replace it with the compatibility wrapper
mv %{buildroot}%{_bindir}/gdmflexiserver %{buildroot}%{_libexecdir}/gdm/gdmflexiserver
install -m 755 %{SOURCE6} %{buildroot}%{_bindir}/gdmflexiserver
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{buildroot}%{_bindir}/gdmflexiserver
#Install /etc/xinit.d/xdm integration script
install -D -m 644 %{SOURCE7} %{buildroot}%{_prefix}/lib/X11/displaymanagers/gdm
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_prefix}/lib/X11/displaymanagers/default-displaymanager
# Install other files
mkdir -p %{buildroot}/run/gdm
mkdir -p %{buildroot}%{_bindir}
ln -s ../sbin/gdm %{buildroot}%{_bindir}/gdm

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE9} %{buildroot}%{_tmpfilesdir}/gdm.conf
%if !0%{?is_opensuse}
sed -e '#/var/lib/gdm/\.pulse#d' -i %{buildroot}%{_tmpfilesdir}/gdm.conf
%endif

mkdir -p %{buildroot}%{_prefix}/lib/systemd/logind.conf.d
install -m 644 %{SOURCE10} %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/reserveVT.conf

mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE11} %{buildroot}%{_sysusersdir}/gdm.conf

%if 0%{?is_opensuse}
install -D -m 644 %{SOURCE20} %{buildroot}%{_prefix}/share/factory/var/lib/gdm/.pulse/default.pa
%endif

install -m 755 %{SOURCE21} %{buildroot}%{_libexecdir}/gdm/keytable

%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}/help

%check
%meson_test

%pre -f gdm.pre
if [ $1 -gt 1 ]; then
  if [ "$(systemctl is-enabled display-manager-legacy)" = "enabled" -a -x /usr/sbin/update-alternatives ]; then
    if [ "$(update-alternatives  --query default-displaymanager | awk '/Value:/ {print $2}')" = "/usr/lib/X11/displaymanagers/gdm" ]; then
        mkdir -p /run/gdm
        touch /run/gdm/migrate_to_gdm
    fi
  fi
fi

%post
%tmpfiles_create gdm.conf

%post xdm-integration
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/gdm 25

%posttrans
# Create dconf database for gdm, to lockdown the gdm session
dconf update

%postun xdm-integration
[ -f %{_prefix}/lib/X11/displaymanagers/gdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_prefix}/lib/X11/displaymanagers/gdm

%pre systemd
%service_add_pre gdm.service

%post systemd
%service_add_post gdm.service

%preun systemd
%service_del_preun gdm.service

%postun systemd
%dnl do not restart gdm.service, as we might lose the graphical session we're in
%service_del_postun_without_restart gdm.service

%posttrans systemd
%dnl migrate a system that still uses xdm abstraction as display manager to gdm
%dnl part of https://en.opensuse.org/openSUSE:DisplayManagerRework
if [ "$(systemctl is-enabled display-manager-legacy)" = "enabled" ]; then
  # display-manager is currently 'legacy mode' - if migration has already occured
  # the above command would return 'disabled'
  if [ -x /usr/sbin/update-alternatives ]; then
    if [ "$(update-alternatives  --query default-displaymanager | awk '/Value:/ {print $2}')" = "/usr/lib/X11/displaymanagers/gdm" ] || [ -f /run/gdm/migrate_to_gdm ]; then
      # the display-manager started by xdm is currently gdm - let's switch to the native service
      # this only force-enables gdm whenever xdm was enabled AND it was uses as wrapper to start gdm
      systemctl enable --force gdm.service
      unlink /run/gdm/migrate_to_gdm || :
    fi
  fi
fi

%ldconfig_scriptlets -n libgdm1

%files
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%dir %config %{_sysconfdir}/gdm
%config %{_sysconfdir}/gdm/[IPXl]*
%{_sbindir}/gdm
%{_bindir}/gdm
%{_bindir}/gdm-config
%dir %{_datadir}/dconf
%dir %{_datadir}/dconf/profile
%{_datadir}/dconf/profile/gdm
%if 0%{?is_opensuse}
%dir %{_datadir}/factory/var
%dir %{_datadir}/factory/var/lib
%{_datadir}/factory/var/lib/gdm
%endif
%{_datadir}/gdm/
%{_datadir}/gnome-session/sessions/gnome-login.session
%{_pam_moduledir}/pam_gdm.so
%dir %{_libexecdir}/gdm
%{_libexecdir}/gdm/gdm-*
%{_libexecdir}/gdm/gdmflexiserver
%ghost %attr(750,gdm,gdm) %dir %{_localstatedir}/lib/gdm
%if 0%{?is_opensuse}
%attr(0700, gdm, gdm) %ghost %dir %{_localstatedir}/lib/gdm/.pulse
%attr(0600, gdm, gdm) %ghost %{_localstatedir}/lib/gdm/.pulse/default.pa
%endif
%ghost %attr(711,root,gdm) %dir %{_localstatedir}/log/gdm
%ghost %attr(1755,root,root) /var/cache/gdm
%ghost %attr(711,root,gdm) %dir /run/gdm
%_config_norepl %{_pam_vendordir}/gdm
%_config_norepl %{_pam_vendordir}/gdm-autologin
%if %{enable_split_authentication}
%_config_norepl %{_pam_vendordir}/gdm-fingerprint
%_config_norepl %{_pam_vendordir}/gdm-smartcard
%endif
%_config_norepl %{_pam_vendordir}/gdm-password
%_config_norepl %{_pam_vendordir}/gdm-launch-environment
%{_datadir}/dbus-1/system.d/gdm.conf
%{_datadir}/polkit-1/rules.d/20-gdm.rules
%{_tmpfilesdir}/gdm.conf
%{_sysusersdir}/gdm.conf
%dir %{_prefix}/lib/systemd/logind.conf.d
%{_prefix}/lib/systemd/logind.conf.d/reserveVT.conf
%dir %{_userunitdir}/gnome-session@gnome-login.target.d
%{_userunitdir}/gnome-session@gnome-login.target.d/gnome-login.session.conf

%files xdm-integration
# /etc/xinit.d/xdm integration
%dir %{_prefix}/lib/X11/displaymanagers
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%{_prefix}/lib/X11/displaymanagers/gdm
%ghost %{_sysconfdir}/alternatives/default-displaymanager

%files -n libgdm1
%{_libdir}/libgdm.so.*

%files -n typelib-1_0-Gdm-1_0
%{_libdir}/girepository-1.0/Gdm-1.0.typelib

%files schema
%{_datadir}/glib-2.0/schemas/org.gnome.login-screen.gschema.xml

%files devel
%{_includedir}/gdm/
%{_libdir}/libgdm.so
%{_libdir}/pkgconfig/gdm.pc
%{_libdir}/pkgconfig/gdm-pam-extensions.pc
%{_datadir}/gir-1.0/Gdm-1.0.gir

%files branding-upstream
%config(noreplace) %{_sysconfdir}/gdm/custom.conf

%files systemd
%{_unitdir}/gdm.service
%{_libexecdir}/gdm/keytable

%files -n gdmflexiserver
%{_bindir}/gdmflexiserver

%files lang -f %{name}.lang

%changelog
