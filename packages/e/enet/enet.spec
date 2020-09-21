#
# spec file for package enet
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 7
Name:           enet
Version:        1.3.16
Release:        0
Summary:        Network Communication Layer on Top of UDP
License:        MIT
Group:          Productivity/Networking/Other
URL:            http://enet.bespin.org/
Source:         http://enet.bespin.org/download/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
ENet provides a relatively thin network communication layer on top of
UDP (User Datagram Protocol). The primary feature it provides is
optional reliable, in-order delivery of packets.

ENet omits certain higher level networking features such as authentication,
lobbying, server discovery, encryption, or other similar tasks that are
particularly application specific so that the library remains flexible,
portable, and embeddable.

%package -n libenet%{sover}
Summary:        Library files for libenet
Group:          System/Libraries

%description -n libenet%{sover}
The libenet7 package contains libraries for libenet.

%package devel
Summary:        Development files for libenet
Group:          Development/Libraries/C and C++
Requires:       libenet%{sover} = %{version}

%description devel
The libenet-devel package contains libraries and header files for
developing applications that use libenet.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

# Correct what fdupes didn't find, because docs are later installed
rm -f docs/html/ftv2link.png
ln -sf ../../docs/html/ftv2doc.png docs/html/ftv2link.png
rm -f docs/html/ftv2mnode.png
ln -sf ../../docs/html/ftv2mlastnode.png docs/html/ftv2mnode.png
rm -f docs/html/{ftv2blank,ftv2vertline,ftv2lastnode}.png
ln -sf ../../docs/html/ftv2node.png docs/html/ftv2blank.png
ln -sf ../../docs/html/ftv2node.png docs/html/ftv2vertline.png
ln -sf ../../docs/html/ftv2node.png docs/html/ftv2lastnode.png
rm -f docs/html/ftv2plastnode.png
ln -sf ../../docs/html/ftv2pnode.png docs/html/ftv2plastnode.png
rm -f docs/html/search/variables_1.js
ln -sf ../../docs/html/search/all_1.js docs/html/search/variables_1.js
rm -f docs/html/search/variables_11.js
ln -sf ../../docs/html/search/all_11.js docs/html/search/variables_11.js
rm -f docs/html/search/variables_a.js
ln -sf ../../docs/html/search/all_a.js docs/html/search/variables_a.js
rm -f docs/html/search/variables_0.js
ln -sf ../../docs/html/search/all_0.js docs/html/search/variables_0.js
rm -f docs/html/search/variables_b.js
ln -sf ../../docs/html/search/all_b.js docs/html/search/variables_b.js
rm -f docs/html/search/variables_d.js
ln -sf ../../docs/html/search/all_d.js docs/html/search/variables_d.js

%post -n libenet%{sover} -p /sbin/ldconfig
%postun -n libenet%{sover} -p /sbin/ldconfig

%files -n libenet%{sover}
%{_libdir}/libenet.so.%{sover}*

%files devel
%license LICENSE
%doc ChangeLog README docs/html
%{_includedir}/enet
%{_libdir}/libenet.so
%{_libdir}/pkgconfig/libenet.pc

%changelog
