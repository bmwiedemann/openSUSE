#
# spec file for package pencil
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015-2016 Michiel van der Wulp.
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


Name:           pencil
Version:        2.0.21
Release:        0
Summary:        Tool for making diagrams and GUI prototyping
License:        GPL-2.0
Group:          Productivity/Graphics/Other
Url:            https://github.com/prikhi/pencil
Source:         https://github.com/prikhi/pencil/archive/v%{version}.zip
# PATCH-FIX-OPENSUSE -- reproducible package build
Patch0:         reproducible.patch
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pencil is a GUI prototyping tool that can be used to create mockups.

Top features:
  * Built-in stencils for diagraming and prototyping
  * Multi-page document with background page
  * On-screen text editing with rich-text supports
  * PNG rasterizing
  * Undo/redo supports
  * Installing user-defined stencils
  * Standard drawing operations: aligning, z-ordering, scaling, rotating...
  * Cross-platforms
  * Adding external objects

This is a fork of the dead original project at http://pencil.evolus.vn/.

%prep
%setup -q
%patch0 -p1

%build
cd build
sed -i 's|BINARIES="xulrunner |BINARIES="|' ./Linux/pencil
sed -i "s|MAX_VERSION='46|MAX_VERSION='50|" ./properties.sh
./build.sh linux

%install
cd build
install -v -d %{buildroot}
cp -r Outputs/LinuxPkg/* %{buildroot}

%suse_update_desktop_file -r %{name} Graphics 2DGraphics Development Design

%fdupes %{buildroot}%{_datadir}/evolus-%{name}

%files
%defattr(-, root, root)
%doc CHANGELOG.md LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/evolus-%{name}/
%{_datadir}/mime/packages/ep.xml

%changelog
