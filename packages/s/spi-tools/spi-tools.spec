#
# spec file for package spi-tools
#
# Copyright (c) 2023 SUSE LLC
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


Name:           spi-tools
Version:        1.0.2
Release:        0
Summary:        A set of SPI tools for Linux
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/cpb-/spi-tools
Source0:        https://github.com/cpb-/spi-tools/archive/%{version}.tar.gz#/spi-tools-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
Requires:       udev

%description
This package contains some simple command line tools to help using Linux
spidev devices.

%prep
%setup -q

%build
autoreconf -fim
%configure
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
