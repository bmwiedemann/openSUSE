#
# spec file for package yamagi-quake2
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2016 Luke Jones <luke.nukem.jones@gmail.com>
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


Name:           yamagi-quake2
Version:        8.10
Release:        0
Summary:        Enhanced Quake 2 Source Port
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Shoot
URL:            https://www.yamagi.org/quake2/
Source:         https://deponie.yamagi.org/quake2/quake2-%{version}.tar.xz
Source100:      yamagi-quake2.appdata.xml
# PATCH-FIX-OPENSUSE set correct path
Patch0:         systemwide.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel

%description
Yamagi Quake II is an enhanced client for id Software's Quake II. The
main focus is an unchanged single player experience; the gameplay and
graphics are unaltered. It also features: anisotropic filtering and
multi-sample anti-aliasing, widescreen aspect ratio and unlimited
screen size, compatibility with most mods, optional support for
retexturing packs and HUD scaling.

%prep
%setup -q -n quake2-%{version}
%patch0 -p1

%build
export SOURCE_DATE_EPOCH=$(date +%s -r CHANGELOG)
%cmake \
    -DSYSTEMWIDE_SUPPORT=ON
make %{_smp_mflags}

%install
q2dir="%{buildroot}%{_libexecdir}/%{name}"
install -dm 755 %{buildroot}%{_bindir}
install -Dpm 755 build/release/quake2 $q2dir/yquake2
install -Dpm 755 build/release/q2ded $q2dir/yq2ded
install -Dpm 644 build/release/ref_gl1.so $q2dir/ref_gl1.so
install -Dpm 644 build/release/ref_gl3.so $q2dir/ref_gl3.so
install -Dpm 644 build/release/baseq2/game.so $q2dir/baseq2/game.so
install -Dpm 644 stuff/yq2.cfg $q2dir/baseq2/yq2.cfg

# Install icons
install -Dpm 644 stuff/icon/Quake2.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/yquake2.svg
for res in 256 128 96 64 32 16; do
    mkdir -p "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps"
    convert -strip stuff/icon/Quake2.png -resize $res"x"$res "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps/yquake2.png"
done

# Install Wrapper
cat > %{buildroot}%{_bindir}/yquake2 << EOF
#!/bin/sh
exec "%{_libexecdir}/%{name}/\${0##*/}" \$@
EOF
ln -s yquake2 %{buildroot}%{_bindir}/yq2ded

install -D -p -m 644 %{SOURCE100}  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%suse_update_desktop_file -c yquake2 'Quake II' 'Yamagi Quake II' yquake2 yquake2 Game ActionGame

%post
cat << EOF

Please read README in %{_docdir}/%{name} for information on
how to install the needed gamedata files.

EOF

%files
%license LICENSE
%doc CHANGELOG README.md
%attr(0755,root,root) %{_bindir}/yquake2
%{_bindir}/yq2ded
%{_libexecdir}/%{name}
%{_datadir}/icons/hicolor/*/apps/yquake2.*
%{_datadir}/applications/yquake2.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
