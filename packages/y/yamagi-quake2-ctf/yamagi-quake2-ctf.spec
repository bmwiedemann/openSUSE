#
# spec file for package yamagi-quake2-ctf
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017-2022, Martin Hauke <mardnh@gmx.de>
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


Name:           yamagi-quake2-ctf
Version:        1.09
Release:        0
Summary:        Quake II - Three Wave Capture The Flag for yamagi-quake2
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://www.yamagi.org/quake2/
Source:         http://deponie.yamagi.org/quake2/quake2-ctf-%{version}.tar.xz
Source1:        yquake2-ctf.desktop
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  yamagi-quake2
Requires:       yamagi-quake2

%description
This package provides the Three Wave Capture The Flag game mode
for yamagi-quake2, an enhanced port of the original Quake II.

%prep
%setup -q -n quake2-ctf-%{version}

# replace __DATE__ and __TIME__ with date/time of the last specfile changelog
# entry
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' -print -exec sh -c '
    sed "/^[ \t]*#[ \t]*if/n;s/__DATE__/$3/g;s/__TIME__/$2/g" "$1" >"$1.new" && \
        mv "$1.new" "$1"
' {} {} "${TIME}" "${DATE}" \;

%build
%cmake
%cmake_build

%install
install -dm 755 %{buildroot}%{_bindir}
install -Dpm 644 build/game.so %{buildroot}%{_libexecdir}/yamagi-quake2/ctf/game.so
echo -e "#!/bin/sh\nexec %{_libexecdir}/yamagi-quake2/yquake2 \+set game ctf \"\$@\"" > %{buildroot}%{_bindir}/yquake2-ctf
chmod 755 %{buildroot}%{_bindir}/yquake2-ctf

%suse_update_desktop_file -i yquake2-ctf

%files
%license LICENSE
%doc CHANGELOG README
%{_bindir}/yquake2-ctf
%dir %{_libexecdir}/yamagi-quake2/ctf
%{_libexecdir}/yamagi-quake2/ctf/game.so
%{_datadir}/applications/yquake2-ctf.desktop

%changelog
