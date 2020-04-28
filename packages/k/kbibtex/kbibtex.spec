#
# spec file for package kbibtex
#
# Copyright (c) 2020 SUSE LINUX LLC
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


%bcond_without lang

Name:           kbibtex
Version:        0.9.2
Release:        0
Summary:        The BibTeX (Latex) bibliography manager by KDE
License:        GPL-2.0-only
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://userbase.kde.org/KBibTeX/
Source:         https://download.kde.org/stable/KBibTeX/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kcompletion-devel
BuildRequires:  kcoreaddons-devel >= 5.51.0
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kparts-devel
BuildRequires:  kservice-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwallet-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libicu-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  qoauth-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
# Only include WebEngine for platforms that support it
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
%else
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
%endif

%description
KBibTeX is a BibTeX editor by KDE to edit bibliographies used with
LaTeX. Features include comfortable input masks, starting web queries
(e. g. Google or PubMed) and exporting to PDF, PostScript, RTF and
XML/HTML. As KBibTeX is using KDE's KParts technology, KBibTeX can be
embedded into Kile or Konqueror.

%package        devel
Summary:        Devel Files for %{name}
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description    devel
This package contains the devel files for %{name}.

%lang_package

%prep
%autosetup -n %{name}-%{version}

%build
%cmake_kf5 -d build
make %{?_smp_mflags}

%install
%make_install -C build
%suse_update_desktop_file -r org.kde.kbibtex Qt KDE Office Database Science DataVisualization Education

%if %{with lang}
%find_lang %{name}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc ChangeLog
%license LICENSE
%{_kf5_libdir}/libkbibtex*.so.*
%config %{_kf5_configdir}/kbibtexrc
%{_kf5_bindir}/kbibtex
%{_kf5_plugindir}/kbibtexpart.so*
%{_kf5_applicationsdir}/org.kde.kbibtex.desktop
%{_kf5_iconsdir}/hicolor/*/apps/kbibtex.png
%{_kf5_sharedir}/kbibtex/
%{_kf5_servicesdir}/kbibtexpart.desktop
%{_kf5_kxmlguidir}/kbibtex/
%{_kf5_kxmlguidir}/kbibtexpart/
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.kbibtex.appdata.xml
%{_kf5_htmldir}/*/kbibtex/
%{_kf5_sharedir}/mime/packages/bibliography.xml
%{_kf5_sharedir}/man/man1/kbibtex.1.gz
%{_kf5_sharedir}/man/*/man1/kbibtex.1.gz

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files devel
%{_kf5_libdir}/libkbibtex*.so

%changelog
