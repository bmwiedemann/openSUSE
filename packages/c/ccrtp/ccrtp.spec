#
# spec file for package ccrtp
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ccrtp
%define lname libccrtp3
Version:        2.1.2
Release:        0
Summary:        A Common C++ Class Framework for RTP Packets
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Development/Libraries/C and C++
Url:            http://gnu.org/software/ccrtp/

#Git-Clone:	git://git.sv.gnu.org/ccrtp
Source:         http://ftp.gnu.org/pub/gnu/ccrtp/%name-%version.tar.gz
Source2:        http://ftp.gnu.org/pub/gnu/ccrtp/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config
BuildRequires:  ucommon-devel >= 6.2.2
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ccrtp package offers a generic framework for sending and receiving
real-time streaming data over UDP packets using sending and receiving
packet queues.

%package -n %lname
Summary:        A Common C++ Class Framework for RTP Packets
Group:          System/Libraries

%description -n %lname
The ccrtp package offers a generic framework for sending and receiving
real-time streaming data over UDP packets using sending and receiving
packet queues.

%package devel
Summary:        Include-files and documentation for ccrtp
Group:          Development/Libraries/C and C++
PreReq:         %install_info_prereq
Requires:       %lname = %version
Requires:       libgcrypt-devel
Requires:       ucommon-devel >= 5.0.0
Provides:       %lname-devel = %version
Provides:       libccrtp-devel = %version
Obsoletes:      libccrtp-devel < %version

%description devel
This package contains files needed when developing applications using
ccrtp.

%package doc
Summary:        Generated class documentation for ccrtp
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1130 || 0%{?fedora_version}
BuildArch:      noarch
%endif

%description doc
Generated class documentation for the ccrtp library from header
files, html browsable.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%post devel
%install_info --info-dir=%_infodir %_infodir/ccrtp.info.gz

%postun devel
%install_info_delete --info-dir=%_infodir %_infodir/ccrtp.info.gz

%files -n %lname
%defattr(-,root,root,0755)
%doc COPYING
%_libdir/libccrtp*.so.3*

%files devel
%defattr(-,root,root,0755)
%doc AUTHORS NEWS README TODO ChangeLog
%_libdir/libccrtp*.so
%_libdir/pkgconfig/*.pc
%_includedir/ccrtp/
%_infodir/ccrtp.info*

%files doc
%defattr(-,root,root)
%doc doc/html/

%changelog
