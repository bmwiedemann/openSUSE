#
# spec file for package glpk
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover   40
%define lname   libglpk%{sover}
Name:           glpk
Version:        4.65
Release:        0
Summary:        GNU Linear Programming Kit
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/glpk/glpk.html
Source0:        https://ftp.gnu.org/gnu/glpk/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/glpk/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch0:         glpk-no_random_return.patch
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  libiodbc-devel
BuildRequires:  libmariadb-devel
BuildRequires:  libtool
BuildRequires:  texlive

%description
The GLPK package is intended for solving large-scale linear
programming, mixed integer programming, and other related problems. It
is a set of routines written in ANSI C and organized in the form of a
callable library.

%package        devel
Summary:        GNU Linear Programming Kit
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description    devel
The GLPK package is intended for solving large-scale linear
programming, mixed integer programming, and other related problems. It
is a set of routines written in ANSI C and organized in the form of a
callable library.

%package     -n %{lname}
Summary:        GNU Linear Programming Kit
Group:          System/Libraries

%description -n %{lname}
The GLPK package is intended for solving large-scale linear
programming, mixed integer programming, and other related problems. It
is a set of routines written in ANSI C and organized in the form of a
callable library.

%package doc
Summary:        GNU Linear Programming Kit
Group:          Documentation/Other
%if 0%{?suse_version} >= 1120 || 0%{?fedora_version}
BuildArch:      noarch
%endif

%description doc
The GLPK package is intended for solving large-scale linear
programming, mixed integer programming, and other related problems. It
is a set of routines written in ANSI C and organized in the form of a
callable library.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
  --with-gmp \
  --enable-dl \
  --enable-odbc \
  --enable-mysql \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%{_bindir}/glpsol

%files -n %{lname}
%license AUTHORS COPYING
%{_libdir}/libglpk.so.%{sover}*

%files devel
%{_includedir}/*
%{_libdir}/libglpk.so

%files doc
%doc ChangeLog NEWS README
%doc doc/*.txt doc/*.pdf
%doc examples/*.mod
%doc examples/*.c
%doc examples/*.dat
%doc examples/*.mps
%doc examples/*.lp

%changelog
