#
# spec file for package aegisub
#
# Copyright (c) 2025 mantarimay
# Copyright (c) 2025 SUSE LLC and contributors
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


%define appid org.aegisub.Aegisub
%define luajit_gitver LuaJIT-04dca7911ea255f37be799c18d74c305b921c1a6
%define luajit_ver 2.1.1720049189
Name:           aegisub
Version:        3.5.1
Release:        0
Summary:        Subtitle editor
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www.aegisub.org/
Source0:        https://github.com/TypesettingTools/Aegisub/archive/v%{version}/Aegisub-%{version}.tar.gz
Source1:        https://github.com/mesonbuild/wrapdb/releases/download/luajit_%{luajit_ver}-2/luajit-%{luajit_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v2/luajit_%{luajit_ver}-2/get_patch#/luajit_%{luajit_ver}-2_patch.zip
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_container-devel
BuildRequires:  libboost_filesystem-devel >= 1.70.0
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libicu-devel
BuildRequires:  meson
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  unzip
BuildRequires:  wxGTK3-3_2-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3) >= 3.3
BuildRequires:  pkgconfig(fontconfig) >= 2.4
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(hunspell) >= 1.2.0
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(libpulse) >= 0.9.9
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    ppc64le

%description
Aegisub is a subtitle editor. It works with the Advanced SubStation
Alpha format (aptly abbreviated ASS) which allows for many advanced
effects in the subtitles, apart from just basic timed text.

%prep
%autosetup -p1 -n Aegisub-%{version}
%setup -n Aegisub-%{version} -DTa1
%setup -n Aegisub-%{version} -DTa2
cp -rf %{luajit_gitver} subprojects

sed "/subdir('tests')/d" -i meson.build

cat > git_version.h <<EOF
#define BUILD_GIT_VERSION_NUMBER 0
#define BUILD_GIT_VERSION_STRING "%{version}"
#define TAGGED_RELEASE 0
#define INSTALLER_VERSION "%{version}"
#define RESOURCE_BASE_VERSION 0, 0, 0
EOF

%build
%meson \
    -Davisynth=disabled \
    -Dluajit:default_library=static \
    -Db_lto=false \
    -Dtests=false \
    -Denable_update_checker=false
%meson_build

%install
%meson_install --skip-subprojects
%find_lang %{name}

%files -f %{name}.lang
%license LICENCE
%doc automation/autoload automation/demos/ automation/v4-docs/ README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appid}.*
%{_datadir}/metainfo/%{appid}.metainfo.xml
%exclude %{_datadir}/aegisub/automation

%changelog
