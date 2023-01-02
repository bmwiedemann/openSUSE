#
# spec file for package xjadeo
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2015 Packman Team <packman@links2linux.de>
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


Name:           xjadeo
Version:        0.8.12
Release:        0
Summary:        Video player that gets sync from Jack
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Visualization
URL:            http://xjadeo.sourceforge.net/
Source0:        https://sourceforge.net/projects/xjadeo/files/xjadeo/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(imlib2) >= 1.3.0
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)

%description
Xjadeo is a video player that gets sync from JACK. When a
sequencer like Muse or Rosegarden acts as a timebase master, xjadeo will
display the video frame in sync with the sequencer transport. This means
that an audio event can be visually synchronized with a certain frame in
the movie, which may be useful for creating a soundtrack for
a video clip.

%prep
%autosetup -p1

%build
export CFLAGS="-Wall %{optflags}"
%configure
%make_build

%install
%make_install

install -Dm644 src/%{name}/icons/%{name}H128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "The X Jack Video Monitor" %{name} %{name} AudioVideo Video Player

%files
%doc README NEWS AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_bindir}/xjremote
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/xjremote.1%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ArdourMono.ttf

%changelog
