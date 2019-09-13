#
# spec file for package libguess
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Scorpio IT, Deidesheim, Germany
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


Name:           libguess
%define         libsoname %{name}1

Summary:        A high-speed character set detection library
License:        BSD-3-Clause
Group:          System/Libraries
Version:        1.2
Release:        0
Url:            https://github.com/kaniini/libguess
Source:         http://rabbit.dereferenced.org/~nenolod/distfiles/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libmowgli2-devel >= 2.0.0
BuildRequires:  pkg-config

%description
libguess employs discrete-finite automata to deduce the character
set of the input buffer. The advantage of this is that all
character sets can be checked in parallel, and quickly. Right now,
libguess passes a byte to each DFA on the same pass, meaning that
the winning character set can be deduced as efficiently as possible.

libguess is fully reentrant, using only local stack memory for DFA
operations.

%package -n %{libsoname}
Summary:        Shared library for libguess
Group:          System/Libraries

%description -n %{libsoname}
A high-speed character set detection library

This package contains the shared libguess library.

%package devel
Summary:        Development package for libguess
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       libmowgli2-devel >= 2.0.0
Requires:       pkg-config

%description devel
A high-speed character set detection library

This package contains the files needed to compile programs that use the
libguess library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

# Fatal error: "autoconf.h": No such file or directory in librcc build.
install -Dm 0644 src/%{name}/autoconf.h %{buildroot}%{_includedir}/%{name}/autoconf.h

%post -n %{libsoname} -p /sbin/ldconfig

%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
