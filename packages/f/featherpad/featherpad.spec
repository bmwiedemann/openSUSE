#
# spec file for package featherpad
#
# Copyright (c) 2025 SUSE LLC
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


Name:           featherpad
Version:        1.6.2
Release:        0
Summary:        Qt-based plaintext editor
License:        GPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://github.com/tsujan/FeatherPad
Source0:        %{url}/releases/download/V%{version}/FeatherPad-%{version}.tar.xz
Source1:        %{url}/releases/download/V%{version}/FeatherPad-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt6Core) >= 6.2.0
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(x11)

%description
FeatherPad is a plain-text editor. It is independent of any desktop environment and has:
* Drag-and-drop support, including tab detachment and attachment;
* X11 virtual desktop awareness (using tabs on current desktop but opening a new window on another);
* An optional permanent search bar with a different search entry for each tab;
* Instant highlighting of found matches when searching;
* A docked window for text replacement;
* Support for showing line numbers and jumping to a specific line;
* Automatic detection of text encoding as far as possible and optional saving with encoding;
* Syntax highlighting for common programming languages;
* Printing;
* Text zooming;
* Non-interrupting prompts;

%lang_package

%prep
%autosetup -p1 -n FeatherPad-%{version}

%build
%cmake_qt6
%qt6_build

%install
%qt6_install

%find_lang %{name} --with-qt

%files
%license COPYING
%doc ChangeLog NEWS README.md
%{_bindir}/%{name}
%{_bindir}/fpad
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help*
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/metainfo/featherpad.metainfo.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations

%changelog
