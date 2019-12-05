#
# spec file for package libtimidity
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 2
Name:           libtimidity
Version:        0.2.6
Release:        0
Summary:        MIDI to WAVE converter library
License:        LGPL-2.1-or-later
URL:            http://libtimidity.sourceforge.net/
Source0:        %{name}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig

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
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libtimidity%{sover} -p /sbin/ldconfig
%postun -n libtimidity%{sover} -p /sbin/ldconfig

%files -n libtimidity%{sover}
%license COPYING
%doc AUTHORS CHANGES README*
%{_libdir}/libtimidity*.so.*

%files devel
%{_includedir}/timidity.h
%{_libdir}/libtimidity*.so
%{_libdir}/pkgconfig/libtimidity.pc

%changelog
