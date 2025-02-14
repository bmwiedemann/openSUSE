#
# spec file for package direwolf
#
# Copyright (c) 2017 Walter Fey DL8FCL
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
# 
# This file is under MIT license

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           direwolf
Version:        1.7
Release:        0
Summary:        Software "soundcard" modem/TNC and APRS
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/wb2osz/direwolf
Source0:        https://github.com/wb2osz/direwolf/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        direwolf.desktop
Patch1:         fix-udev-rules-path.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(avahi-core)

%description
Dire Wolf is a software "soundcard" modem/TNC and APRS * encoder/decoder. It
can be used stand-alone to receive APRS messages, as a digipeater, APRStt
lf.desktop
gateway, or Internet Gateway (IGate). It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC, UISS,
Linux AX25, SARTrack, and many others.

%package doc
Summary:        Dire Wolf documentation
Group:          Documentation/Other
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for Dire Wolf

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -D --mode=644 %{SOURCE1} %{buildroot}%{_datadir}/applications/direwolf.desktop

%check
%ctest

%files
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_prefix}/lib/udev/rules.d/99-direwolf-cmedia.rules
%{_datadir}/pixmaps/direwolf_icon.png
%{_mandir}/*/*

%files doc
%license LICENSE
%doc CHANGES.md README.md
%{_datadir}/doc/direwolf/
%exclude %{_datadir}/doc/direwolf/scripts/dw-start.sh

%changelog
