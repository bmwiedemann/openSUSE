#
# spec file for package lame
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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
Name:           lame
Version:        3.100
Release:        0
Summary:        The LAME MP3 encoder
License:        LGPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://lame.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/lame/lame-%{version}.tar.gz
Source99:       lame-rpmlintrc
Source1000:     baselibs.conf
Patch1:         lame-field-width-fix.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
Requires:       libmp3lame%{sover} >= %{version}
%{?suse_build_hwcaps_libs}
%ifarch %{ix86}
BuildRequires:  nasm
%endif

%description
LAME is an educational tool to be used for learning about MP3 encoding.
The goal of the LAME project is to use the open source model to improve the
psycho acoustics, noise shaping and speed of MP3.
Another goal of the LAME project is to use these improvements for the basis of
a patent free audio compression codec for the GNU project.

%package doc
Summary:        Documentation for the LAME MP3 encoder
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{name} = %{version}

%description doc
LAME is an encoder that converts audio to the MP3 file format. It has
an improved psychoacoustic model and performs well in codec listening
tests.

%package -n libmp3lame%{sover}
Summary:        The LAME MP3 encoder library
Group:          System/Libraries

%description -n libmp3lame%{sover}
LAME is an encoder that converts audio to the MP3 file format. It has
an improved psychoacoustic model and performs well in codec listening
tests.

%package -n libmp3lame-devel
Summary:        Development files for the LAME MP3 encoder
Group:          Development/Libraries/C and C++
Requires:       libmp3lame%{sover} = %{version}

%description -n libmp3lame-devel
Contains the header files for use with LAME's encoding library.

%package mp3rtp
Summary:        MP3 Encoder for RTP Streaming
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       libmp3lame%{sover} >= %{version}

%description mp3rtp
LAME is an encoder that converts audio to the MP3 file format. It has
an improved psychoacoustic model and performs well in codec listening
tests.

This package includes "mp3rtp", an MP3 encoder with RTP streaming of the output.

%prep
%autosetup -p1

%build
LIBS="-lm" \
CFLAGS="%{optflags}" \
%configure \
    --enable-nasm \
    --enable-decoder \
    --disable-debug \
    --enable-mp3rtp \
    --with-fileio=lame \
    --enable-dynamic-frontends \
    --disable-rpath \
    --disable-static

%make_build pkgdocdir=%{_defaultdocdir}/%{name}/

%check
%make_build test

%install
make install pkgdocdir=%{_defaultdocdir}/%{name}/ DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libmp3lame.la

#make package config file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/lame.pc
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/lame

Name:           lame
Description: encoder that converts audio to the MP3 file format.
Version:        %{version}
Libs: -L\${libdir} -lmp3lame
Cflags: -I\${includedir}
EOF
pushd %{buildroot}%{_libdir}/pkgconfig/
ln -s lame.pc libmp3lame.pc
popd

for f in ChangeLog README TODO USAGE; do
    install -m0644 "$f" "%{buildroot}%{_defaultdocdir}/%{name}/"
done

%post   -n libmp3lame%{sover} -p /sbin/ldconfig
%postun -n libmp3lame%{sover} -p /sbin/ldconfig

%files
%{_bindir}/lame
%{_mandir}/man1/lame.1%{?ext_man}

%files doc
%{_defaultdocdir}/%{name}

%files -n libmp3lame%{sover}
%license COPYING LICENSE
%{_libdir}/libmp3lame.so.%{sover}
%{_libdir}/libmp3lame.so.%{sover}.*

%files -n libmp3lame-devel
%doc API HACKING STYLEGUIDE
%{_includedir}/lame/
%{_libdir}/libmp3lame.so
%{_libdir}/pkgconfig/*pc

%files mp3rtp
%{_bindir}/mp3rtp

%changelog
