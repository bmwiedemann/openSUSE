#
# spec file for package ebumeter
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           ebumeter
Version:        0.5.1
Release:        0
Summary:        Loudness measurement according to EBU-R128
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/ebumeter-doc/quickguide.html
Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.xz
BuildRequires:  clxclient-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng16-compat-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zita-resampler-devel
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
Provides:       ebur128

%description
Ebumeter provides real-time level metering according to the EBU R-128
recommendation. The current release implements all features required
by the EBU document except the oversampled peak level monitoring.
ebumeter can only be used with JACK.

A separate command-line utility (ebur128) to measure audio files is
provided as well.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
%make_build -C source PREFIX=%{_prefix}

%install
make -C source DESTDIR=%{buildroot} PREFIX=%{_prefix} install
install -Dm0644 share/redzita.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name} %{name} "Ebumeter" %{name} %{name} AudioVideo Player
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/ebumeter
%{_bindir}/ebur128
%{_datadir}/ebumeter
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
