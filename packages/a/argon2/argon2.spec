#
# spec file for package argon2
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


%ifarch i686 x86_64
%define no_optimize 0
%else
%define no_optimize 1
%endif
# for convenience
%define make %__make %{?_smp_mflags} OPTFLAGS="%{optflags}" OPTTEST=%no_optimize LIB_ST= LIBRARY_REL=%_lib

%define lname libargon2-1
Name:           argon2
Version:        20190702
Release:        0
Summary:        The reference C implementation of Argon2
License:        Apache-2.0 OR CC0-1.0
Group:          Productivity/Networking/Security
URL:            https://github.com/P-H-C/phc-winner-argon2
Source:         https://github.com/P-H-C/phc-winner-argon2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE adjust-makefile.patch -- Allow setting optflags and file permissions of installed libraries
Patch1:         adjust-makefile.patch
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the reference C implementation of Argon2, the password-hashing function
that won the Password Hashing Competition (PHC) in 2015.

Argon2 is a password hashing function that is parametrized by a time cost, a
memory cost and a parallelism degree, used to guard against side-channel
attacks, attacks where lots of memory is available, or attacks where a lot of
processing is available.

%package doc
Summary:        Documentation for Argon2
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Documentation for Argon2, the password hashing function that won the Password
Hashing Competition (PHC) in 2015.

%package -n %{lname}
Summary:        The reference C implementation of Argon2
Group:          System/Libraries

%description -n %{lname}
Reference C implementation of Argon2, the password-hashing function
that won the Password Hashing Competition (PHC) in 2015.

%package devel
Summary:        Development files for argon2
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Headers for argon2, the reference C implementation of Argon2, the
password hashing function that won the Password Hashing Competition
(PHC) in 2015.

%prep
%setup -n phc-winner-argon2-%version
%patch1 -p1

%build
%make

%install
%make install DESTDIR=%{buildroot}

install -D -m 644 man/argon2.1 %{buildroot}%{_mandir}/man1/argon2.1

%check
%make test

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/argon2
%{_mandir}/man1/argon2.1%{ext_man}

%files doc
%defattr(-,root,root)
%doc argon2-specs.pdf

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/libargon2.so.1

%files devel
%defattr(-,root,root)
%{_includedir}/argon2.h
%{_libdir}/libargon2.so
%{_libdir}/pkgconfig/libargon2.pc

%changelog
