#
# spec file for package geda-gaf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libgeda_major 45
%define libgedacairo_major 1
Name:           geda-gaf
Version:        1.9.2
Release:        0
Summary:        Electronic Design Automation Toolsuite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            http://geda-project.org/
Source0:        http://ftp.geda-project.org/geda-gaf/unstable/v1.9/%{version}/%{name}-%{version}.tar.gz
Source1:        geda-gaf-rpmlintrc
# PATCH-FIX-OPENSUSE gschem-doc-path.patch -- set correct path to documentation
Patch0:         gschem-doc-path.patch
# PATCH-FIX-OPENSUSE grenum-no-build-time.patch -- fix "W: file-contains-date-and-time"
Patch1:         grenum-no-build-time.patch
# PATCH-FIX-UPSTREAM fix-gxyrs-utility.patch bnc#1078838 -- fix unittests on tumbleweed
Patch2:         fix-gxyrs-utility.patch
# PATCH-FIX-OPENSUSE geda-gaf-disable-failing-tests.patch -- disable failing tests
Patch3:         geda-gaf-disable-failing-tests.patch
# PATCH-FIX-OPENSUSE geda-gaf-enable-guile-2.2.patch -- enable guile-2.2 (for Factory/TW)
Patch4:         geda-gaf-enable-guile-2.2.patch
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gettext-tools
BuildRequires:  groff
BuildRequires:  gtk2-devel
BuildRequires:  guile-devel
BuildRequires:  intltool
BuildRequires:  libstroke-devel
# Required for Patch4
BuildRequires:  libtool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkg-config
BuildRequires:  shared-mime-info
BuildRequires:  transfig
BuildRequires:  update-desktop-files
Requires:       geda-gattrib = %{version}
Requires:       geda-gnetlist = %{version}
Requires:       geda-gschem = %{version}
Requires:       geda-gsymcheck = %{version}
Requires:       geda-symbols = %{version}
Requires:       geda-utils = %{version}
Requires:       geda-xgsch2pcb
Requires:       pcb
Recommends:     geda-doc
Recommends:     geda-examples

%description
This is a toolkit of Electronic Design Automation tools. They are
used for circuit design, schematic capture, simulation, prototyping,
and production.

%package     -n libgeda%{libgeda_major}
Summary:        Basic Library that is used by several gEDA programs
License:        GPL-2.0-or-later
Group:          System/Libraries
Requires:       libgeda-data >= %{version}

%description -n libgeda%{libgeda_major}
This package provides the basic library for several gEDA programs
related to electronic design automation.

%package     -n libgeda-data
Summary:        Data for basic Library that is used by several gEDA programs
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
# Existed up to Leap 15.1:
Obsoletes:      libgeda42-data <= %{version}
# In fact, translations are not provided, but previous versions vere
# incorrectly packaged, and there is no better way to proceed:
Provides:       libgeda42-data <= %{version}
# This existed only in OBS project electronics:
Obsoletes:      libgeda45-data <= %{version}
Provides:       libgeda45-data <= %{version}
BuildArch:      noarch

%description -n libgeda-data
This package provides data files for libgeda such as icons required by several
gEDA programs.

%package     -n libgeda-devel
Summary:        Development files for gEDA
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       gtk2-devel
Requires:       guile-devel
Requires:       libgeda%{libgeda_major} = %{version}
Requires:       libjpeg-devel
Requires:       libpng-devel

%description -n libgeda-devel
This package provides headers for libgeda.

%package     -n libgedacairo%{libgedacairo_major}
Summary:        Schematic renderer library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libgedacairo%{libgedacairo_major}
This package provides a schematic renderer library.

%package     -n libgedacairo-devel
Summary:        Development files for libgedacairo
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libgedacairo%{libgedacairo_major} = %{version}

%description -n libgedacairo-devel
This package provides headers for libgedacairo.

%package     -n geda-base
Summary:        Common code for gEDA applications
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics

