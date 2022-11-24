#
# spec file for package live555
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 Dominique Leuenberger, Ramiswil, Switzerland
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


%define lmdmaj 107

Name:           live555
Version:        2022.11.19
Release:        0
Summary:        LIVE555 Streaming Media
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            http://www.live555.com/liveMedia/
Source:         http://www.live555.com/liveMedia/public/live.%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         %{name}-fpic.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
This code forms a set of C++ libraries for multimedia streaming,
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries
can be used to build streaming applications

%package -n libliveMedia%{lmdmaj}
Summary:        Basic Usage Environment library of live555 streaming media
Group:          System/Libraries

%description -n libliveMedia%{lmdmaj}
This code forms a set of C++ libraries for multimedia streaming,
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries
can be used to build streaming applications

%package -n libBasicUsageEnvironment1
Summary:        Basic Usage Environment library of live555 streaming media
Group:          System/Libraries

%description -n libBasicUsageEnvironment1
This code forms a set of C++ libraries for multimedia streaming,
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries
can be used to build streaming applications

%package -n libgroupsock30
Summary:        Group sock library of live555 streaming media
Group:          System/Libraries

%description -n libgroupsock30
This code forms a set of C++ libraries for multimedia streaming,
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries
can be used to build streaming applications

%package -n libUsageEnvironment3
Summary:        Usage Environment library of live555 streaming media
Group:          System/Libraries

%description  -n libUsageEnvironment3
This code forms a set of C++ libraries for multimedia streaming,
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries
can be used to build streaming applications

%package devel
Summary:        LIVE555 Streaming Media
Group:          Development/Languages/C and C++
Requires:       libBasicUsageEnvironment1 = %{version}
Requires:       libUsageEnvironment3 = %{version}
Requires:       libgroupsock30 = %{version}
Requires:       libliveMedia%{lmdmaj} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(openssl)

%description devel
This code forms a set of C++ libraries for multimedia streaming,
using open standard protocols (RTP/RTCP, RTSP, SIP). These libraries
can be used to build streaming applications

%prep
%setup -q -n live
%patch0 -p1

# Remove .orig files in source tree
find . -name "*.orig" -delete

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
./genMakefiles linux-with-shared-libraries
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# rpmlint: 'E: shared-library-not-executable'
find %{buildroot}%{_libdir} -type f -exec chmod +x {} \;

# creates support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/live555.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name:           live555
Description: Multimedia streaming libraries
Version:        %{version}
Libs: -lliveMedia -lBasicUsageEnvironment -lUsageEnvironment -lgroupsock
Cflags: -I${includedir}/liveMedia -I${includedir}/UsageEnvironment -I${includedir}/groupsock -I${includedir}/BasicUsageEnvironment
EOF

%post -n libliveMedia%{lmdmaj} -p /sbin/ldconfig
%post -n libBasicUsageEnvironment1 -p /sbin/ldconfig
%post -n libgroupsock30 -p /sbin/ldconfig
%post -n libUsageEnvironment3 -p /sbin/ldconfig
%postun -n libliveMedia%{lmdmaj} -p /sbin/ldconfig
%postun -n libBasicUsageEnvironment1 -p /sbin/ldconfig
%postun -n libgroupsock30 -p /sbin/ldconfig
%postun -n libUsageEnvironment3 -p /sbin/ldconfig

%files
%{_bindir}/*

%files -n libliveMedia%{lmdmaj}
%license COPYING
%{_libdir}/libliveMedia.so.%{lmdmaj}*

%files -n libBasicUsageEnvironment1
%license COPYING
%{_libdir}/libBasicUsageEnvironment.so.1*

%files -n libgroupsock30
%license COPYING
%{_libdir}/libgroupsock.so.30*

%files -n libUsageEnvironment3
%license COPYING
%{_libdir}/libUsageEnvironment.so.3*

%files devel
%license COPYING
%{_libdir}/*.so
%{_includedir}/liveMedia/
%{_includedir}/groupsock/
%{_includedir}/BasicUsageEnvironment/
%{_includedir}/UsageEnvironment/
%{_libdir}/pkgconfig/live555.pc

%changelog
