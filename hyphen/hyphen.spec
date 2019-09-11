#
# spec file for package hyphen
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


%define libname libhyphen0
Name:           hyphen
Version:        2.8.8
Release:        0
Summary:        A text hyphenation library
License:        GPL-2.0+ or LGPL-2.0+ or MPL-1.1+
Group:          System/Libraries
Url:            http://hunspell.sourceforge.net/
Source0:        http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Hyphen is a library for high quality hyphenation and justification.

%package -n %{libname}
Summary:        A simple thesaurus for Libreoffice
Group:          System/Libraries

%description -n %{libname}
Hyphen is a library for high quality hyphenation and justification.

%package devel
Summary:        Files for Developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Hyphen is a library for high quality hyphenation and justification.

This package contains the %{name} development files.

%prep
%setup -q

%build
%configure \
	--disable-static
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

find %{buildroot} -type f -name "*.la" -delete -print

# Provided by myspell-dicts package
rm %{buildroot}%{_datadir}/hyphen/hyph_en_US.dic

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README README.hyphen README.nonstandard TODO
%dir %{_datadir}/hyphen

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/%{name}*
%{_bindir}/substrings.pl

%changelog
