#
# spec file for package linsim
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           linsim
Version:        2.0.6
Release:        0
Summary:        Amateur Radio Digital Mode evaluation under varying HF propagation conditions
License:        GPL-3.0-or-later
URL:            https://www.w1hkj.org/
Source:         https://www.w1hkj.org/files/test_suite/%{name}-%{version}.tar.gz
Patch0:         linsim-desktop.patch
BuildRequires:  c++_compiler
BuildRequires:  fltk-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(samplerate) >= 0.1.1
BuildRequires:  pkgconfig(sndfile) >= 1.0.10

%description
Linsim is designed to read and then add path simulation to any monophonic wav
file recorded at any sampling rate. It works particularly well with files that
were created using fldigi’s audio capture and audio generate functions. The
entire wav file will be saved to computer memory and then duplicated during the
signal processing. The user should try to keep the length of the wav file at 20
Mg or less, but the author has tested some 200 Mg files on both Linux and
Windows-8 without causing a program fault. These files were original VOAR
broadcasts of about 30 minutes duration. The objective of this type of
simulation is to finally measure the character error rate (CER) and bit error
rate (BER) of a specific modem type and decoder design. For most modems a
sequence of 1000 characters provides a sufficient level of confidence in the
CER measurment.

Simulations include path delay, doppler, frequency shift and band limited
Gaussian white noise. All simulations are constrained to a 3000 Hz bandwidth.
The input signal is filtered by a FIR bandpass filter (400 - 3400 Hz).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/linsim
%{_datadir}/applications/linsim.desktop
%{_datadir}/pixmaps/linsim.xpm

%changelog
