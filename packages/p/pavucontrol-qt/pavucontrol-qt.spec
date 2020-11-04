#
# spec file for package pavucontrol-qt
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pavucontrol-qt
Version:        0.16.0
Release:        0
Summary:        Qt port of pavucontrol
License:        GPL-2.0-only
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/pavucontrol-qt
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  xdg-user-dirs
BuildRequires:  cmake(KF5WindowSystem) >= 5.36
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse) >= 5.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 0.9.16
BuildRequires:  pkgconfig(lxqt)
Recommends:     %{name}-lang

%description
PulseAudio Volume Control (pavucontrol) is a simple volume control tool
("mixer") for the PulseAudio sound server. In contrast to classic mixer
tools this one allows you to control both the volume of hardware devices
and of each playback stream separately.

%lang_package

%prep
%setup -q
sed -i '/Name=/s/$/ Qt/' src/%{name}.desktop.in

%build
%cmake \
      -DPULL_TRANSLATIONS=OFF
make %{?_smp_mflags}

%install
%cmake_install

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files lang -f %{name}.lang 
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*

%changelog
