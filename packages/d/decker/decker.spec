#
# spec file for package decker
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


Name:           decker
Version:        1.39
Release:        0
Summary:        A multimedia sketchpad
License:        MIT
URL:            http://beyondloom.com/decker/
Source:         https://github.com/JohnEarnest/Decker/archive/refs/tags/v%{version}.tar.gz
Patch:          install-script.patch
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  xxd

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
make test

%files
%license LICENSE.txt
%doc Readme.md VERSION
%{_bindir}/decker
%{_bindir}/lilt

%changelog

