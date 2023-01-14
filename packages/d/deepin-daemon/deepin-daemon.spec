#
# spec file for package deepin-daemon
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


%define   _name       dde-daemon
%define   import_path github.com/linuxdeepin/dde-daemon

Name:           deepin-daemon
Version:        5.14.45
Release:        0
Summary:        Daemon handling the DDE session settings
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-daemon
Source0:        https://github.com/linuxdeepin/dde-daemon/archive/%{version}/%{_name}-%{version}.tar.gz
Source1:        %{name}.sysusers
Source2:        vendor.tar.gz
Source3:        %{name}-dbus-installer.in
Source4:        %{name}-polkit-installer.in
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM deepin-daemon-fix-policy-settings.patch
# hillwood@opensuse.org - Fix policy settings.
# Patch0:         %{name}-fix-policy-settings.patch
# PATCH-FIX-OPENSUSE deepin-daemon-libinput.patch.patch hillwood@opensuse.org - Fix build on libinput.
Patch1:         %{name}-libinput.patch
# PATCH-FIX-OPENSUSE disable-gobuild-in-makefile.patch hillwood@opensuse.org
# Use gobuild macro instead of makefile to build go binaries
Patch2:         disable-gobuild-in-makefile.patch
Patch3:         harden_deepin-accounts-daemon.service.patch
Group:          System/GUI/Other
BuildRequires:  deepin-gettext-tools
BuildRequires:  fontpackages-devel
BuildRequires:  golang-github-linuxdeepin-dde-api
BuildRequires:  golang-github-linuxdeepin-go-dbus-factory
BuildRequires:  golang-packaging
BuildRequires:  lightdm
BuildRequires:  lightdm-gtk-greeter
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xtst)
%if 0%{?sle_version} == 150200
BuildRequires:  golang-github-stretchr-testify
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
Requires:       acpid
Requires:       gvfs
Requires:       iw
Requires:       rfkill
Requires:       upower
Requires:       wallpaper-branding-openSUSE
Requires:       xdotool
Requires:       xvfb-run
%if %{suse_version} > 1500
Requires:       libgdk_pixbuf_xlib-2_0-0
%else
Requires:       libgdk_pixbuf-2_0-0
%endif
Recommends:     %{name}-lang = %{version}
Recommends:     iso-codes
Recommends:     mobile-broadband-provider-info
AutoReqProv:    Off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
Deepin Daemon is a daemon for handling the deepin session settings

%package polkit
Summary:        Deepin daemon polkit profiles
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description polkit
This package provides polkit profiles for deepin-daemon. These profiles are not
adopted by security team. If you need the polkit feature, you should install
them manually or use deepin-polkit-install package.

%package dbus
Summary:        Deepin daemon DBus profiles
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description dbus
This package provides dbus profiles for deepin-daemon. These profiles are not
adopted by security team. If you need the dbus feature, you should install
them manually or use deepin-dbus-install package.

%package -n golang-github-linuxdeepin-deepin-daemon
Summary:        Deepin daemon golang codes
Group:          Development/Languages/Golang
Requires:       golang-github-linuxdeepin-dde-api
Requires:       golang-github-linuxdeepin-go-dbus-factory
BuildArch:      noarch
AutoReq:        Off
%{go_provides}

%description -n golang-github-linuxdeepin-deepin-daemon
This package contains library source intended forbuilding other packages which
use import path with pkg.deepin.io/dde/daemon prefix.

%package lightdm
Summary:        Deepin Desktop branding setting for lightdm
Group:          System/X11/Displaymanagers
Requires:       %{name} = %{version}
Requires:       lightdm
AutoReqProv:    Off

%description lightdm
Deepin Desktop branding setting for lightdm

%package pam
Summary:        Deepin Keyring - PAM module
Group:          System/GUI/Other
Requires:       %{name} = %{version}
PreReq:         pam-config >= 0.72
PreReq:         sed
AutoReqProv:    Off

%description pam
Deepin Daemon is a daemon for handling the deepin session settings

