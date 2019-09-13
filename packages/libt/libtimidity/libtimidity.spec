#
# spec file for package libtimidity
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


%define sover 2

Name:           libtimidity
Version:        0.2.2
Release:        0
Summary:        MIDI to WAVE converter library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://libtimidity.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkg-config

%description
This library is based on the TiMidity decoder from SDL_sound library.
Purpose to create this library is to avoid unnecessary dependences.
SDL_sound requires SDL and some other libraries, that not needed to
process MIDI files. In addition libtimidity provides more suitable
API to work with MIDI songs, it enables to specify full path to the
timidity configuration file, and have function to retrieve meta data
from MIDI song.

%package -n libtimidity%{sover}
Summary:        MIDI to WAVE converter library
Group:          System/Libraries

%description -n libtimidity%{sover}
This library is based on the TiMidity decoder from SDL_sound library.
Purpose to create this library is to avoid unnecessary dependences.
SDL_sound requires SDL and some other libraries, that not needed to
process MIDI files. In addition libtimidity provides more suitable
API to work with MIDI songs, it enables to specify full path to the
timidity configuration file, and have function to retrieve meta data
from MIDI song.

%package        devel
Summary:        MIDI to WAVE converter library - Development Files
Group:          Development/Libraries/C and C++
Requires:       libtimidity%{sover} = %{version}

%description    devel
This library is based on the TiMidity decoder from SDL_sound library.
Purpose to create this library is to avoid unnecessary dependences.
SDL_sound requires SDL and some other libraries, that not needed to
process MIDI files. In addition libtimidity provides more suitable
API to work with MIDI songs, it enables to specify full path to the
timidity configuration file, and have function to retrieve meta data
from MIDI song.

%prep
%setup -q

%build
%configure --help
%configure \
	--with-timidity-cfg=timidity.cfg \
	--disable-ao \
	--disable-aotest \
	--disable-static
%__make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%clean
rm -rf %{buildroot}

%post -n libtimidity%{sover} -p /sbin/ldconfig

%postun -n libtimidity%{sover} -p /sbin/ldconfig

%files -n libtimidity%{sover}
%defattr(-,root,root,-)
%doc AUTHORS CHANGES COPYING README*
%{_libdir}/libtimidity*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/timidity.h
%{_libdir}/libtimidity*.so
%{_libdir}/pkgconfig/libtimidity.pc

%changelog
