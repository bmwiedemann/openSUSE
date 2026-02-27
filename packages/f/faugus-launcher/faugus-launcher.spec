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


%{?sle15_python_module_pythons}

# Fixes for Leap 15.x
%if 0%{?sle_version} == 150600
# Force python3_sitelib to use 3.11
%global __python3 /usr/bin/python3.11
%global python3_sitelib /usr/lib/python3.11/site-packages
%endif

Name:           faugus-launcher
Version:        1.15.8
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
%if "%{version}" <= "1.15.2"
Requires:       %{python_module filelock}
%endif
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

# Fix for shebangs
sed -i '1s|/usr/bin/env python3|%{__python3}|' faugus_launcher.py
sed -i '1s|/usr/bin/env python3|%{__python3}|' faugus_run.py
sed -i '1s|/usr/bin/env python3|%{__python3}|' faugus_proton_manager.py
sed -i '1s|/usr/bin/env python3|%{__python3}|' faugus/proton_downloader.py

# Fix for non-executable scripts on older versions than 1.14.2
%if "%{version}" <= "1.14.1"
sed -i '1{/^#!.*python/d}' faugus/components.py
sed -i '1{/^#!.*python/d}' faugus/path_manager.py
sed -i '1{/^#!.*python/d}' faugus/proton_downloader.py
%endif

%build
# Compile faugus-launcher
%meson
%meson_build

%install
# Install faugus-launcher
%meson_install

# Fix bytecode mtime for SLE 15 / SLE 16 / Leap 15.x / Leap 16.x / Tumbleweed / Slowroll
%if 0%{?sle_version} == 150600
find %{buildroot}%{python3_sitelib} -name "*.pyc" -delete
find %{buildroot}%{python3_sitelib} -name "*.py" -exec touch -d "1970-01-01 00:00:03" {} +
%{__python3} -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/faugus/
%else
find %{buildroot}%{python3_sitelib} -name "*.pyc" -delete
%{__python3} -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/faugus/
%endif

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
%{_bindir}/faugus-proton-manager
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
