#
# spec file for package feathernotes
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Shawn W Dunn <sfalken@opensuse.org>
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
%global rname FeatherNotes

Name:           feathernotes
Version:        1.3.2
Release:        0
Summary:        Qt-based plaintext editor
License:        GPL-3.0-only
URL:            https://github.com/tsujan/%{rname}
Source0:        %{url}/releases/download/V%{version}/%{rname}-%{version}.tar.xz
Source1:        %{url}/releases/download/V%{version}/%{rname}-%{version}.tar.xz.asc
Source2:        %{name}.keyring

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(x11)

%description
FeatherNotes is a lightweight Qt hierarchical notes-manager for
Linux. It is independent of any desktop environment and has:

* Support for rich text formatting, image embedding and inserting
  editable tables
* Drag-and-drop capability for moving nodes and also for embedding
  images
* A tray icon for quick access on any desktop
* Saving and restoring of size (and also position under X11)
* Compact but complete search and replacement widgets
* The ability to include searchable tags (hidden info on each node)
* Support for optional node icons
* Support for local and remote hyperlinks (bookmarks)
* Text zooming
* Printing and exporting to HTML and PDF
* Password protection
* Auto-saving
* Optional spell checking with Hunspell

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_qt6
%qt6_build

%install
%qt6_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-qt

%files -f %{name}.lang
%license COPYING
%doc ChangeLog NEWS README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/icons/hicolor/*/mimetypes/text-%{name}-fnx.svg
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/mime/packages/%{name}.xml

%changelog
