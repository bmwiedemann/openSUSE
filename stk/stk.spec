#
# spec file for package stk
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without distributable

%define soname 4

Name:           stk
Version:        4.5.0
Release:        0
Summary:        Synthesis ToolKit in C++
License:        MIT
Group:          System/Libraries
Url:            http://ccrma.stanford.edu/software/stk/
%if %{with distributable}
Source0:        stk-%{version}-crippled.tar.gz
%else
Source0:        http://ccrma.stanford.edu/software/stk/release/stk-%{version}.tar.gz
%endif
Source1:        precheckin_cripple_tarball.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)

%description
The Synthesis ToolKit in C++ (STK) is a set of open source audio
signal processing and algorithmic synthesis classes written in the C++
programming language. STK was designed to facilitate rapid development
of music synthesis and audio processing software, with an emphasis on
cross-platform functionality, realtime control, ease of use, and
educational example code. The Synthesis ToolKit is extremely portable
(it's mostly platform-independent C and C++ code), and it's completely
user-extensible (all source included, no unusual libraries, and no
hidden drivers). We like to think that this increases the chances that
our programs will still work in another 5-10 years. In fact, the
ToolKit has been working continuously for about 10 years now. STK
currently runs with realtime support (audio and MIDI) on Linux,
Macintosh OS X, and Windows computer platforms. Generic, non-realtime
support has been tested under NeXTStep, Sun, and other platforms and
should work with any standard C++ compiler.

%package -n libstk%{soname}
Summary:        Synthesis ToolKit in C++
Group:          System/Libraries

%description -n libstk%{soname}
The Synthesis ToolKit in C++ (STK) is a set of open source audio
signal processing and algorithmic synthesis classes written in the C++
programming language. STK was designed to facilitate rapid development
of music synthesis and audio processing software, with an emphasis on
cross-platform functionality, realtime control, ease of use, and
educational example code. The Synthesis ToolKit is extremely portable
(it's mostly platform-independent C and C++ code), and it's completely
user-extensible (all source included, no unusual libraries, and no
hidden drivers). We like to think that this increases the chances that
our programs will still work in another 5-10 years. In fact, the
ToolKit has been working continuously for about 10 years now. STK
currently runs with realtime support (audio and MIDI) on Linux,
Macintosh OS X, and Windows computer platforms. Generic, non-realtime
support has been tested under NeXTStep, Sun, and other platforms and
should work with any standard C++ compiler.

%package -n libstk-devel
Summary:        Development files for stk
Group:          Development/Libraries/C and C++
Requires:       libstk%{soname} = %{version}

%description -n libstk-devel
The libstk-devel package contains libraries and header files for
developing applications that use stk.

%prep
%setup0 -q
%if 0%{?suse_version} >= 1220
#This is needed as apcupsd doesn't recognize ppc64 correctly
cp /usr/share/automake-*/config.* config/ 
%endif
sed -i 's/CXXFLAGS="$cxxflag"/CXXFLAGS="$CXXFLAGS $cxxflag"/' configure

%build
# I don't version the rawwaves directory because apps seems to expect it this way
%configure --prefix=/ --with-jack --with-alsa \
           RAWWAVE_PATH=%{_datadir}/stk/rawwaves/
make %{?_smp_mflags} -C src

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/stk/rawwaves/
cp -p rawwaves/*.raw %{buildroot}%{_datadir}/stk/rawwaves/

%post -n libstk%{soname} -p /sbin/ldconfig

%postun -n libstk%{soname} -p /sbin/ldconfig

%files -n libstk%{soname}
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_libdir}/libstk.so.%{soname}*
# If it's not going to be versioned SLPP doesn't really matter. WTF!! I don't really know if they correctly version the library since they ignored my message in the mailing list...
%{_datadir}/stk

%files -n libstk-devel
%defattr(-,root,root,-)
%doc doc/*
%{_libdir}/libstk.so
%{_includedir}/stk

%changelog
