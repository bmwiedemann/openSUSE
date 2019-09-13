#
# spec file for package ultrastar-deluxe
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


Name:           ultrastar-deluxe
Version:        2017.8.0+git250.4849669
Release:        0
Summary:        Karaoke game
License:        GPL-2.0-only
Group:          Amusements/Games/Action/Other
Url:            https://usdx.eu/
Source0:        USDX-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  fpc
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(lua5.3)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(sqlite3)

%description
UltraStar Deluxe (USDX) is karaoke game. It allows up to six players
to sing along with music using microphones in order to score points,
depending on the pitch of the voice and the rhythm of singing.

%prep
%setup -q -n USDX-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
# There are a lot of duplicated Images
%fdupes %{buildroot}%{_datadir}/ultrastardx
rm %{buildroot}%{_datadir}/ultrastardx/COPYING.txt
# They are only for translators
rm %{buildroot}%{_datadir}/ultrastardx/languages/convert.sh
rm %{buildroot}%{_datadir}/ultrastardx/languages/update.py
# They shouldn't be executable
chmod -x %{buildroot}%{_datadir}/ultrastardx/plugins/*

%files
%doc README.md
%license COPYING.txt
%{_bindir}/ultrastardx
%{_datadir}/ultrastardx

%changelog
