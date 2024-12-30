#
# spec file for package compface
#
# Copyright (c) 2024 SUSE LLC
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


Name:           compface
Version:        1.5.2
Release:        0
Summary:        Library and tools for handling X-Face data
License:        MIT
Group:          Productivity/Graphics/Convertors
URL:            http://www.xemacs.org/Download/optLibs.html
Source:         http://ftp.xemacs.org/pub/xemacs/aux/compface-%{version}.tar.gz
Source1:        xbm2face
Source2:        compface-test.xbm
Patch0:         config.patch
Patch1:         debian.patch
Patch2:         Makefile.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The programs compface and uncompface convert 48x48x1 images to and from
a compressed format.  The purpose of the programs is to allow the
inclusion of face images within mail headers using the field name
"X-face:".  They make use of a library that allows the compression and
decompression algorithms to be used in other programs, such as mail
dispatchers and mail notification daemons.

%package        devel
Summary:        Library and development files for handling X-Face data
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description    devel
These files are needed when building software that uses the Compface
library.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

# do not strip
sed -i "/strip/d" Makefile.in

%build
autoreconf -fi
CFLAGS="%{optflags} -fPIC" \
%configure
make %{?_smp_mflags}

%install
%make_install
sed -i 's/\r//' xbm2xface.pl
install -m 755 xbm2xface.pl %{buildroot}%{_bindir}/xbm2xface
install -m 755 $RPM_SOURCE_DIR/xbm2face %{buildroot}%{_prefix}/bin

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
./compface %{SOURCE2} | ./uncompface -X > __test.xbm
cmp %{SOURCE2} __test.xbm

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README
%{_bindir}/*
%{_libdir}/*.so.*
%doc %{_mandir}/man?/*

%files devel
%defattr(-, root, root)
%{_includedir}/compface.h
%{_libdir}/libcompface.so

%changelog
