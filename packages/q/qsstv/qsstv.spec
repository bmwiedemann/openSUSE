#
# spec file for package qsstv
#
# Copyright (c) 2021 previous contributors, see changelog
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


Name:           qsstv
Version:        9.5.8
Release:        0
Summary:        Qt-based SSTV and HAMDRM
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://www.qsl.net/on4qz/index.html
Source:         https://www.qsl.net/o/on4qz//qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.1
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libv4l2)

%description
QSSTV is a program for receiving and transmitting SSTV and HAMDRM (sometimes
called DSSTV). It is compatible with most of MmSSTV and EasyPal

%prep
%autosetup -p1 -n %{name}

%build
%qmake5 \
	PREFIX=%{_prefix} \
	%{nil}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# Let suse_update_desktop_file find the qsstv icon
cp icons/%{name}.png %{_sourcedir}

# Install man page borrowed from Debian
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%suse_update_desktop_file -c %{name} Qsstv "Qt-based SSTV and HAMDRM" %{name} %{name} "Network;HamRadio"

%files
%doc README.txt
%license COPYING
%{_bindir}/qsstv
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
