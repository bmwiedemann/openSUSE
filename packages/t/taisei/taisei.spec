#
# spec file for package taisei
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


Name:           taisei
Version:        1.4.2
Release:        0
Summary:        Clone of the Touhou Project series of shoot ’em up games
License:        MIT
Group:          Amusements/Games/Action/Arcade
URL:            https://taisei-project.org
Source0:        https://github.com/taisei-project/taisei/releases/download/v%{version}/taisei-%{version}.tar.xz
Source1:        https://github.com/taisei-project/taisei/releases/download/v%{version}/taisei-%{version}.tar.xz.sig
Source2:        gpg.keyring
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.63.0
BuildRequires:  pkgconfig
BuildRequires:  python3-Pygments
BuildRequires:  python3-docutils
BuildRequires:  python3-zstandard
BuildRequires:  pkgconfig(cglm) >= 0.7.8
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gamemode)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebpdecoder) >= 0.5
BuildRequires:  pkgconfig(libzip) >= 1.7.0
BuildRequires:  pkgconfig(libzstd) >= 1.4.0
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2) >= 2.0.16
BuildRequires:  pkgconfig(zlib)
BuildRequires:  shaderc
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  spirv-cross-devel
Requires:       %{name}-data
Suggests:       gamemoded
ExcludeArch:    %{ix86}

%description
Taisei is an open clone of the Touhou Project series. Touhou is a one-man project
of shoot ’em up games set in an isolated world full of Japanese folklore.

%package data
Summary:        Data files for Taisei
Group:          Amusements/Games/Action/Arcade
Requires:       %{name} >= %{version}
BuildArch:      noarch

%description data
Data files for Taisei, an open clone of the Touhou Project series. Touhou is a
one-man project of shoot ’em up games set in an isolated world full of
Japanese folklore.

%prep
%setup -q

%build
_v=%{version}
%meson \
    -Dstrip=false \
    -Db_pch=false \
    -Dinstall_macos_bundle=disabled \
    -Dinstall_relocatable=disabled \
    -Dshader_transpiler=enabled \
    -Dr_gles30=enabled \
%meson_build

%install
%meson_install

%if 0%{?suse_version} && !0%{?fedora_version}
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}
%endif
%fdupes %{buildroot}

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/org.taisei_project.Taisei*.desktop
%{_datadir}/icons/hicolor/*/apps/*%{name}*.png
%{_datadir}/icons/hicolor/*/mimetypes/*%{name}*.png
%{_datadir}/mime/packages/org.taisei_project.Taisei.xml
%{_datadir}/metainfo/org.taisei_project.Taisei.appdata.xml

%files data
%{_datadir}/%{name}

%changelog
