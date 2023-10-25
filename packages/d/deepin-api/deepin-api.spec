#
# spec file for package deepin-api
#
# Copyright (c) 2023 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define   provider        github
%define   provider_tld    com
%define   project         linuxdeepin
%define   repo            dde-api
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     %{provider_prefix}

Name:           deepin-api
Version:        5.5.25
Release:        0
Summary:        Go-lang bingding for dde-daemon
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-api
Source0:        https://github.com/linuxdeepin/dde-api/archive/%{version}/%{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       deepin-api-rpmlintrc
# PATCH-FIX-OPENSUSE default-grub2-theme.patch hillwood@opensuse.org - Set openSUSE grub theme as default
Patch0:         default-grub2-theme.patch
# PATCH-FIX-OPENSUSE disable-gosrc-install-in-makefile.patch hillwood@opensuse.org
# Use goinstall macro instead of makefile
Patch1:         disable-gosrc-install-in-makefile.patch
Patch2:         harden_deepin-login-sound.service.patch
Patch3:         harden_deepin-shutdown-sound.service.patch
Group:          System/GUI/Other
BuildRequires:  deepin-gettext-tools
BuildRequires:  deepin-gir-generator
BuildRequires:  deepin-sound-theme
BuildRequires:  fdupes
BuildRequires:  golang-github-linuxdeepin-go-dbus-factory >= 1.9.17
BuildRequires:  golang-github-linuxdeepin-go-gir-generator
BuildRequires:  golang-github-linuxdeepin-go-lib
BuildRequires:  golang-github-linuxdeepin-go-x11-client
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
Requires:       deepin-desktop-base
Requires:       rfkill
Requires(pre):  group(audio)
AutoReqProv:    Off
%{?systemd_ordering}

%description
The deepin-api is DDE API provides some dbus interfaces that is used for screen
zone detecting, thumbnail generating, sound playing, etc.

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        DDE API golang codes
Group:          Development/Languages/Golang
Requires:       deepin-gir-generator
Requires:       golang-github-linuxdeepin-go-dbus-factory >= 1.9.17
Requires:       golang-github-linuxdeepin-go-lib
Requires:       golang-github-linuxdeepin-go-x11-client
Requires:       pkgconfig(alsa)
Requires:       pkgconfig(cairo-ft)
Requires:       pkgconfig(gdk-pixbuf-xlib-2.0)
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(gudev-1.0)
Requires:       pkgconfig(libcanberra)
Requires:       pkgconfig(libpulse-simple)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(polkit-qt5-1)
Requires:       pkgconfig(poppler-glib)
Requires:       pkgconfig(systemd)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xfixes)
Requires:       pkgconfig(xi)
BuildArch:      noarch
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
export GO111MODULE=off
%goprep %{import_path}
%gobuild ...
%make_build

%install
mv $HOME/rpmbuild/BUILD/go/src/github.com/linuxdeepin .
rm -rf $HOME/rpmbuild/BUILD/go/src/github.com/*\
       $HOME/rpmbuild/BUILD/go/src/golang.org \
       $HOME/rpmbuild/BUILD/go/src/gopkg.in
mv linuxdeepin $HOME/rpmbuild/BUILD/go/src/github.com/
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

install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdeepin-shutdown-sound
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcdeepin-login-sound

# It requests an invali command in openSUSE, please use Yast2 to change locale
rm %{buildroot}%{_datadir}/polkit-1/actions/com.deepin.api.locale-helper.policy

%fdupes %{buildroot}

%pre
getent group deepin-sound-player >/dev/null || %{_sbindir}/groupadd --system deepin-sound-player
getent passwd deepin-sound-player >/dev/null || %{_sbindir}/useradd --system -c "deepin-sound-player User" \
         -d %{_localstatedir}/deepin-sound-player -m -g deepin-sound-player -s %{_sbindir}/nologin \
         -G audio deepin-sound-player
%service_add_pre deepin-shutdown-sound.service deepin-login-sound.service

%post
%service_add_post deepin-shutdown-sound.service deepin-login-sound.service

%preun
%service_del_preun deepin-shutdown-sound.service deepin-login-sound.service

%postun
%service_del_postun deepin-shutdown-sound.service deepin-login-sound.service

%files
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
%{_datadir}/dbus-1/system-services/*.service
%dir %{_datadir}/dbus-1/system.d/
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/actions/*
%{_datadir}/polkit-1/actions/*.policy
%{_prefix}/lib/deepin-api
%dir /var/lib/polkit-1
%dir /var/lib/polkit-1/localauthority
%dir /var/lib/polkit-1/localauthority/10-vendor.d
/var/lib/polkit-1/localauthority/10-vendor.d/com.deepin.api.device.pkla

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst

%changelog
