#
# spec file for package portaudio
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname_c 2
%define soname_p 0

Name:           portaudio
Version:        190600_20161030
Release:        0
Summary:        Portable Real-Time Audio Library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.portaudio.com/
Source:         http://www.portaudio.com/archives/pa_stable_v%{version}.tgz
Source1:        baselibs.conf
Patch1:         0001-Merge-branch-ticket_275_pass_void-into-master.patch
%define lname_c	libportaudio%{soname_c}
%define lname_p	libportaudiocpp%{soname_p}
BuildRequires:  alsa-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(jack)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio
processing. Audio can be generated in various formats, including 32 bit
floating point, and will be converted to the native format internally.

%package -n %lname_c
Summary:        Portable Real-Time Audio Library
# portaudio was last used in openSUSE 12.1
Group:          System/Libraries
Provides:       portaudio = %{version}
Obsoletes:      portaudio < %{version}

%description -n %lname_c
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio
processing. Audio can be generated in various formats, including 32 bit
floating point, and will be converted to the native format internally.
%package -n %lname_p
Summary:        Portable Real-Time Audio Library
# packman used to provide this
Group:          System/Libraries
Obsoletes:      libportaudiocpp

%description -n %lname_p
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio
processing. Audio can be generated in various formats, including 32 bit
floating point, and will be converted to the native format internally.

%package devel
Summary:        Development package for the portaudio library
Group:          Development/Languages/C and C++
Requires:       %lname_c = %{version}
Requires:       %lname_p = %{version}
Obsoletes:      libportaudiocpp-devel

%description devel
This package contains the files needed to compile programs that use the
portaudio library.

%prep
%setup -q -n portaudio
%patch1 -p1
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')  
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" qa/loopback/src/paqa.c src/common/pa_front.c
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')  
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/" qa/loopback/src/paqa.c src/common/pa_front.c
echo 'HTML_TIMESTAMP=NO' >> Doxyfile
echo 'Requires: alsa' >> portaudio-2.0.pc.in

%build
%configure --disable-static \
           --enable-cxx=yes \
           --with-alsa=yes \
           --with-jack=yes \
           --with-oss=yes
make lib/libportaudio.la %{?_smp_mflags}
make %{?_smp_mflags}
doxygen

%install
make install DESTDIR=%{?buildroot}
rm -f %{buildroot}/%{_libdir}/*.la

%post -n %lname_c -p /sbin/ldconfig
%post -n %lname_p -p /sbin/ldconfig

%postun -n %lname_c -p /sbin/ldconfig
%postun -n %lname_p -p /sbin/ldconfig

%files -n %lname_c
%defattr(-,root,root)
%{_libdir}/libportaudio.so.%{soname_c}*
%files -n %lname_p
%defattr(-,root,root)
%{_libdir}/libportaudiocpp.so.%{soname_p}*

%files devel
%defattr(-,root,root)
%doc README.txt LICENSE.txt
%doc doc/html
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
