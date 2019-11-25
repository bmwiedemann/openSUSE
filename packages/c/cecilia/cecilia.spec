#
# spec file for package cecilia
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           cecilia
Version:        5.3.5
Release:        0
Summary:        Sound synthesis and audio signal processing environment
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://ajaxsoundstudio.com/software/cecilia/
Source:         http://ajaxsoundstudio.com/downloads/Cecilia5_%{version}-src.tar.bz2
#PATCH-FIX-OPENSUSE cecilia-setup.patch
Patch0:         %{name}-setup.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3
BuildRequires:  update-desktop-files
Requires:       python3-numpy
Requires:       python3-pyo >= 0.9.0
Requires:       python3-wxPython >= 4.0.1
BuildArch:      noarch

%description
Cecilia is a graphic user interface for the sound synthesis and sound
processing package CSound. Cecilia enables the user to build very
quickly graphic interfaces with sliders and curves to control CSound
instruments. It is also an editor to CSound with syntax highlighting
and a built-in reference. It is also a great tool to explore the parameters
of a new opcode in an interactive and intuitive way.

Cecilia uses the pyo audio engine created for the Python programming language.

Cecilia was designed by and for musicians and sound designers. All
the traditional sound processing devices are included such as EQs,
compressors and delays adapted for the most simple applications and
the wildest imaginable sonic contortions.

%prep
%setup -q -n Cecilia5_%{version}-src
%patch0 -p1

%build
%py3_build

%install
%py3_install
for s in 16 32 48 64 96 128 192 256 512; do
  mkdir -pv %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
  convert -strip -resize ${s} scripts/Cecilia5_512.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
mv %{buildroot}%{_bindir}/Cecilia5.py %{buildroot}%{_bindir}/%{name}
%suse_update_desktop_file -c %{name} %{name} "Sound synthesis and audio signal processing environment" %{name} %{name} "Audio;AudioVideoEditing;"
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc README.rst whatsnew.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
