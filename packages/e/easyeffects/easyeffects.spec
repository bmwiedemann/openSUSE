#
# spec file for package easyeffects
#
# Copyright (c) 2025 SUSE LLC
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


Name:           easyeffects
Version:        7.2.3
Release:        0
Summary:        Audio effects for Pulseaudio applications
License:        GPL-3.0-or-later
URL:            https://github.com/wwmm/easyeffects
#Source0:        https://github.com/wwmm/easyeffects/archive/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  ladspa-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  update-desktop-files
BuildRequires:  zita-convolver-devel
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sigc++-3.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
Requires:       dconf
Recommends:     lv2-calf >= 0.90.1
Recommends:     lv2-lsp-plugins
Recommends:     lv2-zam-plugins

%description
Easyeffects is a limiter, compressor, reverberation, stereo equalizer and auto volume
effects for pipewire applications.

%package doc
Summary:        Documentation of Audio effects for pipewire applications
BuildArch:      noarch

%description doc
This package contains documentation of Audio effects for pipewire applications

%lang_package

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup
# we don't need this
sed -i '/^meson.add_install_script/d' meson.build

export QMAKE_CFLAGS_ISYSTEM=-I

%build
export CC=gcc
export CXX=g++
export LDFLAGS="${LDFLAGS} -fPIC -Wl,--gc-sections -Wl,-O1"
%meson \
            -Db_ndebug=true \
            -Dc_args="${CFLAGS}" \
            -Dcpp_args="${CXXFLAGS}" \
            || (cat */meson-logs/meson-log.txt; exit 1)
######## IDIOTIC WORKAROUND ####################
sed -i s/isystem/I/g $(gcc -dumpmachine)/*.json
sed -i s/isystem/I/g $(gcc -dumpmachine)/*.ninja
######## END OF IDIOTIC WORKAROUND #############

%meson_build

%install
%meson_install

%suse_update_desktop_file -r com.github.wwmm.easyeffects "GTK;AudioVideo;Audio;Mixer;"

%find_lang easyeffects

%files lang -f easyeffects.lang
%exclude %{_datadir}/help/*/%{name}
%{_datadir}/locale/*/LC_MESSAGES/easyeffects-news.mo

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service
%{_datadir}/icons/hicolor/scalable/apps/com.github.wwmm.easyeffects.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.wwmm.easyeffects-symbolic.svg
%{_datadir}/glib-2.0/schemas/com.github.wwmm.%{name}.*.xml
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml

%files doc
%license LICENSE
%doc CHANGELOG.md README.md
%{_datadir}/help/*/%{name}
%exclude %{_datadir}/locale/*

%changelog
