#
# spec file for package garlic
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           garlic
Version:        1.6
Release:        0
Summary:        Molecular Graphics Visualization Tool
License:        LGPL-2.1+
Group:          Productivity/Scientific/Chemistry
Url:            http://www.ccp14.ac.uk/ccp/web-mirrors/garlic/garlic/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{version}-doc.tar.bz2
Source2:        %{name}.1.gz
Patch:          %{name}-%{version}.patch
Patch1:         garlic-%{version}-libpath.patch
Patch2:         garlic-1.6-undef.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
%define _xorg7_prefix /usr

%description
Garlic is an X Window System tool intended for the molecular
visualization of protein structure, DNA structure, and biological
macromolecules. It reads Brookhaven Protein Database (PDB) files.

%package doc
Summary:        Documentation for Garlic, a molecular graphics visualization tool
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
Garlic is an X Window System tool intended for the molecular
visualization of protein structure, DNA structure, and biological
macromolecules.
This subpackage contains the full documentation to Garlic.

%prep
%setup -b 0 
%setup -T -D -a 1 
%patch -p 1
%patch1
%patch2 -p 1
# fix executable permission on text files
cd garlic-1.6
chmod -x README favicon.ico tolower.script garlic.gif cookbook/garlic.gif precompiled_packages/garlic.gif
cd ..

%build
make %{?_smp_mflags} CC="%__cc" CCOPT="$RPM_OPT_FLAGS" LIBPATH="-L/usr/%{_lib}"

%install
mkdir -p $RPM_BUILD_ROOT/{usr/%{_xorg7bin},etc,%{_xorg7_mandir}/man1/}
cp -a garlic $RPM_BUILD_ROOT/usr/%{_xorg7bin}/
cp -a .garlicrc $RPM_BUILD_ROOT/etc/garlicrc
mkdir -p $RPM_BUILD_ROOT/usr/share/garlic
cp -a residues.pdb $RPM_BUILD_ROOT/usr/share/garlic/residues.pdb
mv %{name}-%{version} html
install -m 644 %{S:2} $RPM_BUILD_ROOT/%{_xorg7_mandir}/man1/  
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
cp -a garlic.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/garlic.xpm
rm -rf html/source html/mouse/.xvpics
chmod 644 html/{README,bold_statement.html,docs.html,favicon.ico,garlic.gif,index.html,monster.gif,versions.html}
%suse_update_desktop_file -n -c %name "Garlic" Garlic garlic garlic Education Science Chemistry

# Can't do this via %%doc in %%files, because that runs too late,
# after %%fdupes.
mkdir -p "%buildroot/%_defaultdocdir/%name"
cp -a html 1mal.script 2fcp.script 2omf.script 2por.script \
	BUGS COPYING ENVIRONMENT HISTORY README TODO \
	"%buildroot/%_defaultdocdir/%name"

%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%dir %_defaultdocdir/%name/
%_defaultdocdir/%name/COPYING
%doc %{_xorg7_mandir}/man1/*
%config /etc/garlicrc
/usr/%{_xorg7bin}/%{name}
/usr/share/garlic
/usr/share/garlic/residues.pdb
/usr/share/applications/%{name}.desktop
/usr/share/pixmaps/garlic.xpm

%files doc
%defattr(-,root,root)
%_defaultdocdir/%name/
%exclude %_defaultdocdir/%name/COPYING

%changelog
