#
# spec file for package deepin-start
#
# Copyright (c) 2021 SUSE LLC
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


%define _name       startdde
%define import_path pkg.deepin.io/dde/startdde

Name:           deepin-start
Version:        5.8.7
Release:        0
Summary:        Starter of deepin desktop
License:        GPL-3.0-only
URL:            https://github.com/linuxdeepin/startdde
Source0:        https://github.com/linuxdeepin/startdde/archive/%{version}/%{_name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       deepin-start-rpmlintrc
# PATCH-FIX-OPENSUSE deepin-start-disable-gobuild-in-makefile.patch hillwood@opensuse.org
# Use gobuild macro instead of makefile to build go binaries
Patch0:         deepin-start-disable-gobuild-in-makefile.patch
Group:          System/Daemons
BuildRequires:  fdupes
%if 0%{?suse_version} > 1500
BuildRequires:  golang(API) = 1.15
%endif
BuildRequires:  golang-github-linuxdeepin-dde-api
BuildRequires:  golang-github-linuxdeepin-go-dbus-factory
BuildRequires:  golang-packaging
BuildRequires:  jq
BuildRequires:  xdg-user-dirs
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
Requires:       deepin-daemon
# Requires:       libcgroup-tools
Provides:       startdde
AutoReqProv:    Off

%description
deepin-start is used for launching DDE components and invoking user's
custom applications which compliant with xdg autostart specification.

%package -n golang-github-linuxdeepin-startdde
Summary:        Startdde golang codes
Group:          Development/Languages/Golang
BuildArch:      noarch
Requires:       golang-github-linuxdeepin-dde-api
Requires:       golang-github-linuxdeepin-go-dbus-factory
AutoReq:        Off
%{go_provides}

%description -n golang-github-linuxdeepin-startdde
This package contains library source intended forbuilding other packages which
use import path with pkg.deepin.io/dde/startdde prefix.

%prep
%autosetup -p1 -a1 -n %{_name}-%{version}
mkdir -p $HOME/rpmbuild/BUILD/go/src/
cp vendor/* $HOME/rpmbuild/BUILD/go/src/ -r
rm -rf vendor

# Fix systemd path
sed -i 's|/lib/systemd|/usr/lib/systemd|g' Makefile

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
%make_install
install -m0644 display/listen.c %{buildroot}%{go_contribsrcdir}/%{import_path}/display/
install -m0644 iowait/xcursor_remap.c %{buildroot}%{go_contribsrcdir}/%{import_path}/iowait/
%gofilelist

install -d %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/fix-xauthority-perm %{buildroot}%{_sbindir}/deepin-fix-xauthority-perm
install -d %{buildroot}%{_prefix}/lib/deepin-daemon/
mv %{buildroot}%{_bindir}/greeter-display-daemon %{buildroot}%{_prefix}/lib/deepin-daemon/greeter-display-daemon
rm -rf %{buildroot}%{_datadir}/lightdm/

%fdupes %{buildroot}%{_datadir}

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/startdde
%{_bindir}/wl_display_daemon
%{_sbindir}/deepin-fix-xauthority-perm
%{_datadir}/xsessions/deepin.desktop
%dir %{_datadir}/startdde
%{_datadir}/startdde/auto_launch.json
%{_datadir}/startdde/memchecker.json
%{_datadir}/startdde/*.conf
%{_datadir}/glib-2.0/schemas/com.deepin.*.xml
%dir %{_prefix}/lib/deepin-daemon
%{_prefix}/lib/deepin-daemon/greeter-display-daemon
%config %{_sysconfdir}/profile.d/deepin-xdg-dir.sh
%config %{_sysconfdir}/X11/xinit/xinitrc.d/01deepin-profile
%config %{_sysconfdir}/X11/xinit/xinitrc.d/00deepin-dde-env

%files -n golang-github-linuxdeepin-startdde -f file.lst

%changelog
