#
# spec file for package kanshi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.3.1
Release:        0
Summary:        Dynamic display configuration
License:        MIT
Group:          System/GUI/Other
URL:            https://git.sr.ht/~emersion/kanshi
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  scdoc
BuildRequires:  pkgconfig(wayland-client)

%description
kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug.

%prep
%setup -q -n kanshi-v%{version}

%build
# Disabled because libvarlink is not available in Factory
%meson \
  -Dipc=disabled
%meson_build

%install
%meson_install

%files
%{_bindir}/kanshi
%{_mandir}/man?/%{name}*

%changelog
