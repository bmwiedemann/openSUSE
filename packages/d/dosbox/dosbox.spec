#
# spec file for package dosbox
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


Name:           dosbox
Version:        0.74.3
Release:        0
Summary:        DOS Emulator Well-Suited for Playing Games
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          System/Emulators/PC
URL:            https://www.dosbox.com
Source:         https://downloads.sf.net/dosbox/dosbox-0.74-3.tar.gz
Source1:        dosbox.desktop
Source2:        dosbox.png
Source3:        CONFIG-midi-mt32-gm
Patch0:         dosbox-0.71-manpage.diff
# Patch from https://github.com/munt/munt/releases the latest release libmt32emu.
Patch1:         dosbox-0.74-3-mt32-patch.diff
BuildRequires:  Mesa-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl)
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
BuildRequires:  libmt32emu-devel
%endif

%description
dosbox is a DOS emulator that, thanks to its good graphics and sound
emulation, is exceptionally well-suited for playing games. dosbox
features a built-in DOS operating system and transparent access to the
Linux file system and is therefore very easy to use.

%prep
%setup -q -n dosbox-0.74-3
%patch0 -p1
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
%patch1 -p1
%endif

%build
autoreconf -f -i
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure
%make_build

%check
%make_build check

%install
%make_install
install -dpm0755 %{buildroot}%{_datadir}/pixmaps
install -pm0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/dosbox.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
install -pm0644 %{SOURCE3} .
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
%doc CONFIG-midi-mt32-gm
%endif
%{_bindir}/dosbox
%{_mandir}/man?/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
