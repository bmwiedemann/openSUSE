#
# spec file for package pcb
#
# Copyright (c) 2015-2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pcb
Version:        4.2.0
Release:        0
Summary:        CAD Program for the Design of Printed Circuit Boards
License:        GPL-2.0
Group:          Productivity/Scientific/Electronics

Url:            http://pcb.geda-project.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  ImageMagick
BuildRequires:  Mesa-devel
BuildRequires:  bison
BuildRequires:  dbus-1-devel
BuildRequires:  flex
BuildRequires:  freeglut-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gd-devel >= 2.1.0
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  tk
BuildRequires:  unzip
BuildRequires:  update-desktop-files
#Requires(post):   shared-mime-info
Requires:       m4
Recommends:     pcb-doc = %{version}

%description
pcb is a CAD (computer aided design) program for the physical design
of printed circuit boards.  It has an autorouter, a trace optimizer a
design rule checker and many more features. It can create RS-274-X
(Gerber), Postscript, EPS and PNG output files.

%package doc
Summary:        Documentation for PCB, An interactive printed circuit board editor
Group:          Documentation/Other
Requires(pre):  %install_info_prereq
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description doc
This package contains the documentation of PCB, an interactive printed circuit
board editor.

%prep
%setup -q

%build
# pcb does not like the -D_FORTIFY_SOURCE=2 option, remove it.
export CFLAGS=$(echo %{optflags} | sed "s,-D_FORTIFY_SOURCE=2,,g")
%configure  \
            --docdir=%{_docdir}/%{name} \
            --disable-rpath \
            --enable-dbus \
            --disable-update-desktop-database \
            --disable-update-mime-database \
            --enable-gl \
            --enable-toporouter \
            --enable-toporouter-output

make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file -r %{name} Education Engineering
%find_lang %{name}

# acpcircuits support
# http://www.apcircuits.com/resources/links/pcb_unix.html
unzip tools/apctools.zip
install -p -m 755 apc*.pl  %{buildroot}%{_datadir}/%{name}/tools
rm -f %{buildroot}%{_datadir}/%{name}/tools/apctools.zip

# pcb2ncap convert isn't neened
rm -f %{buildroot}%{_datadir}/%{name}/tools/pcb2ncap.tgz

# fix W: non-executable-script
chmod 755 %{buildroot}%{_datadir}/%{name}/tools/{Merge*,PCB2HPGL,pcbdiff,tgo2pcb.tcl}

# remove static library, header and source file
rm -f %{buildroot}%{_libdir}/libgts.a \
      %{buildroot}%{_includedir}/gts.h \
      %{buildroot}%{_datadir}/%{name}/tools/gerbertotk.c

%post
%mime_database_post

%postun
%mime_database_postun

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%doc NEWS README
%if 0%{?suse_version} > 1330
%license COPYING
%else
%doc COPYING
%exclude %{_docdir}/%{name}/examples/
%exclude %{_docdir}/%{name}/tutorial/
%exclude %{_docdir}/%{name}/*.html
%exclude %{_docdir}/%{name}/*.pdf
%exclude %{_docdir}/%{name}/*.png
%endif
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/gEDA/
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/applications/pcb.desktop
%{_datadir}/mime/packages/*
%{_mandir}/man1/%{name}*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/pcb.appdata.xml

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/examples/
%{_docdir}/%{name}/tutorial/
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.pdf
%{_docdir}/%{name}/*.png
%{_infodir}/%{name}.info*

%changelog
