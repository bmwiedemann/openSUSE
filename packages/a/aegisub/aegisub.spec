#
# spec file for package aegisub
#
# Copyright (c) 2020 SUSE LLC
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


Name:           aegisub
Version:        3.2.2+git20191006
Release:        0
Summary:        Subtitle editor
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.aegisub.org/
Source0:        %{name}-%{version}.tar.xz
Source99:       changelog.txt
Source100:      %{name}-rpmlintrc
Patch1:         Makefile.inc.in.patch
Patch2:         remove-vendor-luajit-dependency.patch
Patch3:         aegisub-no-optimize.patch
Patch4:         luaL_Reg-not-luaL_reg.patch
#luabins.patch
# PATCH-FIX-UPSTREAM aegisub-fix_build_with_make4.3.patch
Patch8:         aegisub-fix_build_with_make4.3.patch
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
BuildRequires:  wxGTK3-3_2-devel
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
%autosetup -p1
cp %{SOURCE99} .

%build
autoreconf -fiv
%configure \
    --disable-update-checker \
    --with-player-audio=PulseAudio \
    --without-oss
%make_build

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
%{_datadir}/metainfo/aegisub.appdata.xml

%changelog