%description -n geda-base
This package provides code common to all gEDA applications.

%package     -n geda-doc
Summary:        Documentation Files for the gEDA Suite
License:        GFDL-1.2-only
Group:          Documentation/Other
BuildArch:      noarch

%description -n geda-doc
This package contains the documentation of the gEDA suite.
The documentation is a snapshot of the gEDA wiki located at
http://wiki.geda-project.org/.

%package     -n geda-examples
Summary:        Some Example Files for the gEDA suite
License:        GPL-2.0-or-later
Group:          Documentation/Other
Requires:       geda-symbols = %{version}
BuildArch:      noarch

%description -n geda-examples
Package with four example projects realized with gEDA.

%package     -n geda-gattrib
Summary:        Symbol and Schematic Attribute Editor of the gEDA Suite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Requires:       geda-base = %{version}
Requires:       geda-symbols = %{version}

%description -n geda-gattrib
With gattrib, attributes of schematic or symbol files can be edited. It has
a spreadsheet-like GUI. gattrib is part of the gEDA suite.

%package     -n geda-gnetlist
Summary:        Schematic Netlist Generator Program of the gEDA Suite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Requires:       geda-base = %{version}
Requires:       geda-symbols = %{version}

%description -n geda-gnetlist
gnetlist is the netlist generator program of the gEDA suite. It reads
schematic files and converts them into different connecitity netlists.
gnetlist has several backends to generate netlists for PCB, Spice,
VHDL, Verilog and many other programs.

%package     -n geda-gschem
Summary:        Schematic Capture Program of the gEDA Suite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Requires:       geda-base = %{version}
Requires:       geda-symbols = %{version}
Recommends:     geda-doc

%description -n geda-gschem
gschem is the schematic capture program of the gEDA suite.
Schematics for simulation, PCB production or documentation can be drawn.
Hierarchical schematics are supported.

%package     -n geda-gsymcheck
Summary:        Schematic Symbol Checker Program of the gEDA Suite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Requires:       geda-base = %{version}
Requires:       geda-symbols = %{version}

%description -n geda-gsymcheck
gsymcheck is a symbol checker of the gEDA suite. It checks symbols for
missing or duplicate pins, missing attributes and definitions.

%package     -n geda-symbols
Summary:        Schematic Symbols for the gEDA Suite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
BuildArch:      noarch

%description -n geda-symbols
Package with schematic symbols for the gEDA suite.

%package     -n geda-utils
Summary:        Various Utilities and Scripts for the gEDA Suite
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Requires:       geda-base = %{version}
Requires:       geda-symbols = %{version}

%description -n geda-utils
This utility package contains several helper utilities for the gEDA
suite, containing an advanced PCB netlister gsch2pcb, symbol converters and
creators, refdes renumbering tools and many others.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# export LDFLAGS="-lm $LDFLAGS"
# Required for Patch4
./autogen.sh
%configure  \
            --docdir=%{_docdir}/%{name} \
            --disable-static \
            --disable-rpath \
            --disable-update-xdg-database
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%suse_update_desktop_file -r geda-gschem Education Engineering
%suse_update_desktop_file -r geda-gattrib Education Engineering

%fdupes -s %{buildroot}%{_docdir}/geda-gaf/examples
%fdupes -s %{buildroot}%{_docdir}/geda-gaf/wiki

%find_lang geda-gaf
%find_lang geda-gattrib
%find_lang geda-gnetlist
%find_lang geda-gschem
%find_lang geda-gsymcheck
%find_lang libgeda%{libgeda_major}

%check
make %{?_smp_mflags} check

%post -n libgeda%{libgeda_major} -p /sbin/ldconfig
%postun -n libgeda%{libgeda_major} -p /sbin/ldconfig
%post -n libgedacairo%{libgedacairo_major} -p /sbin/ldconfig
%postun -n libgedacairo%{libgedacairo_major} -p /sbin/ldconfig
%post -n libgeda-data
%install_info --info-dir=%{_infodir} %{_infodir}/geda-scheme.info.gz
%{_bindir}/update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :

