#
# spec file for package OOKiedokie
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


Name:           OOKiedokie
Version:        0.0.0+git.20151230
Release:        0
Summary:        A tool for transmitting and receiving OOK-modulated data with SDRs
License:        MIT
Group:          Productivity/Hamradio/Other
Url:            https://github.com/jynik/OOKiedokie
Source:         %{name}-%{version}.tar.xz
Patch0:         OOKiedokie-fix-missing-return-type.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libbladeRF)

%description
OOKiedokie is a tool intended to help SDR users interface with miscellaneous
wireless devices utilizing On-Off Keying, a very simple form of
Amplitude Shift Keying modulation.

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/ookiedokie
%{_datadir}/OOKiedokie/

%changelog
