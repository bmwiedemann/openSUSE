#
# spec file for package fstrm
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


%define c_lib   libfstrm0
Name:           fstrm
Version:        0.3.2
Release:        0
Summary:        Frame Streams implementation in C
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/farsightsec/fstrm
Source:         https://dl.farsightsecurity.com/dist/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  libevent-devel >= 2
BuildRequires:  pkgconfig

%description
fstrm is a C implementation of Frame Streams that includes a lockless
circular queue implementation and exposes library interfaces for
setting up a dedicated Frame Streams I/O thread and asynchronously
submitting data frames for transport from worker threads.

Frame Streams is a protocol that allows for the transport of
arbitrarily encoded data payload sequences with just 4 bytes per data
frame. Frame Streams does not specify an encoding format for frames
and can be used with data serialization formats that produces byte
sequences, such as Protocol Buffers, XML, JSON, MessagePack, YAML,
etc. Frame Streams can be used both as a streaming transport over a
reliable byte stream socket (TCP, AF_UNIX, TLS, etc.) for data in
motion, as well as a file format for data at rest. A "Content Type"
header identifies the type of payload being carried over an
individual Frame Stream and allows cooperating programs to determine
how to interpret a given sequence of data payloads.

%package -n %{c_lib}
Summary:        Frame Streams implementation in C
Group:          System/Libraries

%description -n %{c_lib}
This is fstrm, a C implementation of the Frame Streams data transport protocol.

This packages holds the shared library file.

%package devel
Summary:        Development files for fstrm, a Frame Streams implementation in C
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}
Provides:       libfstrm-devel = %{version}-%{release}

%description devel
This is fstrm, a C implementation of the Frame Streams data transport protocol.

This packages holds the development files.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libfstrm.la

%post   -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%doc ChangeLog README* COPYRIGHT LICENSE
%{_bindir}/fstrm_capture
%{_bindir}/fstrm_dump

%files -n %{c_lib}
%{_libdir}/libfstrm.so.*

%files devel
%{_includedir}/fstrm.h
%{_includedir}/fstrm/
%{_libdir}/libfstrm.so
%{_libdir}/pkgconfig/libfstrm.pc

%changelog
