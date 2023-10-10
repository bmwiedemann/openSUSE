#
# spec file for package pixelorama
#
# Copyright (c) 2023 cunix
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

%define _buildshell /bin/bash
%define nameupper Pixelorama

Name:           pixelorama
Version:        0.11.2
Release:        0
Summary:        2D sprite editor
License:        MIT
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/Orama-Interactive/Pixelorama
Source0:        https://codeload.github.com/Orama-Interactive/%{nameupper}/tar.gz/refs/tags/v%{version}#/%{nameupper}-%{version}.tar.gz
BuildRequires:  godot3-headless
BuildRequires:  godot3-runner
BuildRequires:  update-desktop-files
BuildRequires:  vendored_licenses_packager
BuildRequires:  fdupes
ExcludeArch:    %arm
ExcludeArch:    %power64

%description
Graphical tool based on the Godot Engine to create and edit
animated pixel art, game graphics, tiles and many kinds of pixel art

%prep
%setup -q -n %{nameupper}-%{version}
template_dir=$(godot3-headless --version | grep --extended-regexp --only-matching --regexp ^\([0-9]+\\.\)+stable -)
r=$(echo $?)
if [[ x"$template_dir" != x ]]
  then
    if [[ $r -eq 0 ]]
      then echo godot version found: $template_dir
      else echo regex failure; exit 1
    fi
  else echo template_dir empty; exit 1
fi
template_name=linux_x11_%{__isa_bits}_release
target_dir=$HOME/.local/share/godot3/templates/$template_dir
target_file_path=$target_dir/$template_name
mkdir -p $target_dir
cp %{_bindir}/godot3-runner $target_file_path
sed -i "s/binary_format\/embed_pck=false/binary_format\/embed_pck=true/" ./export_presets.cfg
cp addons/README.md addons_README.md
cp Misc/Linux/com.orama_interactive.%{nameupper}.desktop com.orama_interactive.%{nameupper}.desktop
rm pixelorama_data/.gdignore
mkdir binary
%vendored_licenses_packager_prep addons

%build
export_name="Linux/X11 %{__isa_bits}-bit"
godot3-headless --verbose --export "$export_name" binary/%{name}

%install
v=('Brushes' 'Palettes' 'Patterns')
for d in "${v[@]}"
  do
    echo install "$d"
    install -D -d -m 0755 %{buildroot}%{_datadir}/%{name}/$d
    cp -R pixelorama_data/$d/* %{buildroot}%{_datadir}/%{name}/$d/
  done
install -D -p -m 0755 binary/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 assets/graphics/icons/icon.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -p -m 0644 Misc/Linux/com.orama_interactive.%{nameupper}.appdata.xml  %{buildroot}%{_datadir}/metainfo/com.orama_interactive.%{nameupper}.appdata.xml
%suse_update_desktop_file -i com.orama_interactive.%{nameupper}
%vendored_licenses_packager_install
%fdupes -s %{buildroot}/%{_prefix}

%files
%license LICENSE addons_README.md
%doc CHANGELOG.md CONTRIBUTING.md README.md
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/com.orama_interactive.%{nameupper}.appdata.xml
%{_datadir}/applications/com.orama_interactive.%{nameupper}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%vendored_licenses_packager_files

%changelog
