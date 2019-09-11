#
# spec file for package libvdpau
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libvdpau
Version:        1.2
Release:        0
Summary:        VDPAU wrapper and trace libraries
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.freedesktop.org/wiki/Software/VDPAU/
Source:         https://gitlab.freedesktop.org/vdpau/libvdpau/uploads/14b620084c027d546fa0b3f083b800c6/%{name}-%{version}.tar.bz2
Source1:        http://people.freedesktop.org/~aplattner/vdpau/vdpauinfo-1.0.tar.gz
Source2:        README
Source99:       baselibs.conf
Source100:      %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
This package contains the libvdpau wrapper library and the libvdpau_trace
debugging library, along with the header files needed to build VDPAU
applications.  To actually use a VDPAU device, you need a vendor-specific
implementation library.  Currently, this is always libvdpau_nvidia.  You can
override the driver name by setting the VDPAU_DRIVER environment variable.

%package -n libvdpau1
Summary:        VDPAU wrapper library
Group:          System/Libraries
Provides:       libvdpau = %{version}-%{release}
Obsoletes:      libvdpau < %{version}-%{release}

%description -n libvdpau1
This package contains the libvdpau wrapper library and the libvdpau_trace
debugging library, along with the header files needed to build VDPAU
applications.  To actually use a VDPAU device, you need a vendor-specific
implementation library.  Currently, this is always libvdpau_nvidia.  You can
override the driver name by setting the VDPAU_DRIVER environment variable.

%package -n libvdpau-devel
Summary:        VDPAU wrapper development files
Group:          Development/Libraries/X11
Requires:       libvdpau1 = %{version}

%description -n libvdpau-devel
Note that this package only contains the VDPAU headers that are required to
build applications. At runtime, the shared libraries are needed too and may
be installed using the proprietary nVidia driver packages.

%package -n libvdpau_trace1
Summary:        VDPAU trace library
Group:          Development/Libraries/X11
Requires:       libvdpau1 = %{version}
Provides:       libvdpau_trace = %{version}-%{release}
Obsoletes:      libvdpau_trace < %{version}-%{release}

%description -n libvdpau_trace1
This package provides the library for tracing VDPAU function calls.
Its usage is documented in the README.

%prep
%setup -q -b1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

rm %{buildroot}%{_libdir}/libvdpau.la
rm %{buildroot}%{_libdir}/vdpau/libvdpau_trace.la
/sbin/ldconfig -n %{buildroot}/%{_libdir}/vdpau
rm %{buildroot}%{_libdir}/vdpau/libvdpau_trace.so

pushd ../vdpauinfo-*
%configure \
VDPAU_CFLAGS=-I%{buildroot}%{_includedir} \
VDPAU_LIBS="-L%{buildroot}/%{_libdir} -lvdpau -lX11"

make %{?_smp_mflags}
%make_install
popd

cp %{_sourcedir}/README .

%post -n libvdpau1 -p /sbin/ldconfig

%postun -n libvdpau1 -p /sbin/ldconfig

%files -n libvdpau1
%defattr(-,root,root)
%dir %{_libdir}/vdpau
%{_bindir}/vdpauinfo
%{_libdir}/libvdpau.so.*
%config %{_sysconfdir}/vdpau_wrapper.cfg

%files -n libvdpau-devel
%defattr(-,root,root)
%dir %{_libdir}/vdpau
%{_includedir}/vdpau
%{_libdir}/libvdpau.so
%{_libdir}/pkgconfig/vdpau.pc

%files -n libvdpau_trace1
%defattr(-,root,root)
%doc README
%{_libdir}/vdpau/libvdpau_trace.so.*

%changelog
