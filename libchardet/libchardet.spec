#
# spec file for package libchardet
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname   libchardet1
%define _name   chardet
Name:           libchardet
Version:        1.0.5
Release:        0
Summary:        Mozilla Universal Chardet library
License:        MPL-1.1
Group:          Development/Libraries/C and C++
Url:            https://github.com/Joungkyun/libchardet
Source:         https://github.com/Joungkyun/libchardet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake >= 1.12
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
Mozilla's Universal Charset Detector C/C++ API.

%package -n %{lname}
Summary:        Mozilla Universal Chardet library
Group:          System/Libraries

%description -n %{lname}
Mozilla's Universal Charset Detector C/C++ API.

%package devel
Summary:        Development files of libchardet
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The libchardet development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libchardet.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ \
  %{buildroot}%{_docdir}/%{name}/

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_bindir}/%{_name}-config
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{_name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{_name}.pc
%dir %{_mandir}/ko/
%dir %{_mandir}/ko/man3/
%{_mandir}/*/man?/detect*.?%{?ext_man}
%{_mandir}/man?/detect*.?%{?ext_man}

%changelog
