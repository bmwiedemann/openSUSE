#
# spec file for package krusader
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           krusader
Version:        2.7.1
Release:        0
Summary:        A File Manager
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
Url:            https://krusader.org/
Source:         http://download.kde.org/stable/krusader/%{version}/%{name}-%{version}.tar.xz
Source1:        krusader_browse_iso.desktop
Source2:        org.kde.krusader.root-mode.desktop
# PATCH-FIX-UPSTREAM
Patch0:         Prefer-to-find-oktetapart-by-desktop-file.patch
BuildRequires:  extra-cmake-modules >= 1.7.0
BuildRequires:  fdupes
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent) >= 5.5.0
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5DBus) >= 5.5.0
BuildRequires:  cmake(Qt5Gui) >= 5.5.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0
BuildRequires:  cmake(Qt5Xml) >= 5.5.0
Requires:       kio_iso = %{version}
Suggests:       %{name}-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An advanced twin panel (commander style) file manager for KDE.

%package -n kio_iso
Summary:        KIO slave to access ISO images
Group:          System/GUI/KDE
Provides:       kde4-kio_iso = 1.80.99
Obsoletes:      kde4-kio_iso < 1.80.99

%description -n kio_iso
KIO slave to access ISO images like zip- or tar.gz-archives in your
file-browser.

%package doc
Summary:        A File Manager
Group:          Productivity/File utilities

%description doc
An advanced twin panel (commander style) file manager for KDE.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
export RPM_OPT_FLAGS="%{optflags} -fpermissive"
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
mkdir -p %{buildroot}%{_kf5_servicesdir}/ServiceMenus/
cp %{SOURCE1} %{buildroot}%{_kf5_servicesdir}/ServiceMenus/
cp %{SOURCE2} %{buildroot}%{_kf5_applicationsdir}/
%suse_update_desktop_file org.kde.krusader.root-mode FileManager Utility
%find_lang %{name}
%fdupes %{buildroot}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%license COPYING
%doc README AUTHORS ChangeLog TODO
%{_kf5_applicationsdir}/org.kde.krusader*.desktop
%{_kf5_appsdir}/krusader
%{_kf5_bindir}/krusader
%{_kf5_iconsdir}/??color/*/apps/krusader*.png
%{_kf5_plugindir}/kio_krarc.so
%{_kf5_servicesdir}/krarc.protocol
%{_kf5_kxmlguidir}/
%{_kf5_mandir}/man1/krusader.1.gz
%dir %{_kf5_mandir}/uk
%dir %{_kf5_mandir}/uk/man1
%{_kf5_mandir}/*/man1/krusader.1.gz
%exclude %{_kf5_htmldir}/*/krusader
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.krusader.appdata.xml

%files -n kio_iso
%defattr(-,root,root)
%config %{_kf5_configdir}/kio_isorc
%{_kf5_plugindir}/kio_iso.so*
%{_kf5_servicesdir}/iso.protocol
%dir %{_kf5_servicesdir}/ServiceMenus
%{_kf5_servicesdir}/ServiceMenus/krusader_browse_iso.desktop

%files doc
%defattr(-,root,root)
%doc %lang(en) %{_kf5_htmldir}/en/krusader
%doc %lang(uk) %{_kf5_htmldir}/uk/krusader
%doc %lang(sv) %{_kf5_htmldir}/sv/krusader

%changelog
