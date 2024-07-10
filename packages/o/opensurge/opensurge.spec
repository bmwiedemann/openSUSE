#
# spec file for package opensurge
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


Name:           opensurge
Version:        0.6.1.1
Release:        0
Summary:        Game based on Sonic the Hedgehog Universe
License:        Apache-2.0 AND GPL-3.0-or-later AND LGPL-2.1-or-later AND CC-BY-3.0 AND OFL-1.1 AND MIT
Group:          Amusements/Games/Action/Arcade
URL:            https://opensurge2d.org/
Source0:        https://github.com/alemart/opensurge/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(OpenAL)
BuildRequires:  pkgconfig(allegro-5)
BuildRequires:  pkgconfig(allegro_acodec-5)
BuildRequires:  pkgconfig(allegro_audio-5)
BuildRequires:  pkgconfig(allegro_color-5)
BuildRequires:  pkgconfig(allegro_dialog-5)
BuildRequires:  pkgconfig(allegro_font-5)
BuildRequires:  pkgconfig(allegro_image-5)
BuildRequires:  pkgconfig(allegro_main-5)
BuildRequires:  pkgconfig(allegro_memfile-5)
BuildRequires:  pkgconfig(allegro_primitives-5)
BuildRequires:  pkgconfig(allegro_physfs-5)
BuildRequires:  pkgconfig(allegro_ttf-5)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(surgescript) >= 0.5.6
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Open Surge is a retro-style 2D sidescroller inspired by old-school
games. The characters named Surge, Neon and Charge are to save the
world from the evil Gimacian the Dark.

%prep
%autosetup

%build
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC=gcc-11
export CXX=g++-11
%endif

%cmake \
    -DGAME_BINDIR="%{_bindir}" \
    -DGAME_DATADIR="%{_datadir}/%{name}"
%cmake_build

%install
%cmake_install

%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_prefix}

# remove docs
rm -fv %{buildroot}%{_datadir}/%{name}/{CHANGES.md,LICENSE,README.md}
rm -rfv %{buildroot}%{_datadir}/%{name}/licenses

%files
%license licenses/*
%doc CHANGES.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
