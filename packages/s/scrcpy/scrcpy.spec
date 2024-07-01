#
# spec file for package scrcpy
#
# Copyright (c) 2024 SUSE LLC
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


Name:           scrcpy
Version:        2.5
Release:        0
Summary:        Display and control your Android device
License:        Apache-2.0
Group:          Hardware/Mobile
URL:            https://github.com/Genymobile/scrcpy
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/scrcpy-server-v%{version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.48
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sdl2)
Requires:       android-tools
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc11
BuildRequires:  gcc11-PIE
%else
BuildRequires:  gcc
%endif

%description
This application provides display and control of Android devices
connected on USB. It does not require any root access.

%package bash-completion
Summary:        Scrcpy Bash completion
BuildRequires:  bash-completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional dependency offering bash completion for scrcpy.

%package zsh-completion
Summary:        Scrcpy zsh completion
BuildRequires:  zsh
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Optional dependency offering zsh completion for scrcpy.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-11
%endif

%meson -Dprebuilt_server='%{SOURCE1}'
%meson_build

%install
%meson_install

%suse_update_desktop_file scrcpy Network
%suse_update_desktop_file scrcpy-console Network

%files
%license LICENSE
%doc README.md FAQ.md doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/scrcpy{,-console}.desktop
%{_datadir}/icons/hicolor/*/apps/scrcpy.png

%files bash-completion
%{_datadir}/bash-completion/completions/scrcpy

%files zsh-completion
%{_datadir}/zsh/site-functions/_scrcpy

%changelog
