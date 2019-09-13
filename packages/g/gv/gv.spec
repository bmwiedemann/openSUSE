#
# spec file for package gv
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


Name:           gv
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  libzio-devel
BuildRequires:  makeinfo
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw3d)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
%if %suse_version < 1100
BuildRequires:  desktop-data-SuSE
%endif
PreReq:         %install_info_prereq
Requires:       ghostscript_x11
Conflicts:      gs_serv gs_vga
# NOTE: We don't want this dependency and desktop-data-SuSE is in all
# desktop selections.
#Requires:    desktop-data-SuSE
Url:            http://www.gnu.org/software/gv/
Summary:        A Program to View PostScript Files
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/PS
Version:        3.7.4
Release:        0
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        gv.desktop
Source2:        gv.png
Patch1:         gv-3.7.4.dif
Patch2:         gv-3.7.0-I18N-mb.patch
# PATCH-FIX-OPENSUSE: make libzio usable
Patch3:         gv-3.7.2-libzio.dif
# PATCH-FIX-OPENSUSE: Write `Querformat' as `Querformat'
Patch4:         gv-3.7.4-querformat.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%global _mandir     %{_exec_prefix}/man
%define _x11lib     %{_exec_prefix}/%{_lib}
%define _x11data    %{_exec_prefix}/lib/X11
%define _appdefdir  %{_x11data}/app-defaults
%define _x11inc     %{_x11_prefix}/include
%else
%define _x11lib     %{_libdir}
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults
%define _x11inc     %{_includedir}
%endif

%description
GV offers you an X Window System GUI for viewing PostScript files. This
is an X Window System interface to ghostscript.



Authors:
--------
    Tim Theisen <tim@cs.wisc.edu>
    Johannes Plass <plass@dipmza.physik.uni-mainz.de>

%prep
%setup
echo >> src/Makefile.am
%patch1 -p0 -b .one
%patch2 -p0 -b .two
%patch3 -p0 -b .zio
%patch4 -p0 -b .ue

%build
autoreconf -fis
sed -ri 's@[[:blank:]]*-(R|rpath)[[:blank:]]*\$[[:alpha:]_]+@@g' configure
chmod 755 configure
CC=gcc
CFLAGS="$RPM_OPT_FLAGS"
LDFLAGS="-Wl,-z,defs"
cflags ()
{
    local flag=$1; shift
    case "${RPM_OPT_FLAGS}" in
    *${flag}*) return
    esac
    if test -n "$1" && gcc -Werror $flag -S -o /dev/null -xc   /dev/null > /dev/null 2>&1 ; then
	local var=$1; shift
	eval $var=\${$var:+\$$var\ }$flag
    fi
    if test -n "$1" && g++ -Werror $flag -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
	local var=$1; shift
	eval $var=\${$var:+\$$var\ }$flag
    fi
}
cflags -std=gnu89              CFLAGS
cflags -fno-strict-aliasing    CFLAGS
cflags -Wno-unused             CFLAGS
cflags -Wno-unprototyped-calls CFLAGS
cflags -pipe                   CFLAGS
export CC CFLAGS LDFLAGS
./configure --prefix=%{_prefix} \
	--mandir=%{_mandir}	\
	--infodir=%{_infodir}	\
	--with-x		\
	--x-includes=%{_x11inc}	\
	--x-libraries=%{_x11lib}\
	--enable-backing-pixmap	\
	--disable-memmove-code	\
	--disable-setenv-code	\
	--enable-international	\
	--with-libzio		\
	--with-default-papersize=a4
make pkgdatadir='%{_x11data}/gv'

%install
rm -rf %{buildroot}
mkdir  %{buildroot}
make	    DESTDIR=%{buildroot} pkgdatadir='%{_x11data}/gv' install
make	    DESTDIR=%{buildroot} pkgdatadir='%{_x11data}/gv' install-info
make	    DESTDIR=%{buildroot} pkgdatadir='%{_x11data}/gv' install-man
make -C src DESTDIR=%{buildroot} pkgdatadir='%{_x11data}/gv' install-nls
make -C src DESTDIR=%{buildroot} pkgdatadir='%{_x11data}/gv' install-data-local

mkdir -p %{buildroot}/%{_defaultdocdir}/gv
install -m 0444 NOTE %{buildroot}/%{_defaultdocdir}/gv/Copyright
# add font settings to app-defaults:
for i in $(find %{buildroot}%{_x11data} -type f -name "GV")
do
    cat src/gv_font_res-I18N_mb.dat >> ${i}
    chmod 0644 ${i}
done
# japanese app-defaults:
mkdir -p %{buildroot}%{_x11data}/{ja_JP.SJIS,ja_JP.EUC-JP}/app-defaults
iconv -f UTF-8 -t SJIS < %{buildroot}%{_x11data}/ja_JP.UTF-8/app-defaults/GV \
   > %{buildroot}%{_x11data}/ja_JP.SJIS/app-defaults/GV 
iconv -f UTF-8 -t EUC-JP < %{buildroot}%{_x11data}/ja_JP.UTF-8/app-defaults/GV \
   > %{buildroot}%{_x11data}/ja_JP.EUC-JP/app-defaults/GV 
mkdir -p %{buildroot}%{_x11data}/ko_KR.EUC-KR/app-defaults
iconv -f UTF-8 -t EUC-KR < %{buildroot}%{_x11data}/ko_KR.UTF-8/app-defaults/GV \
   > %{buildroot}%{_x11data}/ko_KR.EUC-KR/app-defaults/GV 
%suse_update_desktop_file -i gv Office Viewer

%post
%install_info --info-dir=.%{_infodir} .%{_infodir}/gv.info.gz

%postun
%install_info_delete --info-dir=.%{_infodir} .%{_infodir}/gv.info.gz

%files
%defattr(-,root,root)
%{_datadir}/applications/gv.desktop
%{_datadir}/pixmaps/gv.png
%dir %{_x11data}/gv/
%dir %{_x11data}/gv/safe-gs-workdir/
%config %{_x11data}/gv/*.ad
%dir %{_appdefdir}
%config %{_appdefdir}/GV
%dir %{_x11data}/??
%dir %{_x11data}/??_*
%dir %{_x11data}/*/app-defaults
%config %{_x11data}/*/app-defaults/GV
%{_bindir}/gv
%{_bindir}/gv-update-userconfig
%doc %{_mandir}/man1/gv.1.gz
%doc %{_mandir}/man1/gv-update-userconfig.1.gz
%doc %{_infodir}/gv.info.gz
%dir %{_defaultdocdir}/gv
%docdir %{_defaultdocdir}/gv
%{_defaultdocdir}/gv/Copyright

%changelog
