#
# spec file for package seq24
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           seq24
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  jack-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtkmm-2.4) >= 2.4.0
Summary:        A Small, Real-Time MIDI Sequencer
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Midi
Version:        0.9.3
Release:        0
Source:         http://launchpad.net/seq24/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
Source1:        %name.desktop
Source2:        seq24.png
Url:            https://launchpad.net/seq24
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Seq24 is a real-time midi sequencer. It was created to provide a very
simple interface for editing and playing MIDI 'loops.'

%prep
%setup -q

%if "%{version}" == "0.9.3"
# Bug in 0.9.3 and 0.9.3 prereleases
# class "mutex" in src/* clashes with "std::mutex" due
# to "using namespace std;". Rename mutex to seq24_mutex.
sed -i \
  -e 's,mutex::,seq24_mutex::,' \
  -e 's,\([ cs]\) mutex,\1 seq24_mutex,' \
  -e 's,::mutex,::seq24_mutex,' \
   src/*.h src/*.cpp
%endif

%build
%configure
make %{?jobs:-j %jobs}

%install
%makeinstall
%suse_update_desktop_file -i %name AudioVideo Sequencer
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README RTC SEQ24
%doc seq24usr.example
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
