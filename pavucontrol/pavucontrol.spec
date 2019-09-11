#
# spec file for package pavucontrol
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


Name:           pavucontrol
Version:        4.0
Release:        0
Summary:        PulseAudio Volume Control
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://freedesktop.org/software/pulseaudio/pavucontrol/
Source:         https://freedesktop.org/software/pulseaudio/pavucontrol/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
# Only needed because we don't (and won't) support building xz tarballs by default... See bnc#697467
BuildRequires:  xz
BuildRequires:  pkgconfig(libpulse) >= 0.9.16
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 0.9.16
BuildRequires:  pkgconfig(sigc++-2.0)
Recommends:     %{name}-lang
BuildRequires:  pkgconfig(gtkmm-3.0) >= 2.99
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.16

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume
control tool ("mixer") for the PulseAudio sound server. In contrast to
classic mixer tools this one allows you to control both the volume of
hardware devices and of each playback stream separately.

%lang_package

%prep
%setup -q

%build
%configure --disable-lynx
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}

# This is documentation we prefer to have in the package doc directory
rm -r %{buildroot}%{_datadir}/doc/%{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license LICENSE
%doc doc/README doc/README.html doc/style.css
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files lang -f %{name}.lang

%changelog
