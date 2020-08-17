#
# spec file for package fox16
#
# Copyright (c) 2020 SUSE LLC
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
BuildRequires:  doxygen
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)
#
# SUSE requires
#
%if 0%{?suse_version}
BuildRequires:  cups-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-Mesa-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  xorg-x11-libXfixes-devel
%endif
#
# Mandriva Requires
#
%if 0%{?mandriva_version}
BuildRequires:  cups
BuildRequires:  cups-common
BuildRequires:  libmesaglu-devel
BuildRequires:  libxext-devel
BuildRequires:  libxft-devel
BuildRequires:  xorg-x11
%endif
#
# Fedora Requires
#
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?scientificlinux_version}
BuildRequires:  cups-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  xorg-x11-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%if 0%{?centos_version} >= 800
%global debug_package %{nil}
%endif

%package devel
Summary:        Development Files and Documentation for the FOX GUI Toolkit 1.6
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}
Requires:       bzip2
Requires:       cups-devel
Requires:       cups-libs
Requires:       fontconfig-devel
Requires:       freetype2-devel
Requires:       glibc-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       libtiff-devel
Requires:       xorg-x11-devel
Requires:       zlib-devel
Provides:       fox-devel = %{version}-%{release}
Requires:       pkgconfig(glu)
#
# SUSE requires
#
%if 0%{?suse_version}
Requires:       expat
Requires:       libbz2-devel
Requires:       libexpat-devel
Requires:       xorg-x11-Mesa-devel
Requires:       xorg-x11-libX11-devel
Requires:       xorg-x11-libXau-devel
Requires:       xorg-x11-libXdmcp-devel
Requires:       xorg-x11-libXext-devel
Requires:       xorg-x11-libXfixes-devel
Requires:       xorg-x11-libXrender-devel
Requires:       xorg-x11-libs
%endif
#
# Fedora Requires
#
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?scientificlinux_version}
Requires:       bzip2-devel
Requires:       cups-devel
Requires:       libGLU-devel
Requires:       libXext-devel
Requires:       libXft-devel
Requires:       libXi-devel
Requires:       xorg-x11-devel
%endif

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
%setup -q -n fox-%{version}
%patch1
%patch2

%build
autoreconf -fi
%if 0%{?centos_version} >= 800
export CFLAGS="%optflags -fPIC"
export CXXFLAGS="%optflags -fPIC"
export LDFLAGS="-fPIC"
%endif
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
%if 0%{?mandriva_version}
    --with-opengl="no" \
%endif
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
%if 0%{?suse_version}
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
%endif

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post devel
test -f %{_bindir}/fox-config || ln -s fox16-config %{_bindir}/fox-config
test -f %{_bindir}/reswrap || ln -s reswrap16 %{_bindir}/reswrap
test -f %{_mandir}/man1/reswrap.1.gz || ln -s reswrap16.1.gz %{_mandir}/man1/reswrap.1.gz

%files doc
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}

%files -n %{lname}
%defattr(-,root,root)
%license LICENSE*
%{_libdir}/libFOX-*.so.*
%{_libdir}/libCHART-*.so.*

%files devel
%defattr(-,root,root)
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
%defattr(-,root,root)
%{_libdir}/libFOX-*.a
%{_libdir}/libCHART-*.a

%files example-apps
%defattr(-,root,root)
%{_bindir}/Adie.stx
%{_bindir}/adie
%{_bindir}/PathFinder
%{_bindir}/calculator
%{_bindir}/shutterbug
%if 0%{?suse_version}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%endif
%{_mandir}/man1/adie*
%{_mandir}/man1/calculator*
%{_mandir}/man1/PathFinder*
%{_mandir}/man1/shutterbug*

%changelog
