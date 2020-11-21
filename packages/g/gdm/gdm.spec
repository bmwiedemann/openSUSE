#
# spec file for package gdm
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


%define systemdsystemunitdir %(pkg-config --variable=systemdsystemunitdir systemd)
# FIXME: need to check what should be done to enable this (at least adapt the pam files). See bnc#699999
%define enable_split_authentication 0

Name:           gdm
Version:        3.36.3
Release:        0
Summary:        The GNOME Display Manager
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GDM

Source0:        %{name}-%{version}.tar.xz
Source1:        gdm.pamd
Source2:        gdm-autologin.pamd
Source3:        gdm-launch-environment.pamd
Source4:        gdm-fingerprint.pamd
Source5:        gdm-smartcard.pamd
# gdmflexiserver wrapper, to enable other display managers to abuse the gdmflexiserver namespace (like lightdm)
Source6:        gdmflexiserver-wrapper
# /etc/xinit.d/xdm integration script
Source7:        X11-displaymanager-gdm
# GDM does not boostrap using gnome-autogen.sh, but has it's own bootstrap script
Source8:        autogen.sh
# Use tmpfiles to create directories under /var to support transactional updates
Source9:        gdm.tmpfiles
# Use reserveVT.conf to make autologin user session not to select tty1
Source10:       reserveVT.conf
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
# PATCH-NEEDS-REBASE gdm-add-runtime-option-to-disable-starting-X-server-as-u.patch bnc#1075805 bgo#793255 msrb@suse.com -- Add runtime option to start X under root instead of regular user. Necessary if no DRI drivers are present. rejected upstream WAS: PATCH-FIX-OPENSUSE
Patch8:         gdm-add-runtime-option-to-disable-starting-X-server-as-u.patch
# PATCH-FIX-OPENSUSE gdm-initial-setup-hardening.patch boo#1140851, glgo#GNOME/gnome-initial-setup#76 fezhang@suse.com -- Prevent gnome-initial-setup running if any regular user has perviously logged into the system
Patch9:         gdm-initial-setup-hardening.patch
# PATCH-FIX-OPENSUSE gdm-s390-not-require-g-s-d_wacom.patch bsc#1129412 yfjiang@suse.com -- Remove the runtime requirement of g-s-d Wacom plugin
Patch13:        gdm-s390-not-require-g-s-d_wacom.patch
# PATCH-FIX-UPSTREAM gdm-switch-user-tty7.patch bsc#1155408 glgo#GNOME#gdm#532 xwang@suse.com -- Switch to tty7 when switch user
Patch14:        gdm-switch-user-tty7.patch
# PATCH-FIX-UPSTREAM gdm-disable-wayland-on-mgag200-chipsets.patch bsc#1162888 glgo#GNOME/mutter#57 qkzhu@suse.com -- Disable Wayland on mgag200 chipsets
Patch15:        gdm-disable-wayland-on-mgag200-chipsets.patch
# PATCH-FIX-OPENSUSE gdm-UsrEtc.patch boo#1173049 boo#1173052 boo#1173053 -- needed changes for xdm/xinit/xmodmap move to /usr/etc/X11 
Patch16:        gdm-UsrEtc.patch

### NOTE: Keep please SLE-only patches at bottom (starting on 1000).
# PATCH-FIX-SLE gdm-disable-gnome-initial-setup.patch bnc#1067976 qzhao@suse.com -- Disable gnome-initial-setup runs before gdm, g-i-s will only serve for CJK people to choose the input-method after login.
Patch1000:      gdm-disable-gnome-initial-setup.patch
BuildRequires:  check-devel
# dconf and gnome-session-core are needed for directory ownership
BuildRequires:  dconf
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gnome-session-core
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
BuildRequires:  tcpd-devel
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-server
BuildRequires:  xorg-x11-server-extra
BuildRequires:  pkgconfig(accountsservice) >= 0.6.35
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gio-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.12
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.91.1
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
# FIXME: use proper Requires(pre/post/preun/...)
# For groupadd, useradd, usermod
PreReq:         pwdutils
Requires(post): dconf
Requires(pre):  group(video)
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

%description
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

%package -n libgdm1
Summary:        Client Library for Communicating with GDM Greeter Server
Group:          System/Libraries
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
Supplements:    packageand(%{name}:branding-upstream)
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
Summary:        systemd gdm.service file
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
cp %{SOURCE8} .
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
#patch8 -p1
%patch9 -p1
%ifarch s390 s390x
%patch13 -p1
%endif
%patch14 -p1
%patch15 -p1
%patch16 -p1

# SLE and Leap only patches start at 1000
%if 0%{?sle_version}
%patch1000 -p1
%endif

