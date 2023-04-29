#
# spec file for package libverto
#
# Copyright (c) 2023 SUSE LLC
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


%define sover   1
Name:           libverto
Version:        0.3.2
Release:        0
Summary:        Main loop abstraction library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/latchset/libverto
Source:         https://github.com/latchset/libverto/releases/download/%{version}/libverto-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig

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

%package -n %{name}%{sover}
Summary:        Runtime libraries for libverto
Group:          Development/Libraries/C and C++

%description -n %{name}%{sover}
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

%package        devel
Summary:        Development files for libverto
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description    devel
The libverto-devel package contains libraries and header files
for developing applications that use libverto.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name '*.so.*T' -delete

%post -n libverto%{sover} -p /sbin/ldconfig
%postun -n libverto%{sover} -p /sbin/ldconfig

%files -n libverto%{sover}
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/verto.h
%{_includedir}/verto-module.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
