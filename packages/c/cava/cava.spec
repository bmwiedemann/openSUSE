#
# spec file for package cava
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


Name:           cava
Version:        0.7.3
Release:        0
Summary:        Console-based Audio Visualizer for Alsa
License:        MIT
Group:          Productivity/Multimedia/Sound/Visualization
URL:            https://github.com/karlstav/cava
Source:         https://github.com/karlstav/%{name}/archive/%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  fftw3-devel
# Use system ini parser instead of building own lib
BuildRequires:  libiniparser-devel >= 4.0
BuildRequires:  libpulse-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
# Installing the psf in a directory that comes from kbd
Requires:       kbd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
C.A.V.A. is a bar spectrum audio visualizer for the Linux terminal using ALSA, pulseaudio or fifo buffer for input.

%prep
%setup -q
./autogen.sh
%configure FONT_DIR="%{_datadir}/kbd/consolefonts"

%build
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/cava
%dir %{_datadir}/kbd/
%dir %{_datadir}/kbd/consolefonts/
%{_datadir}/kbd/consolefonts/cava.psf

%changelog
