#
# spec file for package hwinfo
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


Name:           hwinfo
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  perl-XML-Parser
BuildRequires:  pkg-config
BuildRequires:  udev
BuildRequires:  pkgconfig(uuid)
%if 0%{?rhel_version} == 0
BuildRequires:  perl-XML-Writer
%endif
%ifarch %ix86 x86_64
BuildRequires:  libx86emu-devel
%endif
Provides:       libhd
Obsoletes:      libhd
PreReq:         /sbin/ldconfig
Summary:        Hardware Library
# Until migration to github this should be correct url
License:        GPL-2.0-or-later
Group:          Hardware/Other
Url:            http://gitorious.org/opensuse/hwinfo
Version:        21.67
Release:        0
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple program that lists results from the hardware detection
library.



%package      devel
Summary:        Hardware Detection Library
Group:          Development/Libraries/C and C++
Provides:       libhddev
Obsoletes:      libhddev
Requires:       %name = %version
Requires:       perl-XML-Parser
Requires:       udev
Requires:       wireless-tools
%if 0%{?rhel_version} == 0
Requires:       perl-XML-Writer
%endif
%if 0%{?suse_version}
Requires:       libexpat-devel
%else
Requires:       expat-devel
%endif

%description devel
This library collects information about the hardware installed on a
system.



%prep
%setup

%build
  make static
  # make copy of static library for installation
  cp src/libhd.a .
  make clean
  make LIBDIR=%{_libdir}
  make doc

%install
  make install DESTDIR=%{buildroot} LIBDIR=%{_libdir}
  install -m 644 libhd.a %{buildroot}%{_libdir}
  install -d -m 755 %{buildroot}%{_mandir}/man8/
  install -d -m 755 %{buildroot}%{_mandir}/man1/
  install -m 644 doc/check_hd.1 %{buildroot}%{_mandir}/man1/
  install -m 644 doc/convert_hd.1 %{buildroot}%{_mandir}/man1/
  install -m 644 doc/getsysinfo.1 %{buildroot}%{_mandir}/man1/
  install -m 644 doc/mk_isdnhwdb.1 %{buildroot}%{_mandir}/man1/
  install -m 644 doc/hwinfo.8 %{buildroot}%{_mandir}/man8/
  mkdir -p %{buildroot}/var/lib/hardware/udi

%clean 
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/sbin/hwinfo
/usr/sbin/mk_isdnhwdb
/usr/sbin/getsysinfo
%{_libdir}/libhd.so.*
%doc *.md
%doc %{_mandir}/man1/getsysinfo.1*
%doc %{_mandir}/man1/mk_isdnhwdb.1*
%doc %{_mandir}/man8/hwinfo.8*
%dir /var/lib/hardware
%dir /var/lib/hardware/udi
%dir /usr/share/hwinfo
/usr/share/hwinfo/*

%files devel
%defattr(-,root,root)
/usr/sbin/check_hd
/usr/sbin/convert_hd
%doc %{_mandir}/man1/convert_hd.1*
%doc %{_mandir}/man1/check_hd.1*
%{_libdir}/libhd.so
%{_libdir}/libhd.a
%{_libdir}/pkgconfig/hwinfo.pc
/usr/include/hd.h
%doc doc/libhd/html

%changelog
