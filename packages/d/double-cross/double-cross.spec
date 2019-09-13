#
# spec file for package double-cross
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define oname   dcross

Name:           double-cross
Version:        2.0
Release:        0
Summary:        Unconventional falling block game
License:        GPL-3.0+
Group:          Amusements/Games/Action/Arcade
Url:            https://code.google.com/p/double-cross/
Source0:        https://double-cross.googlecode.com/files/%{oname}_%{version}.zip
Source1:        %{name}.sh
Source2:        %{name}-music.tar
Source3:        %{name}-icons.tar
Source4:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  unzip
BuildRequires:  python
Requires:       python-pygame
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unlike your common unilateral falling block games, 'Double Cross'
implements a bidirectional paradigm expanding the genre in both
dimension and difficulty.

Blocks fall from the top and fly in from the side settling in a joined
"play area". Deletions occur when rows of ten blocks are completed.
A horizontal row of 10 will cause the blocks to fall down, and
a vertical row of 10 will cause the blocks to "fall" to the right.
If a vertical row is completed during a vertical drop or a horizontal
row is completed during a horizontal drop the corresponding deletion
will not occur until the next turn. This can and will lead to
non-intuitive results. Focus on the vertical alone and you will die
from horizontal negligence and vice versa.

%prep
%setup -q -a2 -a3 -n %{oname}_%{version}

# Convert to unix line end
find -name "*.py" -print0 -or -name "*.pyw" -print0 | xargs -0 dos2unix

#sed -i -e 's| as pg||' data/main.py

# Remove not usable mp3 music, because not works with pygame
rm -f sound/music/*.mp3

# Copy ogg music, converted with soundKonverter, and replace mp3 with ogg
cp -a music/*.ogg sound/music
sed -i 's|mp3|ogg|' data/setup.py data/menu.py

%build

%install
# install wrapper
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install directories
mkdir -p %{buildroot}%{_datadir}/%{name}/{data,fonts,graphics,sound}
for d in data fonts graphics sound ; do
    cp -a $d %{buildroot}%{_datadir}/%{name}
done

# install files
install -Dm 0664 %{name}.pyw %{buildroot}%{_datadir}/%{name}

# install icons
for i in 32 48 64 72 96 ; do
    install -Dm 0644 icons/%{name}_${i}x${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install Desktop file
install -Dm 0644 %{S:4} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
