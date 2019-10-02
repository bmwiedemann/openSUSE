#
# spec file for package bstone
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           bstone
Version:        1.1.13
Release:        0
Summary:        A source port of Blake Stone
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://bibendovsky.github.io/bstone/
Source:         https://github.com/bibendovsky/bstone/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-SDL2W.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
A source port of the first-person shooter Blake Stone.

Features:
 *  High resolution rendering of world (extended vanilla engine)
 *  Modern and vanilla controls
 *  Allows to customize control bindings
 *  Separate volume control of sound effects and music
Supported games:
 *  Aliens of Gold (v1.0/v2.0/v2.1/v3.0) full or shareware
 *  Planet Strike (v1.0/v1.1)


NOTE: To play Blake Stone with bstone you need the original game files
You need to start the game from within the folder with these files.

%prep
%setup -q
%patch0 -p1

%build
cd src/
%cmake
%make_jobs

%install
install -Dm0755 src/build/bstone %{buildroot}%{_bindir}/bstone

%files
%license LICENSE "Blake Stone source code license.doc"
%doc CHANGELOG.md README.md
%{_bindir}/bstone

%changelog
