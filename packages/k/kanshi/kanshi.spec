#
# spec file for package kanshi
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


Name:           kanshi
Version:        1.6.0
Release:        0
Summary:        Dynamic display configuration
License:        MIT
Group:          System/GUI/Other
URL:            https://git.sr.ht/~emersion/kanshi
Source0:        https://git.sr.ht/~emersion/kanshi/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://git.sr.ht/~emersion/kanshi/refs/download/v%{version}/%{name}-%{version}.tar.gz.sig
# https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19
Source2:        %{name}.keyring
Patch1:         wayland-include-dirs.patch
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  scdoc
BuildRequires:  pkgconfig(libvarlink)
BuildRequires:  pkgconfig(scfg)
BuildRequires:  pkgconfig(wayland-client)

%description
kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug.

%prep
%autosetup -p1

%build
# Disabled because libvarlink is not available in Factory
%meson \
  -Dipc=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/kanshi
%{_bindir}/kanshictl
%{_mandir}/man?/%{name}*

%changelog
