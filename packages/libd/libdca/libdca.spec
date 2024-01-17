#
# spec file for package libdca
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


%define sover 0

Name:           libdca
Version:        0.0.7+2
Release:        0
Summary:        DTS Coherent Acoustics decoder library
License:        GPL-2.0-or-later
URL:            https://www.videolan.org/developers/libdca.html
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  c_compiler
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libdca is a free library for decoding DTS Coherent Acoustics
streams. It is released under the terms of the GPL license. The DTS
Coherent Acoustics standard is used in a variety of applications,
including DVD, DTS audio CD and radio broadcasting.

%package -n libdca%{sover}
Summary:        DTS Coherent Acoustics decoder library

%description -n libdca%{sover}
libdca is a free library for decoding DTS Coherent Acoustics
streams. It is released under the terms of the GPL license. The DTS
Coherent Acoustics standard is used in a variety of applications,
including DVD, DTS audio CD and radio broadcasting.

This package contains the library for decoding DTS Coherent
Acoustics streams.

%package -n dcatools
Summary:        Free DTS Coherent Acoustics decoder tools

%description -n dcatools
libdca is a free library for decoding DTS Coherent Acoustics
streams. It is released under the terms of the GPL license. The DTS
Coherent Acoustics standard is used in a variety of applications,
including DVD, DTS audio CD and radio broadcasting.

This package contains tools for decoding DTS Coherent Acoustics
streams.

%package devel
Summary:        Header files for the libdca library
Requires:       libdca%{sover} = %{version}

%description devel
libdca is a free library for decoding DTS Coherent Acoustics
streams. It is released under the terms of the GPL license. The DTS
Coherent Acoustics standard is used in a variety of applications,
including DVD, DTS audio CD and radio broadcasting.

This package contains header files and static library for the
libdca library. Install this package if you want to compile
programs using the library.

%prep
%autosetup -p1

%build
./bootstrap
%configure \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -f
%fdupes -s %{buildroot}%{_bindir}

%ldconfig_scriptlets -n libdca%{sover}

%files -n libdca%{sover}
%doc COPYING
%{_libdir}/%{name}.so.*

%files -n dcatools
%{_bindir}/dcadec
%{_bindir}/dtsdec
%{_bindir}/extract_dca
%{_bindir}/extract_dts
%{_mandir}/man?/dcadec.?%{ext_man}
%{_mandir}/man?/dtsdec.?%{ext_man}
%{_mandir}/man?/extract_dca.?%{ext_man}
%{_mandir}/man?/extract_dts.?%{ext_man}

%files devel
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/dca.h
%{_includedir}/dts.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libdca.pc
%{_libdir}/pkgconfig/libdts.pc

%changelog
