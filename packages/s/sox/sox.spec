#
# spec file for package sox
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


%define soname 3
Name:           sox
Version:        14.4.2
Release:        0
Summary:        Sound Conversion Tools
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://sox.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/sox/sox/%{version}/%{name}-%{version}.tar.bz2
Patch0:         CVE-2017-11332.patch
Patch1:         CVE-2017-11359.patch
Patch2:         CVE-2017-15371.patch
Patch3:         CVE-2017-15642.patch
Patch4:         CVE-2017-11358.patch
Patch5:         CVE-2017-15370.patch
Patch6:         CVE-2017-15372.patch
Patch7:         CVE-2017-18189.patch
BuildRequires:  ladspa-devel
BuildRequires:  libgsm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libmp3lame)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opencore-amrnb)
BuildRequires:  pkgconfig(opencore-amrwb)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)

%description
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

%package -n libsox%{soname}
Summary:        Sound Conversion Library

%description -n libsox%{soname}
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

%package devel
Summary:        Sound Conversion Tools and Library
Requires:       libsox%{soname} = %{version}

%description devel
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

%prep
%autosetup -p1

%build
%configure \
  --without-oss \
  --disable-static \
  --with-distro=openSUSE
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libsox%{soname}

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/sox
%{_bindir}/play
%{_bindir}/rec
%{_bindir}/soxi
%{_mandir}/man1/play.1%{?ext_man}
%{_mandir}/man1/rec.1%{?ext_man}
%{_mandir}/man1/sox.1%{?ext_man}
%{_mandir}/man1/soxi.1%{?ext_man}
%{_mandir}/man7/soxeffect.7%{?ext_man}
%{_mandir}/man7/soxformat.7%{?ext_man}

%files -n libsox%{soname}
%license COPYING
%{_libdir}/libsox.so.%{soname}*

%files devel
%{_includedir}/*
%{_libdir}/libsox.so
%{_libdir}/pkgconfig/sox.pc
%{_mandir}/man3/libsox.3%{?ext_man}

%changelog
