#
# spec file for package featherpad
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


Name:           featherpad
Version:        0.18.0
Release:        0
Summary:        Qt5-based plaintext editor
License:        GPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://github.com/tsujan/FeatherPad
Source:         https://github.com/tsujan/FeatherPad/archive/V%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} == 1315
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif

%description
FeatherPad is a Qt5-based plain-text editor. It is independent of any desktop environment and has:
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
%setup -q -n FeatherPad-%{version}

%build
%qmake5 \
%if 0%{?suse_version} == 1315
    QMAKE_CXX=%{_bindir}/g++-7
%endif

%make_jobs

%install
%qmake5_install

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

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations

%changelog
