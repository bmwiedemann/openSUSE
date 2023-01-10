#
# spec file for package evolution-ews
#
# Copyright (c) 2023 SUSE LLC
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


# _version needs to be %%{version} stripped to major.minor.micro only...
%define _version %(echo %{version} | grep -E -o '[0-9]+\.[0-9]+\.[0-9]+')

Name:           evolution-ews
Version:        3.46.3
Release:        0
Summary:        Exchange Connector for Evolution, compatible with Exchange 2007 and later
License:        LGPL-2.1-only
Group:          Productivity/Networking/Email/Clients
URL:            https://wiki.gnome.org/Apps/Evolution
Source0:        https://download.gnome.org/sources/evolution-ews/3.46/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(camel-1.2) >= %{_version}
BuildRequires:  pkgconfig(evolution-calendar-3.0) >= %{_version}
BuildRequires:  pkgconfig(evolution-data-server-1.2) >= %{_version}
BuildRequires:  pkgconfig(evolution-mail-3.0) >= %{_version}
BuildRequires:  pkgconfig(evolution-shell-3.0) >= %{_version}
BuildRequires:  pkgconfig(glib-2.0) >= 2.46
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libebackend-1.2) >= %{_version}
BuildRequires:  pkgconfig(libebook-1.2) >= %{_version}
BuildRequires:  pkgconfig(libecal-2.0) >= %{_version}
BuildRequires:  pkgconfig(libedata-book-1.2) >= %{_version}
BuildRequires:  pkgconfig(libedata-cal-2.0) >= %{_version}
BuildRequires:  pkgconfig(libedataserver-1.2) >= %{_version}
BuildRequires:  pkgconfig(libemail-engine) >= %{_version}
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libmspack) >= 0.4
BuildRequires:  pkgconfig(libsoup-3.0)

%description
The EWS Exchange Connector for Evolution provides a Exchange
backend from evolution-data-server as well as plugins for Evolution
to access Exchange features.

The EWS Exchange Connector is using the Exchange Web Services
interface and is therefore compatible with Exchange 2007 and later.

Provides exchange connectivity for exchange server 2007 and later
using exchange web services protocol.

%lang_package

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendmicrosoft365.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendmicrosoft365.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%{_libdir}/evolution-data-server/camel-providers/libcamelmicrosoft365.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmicrosoft365.urls
%{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%{_libdir}/evolution-data-server/registry-modules/module-microsoft365-backend.so
%{_libdir}/evolution-ews/libevolution-microsoft365.so
%{_libdir}/evolution/modules/module-ews-configuration.so
%{_libdir}/evolution/modules/module-microsoft365-configuration.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libcamelews-priv.so
%{_libdir}/%{name}/libevolution-ews.so
%{_datadir}/evolution/errors/module-ews-configuration.error
%dir %{_datadir}/evolution-data-server/ews
%{_datadir}/evolution-data-server/ews/windowsZones.xml
%{_datadir}/metainfo/org.gnome.Evolution-ews.metainfo.xml

%files lang -f evolution-ews.lang

%changelog
