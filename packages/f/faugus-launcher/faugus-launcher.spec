#
# spec file for package faugus-launcher
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?single_pythons_311plus}

Name:           faugus-launcher
Version:        1.18.2
Release:        0
Summary:        A simple and lightweight app for running Windows games using UMU-Launcher
License:        MIT
URL:            https://github.com/Faugus/faugus-launcher
Group:          System/Emulators/PC

# Get the source from tar_scm
Source0:        %{name}-%{version}.tar.xz
# Exclusions
Source1:        faugus-launcher.rpmlintrc

BuildArch:      noarch

# Faugus BuildDeps
BuildRequires:  meson
BuildRequires:  gtk4-tools
BuildRequires:  desktop-file-utils
BuildRequires:  appstream-glib

# To remove duplicated files
BuildRequires:  fdupes

# Python version management
BuildRequires:  python-rpm-macros

Requires:       ImageMagick
Requires:       canberra-gtk-play
Requires:       %{python_module base}
Requires:       %{python_module Pillow}
Requires:       (%{python_module filelock} if faugus-launcher <= 1.15.2)
Requires:       %{python_module gobject}
Requires:       %{python_module icoextract}
Requires:       %{python_module psutil}
Requires:       %{python_module requests}
Requires:       %{python_module vdf}
Requires:       typelib-1_0-AyatanaAppIndicator3-0_1

# Only install gaming selinux policy on SLE +16 / Leap +16 / Tumbleweed / Slowroll
%if 0%{?suse_version} >= 1600 || 0%{?is_opensuse}
Requires:       (selinux-policy-targeted-gaming if selinux-policy-targeted)
%endif

Recommends:     ca-certificates-steamtricks
Recommends:     gamemode%{?_isa}
Recommends:     gamescope
Recommends:     libvkd3d-utils1%{?_isa}
Recommends:     libvkd3d1%{?_isa}
Recommends:     mangohud%{?_isa}
Recommends:     ntsync-autoload
Recommends:     ntsync-autoload-udev-rules

Obsoletes:      faugus-launcher < %{version}

%description
A simple and lightweight app for running Windows games using UMU-Launcher/UMU-Proton.

# Lang subpackage
%lang_package

%prep
%autosetup -n %{name}-%{version}

# Fix for shebangs on current versions
sed -i '1{/^#!.*python/d}' faugus/launcher.py
sed -i '1{/^#!.*python/d}' faugus/proton_manager.py
sed -i '1{/^#!.*python/d}' faugus/runner.py
sed -i '1{/^#!.*python/d}' faugus/shortcut.py
sed -i '1s|#!/usr/bin/env python3|#!%{__python3}|' faugus/proton_downloader.py
sed -i '1s|#!/usr/bin/env bash|#!/usr/bin/bash|' faugus-launcher

%build
# Compile faugus-launcher
%meson
%meson_build

%install
# Install faugus-launcher
%meson_install

# Fix bytecode mtime for SLE 16 / Leap 16.x / Tumbleweed / Slowroll
find %{buildroot}%{python3_sitelib} -name "*.pyc" -delete
%{__python3} -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/faugus/

# Remove duplicated files
%fdupes %{buildroot}%{_datadir}

# Lang files
%find_lang faugus-launcher %{name}.lang
%find_lang faugus-proton-manager faugus-proton-manager.lang
%find_lang faugus-run faugus-run.lang
cat faugus-proton-manager.lang faugus-run.lang >> %{name}.lang

%check
# Checks for desktop files and appstream metadata
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%license LICENSE

# Application data
%dir %{_datadir}/faugus-launcher
%{_datadir}/faugus-launcher/*

# Binaries
%{_bindir}/faugus-launcher
%{_bindir}/faugus-run

# Icons
%{_datadir}/icons/hicolor/*

# .desktop files
%{_datadir}/applications/*.desktop

# Metainfo
%{_datadir}/metainfo/faugus-launcher.metainfo.xml

# Python modules
%{python3_sitelib}/faugus/

# Language files for the subpackage
%files lang -f %{name}.lang

%changelog
