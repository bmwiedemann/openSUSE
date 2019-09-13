#
# spec file for package libLASi
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


%define sover   2
Name:           libLASi
Version:        1.1.3
Release:        0
Summary:        Library to write UTF-8 strings to Postscript stream
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://unifont.org/lasi/
Source:         http://download.sourceforge.net/lasi/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libLASi-link_gobject2.patch aloisio@gmx.com -- self-explanatory
Patch0:         libLASi-link_gobject2.patch
# PATCH-FEATURE-OPENSUSE libLASi-do_not_build_examples.patch
Patch1:         libLASi-do_not_build_examples.patch
BuildRequires:  cmake >= 3.13.2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pango)

%description
libLASi is a library written by Larry Siden that provides a C++ stream
output interface (with operator <<) for creating Postscript
documents that can contain characters from any of the scripts and
symbol blocks supported in Unicode and by Owen Taylor's Pango layout
engine. The library accomodates right-to-left scripts such as Arabic
and Hebrew as easily as left-to-right scripts. Indic and Indic-derived
Complex Text Layout (CTL) scripts, such as Devanagari, Thai, Lao, and
Tibetan are supported to the extent provided by Pango and by the
OpenType fonts installed on your system. All of this is provided
without need for any special configuration or layout calculation on
the programmer's part.

Although the capability to produce Unicode-based multilingual
Postscript documents exists in large Open Source application framework
libraries such as GTK+, QT, and KDE, libLASi was designed for projects
which require the ability to produce Postscript independent of any one
application framework.

%package -n %{name}%{sover}
Summary:        Library to write UTF-8 strings to Postscript stream
Group:          Development/Libraries/C and C++

%description -n %{name}%{sover}
libLASi is a library written that provides a C++ stream output
interface for creating Postscript documents that can contain
characters from any of the scripts and symbol blocks supported in
Unicode and by the Pango layout engine. The library accomodates
right-to-left scripts, Complex Text Layout scripts, as supported to
the extent provided by Pango and by the OpenType fonts installed on
your system.

This package provides the shared libraries for LASi.

%package devel
Summary:        Library to write UTF-8 strings to Postscript stream
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
libLASi is a library written by Larry Siden that provides a C++ stream
output interface (with operator <<) for creating Postscript
documents that can contain characters from any of the scripts and
symbol blocks supported in Unicode and by Owen Taylor's Pango layout
engine. The library accomodates right-to-left scripts such as Arabic
and Hebrew as easily as left-to-right scripts. Indic and Indic-derived
Complex Text Layout (CTL) scripts, such as Devanagari, Thai, Lao, and
Tibetan are supported to the extent provided by Pango and by the
OpenType fonts installed on your system. All of this is provided
without need for any special configuration or layout calculation on
the programmer's part.

Although the capability to produce Unicode-based multilingual
Postscript documents exists in large Open Source application framework
libraries such as GTK+, QT, and KDE, libLASi was designed for projects
which require the ability to produce Postscript independent of any one
application framework.

This package provides the header files necessary for development with
%{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -Ddocdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}

%install
%cmake_install
%fdupes %{buildroot}%{_docdir}/%{name}-%{version}/

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%if 0%{?suse_version} > 1315
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS ChangeLog.* NEWS README README.release
%{_libdir}/%{name}.so.%{sover}*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/lasi.pc
%{_includedir}/LASi.h
%{_datadir}/lasi%{version}/
%{_defaultdocdir}/%{name}-%{version}/

%changelog
