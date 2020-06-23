#
# spec file for package pulseview
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


Name:           pulseview
Version:        0.4.2
Release:        0
Summary:        Qt-based GUI for sigrok
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://sigrok.org
Source0:        https://sigrok.org/download/source/pulseview/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Fix-building-with-Qt-5.15.patch
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libsigrok-devel >= 0.5.2
BuildRequires:  libsigrokdecode-devel >= 0.5.2
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

PulseView is a Qt-based GUI for sigrok.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{optflags} -fpermissive"
%cmake -DDISABLE_WERROR=TRUE ..
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

install -m 644 -D icons/pulseview.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/pulseview.png
install -m 644 -D icons/pulseview.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/pulseview.svg

install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 644 contrib/org.sigrok.PulseView.desktop %{buildroot}%{_datadir}/applications/org.sigrok.PulseView.desktop
%suse_update_desktop_file -r org.sigrok.PulseView Education Engineering

install -m 755 -d %{buildroot}%{_datadir}/metainfo/
install -m 644 contrib/org.sigrok.PulseView.appdata.xml %{buildroot}%{_datadir}/metainfo/org.sigrok.PulseView.appdata.xml

%files
%license COPYING
%doc NEWS README HACKING
%{_bindir}/*
%{_mandir}/man1/pulseview.*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/pulseview*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.sigrok.PulseView.appdata.xml

%changelog
