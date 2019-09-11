#
# spec file for package ilbc
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ilbc
Summary:        Internet Low Bitrate Codec
License:        GPL-2.0+
Group:          Productivity/Telephony/Utilities
Version:        3951
Release:        0
Source:         ilbc-rfc3951.tar.bz2
Url:            http://download.savannah.nongnu.org/releases/linphone/1.3.x/source/ilbc-rfc3951.tar.gz
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch:          %{name}-compilerwarnings.patch
Patch1:         %{name}-libm.patch

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.


%define libilbc_name libilbc0
%package -n %{libilbc_name}
Summary:        Internet Low Bitrate Codec
Group:          Productivity/Telephony/Utilities
Provides:       ilbc = %{version}
Obsoletes:      ilbc <= %{version}

%description -n %{libilbc_name}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for
robust voice communication over IP. The codec is designed for narrow
band speech and results in a payload bit rate of 13.33 kbit/s with an
encoding frame length of 30 ms and 15.20 kbps with an encoding length
of 20 ms. The iLBC codec enables graceful speech quality degradation in
the case of lost frames, which occurs in connection with lost or
delayed IP packets.


%package devel
Summary:        Libraries and Header Files to Develop Programs with iLBC Support
Group:          Development/Libraries/C and C++
Requires:       %{libilbc_name} = %{version}

%description devel
Libraries and Header Files to Develop Programs with iLBC Support


%prep
%setup -n ilbc-rfc3951
%patch
%patch1

%build
autoreconf -fi
%configure --disable-static --with-pic
make MYCFLAGS="$RPM_OPT_FLAGS" 

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libilbc_name} -p /sbin/ldconfig

%postun -n %{libilbc_name} -p /sbin/ldconfig

%files -n %{libilbc_name}
%defattr(-, root, root)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/ilbc/iLBC_decode.h
%{_includedir}/ilbc/iLBC_define.h
%{_includedir}/ilbc/iLBC_encode.h
%{_libdir}/lib%{name}.so
%dir %{_includedir}/ilbc

%changelog
