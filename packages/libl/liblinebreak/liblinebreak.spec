#
# spec file for package liblinebreak
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           liblinebreak
Version:        2.1
Release:        0
Summary:        Unicode line-breaking library
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://sourceforge.net/projects/vimgadgets/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
liblinebreak is an implementation of the line breaking algorithm as
described in Unicode 6.0.0 Standard Annex 14, Revision 26, available
at http://www.unicode.org/reports/tr14/tr14-26.html

%package devel
Summary:        Development files for liblinebreak
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The liblinebreak-devel package contains libraries and header files for
developing applications that use liblinebreak.

%package -n liblinebreak2
Summary:        Unicode line-breaking library
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      liblinebreak2 < %{version}

%description -n liblinebreak2
liblinebreak is an implementation of the line breaking algorithm as
described in Unicode 6.0.0 Standard Annex 14, Revision 26, available
at http://www.unicode.org/reports/tr14/tr14-26.html

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%post -n liblinebreak2 -p /sbin/ldconfig

%postun -n liblinebreak2 -p /sbin/ldconfig

%files -n liblinebreak2
%defattr(-,root,root)
%doc ChangeLog LICENCE NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so

%changelog
