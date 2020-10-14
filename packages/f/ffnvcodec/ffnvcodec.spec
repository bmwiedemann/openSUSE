#
# spec file for package ffnvcodec
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


Name:           ffnvcodec
Version:        10.0.26.1
Release:        0
Summary:        FFmpeg version of NVIDIA codec API headers
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
Source:         nv-codec-headers-%{version}.tar.xz
BuildRequires:  pkgconfig

%description
This package contains the headers required for FFmpeg to interface
with NVIDIA codec APIs.

%package -n %{name}-devel
Summary:        FFmpeg version of NVIDIA codec API headers
Group:          Development/Libraries/C and C++

%description -n %{name}-devel
This package contains the headers required for FFmpeg to interface
with NVIDIA codec APIs.

%prep
%setup -q -n nv-codec-headers-%{version}

%build

%install
make PREFIX=%{_prefix} LIBDIR=%{_lib} DESTDIR=%{buildroot} install

%files -n %{name}-devel
%doc README
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
