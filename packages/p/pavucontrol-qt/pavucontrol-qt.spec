#
# spec file for package pavucontrol-qt
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


Name:           pavucontrol-qt
Version:        2.0.0
Release:        0
Summary:        A Pulseaudio mixer in Qt
License:        GPL-2.0-only
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/pavucontrol-qt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets) >= 6.6.0
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
Recommends:     %{name}-lang = %{version}-%{release}

%description
pavucontrol-qt is the Qt port of the volume control pavucontrol for the
sound server PulseAudio. As such it can be used to adjust all controls
provided by PulseAudio and ALSA as well as some additional settings.

%lang_package

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%license LICENSE

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
