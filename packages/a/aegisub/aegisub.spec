#
# spec file for package aegisub
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


%define _rev 524c6114a82157b143567240884de3a6d030b091
%define gitname Aegisub

Name:           aegisub
Version:        3.2.2+git20180710
Release:        0
Summary:        Subtitle editor
License:        BSD-3-Clause
Url:            http://www.aegisub.org/
Source0:        https://github.com/Aegisub/Aegisub/archive/%{_rev}.tar.gz#/aegisub-%{version}.tar.gz
Source99:       changelog.txt
Patch1:         Makefile.inc.in.patch
Patch2:         remove-vendor-luajit-dependency.patch
Patch3:         aegisub-no-optimize.patch
Patch4:         luabins.patch
#PATCH-FIX-OPENSUSE - davejplater@gmail.com - aegisub-git-version.patch - Create git_version.h which is missing in git.
Patch5:         aegisub-git-version.patch
#PATCH-FIX-UPSTREAM - 9@cirno.systems - aegisub-DataBlockCache-Fix-crash-in-cache-invalidation.patch - Fixes undefined behavior e.g. when scrolling the audio view in spectrogram mode.
Patch6:         aegisub-DataBlockCache-Fix-crash-in-cache-invalidation.patch
#PATCH-FIX-UPSTREAM - davejplater@gmail.com - aegisub-boost169.patch - Fixes build with boost 1.69 where boost/gil/gil_all.hpp is moved to -boost169.patch
Patch7:         aegisub-boost169.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  lua51
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3) >= 3.3
BuildRequires:  pkgconfig(fontconfig) >= 2.4
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(hunspell) >= 1.2.0
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse) >= 0.5
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    ppc ppc64 ppc64le i586

%description
Aegisub is a subtitle editor. It works with the Advanced SubStation
Alpha format (aptly abbreviated ASS) which allows for many advanced
effects in the subtitles, apart from just basic timed text.

%prep
%setup -q -n %{gitname}-%{_rev}
%autopatch -p1

%build
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/version.cpp
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/version.cpp
cp %{SOURCE99} .

./autogen.sh
#autoreconf -fvi
%configure \
    --disable-update-checker \
    --with-player-audio=PulseAudio \
    --without-oss
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%defattr(0644, root, root, 0755)
%license LICENCE
%doc README.md changelog.txt
%attr(0755,root,root) %{_bindir}/aegisub
%{_datadir}/aegisub/
%{_datadir}/applications/aegisub.desktop
%{_datadir}/icons/hicolor/*/apps/aegisub.*

%changelog
