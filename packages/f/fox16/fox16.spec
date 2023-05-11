#
# spec file for package fox16
#
# Copyright (c) 2023 SUSE LLC
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


%define         lname	libFOX-1_6-0

Name:           fox16
Version:        1.6.57
Release:        0
Summary:        Shared Libraries for the FOX Toolkit
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            http://www.fox-toolkit.org/
Source0:        ftp://ftp.fox-toolkit.org/pub/fox-%{version}.tar.gz
Source1:        calculator.png
Source2:        pathfinder.png
Source3:        adie.png
Source4:        fox16-rpmlintrc
Source5:        adie.desktop
Source6:        calculator.desktop
Source7:        pathfinder.desktop
# PATCH-FIX-OPENSUSE remove date from reswrap help to support build compare
Patch1:         fox16-remove_date_from_reswrap.patch
# PATCH-FIX-UPSTREAM add closing html tag
Patch2:         fox-1.6.26-missing_html_tag.patch
BuildRequires:  cups-devel
BuildRequires:  doxygen
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)

%description
FOX is a C++-based library for graphical user interface development.

FOX supports modern GUI features such as drag-and-drop, tooltips, tab
books, tree lists, icons, multiple document interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for 3D
graphics. Subclassing of basic FOX widgets allows for easy extension
beyond the built-in widgets by application writers.

%package -n %{lname}
Summary:        Shared libraries for the FOX toolkit 1.6
Group:          System/Libraries
Provides:       fox = %{version}-%{release}
# Added O/P in 13.2
Provides:       libfox1_6 = %{version}-%{release}
Obsoletes:      libfox1_6 < %{version}

%description -n %{lname}
This package contains the shared libraries needed
by applications compiled with the FOX GUI Toolkit.

%package devel
Summary:        Development Files and Documentation for the FOX GUI Toolkit 1.6
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}
Requires:       bzip2
Requires:       cups-devel
Requires:       cups-libs
Requires:       glibc-devel
Provides:       fox-devel = %{version}-%{release}

Requires:       expat
# lots of -l hardcoded in fox.pc without pkgconfig-level Requires tags
Requires:       libbz2-devel
Requires:       libexpat-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       libtiff-devel
Requires:       zlib-devel
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xft)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xproto)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(xrender)

%description devel
FOX is a C++-based library for graphical user interface development.

The devel package contains the files necessary to develop applications
using the FOX GUI toolkit: the header files, the reswrap resource
compiler, and manual pages.

%package doc
Summary:        Documentation for the FOX Toolkit 1.6
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
FOX is a C++-based library for graphical user interface development.

The doc subpackage contains the HTML documentation to the FOX toolkit 1.6.

%package devel-static
Summary:        Static Libraries for the FOX Toolkit 1.6
Group:          Development/Languages/C and C++
Requires:       %{name}-devel = %{version}
Provides:       %{name}-static = %{version}-%{release}
Obsoletes:      %{name}-static < 1.6.36
# skip dependency checks required by libtool .la files => skip-check-libtool-deps

%description devel-static
This package contains static libraries for developing applications
which are statically linked against the FOX libraries.

FOX is a C++-based library for graphical user interface development.

%package example-apps
Summary:        Example applications for the FOX GUI toolkit
Group:          Development/Languages/C and C++
Provides:       fox-example-apps = %{version}

%description example-apps
The example-apps package contains executables for several FOX-based
applications, including:

* Adie : Programmer's Text Editor

* calculator : Calculator Applet

* shutterbug : Screenshot Utility

* PathFinder : File Browser

%prep
%autosetup -p0 -n fox-%{version}

%build
autoreconf -fi
%configure  \
    --enable-threadsafe \
    --enable-release \
    --enable-cups \
    --with-xft \
    --with-x \
    --with-xcursor \
    --with-xrender \
    --with-xrandr \
    --with-opengl \
    --with-shape \
    --with-xshm \
    --without-profiling
make %{?_smp_mflags}

%install
%make_install
# install docu
pushd doc
doxygen -u doxygen.cfg
make docs
popd
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/html
# FIXME: to be done via configure
if [ -d %{buildroot}%{_datadir}/doc/fox-1.6 ]; then
    mv %{buildroot}%{_datadir}/doc/fox-1.6/* %{buildroot}%{_defaultdocdir}/%{name}/html/
    rm -rf %{buildroot}%{_datadir}/doc/fox-1.6
fi
install -m644 ADDITIONS AUTHORS LICENSE* README TRACING index.html %{buildroot}%{_defaultdocdir}/%{name}/
# install desktop files for example applications
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE6} %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE7} %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file calculator
%suse_update_desktop_file pathfinder
%suse_update_desktop_file adie

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%post devel
test -f %{_bindir}/fox-config || ln -s fox16-config %{_bindir}/fox-config
test -f %{_bindir}/reswrap || ln -s reswrap16 %{_bindir}/reswrap
test -f %{_mandir}/man1/reswrap.1.gz || ln -s reswrap16.1.gz %{_mandir}/man1/reswrap.1.gz

%files doc
%doc %{_defaultdocdir}/%{name}

%files -n %{lname}
%license LICENSE*
%{_libdir}/libFOX-*.so.*
%{_libdir}/libCHART-*.so.*

%files devel
%{_bindir}/reswrap
%{_bindir}/fox-config
%{_mandir}/man1/reswrap.1%{?ext_man}
%{_includedir}/fox-*/
%{_libdir}/pkgconfig/fox.pc
%{_libdir}/libFOX-*.la
%{_libdir}/libCHART-*.la
%{_libdir}/libFOX-*.so
%{_libdir}/libCHART-*.so

%files devel-static
%{_libdir}/libFOX-*.a
%{_libdir}/libCHART-*.a

%files example-apps
%{_bindir}/Adie.stx
%{_bindir}/adie
%{_bindir}/PathFinder
%{_bindir}/calculator
%{_bindir}/shutterbug
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/adie*
%{_mandir}/man1/calculator*
%{_mandir}/man1/PathFinder*
%{_mandir}/man1/shutterbug*

%changelog
