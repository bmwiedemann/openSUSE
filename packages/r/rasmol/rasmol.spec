#
# spec file for package rasmol
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


Name:           rasmol
Version:        2.7.4.2
Release:        0
Summary:        Molecular Graphics Visualization Tool
License:        SUSE-Public-Domain
Group:          Productivity/Scientific/Chemistry
Url:            http://www.bernstein-plus-sons.com/software/rasmol/
Source:         RasMol_2.7.4.2.tar.bz2
Source1:        README_FIRST
Source2:        CBFlib_0.7.9.1.tar.bz2
Patch1:         RasMol_%{version}.patch
#This one is unneeded
#Patch2:         RasMol_%{version}-array.patch
Patch2:         RasMol_%{version}-decrement_var.patch
# this patch ommit downloading CBFlib tarball which is copied from source2
Patch3:         RasMol_%{version}-no_wget_CBFlib.patch
Patch4:         RasMol_%{version}-CBFlib_rpmoptflags.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       RasMol
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
# Exclude PowerPC archs as gcc compiler already defined vector
# that conflicts with vector.h/vector.c when xmkmf calling imake.
ExcludeArch:    ppc ppc64 ppc64le

%description
RasMol is an X Window System tool intended for the visualization of
proteins and nucleic acids. It reads Brookhaven Protein Database (PDB)
files and interactively renders them in a variety of formats on either
an 8-bit or 24/32-bit color display.

Examples are in /usr/lib/rasmol.

%define _xorg7libs %_lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir

%prep
%setup -n RasMol_2.7.4.2_23Mar08 -a2
%patch1
%patch2
%patch3
%patch4
cp %{S:1} .
# it is needed to remove some links in tarball
## these thing were done manualy when repacking the 2.7.4 tarball
## may be reused in future
# fixing executable flag 
#find . -type f -perm -111|xargs chmod -x 
#find . -name *.csh|xargs chmod +x 
# removing forgotten manpage link
#rm -f src/rasmol.man

%build
# export CFLAGS=$RPM_OPT_FLAGS have to be set in Makefile (patch 0 and 5)
cd src
xmkmf -a
make
#make %{?_smp_mflags}

%install
make -C src "DESTDIR=$RPM_BUILD_ROOT" "PIXELDEPTH=16" install
make -C src "DESTDIR=$RPM_BUILD_ROOT" install.man 
rm -rf doc/RCS 
cp -a data $RPM_BUILD_ROOT/usr/%{_xorg7libs}/rasmol

%files
%defattr(-,root,root)
%doc NOTICE PROJECTS TODO* README* README_FIRST ChangeLog.html history.html index.shtml html_graphics doc/{*.pdf.gz,N*,e*,r*.html,raswin.hlp}
%doc %{_xorg7_mandir}/man1/*
/usr/%{_xorg7libs}/rasmol
/usr/%{_xorg7bin}/rasmol

%changelog
