#
# spec file for package gpu-screen-recorder-gtk
#
# Copyright (c) 2024 mantarimay
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


%bcond_with test
%define appid   com.dec05eba.gpu_screen_recorder
Name:           gpu-screen-recorder-gtk
Version:        20241105
Release:        0
Summary:        GTK frontend for GPU Screen Recorder
License:        GPL-3.0-only
URL:            https://git.dec05eba.com/gpu-screen-recorder-gtk/about
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  libayatana-appindicator3-devel
BuildRequires:  meson
BuildRequires:  zstd
Requires:       gpu-screen-recorder

%description
This is a screen recorder that has minimal impact on system performance
by recording your monitor using the GPU only, similar to shadowplay on
windows. This is the fastest screen recording tool for Linux.

This screen recorder can be used for recording your desktop offline, for
live streaming and for nvidia shadowplay-like instant replay, where only
the last few minutes are saved.

GTK frontend for GPU Screen Recorder.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%fdupes %{buildroot}%{_datadir}/icons

%if %{with test}
%check
%meson_test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/*/%{appid}*.png
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.appdata.xml

%changelog
