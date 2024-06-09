#
# spec file for package vacuum-im
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


%define sname vacuum
%define rtime 1639054987
%define rhash g0abd5e1
Name:           %{sname}-im
Version:        1.3.0+git%{rtime}.%{rhash}
Release:        0
Summary:        Jabber client written with Qt
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            http://www.vacuum-im.org/
Source:         %{name}-r%{rhash}.tar.xz
# PATCH-FEATURE-OPENSUSE paranoia.patch
Patch1:         paranoia.patch
# PATCH-FEATURE-OPENSUSE fix_default_smiles.patch
Patch2:         fix_default_smiles.patch
# Fix sending of type attribute in data forms
# PATCH-FIX-UPSTREAM dataform_submit_type_attr.patch
Patch3:         dataform_submit_type_attr.patch
BuildRequires:  cmake >= 3.0
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Multimedia-devel
BuildRequires:  libQt5X11Extras-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  minizip-devel
BuildRequires:  openssl-devel
BuildRequires:  qxtglobalshortcut-devel
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
Recommends:     %{name}-lang
Recommends:     %{name}-plugins-spellchecker
%if 0%{?suse_version} > 1320
BuildRequires:  libXss-devel
%else
BuildRequires:  libXScrnSaver-devel
%endif

%description
The core program is just a plugin loader - all functionality is made
available via plugins. This enforces modularity and ensures well defined
component interaction via interfaces.

%define libname libvacuumutils37

%package -n %{libname}
Summary:        Shared library libvacuumutils for Vacuum-IM
Group:          System/Libraries
Conflicts:      libvacuumutils1_7

%description -n %{libname}
This package includes shared libraris needed to work Vacuum-IM program.

%package devel
Summary:        Development files for Vacuum-IM
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description devel
This package includes files needed to develop Vacuum-IM modules.

%package plugins-spellchecker
Summary:        Vacuum-IM spellchecker plugin
Group:          Productivity/Networking/Instant Messenger
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description plugins-spellchecker
Highlights words that may not be spelled correctly.

%package plugins-statistics
Summary:        Vacuum-IM application statistics collection plugin
Group:          Productivity/Networking/Instant Messenger
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description plugins-statistics
This plugin needed to collect application statistics.

%lang_package

%prep
%autosetup -p1 -n vacuum-im

%build
%cmake \
        -DCMAKE_CXX_FLAGS="%{optflags} -std=c++0x"\
        -DGIT_DATE="%{rtime}"\
        -DGIT_HASH="%{rhash}"\
        -DINSTALL_SDK=ON\
        -DINSTALL_APP_DIR=%{name}\
        -DINSTALL_LIB_DIR=%{_lib}\
        -DINSTALL_DOC_DIR=%{_defaultdocdir}\
        -DSPELLCHECKER_BACKEND=HUNSPELL\
        -DFORCE_BUNDLED_MINIZIP=OFF\
        -DNO_WEBKIT=ON\
        -DPLUGIN_adiummessagestyle=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install

for size in 16 24 32 48 64 96 128; do
    install -Dpm 0644 resources/menuicons/shared/mainwindowlogo$size.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
sed -i "s/^Exec=.*$/Exec=%{name}/;s/^Icon=.*$/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{sname}.desktop
mv %{buildroot}%{_datadir}/applications/%{sname}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_datadir}/pixmaps/%{sname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
mv %{buildroot}%{_bindir}/%{sname} %{buildroot}%{_bindir}/%{name}
%suse_update_desktop_file -c %{name} "Vacuum-IM" "Jabber Client" %{name} %{name}.png Network InstantMessaging

%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%exclude %{_datadir}/%{name}/translations
%doc %{_defaultdocdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/plugins/libspellchecker.so
%exclude %{_libdir}/%{name}/plugins/libstatistics.so
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/vacuum-im.metainfo.xml

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libvacuumutils.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libvacuumutils.so
%{_includedir}/%{name}

%files plugins-spellchecker
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/libspellchecker.so

%files plugins-statistics
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/libstatistics.so

%files lang
%defattr(-,root,root)
%{_datadir}/%{name}/translations
%lang(de) %{_datadir}/%{name}/translations/de/*.qm
%lang(pl) %{_datadir}/%{name}/translations/pl/*.qm
%lang(ru) %{_datadir}/%{name}/translations/ru/*.qm
%lang(uk) %{_datadir}/%{name}/translations/uk/*.qm

%changelog
