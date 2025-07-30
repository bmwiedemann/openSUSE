#
# spec file for package faad2
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020 Packman Team <packman@links2linux.de>
# Copyright (c) 2005-2020 Manfred Tremmel <Manfred.Tremmel@iiv.de>
# Copyright (c) 2004-2005 Rainer Lay <rainer@links2linux.de>
# Copyright (c) 2003 Henne Vogelsang <henne@links2linux.de>
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


%define so_version  2
%define so_name     libfaad%so_version
%define so_name_drm libfaad_drm%so_version
Name:           faad2
Version:        2.11.2
Release:        0
Summary:        Freeware Advanced Audio (AAC) Decoder including SBR decoding
License:        GPL-2.0-or-later
URL:            https://github.com/knik0/faad2
Source0:        %name-%version.tar.zst
Source99:       baselibs.conf

BuildRequires:  cmake >= 3.15
BuildRequires:  pkgconfig
Requires:       %so_name = %version

%description
FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder.
FAAD2 includes code for SBR (HE AAC) decoding.

%package -n %so_name
Summary:        Shared library part of faad2

%description -n %so_name
FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder.
FAAD2 includes code for SBR (HE AAC) decoding.

%package -n %so_name_drm
Summary:        DRM shared library part of faad2

%description -n %so_name_drm
FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder.
FAAD2 includes code for SBR (HE AAC) decoding.
The shared library part of faad2-drm

%package devel
Summary:        Development files of the FAAD 2 AAC decoder
Requires:       %so_name = %version
Requires:       %so_name_drm = %version
Obsoletes:      libfaad2-devel < %version
Provides:       libfaad2-devel = %version
Obsoletes:      libfaad-devel < %version
Provides:       libfaad-devel = %version

%description devel
FAAD2 is a HE, LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder.
FAAD2 includes code for SBR (HE AAC) decoding.
Header files and development documentation for libfaad.

%prep
%autosetup -p1

%build
CFLAGS='%optflags -DBUILD_DATE=\"\"'
%cmake
%cmake_build

%install
%cmake_install
install -m 0755 -d %{buildroot}%{_mandir}/man3
install -D -m 644 docs/libfaad.3 -t %{buildroot}%{_mandir}/man3/

%ldconfig_scriptlets -n %so_name
%ldconfig_scriptlets -n %so_name_drm

%files
%doc ChangeLog
%license COPYING
%_bindir/faad
%_mandir/man1/faad.1%{?ext_man}

%files -n %so_name
%_libdir/libfaad.so.%so_version
%_libdir/libfaad.so.%so_version.*

%files -n %so_name_drm
%_libdir/libfaad_drm.so.%so_version
%_libdir/libfaad_drm.so.%so_version.*

%files devel
%_includedir/faad.h
%_includedir/neaacdec.h
%_libdir/libfaad.so
%_libdir/libfaad_drm.so
%_libdir/pkgconfig/%name.pc
%{_mandir}/man3/libfaad.3*

%changelog
