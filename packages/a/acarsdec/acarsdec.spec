#
# spec file for package acarsdec
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017-2022, Martin Hauke <mardnh@gmx.de>
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


%define srcname %{name}-%{name}-%{version}
Name:           acarsdec
Version:        3.7
Release:        0
Summary:        ACARS SDR decoder
License:        GPL-2.0-or-later
URL:            https://github.com/TLeconte/acarsdec
#Git-Clone:     https://github.com/TLeconte/acarsdec.git
Source:         https://github.com/TLeconte/acarsdec/archive/acarsdec-%{version}.tar.gz#/%{srcname}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libacars-2) >= 2.0.0
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(sndfile)
Provides:       bundled(cJSON)

%description
A multi-channels acars decoder with built-in rtl_sdr front end.
It comes with a database backend : acarsserv to store receved acars messages.

%prep
%setup -q -n %{srcname}
%patch0 -p1

%build
%cmake \
  -DLIBRTL=1 \
  -DLIBAIR=1 \
  -DMQTT=0
%make_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/acarsdec

%changelog
