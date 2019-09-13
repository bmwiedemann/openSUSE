#
# spec file for package sox
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


%define soname 3

%bcond_with amrwb
%bcond_with amrnb

Name:           sox
BuildRequires:  file-devel
BuildRequires:  ladspa-devel
BuildRequires:  libgsm-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
%if %{with amrnb}
BuildRequires:  pkgconfig(opencore-amrnb)
%endif
%if %{with amrwb}
BuildRequires:  pkgconfig(opencore-amrwb)
%endif
BuildRequires:  libtool
BuildRequires:  pkgconfig(twolame)
Version:        14.4.2
Release:        0
Summary:        Sound Conversion Tools
License:        LGPL-2.1+ and GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Url:            http://sox.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/sox/sox/%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.changes
Patch0:         CVE-2017-11332.patch  
Patch1:         CVE-2017-11359.patch  
Patch2:         CVE-2017-15371.patch 
Patch3:         CVE-2017-15642.patch 
Patch4:         CVE-2017-11358.patch 
Patch5:         CVE-2017-15370.patch 
Patch6:         CVE-2017-15372.patch
Patch7:         CVE-2017-18189.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

%package -n libsox%{soname}
Summary:        Sound Conversion Library
Group:          System/Libraries

%description -n libsox%{soname}
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

%package devel
Summary:        Sound Conversion Tools and Library
Group:          Development/Libraries/C and C++
Requires:       libsox%{soname} = %{version}

%description devel
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' | xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
%configure \
  --without-oss \
  --disable-static \
  --with-distro=openSUSE
make %{?_smp_mflags} V=1

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/sox/*.la

%post -n libsox%{soname} -p /sbin/ldconfig

%postun -n libsox%{soname} -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README src/monkey.wav
%attr(0755,root,root) %{_bindir}/sox
%{_bindir}/play
%{_bindir}/rec
%{_bindir}/soxi
%{_mandir}/man1/*
%{_mandir}/man7/*

%files -n libsox%{soname}
%defattr(0644,root,root,0755)
%{_libdir}/libsox.so.%{soname}*

%files devel
%defattr(0644,root,root,0755)
%{_includedir}/*
%{_libdir}/libsox.so
%{_libdir}/pkgconfig/sox.pc
%{_mandir}/man3/libsox.3*

%changelog
