#
# spec file for package libva-vdpau-driver
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


Name:           libva-vdpau-driver
Version:        0.7.4
Release:        0
Summary:        HW video decode support for VDPAU platforms
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            http://cgit.freedesktop.org/vaapi/vdpau-driver
Source:         http://www.freedesktop.org/software/vaapi/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0:         libva-vdpau-driver-0.7.4-glext-85.patch
Patch1:         libva-vdpau-driver-0.7.4-drop-h264-api.patch
Patch2:         libva-vdpau-driver-0.7.4-fix_type.patch
Patch3:         libva-vdpau-driver-0.7.4-sigfpe-crash.patch
Patch4:         libva-vdpau-driver-0.7.4-type-fix.patch
BuildRequires:  libvdpau-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(libva-x11)
# Replace a similar package from packman
Provides:       vdpau-video
Obsoletes:      vdpau-video <= %{version}-%{release}

%description
VDPAU Backend for Video Acceleration (VA) API HW video decode support.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cat > %{name}.sh << EOF
# use this library when NVIDIA's proprietary driver is running
if test -c /dev/nvidiactl; then
  export LIBVA_DRIVER_NAME='vdpau'
  export VDPAU_DRIVER=nvidia
fi
EOF
cat > %{name}.csh << EOF
# use this library when NVIDIA's proprietary driver is running
if (-c /dev/nvidiactl) then
  setenv LIBVA_DRIVER_NAME 'vdpau'
  setenv VDPAU_DRIVER 'nvidia'
endif
EOF

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
find %{buildroot} -name '*.la' -delete
install -Dm 0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -Dm 0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

%files
%doc README COPYING AUTHORS NEWS
%dir %{_libdir}/dri
%{_libdir}/dri/*.so
%config %{_sysconfdir}/profile.d/%{name}.*sh

%changelog
