#
# spec file for package aegisub
#
# Copyright (c) 2021 SUSE LLC
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


%define version_split 3,3,2
Name:           aegisub
Version:        3.3.2
Release:        0
Summary:        Subtitle editor
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.aegisub.org/
Source0:        https://github.com/wangqr/Aegisub/archive/refs/tags/v3.3.2.tar.gz#/Aegisub-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM ax_boost-files.patch -- https://github.com/wangqr/Aegisub/pull/102
Patch0:         ax_boost-files.patch
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
ExcludeArch:    ppc ppc64 ppc64le

%description
Aegisub is a subtitle editor. It works with the Advanced SubStation
Alpha format (aptly abbreviated ASS) which allows for many advanced
effects in the subtitles, apart from just basic timed text.

As upstream is orphaned, this version is the wangqr fork.

%prep
%autosetup -p1 -n Aegisub-%{version}
# Add "cached" version (as we do not build from git)
[ -f "build/version.h" ] || cat > build/git_version.h << EOF
#define BUILD_GIT_VERSION_NUMBER 0
#define BUILD_GIT_VERSION_STRING "%{version}"
#define TAGGED_RELEASE 1
#define INSTALLER_VERSION "%{version}"
#define RESOURCE_BASE_VERSION %{version_split}
EOF

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
%license LICENCE
%doc README.md
%{_bindir}/aegisub
%{_datadir}/aegisub/
%{_datadir}/applications/aegisub.desktop
%{_datadir}/icons/hicolor/*/apps/aegisub.*
%{_datadir}/metainfo/aegisub.appdata.xml

%changelog
