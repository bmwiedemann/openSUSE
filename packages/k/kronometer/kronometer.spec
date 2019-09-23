#
# spec file for package kronometer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kronometer
Version:        2.2.3
Release:        0
Summary:        A stopwatch application by KDE
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://userbase.kde.org/Kronometer
Source:         https://download.kde.org/stable/kronometer/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.9.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
Kronometer is a stopwatch application.

Kronometer's main features are the following:

* Start/pause/resume the stopwatch widget
* Laps recording: you can capture the stopwatch time when you want and add a note to it
* Lap times sorting: you can easily find the shortest lap time or the longest one
* Reset the stopwatch widget and the lap times
* Time format settings: you can choose the stopwatch granularity
* Times saving and resuming: you can save the stopwatch status and resume it later
* Font customization: you can choose the fonts for each of the stopwatch digits
* Color customization: you can choose the color for the stopwatch digits and the stopwatch background
* Lap times export: you can export the lap times on a file using the JSON or CSV format

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %find_lang %{name} --with-kde --with-man
%if 0%{?opensuse_version} > 1320 || 0%{?sle_version} >= 120300
  %{kf5_find_htmldocs}
%else
# %%kf5_find_htmldocs is only defined since Leap 42.3
  CURDIR=`pwd`
  pushd %{buildroot}%{_kf5_htmldir}
  for i in *; do
    if ! [ -d "%{_datadir}/locale/${i}" ]; then
        echo "Removing unsupported translation %{_kf5_htmldir}/${i}"
        rm -rf "$i"
    elif [ "$i" != "en" ]; then
        echo "%doc %lang($i) %{_kf5_htmldir}/${i}" >> $CURDIR/%{name}.lang
    fi
  done
  popd
%endif

%files -f %{name}.lang
%license COPYING
%doc README
%{_kf5_applicationsdir}/org.kde.kronometer.desktop
%{_kf5_bindir}/%{name}
%dir %{_kf5_configkcfgdir}
%{_kf5_configkcfgdir}/%{name}.kcfg
%if 0%{?suse_version} == 1315 && 0%{?sle_version} < 120200
%dir %{_kf5_appstreamdir}
%endif
%{_kf5_appstreamdir}/org.kde.kronometer.appdata.xml
%{_kf5_iconsdir}/hicolor/*/apps/kronometer.*
%doc %lang(en) %{_kf5_htmldir}/en/%{name}
%doc %lang(en) %{_kf5_mandir}/man1/%{name}.1.gz
%if 0%{?suse_version} == 1315 && 0%{?sle_version} < 120300
%dir %{_kf5_mandir}/uk
%dir %{_kf5_mandir}/uk/man1
%endif

%changelog
