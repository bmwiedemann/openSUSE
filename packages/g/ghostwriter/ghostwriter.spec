#
# spec file for package ghostwriter
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


Name:           ghostwriter
Version:        2.1.6
Release:        0
Summary:        A distraction-free Markdown editor
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://ghostwriter.kde.org
Source:         https://github.com/KDE/ghostwriter/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngineCore)
BuildRequires:  pkgconfig(hunspell)
Recommends:     %{name}-lang
Recommends:     multimarkdown
Suggests:       MultiMarkdown-5
Suggests:       MultiMarkdown-6
Suggests:       cmark
Suggests:       discount
Suggests:       pandoc
Suggests:       texlive-context
Suggests:       wkhtmltopdf

%description
ghostwriter is a text editor for Markdown, which is a plain text
markup format. For more information about Markdown, please visit John
Gruber’s website at http://www.daringfireball.net. ghostwriter
provides a relaxing, distraction-free writing environment.

%lang_package

%prep
%autosetup

%build
lrelease-qt5 %{name}.pro
%qmake5 PREFIX=%{_prefix}
%make_jobs

%install
%qmake5_install
%suse_update_desktop_file -r %{name} TextEditor
%find_lang %{name} --with-qt

%files
%license COPYING
%doc README.md CREDITS.md
%{_bindir}/ghostwriter
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/ghostwriter.appdata.xml
%{_datadir}/applications/ghostwriter.desktop
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/ghostwriter.1%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/ghostwriter
%dir %{_datadir}/ghostwriter/translations

%changelog