%build
NOCONFIGURE=1 ./autogen.sh
%configure\
        --disable-static \
        --libexecdir=%{_libexecdir}/gdm \
        --localstatedir=%{_localstatedir} \
        --with-at-spi-registryd-directory=%{_libexecdir}/at-spi \
        --with-check-accelerated-directory=%{_libexecdir} \
        --with-gnome-settings-daemon-directory=%{_libexecdir}/gnome-settings-daemon-3.0 \
        --with-pam-mod-dir=/%{_lib}/security \
        --enable-ipv6 \
        --enable-gdm-xsession \
        --with-plymouth \
        --enable-wayland-support \
        --enable-systemd-journal \
%if %{enable_split_authentication}
        --enable-split-authentication \
%else
        --disable-split-authentication \
%endif
        --with-initial-vt=7 \
        --with-run-dir=/run/gdm \
        --with-udevdir=%{_prefix}/lib/udev
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
## Install PAM files.
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
# Generic pam config
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/gdm
# Pam config for autologin
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/gdm-autologin
# Pam config for the greeter session
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/gdm-launch-environment
%if %{enable_split_authentication}
# Pam config for fingerprint authentication
cp %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/gdm-fingerprint
# Pam config for smartcard authentication
cp %{SOURCE5} %{buildroot}%{_sysconfdir}/pam.d/gdm-smartcard
%endif
# The default gdm pam configuration is the one to be used as pam-password too
%if %{enable_split_authentication}
rm %{buildroot}%{_sysconfdir}/pam.d/gdm-password
echo "We are not ready for this, we need to know what to put in gdm-fingerprint and gdm-smartcard pam config files."
false
%endif
ln -s gdm %{buildroot}%{_sysconfdir}/pam.d/gdm-password
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

mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 %{SOURCE9} %{buildroot}%{_prefix}/lib/tmpfiles.d/gdm.conf

mkdir -p %{buildroot}%{_prefix}/lib/systemd/logind.conf.d
install -m 644 %{SOURCE10} %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/reserveVT.conf

%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}/help

%check
%make_build check

%pre
%{_sbindir}/groupadd -r gdm 2> /dev/null || :
%{_sbindir}/useradd -r -g gdm -G video -s /bin/false \
-c "Gnome Display Manager daemon" -d %{_localstatedir}/lib/gdm gdm 2> /dev/null || :
%{_sbindir}/usermod -g gdm -G video -s /bin/false gdm 2> /dev/null

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
%{_datadir}/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
/%{_lib}/security/pam_gdm.so
%dir %{_libexecdir}/gdm
%{_libexecdir}/gdm/gdm-*
%{_libexecdir}/gdm/gdmflexiserver
%ghost %attr(750,gdm,gdm) %dir %{_localstatedir}/lib/gdm
%ghost %attr(711,root,gdm) %dir %{_localstatedir}/log/gdm
%ghost %dir %{_localstatedir}/cache/gdm
%ghost %attr(711,root,gdm) %dir /run/gdm
%config %{_sysconfdir}/pam.d/gdm
%config %{_sysconfdir}/pam.d/gdm-autologin
%if %{enable_split_authentication}
%config %{_sysconfdir}/pam.d/gdm-fingerprint
%config %{_sysconfdir}/pam.d/gdm-smartcard
%endif
%config %{_sysconfdir}/pam.d/gdm-password
%config %{_sysconfdir}/pam.d/gdm-launch-environment
%config %{_sysconfdir}/dbus-1/system.d/gdm.conf
# /etc/xinit.d/xdm integration
%dir %{_prefix}/lib/X11/displaymanagers
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%{_prefix}/lib/X11/displaymanagers/gdm
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%{_udevrulesdir}/61-gdm.rules
%{_prefix}/lib/tmpfiles.d/gdm.conf
%dir %{_prefix}/lib/systemd/logind.conf.d
%{_prefix}/lib/systemd/logind.conf.d/reserveVT.conf

%files -n libgdm1
%{_libdir}/libgdm.so.*

%files -n typelib-1_0-Gdm-1_0
%{_libdir}/girepository-1.0/Gdm-1.0.typelib

%files devel
%{_includedir}/gdm/
%{_libdir}/libgdm.so
%{_libdir}/pkgconfig/gdm.pc
%{_libdir}/pkgconfig/gdm-pam-extensions.pc
%{_datadir}/gir-1.0/Gdm-1.0.gir

%files branding-upstream
%config(noreplace) %{_sysconfdir}/gdm/custom.conf

%files systemd
%{systemdsystemunitdir}/gdm.service

%files -n gdmflexiserver
%{_bindir}/gdmflexiserver

%files lang -f %{name}.lang

%changelog
