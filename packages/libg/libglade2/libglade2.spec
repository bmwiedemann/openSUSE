#
# spec file for package libglade2
#
# Copyright (c) 2022 SUSE LLC
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


%define _name libglade
Name:           libglade2
Version:        2.6.4
Release:        0
Summary:        Glade Library Compatible with the GNOME 2.x Desktop Platform
# NOTE: on upgrade to a new upstream version, change the Obsoletes from <= to <
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.daa.com.au/~james/gnome/
Source:         https://download.gnome.org/sources/libglade/2.6/libglade-2.6.4.tar.bz2
# PATCH-FEATURE-OPENSUSE libglade2-python3.patch dimstar@opensuse.org -- Use python3
Patch0:         libglade2-python3.patch
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  python3-base
BuildRequires:  python3-xml

%description
This library allows you to load Glade interface files in a program at
runtime. It does not require that you use Glade, but Glade is the
easiest way to create the interface files.  For an idea of how to use
the library, see the documentation, especially
%{_docdir}/libglade/test-libgladee.c and the glade-xml.h
include, which is in the libglade package.

%package -n libglade-2_0-0
Summary:        Glade Library Compatible with the GNOME 2.x Desktop Platform
Group:          Development/Libraries/GNOME
Provides:       %{name} = %{version}
# Note: we keep <= (and a rpmlint warning...) until we get a version higher than 2.6.4 (when this provides/obsoletes was introduced)
Obsoletes:      %{name} <= %{version}
#

%description -n libglade-2_0-0
This library allows you to load Glade interface files in a program at
runtime. It does not require that you use Glade, but Glade is the
easiest way to create the interface files.  For an idea of how to use
the library, see the documentation, especially
%{_docdir}/libglade/test-libgladee.c and the glade-xml.h
include, which is in the libglade package.

%package devel
Summary:        Include files and libraries mandatory for development
Group:          Development/Libraries/GNOME
Requires:       libglade-2_0-0 = %{version}
#

%description devel
This package contains all necessary include files and libraries needed
to compile and link applications that use libglade2.

%package doc
Summary:        Documentation for the Glade library
Group:          Development/Libraries/GNOME
Requires:       libglade-2_0-0 = %{version}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
This package contains documentation and examples for the Glade library.

%prep
%setup -q -n %{_name}-%{version}
%patch0

%build
export PYTHON=%{_bindir}/python3
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/libglade/2.0
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{?suse_version} > 1020
%fdupes %{buildroot}
%endif

%post -n libglade-2_0-0 -p /sbin/ldconfig
%postun -n libglade-2_0-0 -p /sbin/ldconfig

%files -n libglade-2_0-0
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libglade-2.0.so.*
%dir %{_libdir}/libglade
%dir %{_libdir}/libglade/2.0

%files devel
%{_bindir}/*
%{_includedir}/libglade-2.0
%{_libdir}/libglade-2.0.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/gtk-doc/html/libglade
%{_datadir}/xml/libglade

%changelog
