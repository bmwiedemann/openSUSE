#
# spec file for package ddd
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


Name:           ddd
BuildRequires:  ImageMagick
BuildRequires:  apache2-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-library
BuildRequires:  ghostscript_any
BuildRequires:  libapr-util1-devel
BuildRequires:  libtiff-devel
BuildRequires:  ncurses-devel
# configure switch --without-motif is not designated to work
# (you'll get 'don't use --without-motif' in configure time)
BuildRequires:  makeinfo
BuildRequires:  openmotif-devel
BuildRequires:  pcre-devel
BuildRequires:  transfig
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
Requires:       gdb
Version:        3.3.12
Release:        0
Summary:        Debugger with Graphical User Interface
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Debuggers
Url:            http://www.gnu.org/software/ddd
Source:         ddd-%{version}.tar.bz2
Source1:        ddd.png
Source2:        ddd.desktop
Source3:        README.SUSE
Source4:        ddd.wrapper
Patch0:         ddd-3.3.12-gcc44.patch
Patch1:         ddd-wrong-memcpy.patch
Patch2:         ddd-texinfo-5.0.patch
Patch3:         ddd-buildcompare.patch
# http://www.imagemagick.org/discourse-server/viewtopic.php?f=3&t=23462 
Patch4:         ddd-imagemagick-xpm-colors.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         %install_info_prereq
# NOTE: We don't want this dependency and desktop-data-SuSE is in all
# desktop selections.
#Requires:    desktop-data-SuSE

%description
The DDD debugger (Data Display Debugger) is a comfortable GUI to the
well-known debuggers GDB and DBX. Data structures can be represented as
graphs and shown interactively. Programs can be debugged in C, C++,
Pascal, MODULA-2, FORTRAN, ADA, and even at the assembler code level.

%package doc
Summary:        Debugger with Graphical User Interface
Group:          Development/Tools/Debuggers
%if %suse_version > 1110
BuildArch:      noarch
%endif

%description doc
The DDD debugger (Data Display Debugger) is a comfortable GUI to the
well-known debuggers GDB and DBX. Data structures can be represented as
graphs and shown interactively. Programs can be debugged in C, C++,
Pascal, MODULA-2, FORTRAN, ADA, and even at the assembler code level.

%prep
%define apache_docroot %(apxs2 -q PREFIX)/htdocs
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp %{S:3} .
%if %suse_version > 1210
%configure --with-termlib=tinfo
%else
%configure
%endif
make -j1 all 
# BEGIN allow EPS decoder for build [bsc#1109976]
mkdir -p ~/.config/ImageMagick
cat << EOPF > ~/.config/ImageMagick/policy.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE policymap [
  <!ELEMENT policymap (policy)+>
  <!ATTLIST policymap xmlns CDATA #FIXED ''>
  <!ELEMENT policy EMPTY>
  <!ATTLIST policy xmlns CDATA #FIXED '' domain NMTOKEN #REQUIRED
    name NMTOKEN #IMPLIED pattern CDATA #IMPLIED rights NMTOKEN #IMPLIED
    stealth NMTOKEN #IMPLIED value CDATA #IMPLIED>
]>
<policymap>
  <policy domain="coder" rights="read" pattern="{EPS}" />
</policymap>
EOPF
# END allow EPS decoder for build [bsc#1109976]
make html

%install
%makeinstall
mkdir -p  $RPM_BUILD_ROOT/usr/share/X11/app-defaults/
install -m 644 ddd/Ddd $RPM_BUILD_ROOT/usr/share/X11/app-defaults/
install -m 755 -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}/
mkdir -p doc/html/PICS
cp -a ddd/PICS/*.jpg doc/html/PICS
cp -a ddd/style.css doc/html
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/pixmaps/
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/usr/share/applications/
mv $RPM_BUILD_ROOT/usr/bin/ddd $RPM_BUILD_ROOT/usr/bin/ddd.org
install %{SOURCE4} $RPM_BUILD_ROOT/usr/bin/ddd
%suse_update_desktop_file ddd

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ddd-themes.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ddd-themes.info.gz

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README TIPS TODO README.SUSE
%config /usr/share/X11/app-defaults/Ddd
%attr(755, root, root) /usr/bin/ddd.org
%attr(755, root, root) /usr/bin/ddd
%{_mandir}/man1/ddd.*
%{_infodir}/ddd*
/usr/share/ddd-%{version}/ 
/usr/share/applications/ddd.desktop
/usr/share/pixmaps/ddd.png
%exclude /usr/share/ddd-%{version}/NEWS
%exclude /usr/share/ddd-%{version}/COPYING
%exclude /usr/share/ddd-%{version}/ddd/Ddd

%files doc
%defattr(-,root,root,-)
%doc doc/ddd-paper.ps doc/*.pdf doc/html

%changelog
