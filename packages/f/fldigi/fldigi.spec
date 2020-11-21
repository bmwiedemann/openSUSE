#
# spec file for package fldigi
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


Name:           fldigi
Version:        4.1.15
Release:        0
Summary:        Digital modem program (hamradio)
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://sourceforge.net/projects/fldigi/
#Git-Clone:     https://git.code.sf.net/p/fldigi/fldigi
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flxmlrpc)
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Recommends:     %{name}-lang

%description
Digital modem program.
Supports the following modes:
CW, Contestia, DominoEX, Hell, MFSK, MT63, Olivia, Psk, RTTY, Thor, Throb
WEFAX, WWV calibration, Frequency Analysis, Tune

%lang_package

%package -n flarq
Summary:        Transmitting and receiving frames of ARQ data (hamradio)
Group:          Productivity/Hamradio/Other
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description -n flarq
Fast Light Automatic Repeat reQuest is a file transfer application that is based
on the ARQ specification developed by Paul Schmidt, K9PS.  It is capable of
transmitting and receiving frames of ARQ data via Fldigi. The interaction
between Flarq and Fldigi requires no operator intervention.

%prep
%setup -q

%build
export BUILD_DATE=`date -d@0`
export BUILD_USER=openSUSE
export BUILD_HOST=openSUSE
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
%fdupes -s %{buildroot}/%{_mandir}

%suse_update_desktop_file -i fldigi
%suse_update_desktop_file -i flarq

%check
make %{?_smp_mflags} check

%if 0%{?suse_version} < 1325
%post
%desktop_database_post

%post -n flarq
%desktop_database_post

%postun
%desktop_database_postun

%postun -n flarq
%desktop_database_postun
%endif

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/fldigi
%{_datadir}/applications/fldigi.desktop
%{_datadir}/pixmaps/fldigi.xpm
%{_datadir}/fldigi/
%{_mandir}/man1/fldigi.1%{ext_man}

%files lang -f %{name}.lang

%files -n flarq
%{_bindir}/flarq
%{_datadir}/applications/flarq.desktop
%{_datadir}/pixmaps/flarq.xpm
%{_mandir}/man1/flarq.1%{ext_man}

%changelog
