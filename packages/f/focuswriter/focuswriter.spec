#
# spec file for package focuswriter
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 Graeme Gott <graeme@gottcode.org>
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


Name:           focuswriter
Version:        1.8.4
Release:        0
Summary:        A fullscreen, distraction-free writing program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Word Processor
URL:            https://gottcode.org/focuswriter
Source:         https://gottcode.org/focuswriter/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-tools-linguist
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(zlib)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun):hicolor-icon-theme
Requires(postun):update-desktop-files

%description
A fullscreen, distraction-free writing program. You can customize your
environment by changing the font, colors, and background image to add
ambiance as you type. FocusWriter features an on-the-fly updating word
count, optional auto-save, optional daily goals, and an interface that
hides away to allow you to focus more clearly; additionally, when you open
the program your current work-in-progress will automatically load and
position you at the end of your document, so that you can immediately jump
back in.

%lang_package

%prep
%setup -q

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%suse_update_desktop_file %{name}

%find_lang %{name} --with-qt

%fdupes -s %{buildroot}

%files
%doc ChangeLog CREDITS README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/themes
%{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/focuswriter/symbols1500.dat

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/translations

%changelog
