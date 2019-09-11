#
# spec file for package jmol
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jmol
Version:        14.29.26
Release:        0
Summary:        3D Viewer for chemical structures
License:        LGPL-2.1-only
Group:          Productivity/Scientific/Chemistry
Url:            http://jmol.sf.net/

#Source:         http://downloads.sf.net/jmol/Jmol-%version-binary.tar.gz
Source:         jmol-%version.tar.xz
Source2:        Jmol_icon13.png
#Source2-Orig:  http://wiki.jmol.org/index.php/File:Jmol_icon13.png
Source3:        %name.man
Source4:        %name.desktop
Source9:        sanitize_binpkg.sh
Patch1:         datadir.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  update-desktop-files
BuildRequires:  xz
Requires:       java

%description
Jmol is a Java-based viewer for chemical structures in 3D with
features for chemicals, crystals, materials and biomolecules.

%prep
%setup -q
%patch -P 1 -p1
cp %{S:2} .

%build
dos2unix CHANGES.txt COPYRIGHT.txt LICENSE.txt README.txt
perl -i -pe 's{\@pkgdatadir\@}{%_datadir/%name}gs' jmol.sh
# man
cp %{S:3} .
sed -i 's/INST_VERSION/%version/' jmol.man
sed -i 's/INST_SUMMARY/%summary/' jmol.man
gzip -9 jmol.man

%install
b="%buildroot"
# jar
mkdir -p "$b/%_datadir/%name"
install -p -m 644 Jmol.jar "$b/%_datadir/%name/"
# script
install -Dpm0755 jmol.sh "$b/%_bindir/jmol"
# icon
install -Dpm0644 Jmol_icon13.png "$b/%_datadir/pixmaps/%name.png"
# manual
install -Dpm0644 jmol.man.gz "$b/%_mandir/man1/jmol.1.gz"
# .desktop
desktop-file-install --dir %buildroot%_datadir/applications %{S:4}
%suse_update_desktop_file %name

%files
%defattr(-,root,root)
%doc README.txt LICENSE.txt COPYRIGHT.txt CHANGES.txt
%_bindir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png
%_mandir/man1/%name.1.gz

%changelog
