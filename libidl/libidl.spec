#
# spec file for package libidl
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


%define _name libIDL
Name:           libidl
Version:        0.8.14
Release:        0
# NOTE: on upgrade to a new upstream version, change the Obsoletes from <= to < (here and in baselibs.conf)
Summary:        IDL Parsing Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://www.gnome.org
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{_name}/0.8/%{_name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig

%description
LibIDL is a small library for creating parse trees of CORBA
v2.2-compliant Interface Definition Language (IDL) files. IDL is a
specification for defining interfaces that can be used between
different CORBA implementations.

%package -n libIDL-2-0
Summary:        IDL Parsing Library
Group:          System/Libraries
Provides:       %{name} = %{version}
# Note: we keep <= (and a rpmlint warning...) until we get a version higher than 0.8.14 (when this provides/obsoletes was introduced)
Obsoletes:      %{name} <= %{version}
#

%description -n libIDL-2-0
LibIDL is a small library for creating parse trees of CORBA
v2.2-compliant Interface Definition Language (IDL) files. IDL is a
specification for defining interfaces that can be used between
different CORBA implementations.

%package devel
Summary:        Development files for the IDL parsing library
Group:          Development/Languages/Other
Requires:       libIDL-2-0 = %{version}
Requires(post): %{install_info_prereq}
Requires(postun): %{install_info_prereq}
#

%description devel
LibIDL is a small library for creating parse trees of CORBA v2.2
compliant Interface Definition Language (IDL) files, which is a
specification for defining interfaces which can be used between
different CORBA implementations.

%prep
%setup -q -n %{_name}-%{version}

%build
%if 0%{?mageia}
aclocal
autoconf
%endif
%configure\
%if 0%{?mageia}
	--disable-dependency-tracking \
%endif
	--disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_datadir}
mkdir %{buildroot}%{_datadir}/idl
rm -f %{buildroot}%{_infodir}/dir

%post -n libIDL-2-0 -p /sbin/ldconfig
%postun -n libIDL-2-0 -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{_name}2.info%{ext_info}

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{_name}2.info%{ext_info}

%files -n libIDL-2-0
%license COPYING
%doc ChangeLog AUTHORS README* NEWS BUGS tstidl.c
%{_libdir}/libIDL-2.so.*
# generic directory for idl files
%dir %{_datadir}/idl

%files devel
%{_bindir}/%{_name}-config-2
%{_includedir}/*
%{_infodir}/%{_name}2.info%{ext_info}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libIDL-2.so

%changelog
