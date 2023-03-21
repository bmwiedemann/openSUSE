#
# spec file for package ttynvt
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           ttynvt
Version:        0.16
Release:        0
Summary:        Virtual Network Terminal supporting the Com Port Control Option (RFC2217)
License:        GPL-3.0-or-later
Group:          System/Utilities
URL:            https://gitlab.com/lars-thrane-as/ttynvt
#Git-Clone:     https://gitlab.com/lars-thrane-as/ttynvt.git
Source:         https://gitlab.com/lars-thrane-as/ttynvt/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)

%description
ttynvt makes a virtual serial device (tty) and connects
the device to a Network Virtual Terminal (NVT).

%prep
%setup -q -n %{name}-v%{version}

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/ttynvt

%changelog
