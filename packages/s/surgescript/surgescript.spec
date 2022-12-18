#
# spec file for package surgescript
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 Artur Iwicki <fedora@svgames.pl>
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


%define _sover  0_5_6
Name:           surgescript
Version:        0.5.6.1
Release:        0
Summary:        A scripting language for games
License:        Apache-2.0
URL:            https://opensurge2d.org
Source0:        https://github.com/alemart/surgescript/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
SurgeScript is a scripting language for games. It has been designed
with the specific needs of games in mind. Its features include:
- The state-machine pattern: objects are state machines,
  making it easy to create in-game entities
- The composition approach: you may design complex objects
  and behaviors by means of composition
- The hierarchy system: objects have a parent and may have children,
  in a tree-like structure
- The game loop: it's defined implicitly
- Automatic garbage collection, object tagging and more!

SurgeScript is meant to be used in games and in interactive applications.
It's easy to integrate it into existing code, it's easy to extend,
it features a C-like syntax, and it's free and open-source software.

SurgeScript has been designed based on the experience of its developer
dealing with game engines, applications related to computer graphics and so on.
Some of the best practices have been incorporated into the language itself,
making things really easy for developers and modders.

%package devel
Summary:        Files for developing applications using %{name}
License:        Apache-2.0 AND BSD-1-Clause AND BSD-2-Clause AND SUSE-Public-Domain
Requires:       lib%{name}%{_sover} = %{version}

%description devel
This package contains files required for
developing applications using %{name}.

%package -n lib%{name}%{_sover}
Summary:        Files for developing applications using %{name}
License:        Apache-2.0 AND BSD-1-Clause AND BSD-2-Clause AND SUSE-Public-Domain

%description -n lib%{name}%{_sover}
This package contains files required for
developing applications using %{name}.

%prep
%setup -q

%build
%cmake \
       -DWANT_SHARED=YES \
       -DWANT_STATIC=NO \
       -DWANT_EXECUTABLE=YES
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{_sover} -p /sbin/ldconfig
%postun -n lib%{name}%{_sover} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%doc docs
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.0.5.6
%{_libdir}/lib%{name}.so.%{version}

%changelog
