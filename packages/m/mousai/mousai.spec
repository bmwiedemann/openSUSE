#
# spec file for package mousai
#
# Copyright (c) 2025 mantarimay
# Copyright (c) 2022 SUSE LLC
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


%define _lto_cflags %{nil}
Name:           mousai
Version:        0.7.9
Release:        0
Summary:        Identify songs in seconds
License:        GPL-3.0-or-later
URL:            https://github.com/SeaDve/Mousai
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)

%description
Discover songs you are aching to know with an easy-to-use interface.

Mousai is a simple application that can recognize songs similar to Shazam.
Just click the listen button, and then wait a few seconds. It will magically
return the title and artist of that song!

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet \
      %{buildroot}%{_datadir}/metainfo/*.metainfo.xml 

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/mousai/
%{_datadir}/dbus-1/services/*.service

%files lang -f %{name}.lang
#incorrect-locale-subdir
%exclude %{_datadir}/locale/zh_Han{s,t}

%changelog
