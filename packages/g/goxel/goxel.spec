#
# spec file for package goxel
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


Name:           goxel
Version:        0.14.0
Release:        0
Summary:        Voxel graphics editor
License:        GPL-3.0-only
Group:          Productivity/Graphics/3D Editors
URL:            https://goxel.xyz/
Source:         https://github.com/guillaumechereau/goxel/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(zlib)

%description
Goxel is an open source voxel graphics editor. Voxels are 3D images formed
of cubic elements.

%prep
%autosetup -p1

%build
# Manually set build flag as Leap 15.2 does not support %%{set_build_flags} macro unlike TW.
CFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto'
export CFLAGS
CXXFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto'
export CXXFLAGS
FFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto '
export FFLAGS
FCFLAGS='-O2 -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto '
export FCFLAGS
LDFLAGS=-flto=auto
export LDFLAGS
scons mode=release

%install
%make_install PREFIX=%{_prefix}

# PATCH-FIX-UPSTREAM https://github.com/guillaumechereau/goxel/pull/229
chmod +x %{buildroot}%{_bindir}/%{name}

sed -i 's/\${SNAP}\/icon.png/%{name}/g' %{buildroot}%{_datadir}/applications/%{name}.desktop

# PATCH-FIX-UPSTREAM https://github.com/guillaumechereau/goxel/pull/228
%suse_update_desktop_file -r %{name} Graphics 3DGraphics

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/io.github.guillaumechereau.Goxel.metainfo.xml

%changelog
