#
# spec file for package kbibtex
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kbibtex
Version:        0.10.50git.20260801T020758~7ee937e1
Release:        0
Summary:        The BibTeX (Latex) bibliography manager by KDE
License:        GPL-2.0-only
URL:            https://apps.kde.org/kbibtex/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{qt6_version}
%ifarch x86_64 aarch64 riscv64
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(poppler-qt6)

%description
KBibTeX is a BibTeX editor by KDE to edit bibliographies used with
LaTeX. Features include comfortable input masks, starting web queries
(e. g. Google or PubMed) and exporting to PDF, PostScript, RTF and
XML/HTML. As KBibTeX is using KDE's KParts technology, KBibTeX can be
embedded into Kile or Konqueror.

%package        devel
Summary:        Development files for kbibtex
Requires:       kbibtex = %{version}

%description    devel
This package contains the development files for kbibtex.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc ChangeLog
%doc %lang(en) %{_kf6_htmldir}/en/kbibtex
%{_kf6_applicationsdir}/org.kde.kbibtex.desktop
%{_kf6_appstreamdir}/org.kde.kbibtex.appdata.xml
%{_kf6_bindir}/kbibtex
%{_kf6_bindir}/kbibtex-cli
%{_kf6_debugdir}/kbibtex.categories
%{_kf6_iconsdir}/hicolor/*/apps/kbibtex.png
%{_kf6_libdir}/libkbibtex*.so.*
%{_kf6_mandir}/man1/kbibtex.1%{?ext_man}
%{_kf6_plugindir}/kf6/parts/kbibtexpart.so
%{_kf6_sharedir}/kbibtex/
%{_kf6_sharedir}/mime/packages/bibliography.xml

%files devel
%{_includedir}/KBibTeX/
%{_kf6_cmakedir}/KBibTeX/
%{_kf6_libdir}/libkbibtex*.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
