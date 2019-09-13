#
# spec file for package mythes
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define libname libmythes-1_2-0
Name:           mythes
Version:        1.2.4
Release:        0
Summary:        A simple thesaurus for Libreoffice
License:        BSD-2-Clause and MIT
Group:          System/Libraries
Url:            http://hunspell.sourceforge.net/
Source0:        http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return
information on part of speech, meanings, and synonyms.

%package -n %{libname}
Summary:        A simple thesaurus for Libreoffice
Group:          System/Libraries

%description -n %{libname}
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return
information on part of speech, meanings, and synonyms.

%package devel
Summary:        Files for Developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return
information on part of speech, meanings, and synonyms.

This package contains the %{name} development files.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-rpath
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING README* AUTHORS
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}*
%{_bindir}/th_gen_idx.pl

%changelog
