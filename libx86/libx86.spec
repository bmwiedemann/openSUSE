#
# spec file for package libx86
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


Name:           libx86
Url:            http://www.codon.org.uk/~mjg59/libx86/
Version:        1.1
Release:        0
Summary:        x86 real-mode library
License:        MIT AND BSD-3-Clause
Group:          Development/Libraries/C and C++
Source:         http://www.codon.org.uk/~mjg59/%{name}/downloads/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64

%description
A library to provide support for making real-mode calls x86 calls. On
x86 hardware, vm86 mode is used. On other platforms, x86 emulation is
provided.

%package -n libx86-1
Summary:        x86 real-mode library
Group:          System/Libraries
Provides:       libx86 = %{version}
Obsoletes:      libx86 <= %{version}

%description -n libx86-1
A library to provide support for making real-mode calls x86 calls. On
x86 hardware, vm86 mode is used. On other platforms, x86 emulation is
provided.

%package devel
Requires:       libx86-1 = %{version}
Summary:        Development files for libx86
Group:          Development/Libraries/C and C++

%description devel
Development files for libx86. libx86 is a x86 real-mode library.

%package devel-static
Requires:       %{name}-devel = %{version}
Summary:        Static development library for libx86
Group:          Development/Libraries/C and C++

%description devel-static
Static development library for libx86. libx86 is a x86 real-mode library.

%prep
%setup

%build
# %ifnarch %ix86
MAKEARGS="BACKEND=x86emu"
# %endif
make CFLAGS="%{optflags} -DDEBUG -g -fPIC" $MAKEARGS LIBDIR=%{_libdir} \
	%{?_smp_mflags}

%install
%make_install LIBDIR=%{_libdir}
chmod a-x %{buildroot}/%{_libdir}/libx86.a

%post -n libx86-1 -p /sbin/ldconfig

%postun -n libx86-1 -p /sbin/ldconfig

%files -n libx86-1
%defattr (-,root,root)
%{_libdir}/libx86.so.*
%doc COPYRIGHT

%files devel
%defattr (-,root,root)
%{_libdir}/libx86.so
%_includedir/libx86.h

%files devel-static
%defattr (-,root,root)
%{_libdir}/libx86.a

%changelog
