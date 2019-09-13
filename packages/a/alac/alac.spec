#
# spec file for package alac
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   0
Name:           alac
Version:        0.0+git.20160511
Release:        0
Summary:        Apple Lossless Audio Codec
License:        Apache-2.0
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Url:            https://macosforge.github.io/alac/
Source:         %{name}-%{version}.tar.xz
Patch1:         libalac-makefile.patch
Patch2:         alac-endian.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss of
information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

This package contains a command-line utility to convert the ALAC format.

%package -n lib%{name}%{sover}
Summary:        Apple Lossless Audio Codec
Group:          System/Libraries

%description -n lib%{name}%{sover}
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss of
information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package devel
Summary:        Apple Lossless Audio Codec
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Provides:       lib%{name}-devel = %{version}
Obsoletes:      lib%{name}-devel < %{version}

%description devel
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss of
information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%prep
%setup -q
%patch1
%patch2

%build
for d in codec convert-utility; do
    make -C "$d" \
        OPTFLAGS="%{optflags} -fvisibility-inlines-hidden -fno-strict-aliasing -D_GNU_SOURCE" \
        CC="g++"
done

%install
install -D -p -m 0755 convert-utility/alacconvert \
  %{buildroot}%{_bindir}/alacconvert

install -d %{buildroot}%{_includedir}
cp -a codec/*.h %{buildroot}%{_includedir}/

install -d %{buildroot}%{_libdir}
cp -a codec/libalac.so* %{buildroot}%{_libdir}/

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc codec/APPLE_LICENSE.txt LICENSE
%{_bindir}/alacconvert

%files -n lib%{name}%{sover}
%defattr(-,root,root)
%doc codec/APPLE_LICENSE.txt LICENSE
%{_libdir}/libalac.so.%{sover}*

%files devel
%defattr(-,root,root)
%doc codec/APPLE_LICENSE.txt LICENSE
%{_includedir}/*.h
%{_libdir}/libalac.so

%changelog
