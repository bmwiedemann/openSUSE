#
# spec file for package libargtable2
#
# Copyright (c) 2024 SUSE LLC
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


%define name1   argtable
%define name2   argtable2
%define soname  0
%define oversion 13

Name:           libargtable2
Version:        2.13
Release:        0
Summary:        ANSI C Command line parser library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://argtable.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name1}/%{version}/%{name2}-%{oversion}.tar.gz
Patch0:         %{name}-Makefile.in.patch
Patch1:         implicit-declaration.patch
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Argtable is an ANSI C library for parsing GNU style command line options with a
minimum of fuss. It enables a program's command line syntax to be defined in the
source code as an array of argtable structs. The command line is then parsed
according to that specification and the resulting values are returned in those same
structs where they are accessible to the main program. Both tagged (-v, --verbose,
--foo=bar) and untagged arguments are supported, as are multiple instances of each
argument. Syntax error handling is automatic and the library also provides the means
for generating a textual description of the command line syntax.

%package -n %{name}-%{soname}
Summary:        Command line parsing library
Group:          System/Libraries

%description -n %{name}-%{soname}
The libargtable2 package contains libraries for libargtable.

%package devel
Summary:        Development files for argtable, a command line parsing library
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{soname} = %{version}

%description devel
The libargtable2-devel package contains libraries and header files for
developing applications that use libargtable.

%prep
%autosetup -p0 -n %{name2}-%{oversion}

%build
%configure --disable-static --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

# install man
install -Dm 0644 doc/%{name1}.3 %{buildroot}%{_mandir}/man3/%{name1}.3
install -Dm 0644 doc/%{name2}.3 %{buildroot}%{_mandir}/man3/%{name2}.3

find %{buildroot}%{_libdir} -type f -name '*.la' -delete

%fdupes -s %{buildroot}%{_prefix}
%fdupes -s %{buildroot}%{_mandir}

%post -n %{name}-%{soname} -p /sbin/ldconfig

%postun -n %{name}-%{soname} -p /sbin/ldconfig

%files -n %{name}-%{soname}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog doc/*.gif doc/*.html doc/*.pdf doc/*.ps example
%{_mandir}/man3/%{name1}.3%{ext_man}
%{_mandir}/man3/%{name2}.3%{ext_man}
%{_includedir}/%{name2}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name2}.pc

%changelog
