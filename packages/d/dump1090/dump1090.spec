#
# spec file for package dump1090
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dump1090
Version:        1.14+git.20180110
Release:        0
Summary:        An ADS-B Mode S decoder for RTLSDR devices (MalcolmRobb's fork)
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
Url:            https://github.com/MalcolmRobb/dump1090
Source:         %{name}-%{version}.tar.xz
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libusb-1.0)

%description
An ADS-B Mode S decoder specifically designed for RTLSDR devices.
MalcolmRobb's fork

%prep
%setup -q

%build
make CC="cc %{optflags} -Wno-format-truncation" %{?_smp_mflags}

%install
install -D -p -m 0755 dump1090 \
  %{buildroot}/%{_bindir}/dump1090
install -D -p -m 0755 view1090 \
  %{buildroot}/%{_bindir}/view1090

%check
make test %{?_smp_mflags}

%files
%doc README.md
%{_bindir}/dump1090
%{_bindir}/view1090

%changelog
