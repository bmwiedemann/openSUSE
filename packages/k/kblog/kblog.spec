#
# spec file for package kblog
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


%define kf5_version 5.63.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kblog
Version:        20.04.2
Release:        0
Summary:        Client-side support library for web application remote blogging APIs
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5XmlRpcClient)
BuildRequires:  cmake(Qt5Test)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
KBlog is a library for calling functions on Blogger 1.0, MetaWeblog,
MovableType and GData compatible blogs.

%package -n libKF5Blog5
Summary:        Client-side support library for web application remote blogging APIs
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5Blog5
KBlog is a library for calling functions on Blogger 1.0, MetaWeblog,
MovableType and GData compatible blogs. It supports asynchronous
sending and fetching of posts and, if supported on the server,
multimedia files. Almost every modern blogging web application that
provides an XML data interface supports one of the APIs mentioned
above.

%package devel
Summary:        Development files for KDE's web application remote blogging API library
Group:          Development/Libraries/KDE
Requires:       libKF5Blog5 = %{version}
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Syndication)
Obsoletes:      kblog5-devel < %{version}
Provides:       kblog5-devel = %{version}

%description devel
KBlog is a library for calling functions on Blogger 1.0, MetaWeblog,
MovableType and GData compatible blogs. It calls the APIs using
KXmlRpcClient and Syndication. It supports asynchronous sending and
fetching of posts and, if supported on the server, multimedia files.

This package contains necessary include files for the library.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kblog-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5Blog5 -p /sbin/ldconfig
%postun -n libKF5Blog5 -p /sbin/ldconfig

%files -n libKF5Blog5
%license COPYING.LIB
%{_kf5_libdir}/libKF5Blog.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5Blog/
%{_kf5_includedir}/KBlog/
%{_kf5_includedir}/kblog_version.h
%{_kf5_libdir}/libKF5Blog.so
%{_kf5_mkspecsdir}/qt_KBlog.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
