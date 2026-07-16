#
# spec file for package panini
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


Name:           panini
Version:        0.75.0
Release:        0
Summary:        A tool for creating perspective views from panoramic and wide angle images
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/lazarus-pkgs/panini
Source:         https://github.com/lazarus-pkgs/panini/archive/%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(zlib)
# Disable on Arm, since build fails
ExcludeArch:    aarch64 %{arm}

%description
Visual tool for creating perspective views from panoramic and wide angle photographs.

%prep
%setup -q

%build
%qmake6 PREFIX=%{_prefix}
%qmake6_build

%install
%qmake6_install

%files
%license LICENSE
%doc README.md USAGE.md
%{_bindir}/panini
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/panini.appdata.xml

%changelog
