#
# spec file for package libverto-glib
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


%define sover   1
%define src_name libverto
Name:           libverto-glib
Version:        0.2.6
Release:        0
Summary:        Main loop abstraction library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://fedorahosted.org/libverto
Source:         http://fedorahosted.org/releases/l/i/%{src_name}/%{src_name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libverto) = %{version}

%description
libverto provides a way for libraries to expose asynchronous
interfaces without having to choose a particular event loop,
offloading this decision to the end application which consumes the
library.

If you are packaging an application, not library, based on libverto,
you should depend either on a specific implementation module or you
can depend on the virtual provides 'libverto-module-base'. This will
ensure that you have at least one module installed that provides io,
timeout and signal functionality. Currently glib is the only module
that does not provide these three because it lacks signal. However,
glib will support signal in the future.

%package        -n %{src_name}-glib%{sover}
Summary:        Backend module for libverto -- glib
Group:          Development/Libraries/C and C++
Requires:       libverto%{sover} = %{version}

%description    -n %{src_name}-glib%{sover}
Module for libverto which provides integration with glib.

This package does NOT yet provide libverto-module-base.

%package        -n %{src_name}-glib-devel
Summary:        Development files for libverto-glib%{sover}
Group:          Development/Libraries/C and C++
Requires:       %{src_name}-devel%{?_isa} = %{version}
Requires:       %{src_name}-glib%{sover}%{?_isa} = %{version}

%description    -n %{src_name}-glib-devel
The libverto-glib-devel package contains libraries and header files
for developing applications that use libverto-glib.

%prep
%setup -q -n %{src_name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name '*.so.*T' -delete

# stuff in libverto already
rm -rf %{buildroot}/%{_includedir}/verto-module.h %{buildroot}/%{_includedir}/verto.h
rm -rf %{buildroot}/%{_libdir}/%{src_name}.so*
rm -rf %{buildroot}/%{_libdir}/pkgconfig/%{src_name}.pc

%post -n %{src_name}-glib%{sover} -p /sbin/ldconfig

%postun -n %{src_name}-glib%{sover} -p /sbin/ldconfig

%files -n %{src_name}-glib%{sover}
%defattr(-,root,root)
%{_libdir}/%{src_name}-glib.so.*

%files -n %{src_name}-glib-devel
%defattr(-,root,root)
%{_includedir}/verto-glib.h
%{_libdir}/%{src_name}-glib.so
%{_libdir}/pkgconfig/%{src_name}-glib.pc

%changelog
