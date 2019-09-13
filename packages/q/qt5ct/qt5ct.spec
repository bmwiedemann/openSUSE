#
# spec file for package qt5ct
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qt5ct
Version:        0.37
Release:        0
Summary:        Qt5 Configuration Tool
License:        BSD-2-Clause
Group:          Development/Libraries/X11
URL:            https://sourceforge.net/projects/qt5ct
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        qt5ct.sh
Source2:        qt5ct.csh
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-private-headers-devel >= 5.4.0
BuildRequires:  libQt5PlatformSupport-private-headers-devel >= 5.4.0
BuildRequires:  libqt5-linguist >= 5.4.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.4.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.4.0
%requires_eq    libQt5Gui5
# libqt5-qtct was last used in openSUSE Leap 42.1.
Provides:       libqt5-qtct = %{version}
Obsoletes:      libqt5-qtct < %{version}

%description
This applications allows users to configure Qt5 settings (theme,
font, icons, etc.) under DE/WM without Qt integration.

%prep
%setup -q

%build
%qmake5
make %{?_smp_mflags} V=1

%install
%qmake5_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

%files
%license COPYING
%doc AUTHORS ChangeLog README
%config %{_sysconfdir}/profile.d/%{name}.*sh
%{_bindir}/%{name}
%dir %{_libdir}/qt5/plugins/platformthemes/
%{_libdir}/qt5/plugins/platformthemes/lib%{name}.so
%dir %{_libdir}/qt5/plugins/styles/
%{_libdir}/qt5/plugins/styles/lib%{name}-style.so
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
