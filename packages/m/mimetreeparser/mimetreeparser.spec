#
# spec file for package mimetreeparser
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           mimetreeparser
Version:        24.05.1
Release:        0
Summary:        Library to parse MIME trees
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KPim6Libkleo) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mbox) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
mimetreeparser is a parser for MIME trees. Given a MIME tree, it extracts
the parts (text, html...) and attachments.

%package -n libKPim6MimeTreeParserCore6
Summary:        Core library to parse MIME trees
Requires:       mimetreeparser >= %{version}

%description -n libKPim6MimeTreeParserCore6
mimetreeparser is a parser for MIME trees. Given a MIME tree, it extracts
the parts (text, html...) and attachments. This package provides
the core library needed for parsing.

%package -n libKPim6MimeTreeParserWidgets6
Summary:        Widgets for library to parse MIME trees
Requires:       libKPim6MimeTreeParserCore6 = %{version}

%description -n libKPim6MimeTreeParserWidgets6
mimetreeparser is a parser for MIME trees. Given a MIME tree, it extracts
the parts (text, html...) and attachments. This package provides graphical
widgets for the parser.

%package imports
Summary:        QML support for MIME tree parser
Requires:       libKPim6MimeTreeParserCore6 = %{version}
Requires:       libKPim6MimeTreeParserWidgets6 = %{version}

%description imports

mimetreeparser is a parser for MIME trees. Given a MIME tree, it extracts
the parts (text, html...) and attachments. This package provides QML
support, allowing to use the library with QtQuick applications.

%package devel
Summary:        Development files for for MIME tree parser
Requires:       libKPim6MimeTreeParserCore6 = %{version}
Requires:       libKPim6MimeTreeParserWidgets6 = %{version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KPim6Mbox) >= %{kpim6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}

%description devel
mimetreeparser is a parser for MIME trees. Given a MIME tree, it extracts
the parts (text, html...) and attachments. This package provides
files to develop applications using this library.

%lang_package -n libKPim6MimeTreeParserCore6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install
%ifnarch aarch64 riscv64 x86_64 %{x86_64}
# Qt WebEngine not available
rm %{buildroot}%{_kf6_qmldir}/org/kde/pim/mimetreeparser/private/HtmlPart.qml
%endif

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6MimeTreeParserCore6
%ldconfig_scriptlets -n libKPim6MimeTreeParserWidgets6

%files
%{_kf6_debugdir}/mimetreeparser.categories

%files -n libKPim6MimeTreeParserCore6
%license LICENSES/*
%{_kf6_libdir}/libKPim6MimeTreeParserCore.so.*

%files -n libKPim6MimeTreeParserWidgets6
%{_kf6_libdir}/libKPim6MimeTreeParserWidgets.so.*

%files imports
%dir %{_kf6_qmldir}/org/kde/pim/
%{_kf6_qmldir}/org/kde/pim/mimetreeparser/

%files devel
%doc %{_kf6_qchdir}/KPim6MimeTreeParserCore.*
%doc %{_kf6_qchdir}/KPim6MimeTreeParserWidgets.*
%{_includedir}/KPim6/MimeTreeParserCore/
%{_includedir}/KPim6/MimeTreeParserWidgets/
%{_kf6_cmakedir}/KPim6MimeTreeParserCore/
%{_kf6_cmakedir}/KPim6MimeTreeParserWidgets/
%{_kf6_libdir}/libKPim6MimeTreeParserCore.so
%{_kf6_libdir}/libKPim6MimeTreeParserWidgets.so
%{_kf6_mkspecsdir}/qt_MimeTreeParserCore.pri
%{_kf6_mkspecsdir}/qt_MimeTreeParserWidgets.pri

%files -n libKPim6MimeTreeParserCore6-lang -f %{name}.lang

%changelog
