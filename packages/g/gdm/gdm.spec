#
# spec file for package gdm
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


%define enable_split_authentication 1

# special hack for SLE15/Leap 15: it does not yet know /usr/etc, and files in /etc should be %%config
%if 0%{?suse_version} >= 1550
  %define _config_norepl %nil
%else
  %define _pam_vendordir %{_sysconfdir}/pam.d
  %define _config_norepl %config(noreplace)
%endif

Name:           gdm
Version:        43.0
Release:        0
Summary:        The GNOME Display Manager
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GDM

Source0:        https://download.gnome.org/sources/gdm/43/%{name}-%{version}.tar.xz
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
# WARNING: do not remove/significantly change patch0 without updating the relevant patch in accountsservice too
# PATCH-FIX-OPENSUSE  gdm-sysconfig-settings.patch bnc432360 bsc#919723 hpj@novell.com -- Read autologin options from /etc/sysconfig/displaymanager; note that accountsservice has a similar patch (accountsservice-sysconfig.patch)
Patch0:         gdm-sysconfig-settings.patch
# PATCH-FIX-OPENSUSE gdm-suse-xsession.patch vuntz@novell.com -- Use the /etc/X11/xdm/* scripts
Patch2:         gdm-suse-xsession.patch
# PATCH-FIX-OPENSUSE gdm-default-wm.patch vuntz@novell.com -- Use sysconfig to know to which desktop to use by default
Patch3:         gdm-default-wm.patch
# PATCH-FIX-OPENSUSE gdm-xauthlocalhostname.patch bnc#538064 vuntz@novell.com -- Set XAUTHLOCALHOSTNAME to current hostname when we authenticate, for local logins, to avoid issues in the session in case the hostname changes later one. See comment 24 in the bug.
Patch4:         gdm-xauthlocalhostname.patch
# PATCH-FIX-OPENSUSE gdm-switch-to-tty1.patch bsc#1113700 xwang@suse.com -- switch to tty1 when stopping gdm service
Patch6:         gdm-switch-to-tty1.patch
# PATCH-FIX-OPENSUSE gdm-initial-setup-hardening.patch boo#1140851, glgo#GNOME/gnome-initial-setup#76 fezhang@suse.com -- Prevent gnome-initial-setup running if any regular user has perviously logged into the system
Patch9:         gdm-initial-setup-hardening.patch
# PATCH-FIX-OPENSUSE gdm-s390-not-require-g-s-d_wacom.patch bsc#1129412 yfjiang@suse.com -- Remove the runtime requirement of g-s-d Wacom plugin
Patch13:        gdm-s390-not-require-g-s-d_wacom.patch
# PATCH-FIX-UPSTREAM gdm-switch-user-tty7.patch bsc#1155408 glgo#GNOME#gdm#532 xwang@suse.com -- Switch to tty7 when switch user
Patch14:        gdm-switch-user-tty7.patch
# PATCH-FIX-UPSTREAM gdm-disable-wayland-on-mgag200-chipsets.patch bsc#1162888 glgo#GNOME/mutter#57 qkzhu@suse.com -- Disable Wayland on mgag200 chipsets
Patch15:        gdm-disable-wayland-on-mgag200-chipsets.patch

### NOTE: Keep please SLE-only patches at bottom (starting on 1000).
# PATCH-FIX-SLE gdm-disable-gnome-initial-setup.patch bnc#1067976 qzhao@suse.com -- Disable gnome-initial-setup runs before gdm, g-i-s will only serve for CJK people to choose the input-method after login.
Patch1000:      gdm-disable-gnome-initial-setup.patch
# PATCH-FIX-SLE gdm-add-runtime-option-to-disable-starting-X-server-as-u.patch bnc#1188912 jsc#SLE-17880 xwang@suse.com -- Add runtime option to start X under root instead of regular user.
Patch1001:      gdm-add-runtime-option-to-disable-starting-X-server-as-u.patch
# PATCH-FIX-SLE gdm-restart-session-when-X-server-restart.patch bsc#1196974 xwang@suse.com -- Fix blank screen when X restarts with GDM_DISABLE_USER_DISPLAY_SERVER=1.
Patch1002:      gdm-restart-session-when-X-server-restart.patch
BuildRequires:  check-devel
# dconf and gnome-session-core are needed for directory ownership
BuildRequires:  dconf
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gnome-session-core
BuildRequires:  meson >= 0.50.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  tcpd-devel
BuildRequires:  update-desktop-files
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
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.4
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
Requires:       gdmflexiserver
Requires:       gnome-session-core
Requires:       gnome-settings-daemon
Requires:       gnome-shell
# xdm package ships systemd display-manager service and other common scripts
# between display managers (bsc#1084655)
Requires:       xdm
Requires(post): dconf
Requires(pre):  group(video)
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     iso-codes
# accessibility
Recommends:     orca
Provides:       gdm2 = %{version}
Obsoletes:      gdm2 < %{version}
Provides:       gnome-applets-gdm = %{version}
Obsoletes:      gnome-applets-gdm < %{version}
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

