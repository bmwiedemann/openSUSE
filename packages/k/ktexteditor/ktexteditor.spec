#
# spec file for package ktexteditor
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


# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define _tar_path 5.74
%bcond_without lang
Name:           ktexteditor
Version:        5.74.0
Release:        0
Summary:        Embeddable text editor component
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-MISFEATURE-OPENSUSE - Disliked by the security team (boo#1033055)
Patch1:         0001-Disable-KAuth-integration.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libeditorconfig-devel
BuildRequires:  libgit2-devel
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Parts) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Sonnet) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5SyntaxHighlighting) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0
Requires:       syntax-highlighting >= %{_kf5_bugfix_version}
Recommends:     %{name}-lang = %{version}
Obsoletes:      libKF5TextEditor4
Obsoletes:      libKF5TextEditor5

%description
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF5::TextEditor library.

%package devel
Summary:        Header files for ktexteditor, an embeddable text editor component
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5Parts) >= %{_kf5_bugfix_version}

%description devel
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF5::TextEditor library.

This subpackage provides the header files.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
  %cmake_kf5 -d build -- -DSYSCONF_INSTALL_DIR=%{_kf5_sysconfdir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with lang}
%files -n %{name}-lang -f %{name}5.lang
%endif

%files
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5TextEditor.so.*
%{_kf5_sharedir}/katepart5/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%dir %{_kf5_sharedir}/kdevappwizard/
%{_kf5_sharedir}/kdevappwizard/templates/
%{_kf5_debugdir}/ktexteditor.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/libKF5TextEditor.so
%{_kf5_libdir}/cmake/KF5TextEditor/
%dir %{_kf5_includedir}/*/
%{_kf5_includedir}/*/
%{_kf5_includedir}/*.h
%{_kf5_mkspecsdir}/qt_KTextEditor.pri

%changelog
