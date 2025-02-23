#
# spec file for package aldo
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


Name:           aldo
Version:        0.7.8
Release:        0
Summary:        Console-based morse tutor
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://www.nongnu.org/aldo
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ao)

%description
Aldo is a morse code learning tool which provides multiple types of training
exercises: Classic exercise, Koch method, Read from file (text file), Callsign
exercies (random callsigns).

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%check
%make_build check

%files -n %{name}
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/aldo
%{_mandir}/man1/*.1%{?ext_man}

%changelog
