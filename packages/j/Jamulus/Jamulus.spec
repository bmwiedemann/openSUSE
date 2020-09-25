#
# spec file for package Jamulus
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define tarball_version 3_5_11

Name:           Jamulus
Version:        3.5.11
Release:        0
Summary:        Low-latency internet connection tool for real-time jam sessions
License:        GPL-2.0-or-later
URL:            http://llcon.sourceforge.net/index.html
Source0:        https://github.com/corrados/jamulus/archive/r%{tarball_version}.tar.gz#/jamulus-r%{tarball_version}.tar.gz
Source1:        %{name}_icon.png
# PATCH-FIX-UPSTREAM Jamulus-disable_version_check.patch
Patch0:         Jamulus-disable_version_check.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  jack-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(opus)
Requires:       jack
Provides:       llcon = %{version}
Obsoletes:      llcon < %{version}
Provides:       jamulus = %{version}
Obsoletes:      jamulus < %{version}

%description
The Jamulus software enables musicians to perform real-time jam sessions over
the internet. There is one server running the Jamulus server software which
collects the audio data from each Jamulus client software, mixes the audio data
and sends the mix back to each client.

%prep
%autosetup -p1 -n jamulus-r%{tarball_version}
install %{SOURCE1} .

%build
%qmake5 CONFIG+=opus_shared_lib CONFIG+=disable_version_check
%make_jobs

%install
install -D -m0755 Jamulus %{buildroot}%{_bindir}/%{name}
for s in 16 22 32 48 64 72 96 128 192; do
   mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
   convert -strip -resize ${s}x${s} %{name}_icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
install -Dm0644 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png \
                %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -c %{name} %{name} "Internet Jam Session Software" %{name} %{name} "AudioVideo;Audio;Mixer;Qt"
%suse_update_desktop_file -C "Jam Session" %{name}

%fdupes %{buildroot}%{_datadir}

%files
%doc README.md ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png

%changelog
