#
# spec file for package udtrace
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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

Name:           udtrace
Version:        0.0.0+git.20180402
Release:        0
Summary:        Unix domain socket tracing
License:        GPL-3.0
Group:          Development/Tools/Debuggers
URL:            https://github.com/laf0rge/udtrace
#Git-Clone:     git://git.gnumonks.org/udtrace
Source:         %{name}-%{version}.tar.xz
Source99:       udtrace-rpmlintrc
BuildRequires:  libpcap-devel

%description
This is a LD_PRELOAD wrapper library which can be used to trace the
data sent and/or received via unix domain sockets.

Unlike IP based communication that can be captured/traced with pcap
programs like tcpdump or wireshark, there is no similar mechanism
available for unix domain sockets.

This LD_PRELOAD library intercepts the C library function calls of
dynamically linked programs. It will detect all file descriptors
representing unix domain sockets and will then print traces of all
data sent/received via the socket.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dm 0755 libudtrace.so %{buildroot}/%{_libdir}/libudtrace.so

%files
%license COPYING
%doc README.md
%{_libdir}/libudtrace.so

%changelog
