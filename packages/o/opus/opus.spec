#
# spec file for package opus
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define sover   0
Name:           opus
Version:        1.5.2
Release:        0
Summary:        Audio Codec Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://opus-codec.org/
Source:         https://downloads.xiph.org/releases/opus/opus-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  pkgconfig

%description
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package -n libopus%{sover}
Summary:        Opus Audio Codec Library
Group:          System/Libraries

%description -n libopus%{sover}
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package -n libopus-devel
Summary:        Opus Audio Codec Library Development Environment
Group:          Development/Libraries/C and C++
Requires:       libopus%{sover} = %{version}

%description -n libopus-devel
The Opus codec is designed for interactive speech and audio transmission over
the Internet. It is designed by the IETF Codec Working Group and incorporates
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --disable-silent-rules \
  --disable-doc \
  --enable-custom-modes
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libopus%{sover}

%files -n libopus%{sover}
%license COPYING
%{_libdir}/libopus.so.%{sover}*

%files -n libopus-devel
%license COPYING
%doc AUTHORS README
%{_libdir}/libopus.so
%{_includedir}/opus
%{_libdir}/pkgconfig/opus.pc
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/opus.m4

%changelog
