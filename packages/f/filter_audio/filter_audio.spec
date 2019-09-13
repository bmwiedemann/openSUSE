#
# spec file for package filter_audio
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           filter_audio
Version:        0.0.1
Release:        0
Summary:        Audio filtering library made from WebRTC code
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            https://github.com/irungentoo/filter_audio
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
An audio filtering library made from webrtc code.

%package -n libfilteraudio0
Summary:        Audio filtering library made from WebRTC code
Group:          System/Libraries

%description -n libfilteraudio0
An audio filtering library made from webrtc code.

This package provides shared libraries for filter_audio.

%package devel
Summary:        Development headers for filter_audio
Group:          Development/Libraries/C and C++
Requires:       libfilteraudio0 = %{version}

%description devel
An audio filtering library made from WebRTC code.

This package provides development headers for filter_audio.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR=/%{_lib}

%install
%make_install PREFIX=%{_prefix} LIBDIR=/%{_lib} %{?_smp_mflags}

find %{buildroot} -name "*.a" -print -delete

%post -n libfilteraudio0 -p /sbin/ldconfig
%postun -n libfilteraudio0 -p /sbin/ldconfig

%files -n libfilteraudio0
%doc README
%{_libdir}/libfilteraudio.so.0
%{_libdir}/libfilteraudio.so.0.0.0

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libfilteraudio.so
%{_libdir}/pkgconfig/filteraudio.pc

%changelog