%package systemd
Summary:        Systemd gdm.service file
Group:          System/GUI/GNOME
Requires:       gdm
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
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch9 -p1
%ifarch s390 s390x
%patch13 -p1
%endif
%patch14 -p1
%patch15 -p1

# SLE and Leap only patches start at 1000
%if 0%{?sle_version}
%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
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
        -Dplymouth=enabled \
        -Drun-dir=/run/gdm \
%if %{enable_split_authentication}
        -Dsplit-authentication=true \
%else
        -Dsplit-authentication=false \
%endif
        -Dudev-dir=%{_udevrulesdir} \
        -Dwayland-support=true \
        %nil
%meson_build
%sysusers_generate_pre %{SOURCE11} gdm gdm.conf

%install
%meson_install
## Install PAM files.
mkdir -p %{buildroot}%{_pam_vendordir}
# Generic pam config
cp %{SOURCE1} %{buildroot}%{_pam_vendordir}/gdm
# Pam config for autologin
cp %{SOURCE2} %{buildroot}%{_pam_vendordir}/gdm-autologin
# Pam config for the greeter session
cp %{SOURCE3} %{buildroot}%{_pam_vendordir}/gdm-launch-environment
%if %{enable_split_authentication}
# Pam config for fingerprint authentication
cp %{SOURCE4} %{buildroot}%{_pam_vendordir}/gdm-fingerprint
# Pam config for smartcard authentication
cp %{SOURCE5} %{buildroot}%{_pam_vendordir}/gdm-smartcard
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

mkdir -p %{buildroot}%{_prefix}/lib/systemd/logind.conf.d
install -m 644 %{SOURCE10} %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/reserveVT.conf

mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE11} %{buildroot}%{_sysusersdir}/gdm.conf

%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}/help

%check
%meson_test

# FIXME -- Document why we don't use %%service_add_*/%%service_del_* macros.

%pre -f gdm.pre

%post
%tmpfiles_create gdm.conf
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/gdm 25

%posttrans
# Create dconf database for gdm, to lockdown the gdm session
dconf update

%postun
[ -f %{_prefix}/lib/X11/displaymanagers/gdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_prefix}/lib/X11/displaymanagers/gdm

%post -n libgdm1 -p /sbin/ldconfig
%postun -n libgdm1 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%dir %config %{_sysconfdir}/gdm
%config %{_sysconfdir}/gdm/[IPXl]*
%{_sbindir}/gdm
%{_bindir}/gdm
%{_bindir}/gdm-screenshot
%dir %{_datadir}/dconf
%dir %{_datadir}/dconf/profile
%{_datadir}/dconf/profile/gdm
%{_datadir}/gdm/
%{_datadir}/gnome-session/sessions/gnome-login.session
%{_pam_moduledir}/pam_gdm.so
%dir %{_libexecdir}/gdm
%{_libexecdir}/gdm/gdm-*
%{_libexecdir}/gdm/gdmflexiserver
%ghost %attr(750,gdm,gdm) %dir %{_localstatedir}/lib/gdm
%ghost %attr(711,root,gdm) %dir %{_localstatedir}/log/gdm
%ghost %dir %{_localstatedir}/cache/gdm
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
# /etc/xinit.d/xdm integration
%dir %{_prefix}/lib/X11/displaymanagers
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%{_prefix}/lib/X11/displaymanagers/gdm
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%{_udevrulesdir}/61-gdm.rules
%{_tmpfilesdir}/gdm.conf
%{_sysusersdir}/gdm.conf
%dir %{_prefix}/lib/systemd/logind.conf.d
%{_prefix}/lib/systemd/logind.conf.d/reserveVT.conf
%dir %{_userunitdir}/gnome-session@gnome-login.target.d
%{_userunitdir}/gnome-session@gnome-login.target.d/session.conf

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

%files -n gdmflexiserver
%{_bindir}/gdmflexiserver

%files lang -f %{name}.lang

%changelog
