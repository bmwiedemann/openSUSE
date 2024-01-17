#
# spec file for package deepin-voice-note
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-voice-note
Version:        5.10.18
Release:        0
License:        GPL-3.0+
Summary:        Deepin Voice Note 
Url:            https://github.com/linuxdeepin/deepin-voice-note
Group:          Productivity/Multimedia/Video/Editors and Convertors
Source0:        https://github.com/linuxdeepin/deepin-voice-note/archive/%{version}/%{name}-%{version}.tar.gz
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  libqt5-linguist
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libvlc)
Recommends:     %{name}-lang
# Qt5WebEngineWidgets is invalid on these arches
ExcludeArch:    ppc ppc64 ppc64le s390 s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Voice Notes is a lightweight memo tool to make text notes and voice and audio
recordings. 

%lang_package

%prep
%setup -q
sed -i 's/lupdate/lupdate-qt5/g;s/lrelease/lrelease-qt5/g' assets/translate_generation.sh

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DAPP_VERSION=%{version}-%{distribution} \
       -DVERSION=%{version}-%{distribution}
%cmake_build

%install
%cmake_install

%suse_update_desktop_file -r %{name} Audio AudioVideoEditing
%fdupes %{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.conf
%{_datadir}/%{name}/web
%{_datadir}/deepin-manual/manual-assets/application/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%files lang
%{_datadir}/%{name}/translations

%changelog

