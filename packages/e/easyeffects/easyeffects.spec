#
# spec file for package easyeffects
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


%ifarch riscv64
%bcond_with gold
%else
%bcond_without gold
%endif

Name:           easyeffects
Version:        6.1.2+0~git.89063a4b
Release:        0
Summary:        Audio effects for Pulseaudio applications
License:        GPL-3.0-or-later
URL:            https://github.com/wwmm/easyeffects
#Source0:        https://github.com/wwmm/easyeffects/archive/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
%if %{with gold}
BuildRequires:  binutils-gold
%endif
BuildRequires:  cmake
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zita-convolver-devel
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtkmm-4.0) >= 4.0.0
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
Requires:       dconf
Requires:       gstreamer-plugins-bad >= 1.12.5
Requires:       gstreamer-plugins-good >= 1.12.5
Requires:       ladspa-swh-plugins
Recommends:     lv2-calf >= 0.90.1
Recommends:     lv2-lsp-plugins
Recommends:     lv2-zam-plugins
Recommends:     rubberband-ladspa

%description
PulseEffects is a limiter, compressor, reverberation, stereo equalizer and auto volume
effects for Pulseaudio applications.

%package doc
Summary:        Documentation of Audio effects for Pulseaudio applications

%description doc
This package contains documentation of Audio effects for Pulseaudio applications

%lang_package

%prep
%setup -q
# we don't need this
sed -i '/^meson.add_install_script/d' meson.build

%build
%if %{with gold}
export LD=ld.gold
alias ld=gold
%endif
export CC=gcc-10
export CXX=g++-10
export LDFLAGS="${LDFLAGS} -fPIC -Wl,--gc-sections -Wl,-O1"
%if %{with gold}
LDFLAGS+=" -fuse-ld=gold -Wl,--icf=safe"
%endif
%meson \
            -Db_ndebug=true \
            -Dc_args="${CFLAGS}" \
            -Dcpp_args="${CXXFLAGS}" \
            -Dld_args="${LDFLAGS}" \
            || (cat */meson-logs/meson-log.txt; exit 1)

%meson_build

%install
%meson_install

%suse_update_desktop_file -r com.github.wwmm.easyeffects "GTK;AudioVideo;Audio;Mixer;"

%find_lang easyeffects

%files lang -f easyeffects.lang
%exclude %{_datadir}/help/*/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.github.wwmm.%{name}.*.xml
%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml

%files doc
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_datadir}/help/*/%{name}

%changelog