The PAM module can be used to unlock the keyring on login.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
AutoReqProv:    Off

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup -p1 -a2 -n %{_name}-%{version}
%if 0%{?sle_version} == 150200
rm -rf vendor/github.com/stretchr/testify/
%endif
mkdir -p $HOME/rpmbuild/BUILD/go/src/
cp vendor/* $HOME/rpmbuild/BUILD/go/src/ -r
rm -rf vendor

sed -i '/systemd/s|lib|usr/lib|' Makefile
sed -i 's|lib/NetworkManager|lib|' network/utils_test.go

# Fix grub.cfg path and don't change openSUSE default grub2 theme
sed -i 's|boot/grub/deepin|boot/grub2/openSUSE|' grub2/*.go
sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|' accounts/user.go

sed -i 's|/lib/udev|/usr/lib/udev|g' Makefile
sed -i 's|/etc/modules-load.d|/usr/lib/modules-load.d|g' Makefile

sed -i 's|qdbus|qdbus-qt5|g' network/examples/set_wired_static_ip.sh misc/etc/acpi/powerbtn.sh

%build
export GO111MODULE=off
%goprep %{import_path}
%gobuild ...
%make_build

%install
rm -rf $HOME/rpmbuild/BUILD/go/src/github.com \
       $HOME/rpmbuild/BUILD/go/src/golang.org \
       $HOME/rpmbuild/BUILD/go/src/gopkg.in
%goinstall
%gosrc
%make_install
%gofilelist
pushd %{buildroot}%{_prefix}/lib/deepin-daemon
    ln -s ../../bin/* .
%if 0%{?suse_version} > 1500
    mv %{buildroot}%{_libexecdir}/dde-daemon/keybinding .
%else
    mv %{buildroot}%{_prefix}/libexec/dde-daemon/keybinding .
%endif
popd

install -Dm644 %{SOURCE1} %{buildroot}%{_prefix}/lib/sysusers.d/deepin-daemon.conf
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-dbus-installer
install -Dm755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}-polkit-installer

# fix systemd/logind config
install -d %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/
cat > %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/10-%{name}.conf <<EOF
[Login]
HandlePowerKey=ignore
HandleSuspendKey=ignore
EOF

install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdeepin-accounts-daemon
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rchwclock_stop

# File all polkit profiles, workaround boo#1070943
mkdir build
pushd build
mkdir polkit
mv %{buildroot}%{_datadir}/polkit-1/actions/* polkit/
tar -cvf polkit.tar.gz polkit
install -m 0644 polkit.tar.gz %{buildroot}%{_datadir}/dde-daemon/

# File all dbus service profiles, workaround boo#1070943
mkdir dbus
mkdir dbus/system-services
mkdir dbus/system.d
mv %{buildroot}%{_datadir}/dbus-1/system-services/* dbus/system-services
mv %{buildroot}%{_datadir}/dbus-1/system.d/* dbus/system.d
tar -cvf dbus.tar.gz dbus
install -m 0644 dbus.tar.gz %{buildroot}%{_datadir}/dde-daemon/
popd

%find_lang %{_name}

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/deepin-auth-keyboard %{buildroot}%{_pam_vendordir}
%endif

%pre
%service_add_pre deepin-accounts-daemon.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/deepin-auth-keyboard ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%post
%service_add_post deepin-accounts-daemon.service
if [ $1 -ge 1 ]; then
  %sysusers_create deepin-daemon.conf
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_prefix}/lib/%{name}/default-terminal 30
fi

%preun
%service_del_preun deepin-accounts-daemon.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator \
    %{_prefix}/lib/%{name}/default-terminal
fi

%postun
%service_del_postun deepin-accounts-daemon.service
if [ $1 -eq 0 ]; then
  rm -f /var/cache/deepin/mark-setup-network-services
  rm -f /var/log/deepin.log
  rm -f /usr/share/polkit-1/actions/com.deepin.daemon*
  rm -f /usr/share/dbus-1/system.d/com.deepin.daemon*
  rm -f /usr/share/dbus-1/system-services/com.deepin.daemon*
fi

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/deepin-auth-keyboard ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/*
%exclude %{_bindir}/%{name}-dbus-installer
%exclude %{_bindir}/%{name}-polkit-installer
%dir %{_sysconfdir}/default/grub.d
%config %{_sysconfdir}/default/grub.d/10_deepin.cfg
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/deepin-auth-keyboard
%else
%config %{_sysconfdir}/pam.d/deepin-auth-keyboard
%endif
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/conf.d
%config %{_sysconfdir}/NetworkManager/conf.d/deepin.dde.daemon.conf
# %{_prefix}/lib/modules-load.d/i2c_dev.conf
%dir %{_sysconfdir}/pulse/daemon.conf.d
%config %{_sysconfdir}/pulse/daemon.conf.d/10-deepin.conf
%{_prefix}/lib/%{name}/
%dir %{_sysusersdir}
%{_sysusersdir}/%{name}.conf
%dir %{_prefix}/lib/systemd/logind.conf.d
%dir %{_sysconfdir}/acpi
%dir %{_sysconfdir}/acpi/actions
%dir %{_sysconfdir}/acpi/events
%{_sysconfdir}/acpi/actions/deepin_lid.sh
%config %{_sysconfdir}/acpi/events/deepin_lid
%dir %{_sysconfdir}/deepin
%config %{_sysconfdir}/deepin/grub2_edit_auth.conf
%{_prefix}/lib/systemd/logind.conf.d/10-%{name}.conf
%{_prefix}/lib/udev/rules.d/80-deepin-fprintd.rules
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/%{_name}/
%exclude %{_datadir}/%{_name}/*.tar.gz
%{_datadir}/dde/
%{_datadir}/icons/hicolor/*/status/*
%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/configs
%dir %{_datadir}/dsg/configs/org.deepin.dde.daemon
%{_datadir}/dsg/configs/org.deepin.dde.daemon/org.deepin.dde.daemon.gesture.json
%{_unitdir}/deepin-accounts-daemon.service
%{_sbindir}/rcdeepin-accounts-daemon
%{_sbindir}/rchwclock_stop
%dir %{_var}/lib/polkit-1
%dir %{_var}/lib/polkit-1/localauthority
%dir %{_var}/lib/polkit-1/localauthority/10-vendor.d
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.*.pkla

%files lightdm
%dir %{_sysconfdir}/lightdm/deepin
%{_sysconfdir}/lightdm/deepin/xsettingsd.conf

%files -n golang-github-linuxdeepin-deepin-daemon -f file.lst
%defattr(-,root,root,-)

%files polkit
%defattr(-,root,root,-)
%{_bindir}/%{name}-polkit-installer
%{_datadir}/%{_name}/polkit.tar.gz

%files dbus
%defattr(-,root,root,-)
%{_bindir}/%{name}-dbus-installer
%{_datadir}/%{_name}/dbus.tar.gz

%files lang -f %{_name}.lang

%changelog
