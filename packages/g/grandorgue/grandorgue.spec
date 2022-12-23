#
# spec file for package grandorgue
#
# Copyright (c) 2022 SUSE LLC
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


%define version_suffix 1

Name:           grandorgue
Version:        3.9.4
Release:        0
Summary:        Virtual Pipe Organ Software
License:        GPL-2.0-or-later
URL:            https://github.com/GrandOrgue/grandorgue
Source:         https://github.com/GrandOrgue/grandorgue/archive/%{version}-%{version_suffix}.tar.gz#/%{name}-%{version}-%{version_suffix}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt-tools
BuildRequires:  po4a
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel
BuildRequires:  zip
BuildRequires:  zita-convolver-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rtaudio)
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
Recommends:     grandorgue-demo

%package demo
Summary:        GrandOrgue demo sampleset
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
BuildArch:      noarch

%description
GrandOrgue is a virtual pipe organ sample player application supporting a HW1 compatible file format.

%description demo
This package contains the demo sampleset for GrandOrgue.

%prep
%setup -qn %{name}-%{version}-%{version_suffix}

%build
%cmake -DDOC_INSTALL_DIR=%{_docdir} \
       -DLIBINSTDIR=%{_lib} \
       -DUSE_INTERNAL_RTAUDIO=OFF \
       -DUSE_INTERNAL_PORTAUDIO=OFF \
       -DUSE_INTERNAL_ZITACONVOLVER=OFF
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 644 README* %{buildroot}%{_docdir}/%{name}
%find_lang GrandOrgue
%suse_update_desktop_file GrandOrgue

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f GrandOrgue.lang
%{_bindir}/*
%{_libdir}/libGrandOrgue*
%dir %{_datadir}/GrandOrgue/packages
%dir %{_datadir}/GrandOrgue
%doc %{_docdir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*
%{_datadir}/GrandOrgue/help
%{_datadir}/GrandOrgue/sounds
%{_datadir}/GrandOrgue/perftests
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/*

%files demo
%{_datadir}/GrandOrgue/packages/*.orgue

%changelog
