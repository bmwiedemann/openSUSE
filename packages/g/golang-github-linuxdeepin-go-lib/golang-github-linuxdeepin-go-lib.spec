#
# spec file for package golang-github-linuxdeepin-go-lib
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


%define   _name           go-lib
%define   import_path     pkg.deepin.io/lib

Name:           golang-github-linuxdeepin-go-lib
Version:        5.7.0
Release:        0
Summary:        Go bindings for Deepin Desktop Environment development
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/go-lib
Source0:        https://github.com/linuxdeepin/go-lib/archive/%{version}/%{_name}-%{version}.tar.gz
# The development package of golang is named *-source, please skip this rpmlint elibX11-1rror.
Source1:        golang-github-linuxdeepin-go-lib-rpmlintrc
Group:          Development/Languages/Golang
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  libpulse0
BuildRequires:  mobile-broadband-provider-info
BuildRequires:  golang(pkg.deepin.io/gir/gio-2.0)
BuildRequires:  golang(pkg.deepin.io/gir/glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} > 1500
BuildRequires:  golang(API) = 1.15
%endif
BuildArch:      noarch
Requires:       golang(pkg.deepin.io/gir/gio-2.0)
Requires:       golang(pkg.deepin.io/gir/glib-2.0)
AutoReq:        Off
%{go_provides}

%description
DLib is a set of Go bindings/libraries for DDE development.
Containing dbus (forking from guelfey), glib, gdkpixbuf, pulse and more.

%prep
%setup -q -n %{_name}-%{version}

%build
%goprep %{import_path}

%install
%goinstall
%gosrc
install -m 0644 %{_builddir}/go/src/%{import_path}/gdkpixbuf/blur.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/gdkpixbuf/
install -m 0644 %{_builddir}/go/src/%{import_path}/gdkpixbuf/gaussianiir2d.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/gdkpixbuf/
install -m 0644 %{_builddir}/go/src/%{import_path}/gdkpixbuf/gdk_pixbuf_utils.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/gdkpixbuf/
install -m 0644 %{_builddir}/go/src/%{import_path}/pulse/dde-pulse.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/pulse/
install -m 0644 %{_builddir}/go/src/%{import_path}/pulse/meter.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/pulse/
install -m 0644 %{_builddir}/go/src/%{import_path}/sound/player.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/sound/
install -m 0644 %{_builddir}/go/src/%{import_path}/stb_vorbis/stb_vorbis.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/stb_vorbis/
install -m 0644 %{_builddir}/go/src/%{import_path}/pam/transaction.c \
                %{buildroot}%{go_contribsrcdir}/%{import_path}/pam/
%gofilelist

%fdupes %{buildroot}

%files -f file.lst
%defattr(-,root,root)
%doc README.md
%license LICENSE

%changelog
