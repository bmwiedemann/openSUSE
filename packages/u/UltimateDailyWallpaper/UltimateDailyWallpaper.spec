#
# spec file for package UltimateDailyWallpaper
#
# Copyright (c) 2023 Patrice Coni <patrice.coni-dev@yandex.com>
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

Name:           UltimateDailyWallpaper
Version:        3.2.0
Release:        0
Summary:        A wallpaper changer and downloader
License:        GPL-3.0+
Group:          Productivity/Multimedia/Other
URL:            https://github.com/pagaco-swita/ultimatedailywallpaper
Source0:        %{url}/archive/v%{version}.tar.gz#/ultimatedailywallpaper-%{version}.tar.gz

BuildRequires:  libstdc++-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qttranslations
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  update-desktop-files
BuildRequires:  glibc-devel

Requires:       curl

%description
UltimateDailyWallpaper is a utility to set the daily
picture as wallpaper of a selected provider. It saves
images in a high quality. Further information about
each picture can be obtained from the Internet with a
single click. It integrates with most desktop
environments to provide automatically changing wallpaper.
It allows a simple integration of external plugins, which
allows downloading a daily wallpaper from any one provider.

%prep
rm -rf debian
rm -rf screenshots
rm -rf src/macOS
%setup -q -n ultimatedailywallpaper-%{version} -a 0

%build
export QTDIR="%{_qt5_prefix}"
export PATH="%{_qt5_bindir}:$PATH"
lrelease-qt5 src/src.pro
qmake-qt5
%make_build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_libdir}/%{name}-plugins
mkdir -p %{buildroot}/%{_datadir}/locale/ca/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/de/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/es/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/fi/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/fr/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/it/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/ru/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/uk/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/ko/LC_MESSAGES
mkdir -p %{buildroot}/%{_datadir}/locale/pt/LC_MESSAGES
cp language/%{name}_ca.qm %{buildroot}/%{_datadir}/locale/ca/LC_MESSAGES
cp language/%{name}_de.qm %{buildroot}/%{_datadir}/locale/de/LC_MESSAGES
cp language/%{name}_es.qm %{buildroot}/%{_datadir}/locale/es/LC_MESSAGES
cp language/%{name}_fi.qm %{buildroot}/%{_datadir}/locale/fi/LC_MESSAGES
cp language/%{name}_fr.qm %{buildroot}/%{_datadir}/locale/fr/LC_MESSAGES
cp language/%{name}_it.qm %{buildroot}/%{_datadir}/locale/it/LC_MESSAGES
cp language/%{name}_ru.qm %{buildroot}/%{_datadir}/locale/ru/LC_MESSAGES
cp language/%{name}_uk.qm %{buildroot}/%{_datadir}/locale/uk/LC_MESSAGES
cp language/%{name}_ko.qm %{buildroot}/%{_datadir}/locale/ko/LC_MESSAGES
cp language/%{name}_pt.qm %{buildroot}/%{_datadir}/locale/pt/LC_MESSAGES
cp src/icons/ultimatedesktopwallpaper_icon.png %{buildroot}/%{_datadir}/pixmaps
install -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
install -m 0755 plugins/libbing-wallpaper-downloader-*.so %{buildroot}/%{_libdir}/%{name}-plugins
install -m 0755 plugins/libwikimedia-commons-potd-*.so %{buildroot}/%{_libdir}/%{name}-plugins
%suse_update_desktop_file -i %{name}
%find_lang %{name} --with-qt

%files -f %{name}.lang

%files
%defattr(-,root,root)
%dir %{_libdir}/%{name}-plugins
%{_bindir}/%{name}
%{_datadir}/pixmaps/ultimatedesktopwallpaper_icon.png
%{_libdir}/%{name}-plugins/libbing-wallpaper-downloader-*.so
%{_libdir}/%{name}-plugins/libwikimedia-commons-potd-*.so
%{_datadir}/applications/%{name}.desktop
%license LICENSE
%doc README.md AUTHORS

%changelog
