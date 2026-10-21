#
# spec file for package decker
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


Name:           decker
Version:        1.71
Release:        0
Summary:        A multimedia sketchpad
License:        MIT
URL:            https://beyondloom.com/decker/
Source:         https://github.com/JohnEarnest/Decker/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(sdl2)

%description
Decker is a multimedia platform for creating and sharing interactive documents, with sound, images, hypertext, and scripted behavior.

%prep
%autosetup -p1 -n Decker-%{version}

%build
%make_build lilt
%make_build decker

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} %make_install

%check
%make_build test

%files
%license LICENSE.txt
%doc Readme.md VERSION
%{_bindir}/decker
%{_bindir}/lilt

%changelog
