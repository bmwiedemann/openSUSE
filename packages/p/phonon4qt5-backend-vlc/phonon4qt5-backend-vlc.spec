#
# spec file for package phonon4qt5-backend-vlc
#
# Copyright (c) 2021 SUSE LLC
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


%define filename phonon-backend-vlc
%define _phonon4qt5_version 4.10.60
%bcond_without lang
Name:           phonon4qt5-backend-vlc
Version:        0.11.3
Release:        0
Summary:        Phonon VLC Backend
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/phonon/%{filename}/%{version}/%{filename}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  kf5-filesystem
BuildRequires:  vlc-devel >= 2.1.0
BuildRequires:  cmake(Phonon4Qt5) >= %{_phonon4qt5_version}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
Requires:       libphonon4qt5 >= %{_phonon4qt5_version}
Requires:       vlc-noX >= %( echo `rpm -q --queryformat '%%{VERSION}' vlc-devel`)
Conflicts:      vlc-noX > %( echo `rpm -q --queryformat '%%{VERSION}' vlc-devel | cut -f -2 -d .`.99)
Provides:       phonon4qt5-backend = %{version}

%description
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

This is the VLC backend for Phonon

%lang_package

%prep
%setup -q -n phonon-backend-vlc-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build

%if %{with lang}
  %find_lang phonon_vlc %{name}.lang --with-qt
%endif

%post
%if 0%{?suse_version} >= 1500
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins
%else
%{_libdir}/vlc/vlc-cache-gen -f %{_libdir}/vlc/plugins
%endif

%files
%license COPYING.LIB
%doc AUTHORS
%dir %{_kf5_plugindir}/phonon4qt5_backend
%{_kf5_plugindir}/phonon4qt5_backend/phonon_vlc.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
