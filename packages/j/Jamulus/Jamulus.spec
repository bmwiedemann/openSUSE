#
# spec file for package Jamulus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           Jamulus
Version:        3.4.3
Release:        0
Summary:        Low-latency internet connection tool for real-time jam sessions
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://llcon.sourceforge.net/index.html
Source0:        https://sourceforge.net/projects/llcon/files/Jamulus/%{version}/Jamulus-%{version}.tar.gz
Source1:        %{name}.png
BuildRequires:  ImageMagick
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  jack-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(opus)
Requires:       jack
Provides:       llcon = %{version}
Obsoletes:      llcon < %{version}
Provides:       jamulus = %{version}-%{release}
Obsoletes:      jamulus

%description
The Jamulus software enables musicians to perform real-time jam sessions over
the internet. There is one server running the Jamulus server software which
collects the audio data from each Jamulus client software, mixes the audio data
and sends the mix back to each client.

%prep
%setup -q -n %{name}%{version}
sed -i -e '/^Exec/cExec=%{name}' -e '/^Icon/cIcon=%{name}' src/res/jamulus.desktop
chmod -x README
install %{SOURCE1} .

%build
%qmake5 CONFIG+=opus_shared_lib
make %{?_smp_mflags}

%install
install -D -m0755 Jamulus %{buildroot}%{_bindir}/%{name}
install -D -m0644 src/res/jamulus.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
for s in 16 22 32 48 64 72 96 128 192; do
   mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
   convert -strip -resize ${s}x${s} %{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
pushd %{buildroot}%{_datadir}/pixmaps
ln -s ../icons/hicolor/48x48/apps/%{name}.png .
popd

%files
%doc README AUTHORS ChangeLog TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png

%changelog
