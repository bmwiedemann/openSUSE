#
# spec file for package pixelorama
#
# Copyright (c) 2023-2025 cunix
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
Version:        1.0.5
Release:        0
Summary:        2D sprite editor
License:        MIT
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/Orama-Interactive/Pixelorama
Source0:        https://codeload.github.com/Orama-Interactive/%{nameupper}/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  godot >= 4.3
BuildRequires:  godot-runner >= 4.3
BuildRequires:  vendored_licenses_packager
# currently no godot binary
ExcludeArch:    %arm
# build fails: Segmentation fault godot --headless --verbose --import
ExcludeArch:    %ix86
ExcludeArch:    %power64

%description
Graphical tool based on the Godot Engine to create and edit
animated pixel art, game graphics, tiles and many kinds of pixel art

%prep
%autosetup -n %{nameupper}-%{version}
template_dir=$(godot-runner --version | grep --extended-regexp --only-matching --regexp ^\([0-9]+\\.\)+stable -)
r=$(echo $?)
if [[ x"$template_dir" != x ]]
  then
    if [[ $r -eq 0 ]]
      then echo godot version found: $template_dir
      else echo regex failure; exit 1
    fi
  else echo template_dir empty; exit 1
fi
%ifarch %{arm} %{arm64}
template_name=linux_release.arm%{__isa_bits}
%elifarch %{ix86} %{x86_64}
template_name=linux_release.x86_%{__isa_bits}
%else
template_name=linux_release.%{_arch}
%endif
target_dir=$HOME/.local/share/godot/export_templates/$template_dir
target_file_path=$target_dir/$template_name
mkdir -p $target_dir
cp %{_bindir}/godot-runner $target_file_path
sed -i "s/binary_format\/embed_pck=false/binary_format\/embed_pck=true/" ./export_presets.cfg
cp addons/README.md addons_README.md
cp Misc/Linux/com.orama_interactive.%{nameupper}.desktop com.orama_interactive.%{nameupper}.desktop
rm pixelorama_data/.gdignore
mkdir binary
%vendored_licenses_packager_prep addons

%build
%ifarch %{arm} %{arm64}
export_name="Linux ARM%{__isa_bits}"
%else
export_name="Linux %{__isa_bits}-bit"
%endif

godot --headless --verbose --import
godot --headless --verbose --export-release "$export_name" binary/%{name}

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
install -D -p -m 0644 Misc/Linux/com.orama_interactive.%{nameupper}.desktop %{buildroot}%{_datadir}/applications/com.orama_interactive.%{nameupper}.desktop
install -D -p -m 0644 Misc/Linux/com.orama_interactive.%{nameupper}.appdata.xml  %{buildroot}%{_datadir}/metainfo/com.orama_interactive.%{nameupper}.appdata.xml
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
