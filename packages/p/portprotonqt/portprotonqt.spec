#
# spec file for package portprotonqt
#
# Copyright (c) 2026 SUSE LLC
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
#
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
%define bash_completions_dir %{_datadir}/bash-completion/completions
%define fish_completions_dir %{_datadir}/fish/vendor_completions.d
%define zsh_completions_dir  %{_datadir}/zsh/site-functions
%define _metainfodir         %{_datadir}/metainfo
%global pypi_name portprotonqt
%global pypi_version 1.4.1
%global oname PortProtonQt
%global _python_no_extras_requires 1

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        0
Summary:        GUI for managing and launching games from PortProton and Steam
#Source URL     https://git.linux-gaming.ru/Linux-Gaming/PortProtonQt/archive/v%%{pypi_version}
Source0:        %{oname}-v%{pypi_version}.tar.gz
License:        GPL-3.0
URL:            https://git.linux-gaming.ru/Linux-Gaming/PortProtonQt
ExclusiveArch:  x86_64 

BuildRequires:  meson 
BuildRequires:  ninja
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
BuildRequires:  vulkan-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  bash-completion
BuildRequires:  zsh
BuildRequires:  fish
BuildRequires:  fdupes

Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
Provides:       python3-%{pypi_name} = %{version}-%{release}

Requires:       python3-Babel
Requires:       python3-evdev
Requires:       python3-websocket-client
Requires:       python3-orjson
Requires:       python3-psutil
Requires:       python3-pyside6
Requires:       python3-requests
Requires:       python3-tqdm
Requires:       python3-vdf
Requires:       python3-pefile
Requires:       python3-Pillow
Requires:       python3-rapidfuzz
Requires:       python3-libarchive-c
Requires:       perl-Image-ExifTool
Requires:       qt6-multimedia
Requires:       qt6-imageformats
Requires:       cabextract
Requires:       gzip
Requires:       unzip
Requires:       curl
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       tar
Requires:       xz
Requires:       zstd
Requires:       unrar
Requires:       Mesa-demo-x
Requires:       pciutils
Requires:       procps
Requires:       psmisc
Requires:       7zip
Requires:       python3-dbus_fast

Recommends:     NetworkManager
Recommends:     bluez
Recommends:     upower
Recommends:     pulseaudio-utils
Recommends:     python3-qrcode
Recommends:     squashfs

%description
A GUI for managing and launching games from PortProton and Steam. Combines libraries in one place and simplifies running Windows games on Linux.

%package        bash-completion
Summary:        Bash Completion for %{pypi_name}      
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
Requires:       portprotonqt
Requires:       bash
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{pypi_name}.

%package        fish-completion
Summary:        Fish Completion for %{pypi_name}      
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
Requires:       portprotonqt
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{pypi_name}.

%package        zsh-completion
Summary:        Zsh Completion for %{pypi_name}      
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
Requires:       portprotonqt
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{pypi_name}.



%{?python_disable_dependency_generator}

%prep
%autosetup -n portprotonqt

%build
%meson \
    -Dpython_purelibdir=%{python3_sitelib} \
    -Dudev_rulesdir=%{_udevrulesdir}
%meson_build

%install
%meson_install
bash ./dev-scripts/generate-completions.sh
install -Dpm 0644 ./completions/portprotonqt -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 ./completions/portprotonqt.fish -t %{buildroot}%{fish_completions_dir}
install -Dpm 0644 ./completions/_portprotonqt -t %{buildroot}%{zsh_completions_dir}

chmod -x %{buildroot}%{_datadir}/portproton/conf/*.conf
chmod -x %{buildroot}%{_datadir}/portproton/scripts/thanks

find %{buildroot}%{_datadir}/portproton/scripts -type f -exec sed -i 's|#!/usr/bin/env bash|#!/usr/bin/bash|g' {} +
find %{buildroot}%{_datadir}/portproton/scripts -type f -exec sed -i 's|#!/usr/bin/env sh|#!/usr/bin/sh|g' {} +
find %{buildroot} -type f -name "vk_gpu_info" -exec strip --strip-unneeded {} +
find %{buildroot}%{python3_sitelib}/%{pypi_name} -type f -name "libportprotonqt_gamepad.so" -exec strip --strip-unneeded {} +

sed -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/portprotonqt/scripts_utils/easyterm.py
sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|g' %{buildroot}%{_bindir}/portprotonqt
sed -i 's|Categories=Game;Utility;|Categories=Game;Amusement;|g' %{buildroot}%{_datadir}/applications/ru.linux_gaming.PortProtonQt.desktop

%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_datadir}

%find_lang %{pypi_name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/ru.linux_gaming.PortProtonQt.desktop
%meson_test

%files -f %{pypi_name}.lang
%license LICENSE
%doc README.md README.ru.md CHANGELOG.md
%{_bindir}/%{pypi_name}
%{_bindir}/vk_gpu_info
%{python3_sitelib}/%{pypi_name}/
%{_datadir}/icons/hicolor/scalable/apps/ru.linux_gaming.PortProtonQt.svg
%{_sysusersdir}/portprotonqt.conf
%{_metainfodir}/ru.linux_gaming.PortProtonQt.metainfo.xml
%{_udevrulesdir}/60-portprotonqt.rules
%dir %attr(0555,root,root) %{_datadir}/polkit-1/rules.d
%{_datadir}/polkit-1/rules.d/ru.linux_gaming.PortProtonQt.rules
%{_datadir}/applications/ru.linux_gaming.PortProtonQt.desktop
%{_datadir}/applications/ru.linux_gaming.PortProtonQt.log.desktop
%{_datadir}/applications/ru.linux_gaming.PortProtonQt.silent.desktop
%{_datadir}/mime/packages/ru.linux_gaming.PortProtonQt.xml
%dir %{_datadir}/portproton
%{_datadir}/portproton/*

%files bash-completion
%{bash_completions_dir}/portprotonqt

%files fish-completion
%{fish_completions_dir}/portprotonqt.fish

%files zsh-completion
%{zsh_completions_dir}/_portprotonqt

%changelog
