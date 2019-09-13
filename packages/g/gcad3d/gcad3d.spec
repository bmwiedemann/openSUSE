#
# spec file for package gcad3d
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define rname gCAD3D
%define bit %(getconf LONG_BIT)
Name:           gcad3d
Version:        2.352+git20170420.b5668e9
Release:        0
Summary:        3D CAD-CAM application
License:        GPL-3.0
Group:          Productivity/Graphics/CAD
Url:            http://gcad3d.org
Source0:        %{name}-%{version}.tar.xz
Source100:      %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM return.patch avvissu@yandex.ru -- E: Program returns random data in a function
Patch0:         gcad3d-2.35_return.patch
# PATCH-FIX-UPSTREAM sequence-point.patch avvissu@yandex.ru -- W:Program causes undefined operation
Patch1:        	gcad3d-2.35_sequence-point.patch
BuildRequires:  ctags
BuildRequires:  doxygen
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
ExclusiveArch:	%ix86 x86_64 %power64

%description
gCAD3D is a 3D CAD-CAM application that features an integrated 3D OpenGL
viewer, a program interpreter for geometry and NC-commands in 3D, an
integrated NC-processor, and a programming interface for user programs. It
has support for importing Step files and support for both importing and
exporting Iges, DXF, and VRML files, and for exporting SVG.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Rebuild G-Code
find . -type f -name \*.o -exec rm {} \;
# Building...
sed -i '/xdg-open/d' doc/gcad_doxygen.sh
# Build with optflags
sed -e '/^CPFLG/s/\((GLBCP)\)/\1 ${EXTRACFLAGS}/' \
    -e '/^C..\?FLG/s/$/ ${EXTRACFLAGS}/' \
	-i $(grep -rl 'CPFLG\|CXFLG\|CPPFLG')
# Set new gcad-version
gcad_version=$(echo %{version} | sed 's/\+\?git.*//')
gcad_date=$(echo %{version} | sed 's/.*git\([0-9]\+\)\.\?.*/\1/')
sed -e "s/\ [.0-9]\+\(.*\)\ [-0-9]\+/ $gcad_version\1 $gcad_date/"  \
    -i src/xa/gcad_version.h
# Change gtk-version
sed -i '/^VGUI/s/gtk[0-9]/gtk3/' src/options.mak
# Startproc for gCAD3D on 64bit
sed -i 's|/usr/lib|%{_libdir}|' debian/gcad3d
# Make hidden directory
sed -e '/strcat.*gCAD3D/s/gCAD3D/\.gCAD3D/' \
    -e 's/\(\~\/\)\(gCAD3D\)/\1\.\2/g' \
    -i $(grep -rl '\"gCAD3D\"\|\~\/gCAD3D')
# Find executable files
find . -name \*.txt -type f -executable -exec chmod 644 {} \;
# Fix: wrong-file-end-of-line-encoding
find . -name \*.txt -exec dos2unix -k {} \;
# Fix: implicit-fortify-decl (too many warnings)
for _file in $(grep -rl 'stdlib\.h'); do
  if ! grep 'string\.h' $_file; then
    sed -i '/stdlib\.h/a #include <string.h>' $_file
  fi
done

%build
EXTRACFLAGS="%{optflags} -fno-strict-aliasing"
export EXTRACFLAGS="${EXTRACFLAGS/-fomit-frame-pointer /}"
# see: src/option.sh
export gcad_dir_dev="$PWD"
export gcad_dir_bin="$PWD/binLinux%{bit}"
export OUTDIR="$gcad_dir_bin"
# see: src/APP/dev_setup.sh
mkdir -p $gcad_dir_bin
mkdir -p $gcad_dir_bin/plugins
mkdir -p $gcad_dir_bin/plugins/cut1
mkdir -p $gcad_dir_dev/src/tags
# see: src/APP/do
pushd src/APP
make %{?_smp_mflags} -f gcad_gui__.mak
make %{?_smp_mflags} -f gcad_gui__.mak link
make %{?_smp_mflags} -f gcad3d.mak
make %{?_smp_mflags} -f gcad3d.mak all
make %{?_smp_mflags} -f gcad3d.mak allDemos
sh ../../doc/gcad_doxygen.sh
popd

%install
install -d %{buildroot}/%{_libdir}/%{rname}/binLinux%{bit}/plugins
install -d %{buildroot}/%{_libdir}/%{rname}/binLinux%{bit}/plugins/cut1
install -d %{buildroot}/%{_datadir}/%{name}/icons
install -d %{buildroot}%{_datadir}/doc/%{name}/html
install -d %{buildroot}%{_datadir}/doc/%{name}/msg

install -Dm 0755 debian/gcad3d %{buildroot}%{_bindir}/gcad3d
install -m 0755 binLinux%{bit}/%{rname} %{buildroot}%{_libdir}/%{rname}/binLinux%{bit}/
install -m 0644 binLinux%{bit}/*.so %{buildroot}%{_libdir}/%{rname}/binLinux%{bit}/
install -m 0644 binLinux%{bit}/plugins/*.so %{buildroot}%{_libdir}/%{rname}/binLinux%{bit}/plugins/
install -m 0755 binLinux%{bit}/plugins/cut1/G-Code %{buildroot}%{_libdir}/%{rname}/binLinux%{bit}/plugins/cut1/
install -m 0644 icons/{*.png,*.xpm,*.bmp} %{buildroot}%{_datadir}/%{name}/icons/
install -m 0644 doc/html/{*.htm,*.png,*.js} %{buildroot}%{_datadir}/doc/%{name}/html/
install -m 0644 doc/msg/*.txt %{buildroot}%{_datadir}/doc/%{name}/msg/

install -Dm 0644 %{buildroot}%{_datadir}/{%{name}/icons/,pixmaps/}%{rname}.xpm
%suse_update_desktop_file -c %{rname} %{rname} "CAD-CAM-Application" %{name} %{rname} GTK Graphics 3DGraphics Engineering

%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%if 0%{?suse_version} > 1320
%license LICENSE LICENSE_GPLv3.txt
%else
%doc LICENSE LICENSE_GPLv3.txt
%endif
%doc doc/gCAD3D_log.txt
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_libdir}/%{rname}
%{_datadir}/%{name}
%{_datadir}/applications/%{rname}.desktop
%{_datadir}/pixmaps/%{rname}.xpm

%changelog
