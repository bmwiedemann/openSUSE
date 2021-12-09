#
# spec file for package novprog
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2016 Graeme Gott <graeme@gottcode.org>
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


Name:           novprog
Version:        3.2.0
Release:        0
Summary:        Wordcount graphing program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://gottcode.org/novprog/
Source:         http://gottcode.org/novprog/%{name}-%{version}-src.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       hicolor-icon-theme

%description
NovProg allows you to create a graph of your progress in writing a
NaNoWriMo style novel. You enter your wordcount and it updates a graph
showing you how much progress you have made. It also shows you how far you
are through your daily goal, and your total goal. Mousing over a bar in the
graph will show a tooltip with that day's wordcount.

%lang_package

%prep
%setup -q

%build
%qmake5 PREFIX=%{_prefix}
%make_jobs

%install
%qmake5_install
%suse_update_desktop_file -u -r %{name} Office Publishing
%find_lang %{name} --with-qt

%files
%license COPYING
%doc ChangeLog CREDITS README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/novprog.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
