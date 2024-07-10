#
# spec file for package libbs2b
#
# Copyright (c) 2024 SUSE LLC
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


%define soname 0
Name:           libbs2b
Version:        3.1.0
Release:        0
Summary:        The Bauer stereophonic-to-binaural DSP library
License:        MIT
Group:          System/Libraries
URL:            http://bs2b.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/bs2b/libbs2b/%{version}/libbs2b-%{version}.tar.bz2
Patch0:         libbs2b-security.patch
Patch1:         libbs2b-clipping.patch
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile)

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is designed to
improve headphone listening of stereo audio records. Recommended for headphone
prolonged listening to disable superstereo fatigue without essential
distortions.

%package -n libbs2b%{soname}
Summary:        The Bauer stereophonic-to-binaural DSP library
Group:          System/Libraries

%description -n libbs2b%{soname}
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is designed to
improve headphone listening of stereo audio records. Recommended for headphone
prolonged listening to disable superstereo fatigue without essential
distortions.

%package -n libbs2b-devel
Summary:        Development files for libbs2b
Group:          Development/Libraries/C and C++
Requires:       libbs2b%{soname} = %{version}

%description -n libbs2b-devel
Headers and libraries to program against libbs2b.

%package -n bs2b-tools
Summary:        Tools to use the Bauer stereophonic-to-binaural DSP
Group:          Productivity/Multimedia/Sound/Utilities

%description -n bs2b-tools
Tools (bs2bconvert and bs2bstream) to use the Bauer stereophonic-to-binaural
DSP.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f '%{buildroot}%{_libdir}/libbs2b.la'

%post -n libbs2b%{soname} -p /sbin/ldconfig
%postun -n libbs2b%{soname} -p /sbin/ldconfig

%files -n libbs2b%{soname}
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/libbs2b.so.%{soname}*

%files -n libbs2b-devel
%{_libdir}/libbs2b.so
%{_includedir}/bs2b
%{_libdir}/pkgconfig/libbs2b.pc

%files -n bs2b-tools
%{_bindir}/bs2bconvert
%{_bindir}/bs2bstream

%changelog
