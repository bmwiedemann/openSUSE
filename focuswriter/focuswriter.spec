#
# spec file for package focuswriter
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.7.2
Release:        0
Summary:        A fullscreen, distraction-free writing program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Word Processor
URL:            http://gottcode.org/focuswriter
Source:         http://gottcode.org/focuswriter/%{name}-%{version}-src.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5Gui) >= 5.9
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.9
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.9
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(zlib)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     %{name}-lang

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
lrelease-qt5 %{name}.pro
%qmake5 PREFIX=%{_prefix}
%make_jobs

%install
%qmake5_install
%suse_update_desktop_file %{name}
%find_lang %{name} --with-qt
%fdupes -s %{buildroot}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc ChangeLog CREDITS README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/themes
%{_datadir}/focuswriter/symbols1000.dat
%{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/translations

%changelog
