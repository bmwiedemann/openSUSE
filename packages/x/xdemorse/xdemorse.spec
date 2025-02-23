#
# spec file for package xdemorse
#
# Copyright (c) 2024 Wojciech Kazubski <wk@ire.pw.edu.pl>
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


%bcond_with perseus-sdr
Name:           xdemorse
Version:        3.6.7
Release:        0
Summary:        Simple morse decoder for X11
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Morse
URL:            https://www.qsl.net/5b4az/pages/morse.html
Source:         https://www.qsl.net/5b4az/pkg/morse/xdemorse/%{name}-%{version}.tar.bz2
Patch0:         xdemorse-3.6.7-xdemorserc-message.patch
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
%if %{with perseus-sdr}
BuildRequires:  libperseus-sdr-devel
BuildRequires:  pkgconfig(libusb-1.0)
%endif

%description
Xdemorse is a simple morse decoder for X11.

%prep
%autosetup -p1

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install
mv %{buildroot}%{_datadir}/examples/xdemorse/* %{buildroot}/%{_docdir}/%{name}

%check
%make_build check

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_docdir}/xdemorse/

%changelog
