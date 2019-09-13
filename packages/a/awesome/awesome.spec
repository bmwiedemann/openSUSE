#
# spec file for package awesome
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           awesome
Version:        4.3
Release:        0
Summary:        Configurable tiling and floating Window Manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Url:            https://awesomewm.org/
Source:         https://github.com/awesomeWM/awesome-releases/raw/master/%{name}-%{version}.tar.xz
Source1:        https://github.com/awesomeWM/awesome-releases/raw/master/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  grep
BuildRequires:  lua-lgi >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  Lua(devel) >= 5.2
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.10
BuildRequires:  pkgconfig(libxdg-basedir) >= 1.0.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-icccm) >= 0.3.8
BuildRequires:  pkgconfig(xcb-keysyms) >= 0.3.4
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util) >= 0.3.8
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xproto) >= 7.0.15
BuildRequires:  rubygem(%{rb_default_ruby_abi}:asciidoctor)
BuildRequires:  typelib(GLib)
BuildRequires:  typelib(Gio)
BuildRequires:  typelib(Pango)
BuildRequires:  typelib(PangoCairo)
BuildRequires:  typelib(cairo)
Requires:       %{name}-branding = %{version}
Requires:       lua-lgi
Requires:       typelib(GLib)
Requires:       typelib(Gio)
Requires:       typelib(Pango)
Requires:       typelib(PangoCairo)
Requires:       typelib(cairo)
Provides:       windowmanager

%description
awesome is a dynamic window manager.

It manages windows in several layout modes: tiled, floating, etc.
Each layout can be applied dynamically, optimizing the environment
for the application in use and the task performed.

%package branding-upstream
Summary:        Upstream Branding for awesome
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for awesome.

%prep
%setup -q
sed -i 's/nano/vi/g' %{name}rc.lua
sed -i 's/^\(Type=\).*$/\1XSession/' %{name}.desktop
sed -i 's/#!\/usr\/bin\/env bash/#!\/bin\/bash/' ./utils/awesome-client

%build
%cmake \
  -DAWESOME_DOC_PATH=%{_docdir}/%{name} \
  -DXDG_CONFIG_DIR=%{_sysconfdir}/xdg   \
  -DCOMPRESS_MANPAGES=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install

# xsession default selector
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/awesome.desktop 20

%postun
[ -f %{_datadir}/xsessions/awesome.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/awesome.desktop

%files
%license LICENSE
%doc README.md
%doc %{_docdir}/%{name}/
%dir %{_sysconfdir}/xdg/%{name}/
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/themes/
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/%{name}.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_mandir}/man?/%{name}*.?%{?ext_man}
%{_mandir}/*/man?/%{name}*.?%{?ext_man}

%files branding-upstream
%license LICENSE
%config(noreplace) %{_sysconfdir}/xdg/%{name}/rc.lua
%{_datadir}/%{name}/themes/

%changelog
