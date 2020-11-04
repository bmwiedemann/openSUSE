#
# spec file for package taigo
#
# Copyright (c) 2019 SUSE LLC
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


Name:           taigo
Version:        0.3
Release:        0
Summary:        A virtual pet for your desktop
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            https://github.com/Appadeia/taigo
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)

%define __rdns_name com.github.appadeia.Taigo

%description
A virtual pet for your desktop that needs your
care in raising it.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{__rdns_name}.desktop Game Amusement Simulation

%files
%license COPYING
%doc README.md
%{_bindir}/taigo
%{_datadir}/applications/%{__rdns_name}.desktop
%{_datadir}/metainfo/%{__rdns_name}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{__rdns_name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{__rdns_name}{,-symbolic}.svg

%changelog
