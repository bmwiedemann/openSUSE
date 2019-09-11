#
# spec file for package phonon-backend-vlc
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
Name:           phonon-backend-vlc
Version:        0.10.3
Release:        0
Summary:        Phonon VLC Backend
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/phonon/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  pkgconfig
BuildRequires:  vlc-devel >= 2.1.0
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(phonon) >= %{_phonon_version}
Requires:       libphonon4 >= %{_phonon_version}
%requires_ge    vlc-noX
Conflicts:      vlc-noX > %( echo `rpm -q --queryformat '%%{VERSION}' vlc-devel | cut -f -2 -d .`.99)
Provides:       phonon-backend

%description
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the
same quality on all platforms, no matter which underlying
architecture is used.

This is the VLC backend for Phonon.

%prep
%setup -q -n phonon-vlc-%{version}

%build
%cmake_kde4 -d build
%make_jobs

%install
%kde4_makeinstall -C build
%fdupes %{buildroot}

%kde_post_install

%post
%if 0%{?suse_version} >= 1500
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
%else
%{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc/plugins
%endif

%files
%license COPYING.LIB
%doc AUTHORS
%dir %{_kde4_servicesdir}/phononbackends
%{_kde4_modulesdir}/plugins/phonon_backend/phonon_vlc.so
%{_kde4_servicesdir}/phononbackends/vlc.desktop

%changelog
