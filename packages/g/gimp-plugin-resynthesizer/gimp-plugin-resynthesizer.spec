#
# spec file for package gimp-plugin-resynthesizer
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gimp-plugin-resynthesizer
Version:        3.0+git.1749847142.32e3962
Release:        0
License:        GPL-3.0-or-later
Summary:        Suite of gimp plugins for texture synthesis
URL:            https://github.com/bootchk/resynthesizer
Group:          Productivity/Graphics/Bitmap Editors
Source:         resynthesizer-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gimp-devel >= 3.0
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(glib-2.0)

%description
This package is a set of plugins for use with the Gimp program.
The package includes:

- resynthesizer plugin engine (without a GUI)
- resynthesizer-gui plugin control panel for the engine
- various plugins (in Python language) that call the resynthesizer engine

%lang_package

%prep
%autosetup -p1 -n resynthesizer-%{version}

# fix shebangs
find . -name \*.scm -print0 | xargs -0 -l sed -i -e 's^#!%{_bindir}/env gimp^#!%{_bindir}/gimp^'
sed -i -e 's^#!%{_bindir}/env python^#!%{_bindir}/python^' test/testResynth.py

%build
%meson
%meson_build

%install
%meson_install
# %%find_lang resynthesizer3

%check
# %%meson_test ../test

%files
%doc README.md
%license COPYING
%{_libdir}/gimp/3.0/plug-ins/*

# %%files lang -f resynthesizer3.lang

%changelog
