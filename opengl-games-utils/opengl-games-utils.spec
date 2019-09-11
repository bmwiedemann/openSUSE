#
# spec file for package opengl-games-utils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           opengl-games-utils
Version:        0.1
Release:        0
Summary:        Utilities to check proper 3d support before launching 3d games
License:        SUSE-Public-Domain
Group:          Amusements/Games/3D/Other
Url:            http://fedoraproject.org/wiki/SIGs/Games
Source0:        opengl-game-wrapper.sh
Source1:        opengl-game-functions.sh
Source2:        README
Requires:       %{_bindir}/glxinfo
Requires:       zenity
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains various shell scripts which are intended for use by
3D games packages. These shell scripts can be used to check if direct rendering
is available before launching an OpenGL game. This package is intended for use
by other packages and is not intended for direct end user use!

%prep
%setup -q -c -T
cp %{SOURCE2} .

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/opengl-game-wrapper.sh
%{_datadir}/%{name}

%changelog
