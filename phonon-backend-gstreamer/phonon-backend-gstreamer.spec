#
# spec file for package phonon-backend-gstreamer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _phonon_version 4.7.0
Name:           phonon-backend-gstreamer
Version:        4.9.1
Release:        0
Summary:        Phonon Multimedia Platform Abstraction
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/phonon/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(phonon) >= %{_phonon_version}
Requires:       libphonon4 >= %{_phonon_version}
Supplements:    packageand(gstreamer-plugins-base:phonon)
Obsoletes:      phonon-backend-gstreamer-0_10 < %{version}
Provides:       phonon-backend
Provides:       phonon-backend-gstreamer-0_10 = %{version}

%description
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the
same quality on all platforms, no matter which underlying
architecture is used.

This is the GStreamer backend for Phonon.

%prep
%setup -q -n phonon-gstreamer-%{version}

%build
%cmake_kde4 -d build
%make_jobs

%install
%kde4_makeinstall -C build
%suse_update_desktop_file %{buildroot}%{_kde4_servicesdir}/phononbackends/gstreamer.desktop
%fdupes %{buildroot}%{_includedir}

# Icons conflict with phonon4qt5-backend-gstreamer, so remove them here
rm -rf %{buildroot}%{_datadir}/icons/*/*/apps/

%kde_post_install

%files
%license COPYING.LIB
%dir %{_kde4_servicesdir}/phononbackends
%{_kde4_modulesdir}/plugins/phonon_backend/phonon_gstreamer.so
%{_kde4_servicesdir}/phononbackends/gstreamer.desktop

%changelog
