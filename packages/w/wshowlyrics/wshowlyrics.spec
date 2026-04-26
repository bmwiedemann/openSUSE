#
# spec file for package wshowlyrics
#
# Copyright (c) 2026 mantarimay
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


Name:           wshowlyrics
Version:        0.10.0
Release:        0
Summary:        A lightweight lyrics overlay for Wayland compositors
License:        GPL-3.0-or-later
URL:            https://github.com/unstable-code/lyrics
Source0:        %{url}/archive/v%{version}/lyrics-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  hicolor-icon-theme
BuildRequires:  wayland-protocols-devel
BuildRequires:  cairo-devel
BuildRequires:  libcurl-devel
BuildRequires:  pango-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  libappindicator3-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libjson-c-devel

%description
A lightweight lyrics overlay for Wayland compositors that displays
synchronized lyrics for currently playing music.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

#fix wrong binary name
sed -i 's|Exec=wshowlyrics|Exec=lyrics|g' \
    %{buildroot}%{_datadir}/applications/wshowlyrics.desktop

%files
%license LICENSE
%doc README*
%{_bindir}/lyrics
%{_bindir}/%{name}-offset
%{_userunitdir}/%{name}.service
%{_datadir}/applications/wshowlyrics.desktop
%{_datadir}/icons/hicolor/scalable/apps/wshowlyrics.svg
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/settings.ini

%changelog