%postun -n libgeda-data
%install_info_delete --info-dir=%{_infodir} %{_infodir}/geda-scheme.info.gz
%{_bindir}/update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :

%files
%doc AUTHORS ChangeLog NEWS README

%files -n libgeda%{libgeda_major} -f libgeda%{libgeda_major}.lang
%{_libdir}/libgeda.so.%{libgeda_major}*

%files -n libgeda-data
%dir %{_datadir}/gEDA
%dir %{_datadir}/gEDA/scheme
%dir %{_datadir}/gEDA/icons
%dir %{_datadir}/gEDA/icons/hicolor
%dir %{_datadir}/gEDA/icons/hicolor/16x16
%dir %{_datadir}/gEDA/icons/hicolor/22x22
%{_datadir}/gEDA/gafrc.d
%{_datadir}/gEDA/system-gafrc
%{_datadir}/gEDA/print-colormap-lightbg
%{_datadir}/gEDA/print-colormap-darkbg
%{_datadir}/gEDA/scheme/geda.scm
%{_datadir}/gEDA/scheme/color-map.scm
%{_datadir}/gEDA/icons/hicolor/*/actions*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/libgeda.xml
%{_infodir}/geda-scheme.info%{?ext_info}

%files -n libgeda-devel
%{_includedir}/libgeda/
%{_libdir}/libgeda.so
%{_libdir}/pkgconfig/libgeda.pc

%files -n libgedacairo%{libgedacairo_major}
%{_libdir}/libgedacairo.so.%{libgedacairo_major}*

%files -n libgedacairo-devel
%{_includedir}/libgedacairo/
%{_libdir}/libgedacairo.so
%{_libdir}/pkgconfig/libgedacairo.pc

%files -n geda-doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/gedadocs.html
%doc %{_docdir}/%{name}/nc.pdf
%doc %{_docdir}/%{name}/man/
%doc %{_docdir}/%{name}/readmes/
%doc %{_docdir}/%{name}/wiki/

%files -n geda-examples
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/examples/

%files -n geda-gattrib -f geda-gattrib.lang
%{_bindir}/gattrib
%{_datadir}/gEDA/system-gattribrc
%{_datadir}/gEDA/gattrib-menus.xml
%{_datadir}/icons/hicolor/*/apps/geda-gattrib.*
%{_datadir}/applications/geda-gattrib.desktop
%{_mandir}/man1/gattrib.1%{?ext_man}

%files -n geda-gnetlist -f geda-gnetlist.lang
%{_bindir}/gnetlist
%{_datadir}/gEDA/scheme/gnetlist
%{_datadir}/gEDA/system-gnetlistrc
%{_datadir}/gEDA/scheme/gnet-*.scm
%{_datadir}/gEDA/scheme/gnetlist-post.scm
%{_datadir}/gEDA/scheme/gnetlist.scm
%{_datadir}/gEDA/scheme/partslist-common.scm
%{_mandir}/man1/gnetlist.1%{?ext_man}

