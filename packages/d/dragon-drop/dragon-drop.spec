#
# spec file for package dragon-drop
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

Name:           dragon-drop 
Version:        1.2.0
Release:        0
Summary:        Simple drag-and-drop source/sink for X or Wayland
License:        GPL-3.0
Url:            https://github.com/mwh/dragon
Source:         https://github.com/mwh/dragon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-3.0)

%description 
dragon is a lightweight drag-and-drop source/target for X or Wayland.

%prep 
%autosetup -n dragon-%{version}

%build 
%make_build NAME=%{name} CC='gcc %{optflags}'

%install 
%make_install NAME=%{name} PREFIX=/usr

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%doc README
%license LICENCE

%changelog
