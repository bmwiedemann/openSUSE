#
# spec file for package go-for-it
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


%define appid com.github.jmoerman.go-for-it
%define sover 0
Name:           go-for-it
Version:        1.9.2
Release:        0
Summary:        A to-do list with built-in productivity timer
%define libname lib%{name}-%{sover}
License:        GPL-3.0-only
URL:            https://github.com/mank319/Go-For-It
Source0:        https://github.com/mank319/Go-For-It/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM vala-0.56-update-interval-visibility.patch https://github.com/JMoerman/Go-For-It/pull/173
Patch0:         vala-0.56-update-interval-visibility.patch
BuildRequires:  cmake >= 2.8.9
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
# valac (cmake FindVala); spec-cleaner rewrites this to vapigen*.pc
BuildRequires:  vala >= 0.36.15
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
Recommends:     %{name}-lang

%description
Go For It! keeps track of tasks and assists in processing
them subsequently. The timer avoids distraction by keeping the user's
focus on the recent task, while issuing reminders to take short breaks
on a regular basis.

%lang_package

%package -n %{libname}-%{sover}
Summary:        Shared library for Go For It!

%description -n %{libname}-%{sover}
Shared library used by the Go For It! to-do list application and its plugins.

%package devel
Summary:        Development files for Go For It!
Requires:       %{libname}-%{sover} = %{version}
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(libpeas-1.0)

%description devel
Header files, pkg-config metadata and Vala bindings for the Go For It!
shared library.

%prep
%autosetup -p1 -n Go-For-It-%{version}

%build
# cmake 4 rejects cmake_minimum_required() < 3.5
%cmake \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DAPP_SYSTEM_NAME=%{name} \
  -DICON_UPDATE:BOOL=OFF \
  -DGSETTINGS_COMPILE:BOOL=OFF \
  -DBUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install
# keep the reverse-DNS name from 1.6.3 as a compatibility symlink
ln -s %{name} %{buildroot}%{_bindir}/%{appid}
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%check
export NO_AT_BRIDGE=1
export GTK_A11Y=none
xvfb-run -a build/tests/%{appid}-tests

%ldconfig_scriptlets -n %{libname}-%{sover}

%files
%license COPYING
%doc AUTHORS CHANGELOG.md CONFIGURING.md README.md
%{_bindir}/%{name}
%{_bindir}/%{appid}
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/*/%{appid}*
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugins/

%files -n %{libname}-%{sover}
%license COPYING
%{_libdir}/%{libname}.so.%{sover}*

%files devel
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}-%{sover}.pc
%{_includedir}/%{name}-%{sover}.h
%{_datadir}/vala/vapi/%{name}-%{sover}.vapi
%{_datadir}/vala/vapi/%{name}-%{sover}.deps

%files lang -f %{appid}.lang

%changelog
