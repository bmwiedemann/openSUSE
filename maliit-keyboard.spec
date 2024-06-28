#
# spec file for package maliit-keyboard
#
# Copyright (c) 2024 SUSE LLC
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


%global __requires_exclude qmlimport\\((MaliitKeyboard|keys)
Name:           maliit-keyboard
Version:        2.3.1
Release:        0
License:        BSD-3-Clause AND LGPL-3.0-only AND CC-BY-3.0
Summary:        Maliit virtual keyboard
URL:            https://github.com/maliit/keyboard
Source0:        keyboard-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpresage-devel
BuildRequires:  presage
BuildRequires:  sqlite3
BuildRequires:  cmake(MaliitPlugins)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  pkgconfig(anthy)
BuildRequires:  pkgconfig(chewing)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libpinyin)
Requires:       libqt5-qtwayland
Recommends:     %{name}-layouts
Recommends:     %{name}-styles-ubuntu
Recommends:     %{name}-themes
Suggests:       dejavu-fonts
Obsoletes:      maliit-keyboard2 < %{version}
Provides:       maliit-keyboard2 = %{version}
Obsoletes:      maliit-keyboard-emoji < %{version}
Provides:       maliit-keyboard-emoji = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Maliit provides a flexible and cross-platform input method framework.
It has a plugin-based client-server architecture where applications
act as clients and communicate with the Maliit server via input
context plugins. The communication link currently uses D-Bus. Maliit
is an open source framework (LGPL 2) with open source plugins (BSD).

%package        layouts
Summary:        Maliit Keyboard Layout Files
Requires:       %{name} = %{version}

%description    layouts
Provides layouts that are not english QWERTY
for Maliit Virtual Keyboard.

%lang_package

%prep
%autosetup -p1 -n keyboard-%{version}

%build
%cmake -Denable-presage=ON -Denable-hunspell=ON -Denable-tests=OFF
%cmake_build

%install
%cmake_install
%{__rm} -rf %{buildroot}%{_datadir}/doc/%{name}
%fdupes %{buildroot}%{_prefix}

%check
%ctest

%find_lang %{name} --with-qt

%files layouts
%{_libdir}/maliit/keyboard2/languages/
%exclude %{_libdir}/maliit/keyboard2/languages/en/
%dnl %{_datadir}/locale/*

%files
%defattr(-,root,root,-)
%license COPYING.BSD COPYING
%{_bindir}/%{name}
%dir %{_libdir}/maliit/keyboard2
%{_libdir}/maliit/keyboard2/qml/
%{_libdir}/maliit/keyboard2/languages/en/
%dir %{_datadir}/maliit
%dir %{_datadir}/maliit/keyboard2
%{_datadir}/maliit/keyboard2/{devices,icons,images}/
%dir %{_libdir}/maliit/
%{_libdir}/maliit/plugins/
%{_datadir}/glib-2.0/schemas/org.maliit.keyboard.maliit.gschema.xml
%{_datadir}/applications/com.github.maliit.keyboard.desktop
%{_datadir}/metainfo/*.metainfo.xml

%files lang -f %{name}.lang

%changelog
