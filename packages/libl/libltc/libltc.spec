#
# spec file for package libltc
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 11
Name:           libltc
Version:        1.3.2
Release:        0
Summary:        Linear/longitudinal timecode library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/x42/libltc
Source0:        https://github.com/x42/libltc/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of SMPTE timecode
data as a Manchester-Biphase encoded audio signal. The audio signal is
commonly recorded on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC audio from/to SMPTE
or EBU timecode, including SMPTE date support.

%package -n %{name}%{sover}
Summary:        Linear/longitudinal timecode library
Group:          System/Libraries

%description -n %{name}%{sover}
Linear (or Longitudinal) Timecode (LTC) is an encoding of SMPTE timecode
data as a Manchester-Biphase encoded audio signal. The audio signal is
commonly recorded on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC audio from/to SMPTE
or EBU timecode, including SMPTE date support.

%package devel
Summary:        Linear/longitudinal timecode library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Linear (or Longitudinal) Timecode (LTC) is an encoding of SMPTE timecode
data as a Manchester-Biphase encoded audio signal. The audio signal is
commonly recorded on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC audio from/to SMPTE
or EBU timecode, including SMPTE date support.

%prep
%setup -q

%build
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libltc.so.*

%files devel
%{_includedir}/ltc.h
%{_libdir}/libltc.so
%{_libdir}/pkgconfig/ltc.pc
%{_mandir}/man3/ltc.h.3%{?ext_man}

%changelog