%files -n geda-gschem -f geda-gschem.lang
%dir %{_datadir}/gEDA/scheme/gschem
%dir %{_datadir}/gEDA/scheme/gschem/core
%{_bindir}/gschem
%{_datadir}/gEDA/system-gschemrc
%{_datadir}/gEDA/gschem-gtkrc
%{_datadir}/gEDA/gschem-colormap-darkbg
%{_datadir}/gEDA/gschem-colormap-lightbg
%{_datadir}/gEDA/gschem-colormap-bw
%{_datadir}/gEDA/scheme/pcb.scm
%{_datadir}/gEDA/scheme/auto-uref.scm
%{_datadir}/gEDA/scheme/auto-refdes.scm
%{_datadir}/gEDA/scheme/gschem.scm
%{_datadir}/gEDA/scheme/auto-place-attribs.scm
%{_datadir}/gEDA/scheme/auto-place-netname.scm
%{_datadir}/gEDA/scheme/print.scm
%{_datadir}/gEDA/scheme/default-attrib-positions.scm
%{_datadir}/gEDA/scheme/generate_netlist.scm
%{_datadir}/gEDA/scheme/geda-deprecated-config.scm
%{_datadir}/gEDA/scheme/image.scm
%{_datadir}/gEDA/scheme/list-keys.scm
%{_datadir}/gEDA/scheme/spice-common.scm
%{_datadir}/gEDA/scheme/print-NB-attribs.scm
%{_datadir}/gEDA/scheme/gschem/action.scm
%{_datadir}/gEDA/scheme/gschem/attrib.scm
%{_datadir}/gEDA/scheme/gschem/builtins.scm
%{_datadir}/gEDA/scheme/gschem/core/gettext.scm
%{_datadir}/gEDA/scheme/gschem/deprecated.scm
%{_datadir}/gEDA/scheme/gschem/gschemdoc.scm
%{_datadir}/gEDA/scheme/gschem/hook.scm
%{_datadir}/gEDA/scheme/gschem/keymap.scm
%{_datadir}/gEDA/scheme/gschem/selection.scm
%{_datadir}/gEDA/scheme/gschem/util.scm
%{_datadir}/gEDA/scheme/gschem/window.scm
%{_datadir}/gEDA/bitmap
%{_datadir}/icons/hicolor/*/apps/geda-gschem.*
%{_datadir}/applications/geda-gschem.desktop
%{_mandir}/man1/gschem.1%{?ext_man}

%files -n geda-base
%license COPYING
%dir %{_datadir}/gEDA/scheme/geda
%dir %{_datadir}/gEDA/scheme/geda/core
%{_datadir}/gEDA/scheme/geda/attrib.scm
%{_datadir}/gEDA/scheme/geda/config.scm
%{_datadir}/gEDA/scheme/geda/deprecated.scm
%{_datadir}/gEDA/scheme/geda/object.scm
%{_datadir}/gEDA/scheme/geda/os.scm
%{_datadir}/gEDA/scheme/geda/page.scm
%{_datadir}/gEDA/scheme/geda/core/gettext.scm

%files -n geda-gsymcheck -f geda-gsymcheck.lang
%{_bindir}/gsymcheck
%{_datadir}/gEDA/system-gsymcheckrc
%{_mandir}/man1/gsymcheck.1%{?ext_man}

%files -n geda-symbols
%{_datadir}/gEDA/sym

%files -n geda-utils -f geda-gaf.lang
%{_bindir}/gaf
%{_bindir}/garchive
%{_bindir}/grenum
%{_bindir}/gsch2pcb
%{_bindir}/gschlas
%{_bindir}/gsymfix
%{_bindir}/gxyrs
%{_bindir}/pcb_backannotate
%{_bindir}/refdes_renum
%{_bindir}/schdiff
%{_bindir}/tragesym
%{_mandir}/man1/gaf.1%{?ext_man}
%{_mandir}/man1/garchive.1%{?ext_man}
%{_mandir}/man1/grenum.1%{?ext_man}
%{_mandir}/man1/gsch2pcb.1%{?ext_man}
%{_mandir}/man1/gschlas.1%{?ext_man}
%{_mandir}/man1/gsymfix.1%{?ext_man}
%{_mandir}/man1/gxyrs.1%{?ext_man}
%{_mandir}/man1/pcb_backannotate.1%{?ext_man}
%{_mandir}/man1/refdes_renum.1%{?ext_man}
%{_mandir}/man1/schdiff.1%{?ext_man}
%{_mandir}/man1/tragesym.1%{?ext_man}
%{_datadir}/gEDA/perl/
%{_datadir}/gEDA/system-gschlasrc

%changelog
