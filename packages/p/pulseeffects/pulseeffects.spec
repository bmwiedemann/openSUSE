#
# spec file for package pulseeffects
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


Name:           pulseeffects
Version:        4.8.2
Release:        0
Summary:        Audio effects for Pulseaudio applications
License:        GPL-3.0-or-later
URL:            https://github.com/wwmm/pulseeffects
Source0:        https://github.com/wwmm/pulseeffects/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  libboost_filesystem-devel >= 1.72
BuildRequires:  libboost_system-devel >= 1.72
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zita-convolver-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.2.4
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
Requires:       dconf
Requires:       gstreamer-plugins-bad >= 1.12.5
Requires:       gstreamer-plugins-good >= 1.12.5
Requires:       ladspa-swh-plugins
Requires:       pulseaudio
Recommends:     %{name}-lang
Recommends:     ladspa-zam-plugins
Recommends:     lv2-calf >= 0.90.1
Recommends:     lv2-lsp-plugins
Recommends:     rubberband-ladspa

%description
PulseEffects is a limiter, compressor, reverberation, stereo equalizer and auto volume
effects for Pulseaudio applications.

%lang_package

%prep
%setup -q
# we don't need this
sed -i '/^meson.add_install_script/d' meson.build

%build
%meson
%meson_build

%install
%meson_install

%suse_update_desktop_file -r com.github.wwmm.pulseeffects "GTK;AudioVideo;Audio;Mixer;"

%find_lang pulseeffects

%files lang -f pulseeffects.lang
%exclude %{_datadir}/help/C/%{name}

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.wwmm.%{name}.desktop
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service
%{_datadir}/help/C/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/glib-2.0/schemas/com.github.wwmm.%{name}.*.xml
%{_datadir}/metainfo/com.github.wwmm.%{name}.appdata.xml
%{_libdir}/gstreamer-1.0/libgstpeadapter.so
%{_libdir}/gstreamer-1.0/libgstpeautogain.so
%{_libdir}/gstreamer-1.0/libgstpeconvolver.so
%{_libdir}/gstreamer-1.0/libgstpecrystalizer.so

%changelog
