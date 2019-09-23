#
# spec file for package guvcview-qt5
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
# Copyright (c) 2013 Marguerite Su <marguerite@opensuse.org>
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


%define         sover 2_0-2

Name:           guvcview-qt5
Version:        2.0.6
Release:        0
# Reference to GPL-2.0 in some files?
Summary:        Qt5 UVC Viewer and Capturer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Players
Url:            http://guvcview.sourceforge.net/
Source0:        https://sourceforge.net/projects/guvcview/files/source/guvcview-src-%{version}.tar.gz
Source90:       pre_checkin.sh
# PATCH-FIX-OPENSUSE guvcview-SUSE.patch -- use SUSE-specific paths
Patch0:         guvcview-SUSE.patch
# PATCH-FIX-OPENSUSE guvcview-qt5-nolibs_qt5names.patch -- use libraries from the GTK+ package
Patch1:         guvcview-qt5-nolibs_qt5names.patch

BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  guvcview-devel = %{version}
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang

%description
A Qt5 interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%lang_package

%prep
%setup -q -n guvcview-src-%{version}
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv
%configure --disable-debian-menu \
           --disable-desktop \
           --disable-gtk3 \
           --enable-qt5 \
           --program-suffix=-qt5

make %{?_smp_mflags}

%install
%make_install
# Create desktop file as disabled during build
%suse_update_desktop_file -c %{name} "A video viewer and capturer for the linux uvc driver" %{name} %{name} %{name} AudioVideo AudioVideoEditing
%fdupes %{buildroot}

%find_lang %{name} %{?no_lang_C}

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{ext_man}

%files lang -f %{name}.lang

%changelog
