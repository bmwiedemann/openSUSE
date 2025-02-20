#
# spec file for package tucnak
#
# Copyright (c) 2021 Walter Fey DL8FCL
# Copyright (c) 2022 Walter Fey DL8FCL
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
# This file is under MIT license
#

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           tucnak
Version:        4.67
Release:        0
Summary:        VHF and microwave contest log
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Logging
URL:            https://tucnak.nagano.cz/
Source:         https://tucnak.nagano.cz/%{name}-%{version}.tar.gz
Patch0:         reproducible.patch
# for reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
#
BuildRequires:  gpm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(librtlsdr)
# From https://tucnak.nagano.cz/download.php
# "Tucnak requires the libzia library of same version"
BuildRequires:  pkgconfig(libzia) = %{version}
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile) >= 1.0.2

%description
Tucnak is a amateur radio VHF and above contest logging program
with some useful features as networking, cw keying, ssb voicer,
sound recorder and more. User interface is based on Taclog.

%prep
%autosetup -p1

%build
# for reproducible.patch
autoreconf -fiv
#
export CFLAGS="%{optflags} -fcommon"
%configure \
	--with-gpm \
	--with-rtlsdr \
	--enable-pedantic \
	%{nil}
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc NEWS README AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}/
%{_prefix}/lib/%{name}

%changelog
