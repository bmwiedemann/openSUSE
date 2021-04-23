#
# spec file for package reco
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           reco
Version:        2.4.0
Release:        0
Summary:        Audio Recording App
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/ryonakano/reco
Source:         https://github.com/ryonakano/reco/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
An audio recording app designed for elementary OS.

%lang_package

%prep
%setup -q

# Switch to bugs.opensuse.org
find -name \*.xml* -exec \
sed -i '/bugtracker/s|>[^>]*<|>https://bugs.opensuse.org<|' {} +

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.ryonakano.reco GTK Utility AudioVideo
%find_lang com.github.ryonakano.reco %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license LICENSE
%doc README.md
%{_bindir}/com.github.ryonakano.reco
%{_datadir}/applications/com.github.ryonakano.reco.desktop
%{_datadir}/glib-2.0/schemas/com.github.ryonakano.reco.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.ryonakano.reco.??g
%{_datadir}/icons/hicolor/*/apps/record-completed-symbolic.??g
%{_datadir}/metainfo/com.github.ryonakano.reco.appdata.xml

%files lang -f %{name}.lang

%changelog
