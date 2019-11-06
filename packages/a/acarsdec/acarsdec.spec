#
# spec file for package acarsdec
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           acarsdec
Version:        3.4
Release:        0
Summary:        ACARS SDR decoder 
License:        GPL-2.0-or-later
Url:            https://github.com/TLeconte/acarsdec
#Git-Clone:     https://github.com/TLeconte/acarsdec.git
Source:         https://github.com/TLeconte/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         acarsdec-fix-makefile.diff
#BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sqlite3)

%description
A multi-channels acars decoder with built-in rtl_sdr front end.
It comes with a database backend : acarsserv to store receved acars messages.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
export CFLAGS='%{optflags}'
make acarsdec acarsserv %{?_smp_mflags}

%install
install -Dpm 0755 acarsdec %{buildroot}/%{_bindir}/acarsdec
install -Dpm 0755 acarsserv %{buildroot}/%{_bindir}/acarsserv

%files
%defattr(-,root,root)
%doc README.md docs/index.md
%{_bindir}/acarsdec
%{_bindir}/acarsserv

%changelog
