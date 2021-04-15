#
# spec file for package deepin-api
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%define   provider        github
%define   provider_tld    com
%define   project         linuxdeepin
%define   repo            dde-api
%define   import_path     pkg.deepin.io/dde/api

Name:           deepin-api
Version:        5.4.2
Release:        0
Summary:        Go-lang bingding for dde-daemon
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dde-api
Source0:        https://github.com/linuxdeepin/dde-api/archive/%{version}/%{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}-dbus-installer.in
Source3:        %{name}-polkit-installer.in
Source99:       deepin-api-rpmlintrc
# PATCH-FIX-OPENSUSE default-grub2-theme.patch hillwood@opensuse.org - Set openSUSE grub theme as default
Patch0:         default-grub2-theme.patch
# PATCH-FIX-OPENSUSE disable-gosrc-install-in-makefile.patch hillwood@opensuse.org
# Use goinstall macro instead of makefile
Patch1:         disable-gosrc-install-in-makefile.patch
Group:          System/GUI/Other
BuildRequires:  fdupes
BuildRequires:  deepin-gettext-tools
# BuildRequires:  golang(API) = 1.11
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  update-desktop-files
BuildRequires:  deepin-sound-theme
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  golang(github.com/linuxdeepin/go-x11-client)
BuildRequires:  golang(github.com/linuxdeepin/go-dbus-factory/com.deepin.wm)
BuildRequires:  golang-github-linuxdeepin-go-x11-client
BuildRequires:  deepin-gir-generator
Requires:       deepin-desktop-base
Requires:       rfkill
AutoReqProv:    Off
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
The deepin-api is DDE API provides some dbus interfaces that is used for screen
zone detecting, thumbnail generating, sound playing, etc.

%package polkit
Summary:        Deepin API polkit profiles
License:        GPL-3.0+ and WTFPL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description polkit
This package provides polkit profiles for deepin-api. These profiles are not
adopted by security team. If you need the polkit feature, you should install
them manually or use deepin-polkit-install package.

%package dbus
Summary:        Deepin API DBus profiles
License:        GPL-3.0+ and WTFPL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description dbus
This package provides dbus profiles for deepin-api. These profiles are not
adopted by security team. If you need the dbus feature, you should install
them manually or use deepin-dbus-install package.

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        DDE API golang codes
Group:          Development/Languages/Golang
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(cairo-ft)
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(gdk-pixbuf-xlib-2.0)
Requires:       pkgconfig(gudev-1.0)
Requires:       pkgconfig(libcanberra)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(poppler-glib)
Requires:       pkgconfig(polkit-qt5-1)
Requires:       pkgconfig(systemd)
Requires:       pkgconfig(xfixes)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(libpulse-simple)
Requires:       pkgconfig(alsa)
Requires:       golang(pkg.deepin.io/lib)
Requires:       golang(github.com/linuxdeepin/go-x11-client)
Requires:       golang(github.com/linuxdeepin/go-dbus-factory/com.deepin.wm)
Requires:       golang-github-linuxdeepin-go-x11-client
Requires:       go-gir-generator
BuildArch:      noarch
AutoReqProv:    On
AutoReq:        Off
%{go_provides}

%description -n golang-%{provider}-%{project}-%{repo}
The deepin-api is DDE API provides some dbus interfaces that is used for screen
zone detecting, thumbnail generating, sound playing, etc.

This package contains library source intended forbuilding other packages which
use import path with pkg.deepin.io/dde/api prefix.

%prep
%autosetup -p1 -a1 -n %{repo}-%{version}
mkdir -p $HOME/rpmbuild/BUILD/go/src/
cp vendor/* $HOME/rpmbuild/BUILD/go/src/ -r
rm -rf vendor

%build
%goprep %{import_path}
%gobuild ...
%make_build

%install
rm -rf $HOME/rpmbuild/BUILD/go/src/github.com \
       $HOME/rpmbuild/BUILD/go/src/golang.org \
       $HOME/rpmbuild/BUILD/go/src/gopkg.in
%goinstall
%gosrc
install -m0644 themes/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/themes/
install -m0644 gtk-thumbnailer/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/gtk-thumbnailer/
install -m0644 dxinput/utils/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/dxinput/utils/
install -m0644 thumbnails/icon/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/thumbnails/icon/
install -m0644 thumbnails/text/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/thumbnails/text/
install -m0644 thumbnails/images/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/thumbnails/images/
install -m0644 thumbnails/font/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/thumbnails/font/
install -m0644 thumbnails/pdf/*.c %{buildroot}%{go_contribsrcdir}/%{import_path}/thumbnails/pdf/
%gofilelist

mkdir -p out/bin/
mv %{buildroot}%{_bindir}/* out/bin/
%make_install SYSTEMD_SERVICE_DIR=%{_unitdir}
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-dbus-installer
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-polkit-installer

install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdeepin-shutdown-sound
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdeepin-login-sound

install -d %{buildroot}%{_datadir}/dde-api/
# File all polkit profiles, workaround boo#1070943
mkdir polkit
mv %{buildroot}%{_datadir}/polkit-1/actions/* polkit/
tar -cvf polkit.tar.gz polkit
install -m 0644 polkit.tar.gz %{buildroot}%{_datadir}/dde-api/

# File all dbus service profiles, workaround boo#1070943
mkdir dbus
mkdir dbus/system-services
mkdir dbus/system.d
mv %{buildroot}%{_datadir}/dbus-1/system-services/* dbus/system-services
mv %{buildroot}%{_datadir}/dbus-1/system.d/* dbus/system.d
tar -cvf dbus.tar.gz dbus
install -m 0644 dbus.tar.gz %{buildroot}%{_datadir}/dde-api/

%fdupes %{buildroot}

%pre
%service_add_pre deepin-shutdown-sound.service deepin-login-sound.service

%post
%service_add_post deepin-shutdown-sound.service deepin-login-sound.service

%preun
%service_del_preun deepin-shutdown-sound.service deepin-login-sound.service

%postun
%service_del_postun deepin-shutdown-sound.service deepin-login-sound.service
if [ $1 -eq 0 ]; then
  rm -f /usr/share/polkit-1/actions/com.deepin.api*
  rm -f /usr/share/dbus-1/system.d/com.deepin.api*
  rm -f /usr/share/dbus-1/system-services/com.deepin.api*
fi

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/*
%exclude %{_bindir}/deepin-api-polkit-installer
%exclude %{_bindir}/deepin-api-dbus-installer
%{_sbindir}/rcdeepin-shutdown-sound
%{_sbindir}/rcdeepin-login-sound
%{_unitdir}/*.service
%{_datadir}/dde-api
%exclude %{_datadir}/dde-api/*.tar.gz
%{_datadir}/dbus-1/services/*.service
# %{_datadir}/dbus-1/system-services/*.service
# %dir %{_datadir}/dbus-1/system.d/
# %{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/actions/*
# %{_datadir}/polkit-1/actions/*.policy
%{_prefix}/lib/deepin-api
%dir /var/lib/polkit-1
%dir /var/lib/polkit-1/localauthority
%dir /var/lib/polkit-1/localauthority/10-vendor.d
/var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.api.device.pkla

%files polkit
%defattr(-,root,root,-)
%{_bindir}/deepin-api-polkit-installer
%{_datadir}/dde-api/polkit.tar.gz

%files dbus
%defattr(-,root,root,-)
%{_bindir}/deepin-api-dbus-installer
%{_datadir}/dde-api/dbus.tar.gz

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%defattr(-,root,root,-)

%changelog
