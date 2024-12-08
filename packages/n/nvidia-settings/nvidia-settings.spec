#
# spec file for package nvidia-settings
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


Name:           nvidia-settings
Version:        565.77
Release:        0
Summary:        Configure the NVIDIA graphics driver
License:        GPL-2.0-only
URL:            https://github.com/NVIDIA/nvidia-settings
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-load.desktop
Source2:        nvidia-libXNVCtrl.rpmlintrc
Patch0:         %{name}-desktop.patch
Patch1:         %{name}-lib-permissions.patch
Patch2:         %{name}-link-order.patch
Patch3:         %{name}-libXNVCtrl.patch
Patch4:         %{name}-ld-dep-remove.patch

BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  dbus-1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXv-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjansson-devel
BuildRequires:  libvdpau-devel >= 1.0
BuildRequires:  m4
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)

Requires:       nvidia-libXNVCtrl = %{version}
# Loaded at runtime
Requires:       libvdpau1 >= 0.9

%description
The %{name} utility is a tool for configuring the NVIDIA graphics
driver. It operates by communicating with the NVIDIA X driver, querying and
updating state as appropriate.

This communication is done with the NV-CONTROL X extension.

%package -n nvidia-libXNVCtrl
Summary:        Library providing the NV-CONTROL API
Obsoletes:      libXNVCtrl0 < %{version}
Provides:       libXNVCtrl0 = %{version}

%description -n nvidia-libXNVCtrl
This library provides the NV-CONTROL API for communicating with the proprietary
NVidia xorg driver. It is required for proper operation of the %{name} utility.

%package -n nvidia-libXNVCtrl-devel
Summary:        Development files for libXNVCtrl
Requires:       libX11-devel
Requires:       nvidia-libXNVCtrl = %{version}
Obsoletes:      libXNVCtrl-devel < %{version}
Provides:       libXNVCtrl-devel = %{version}

%description -n nvidia-libXNVCtrl-devel
This devel package contains libraries and header files for
developing applications that use the NV-CONTROL API.

%prep
%autosetup -p1

# Remove bundled jansson
rm -fr src/jansson

# Remove additional CFLAGS added when enabling DEBUG
sed -i '/+= -O0 -g/d' utils.mk src/libXNVCtrl/utils.mk

# Change all occurrences of destinations in each utils.mk.
sed -i -e 's|$(PREFIX)/lib|$(PREFIX)/%{_lib}|g' utils.mk src/libXNVCtrl/utils.mk

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{?__global_ldflags}"
%make_build \
    DEBUG=1 \
    NV_USE_BUNDLED_LIBJANSSON=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    XNVCTRL_LDFLAGS="-L%{_libdir}"

%install
# Install libXNVCtrl headers
mkdir -p %{buildroot}%{_includedir}/NVCtrl
cp -af src/libXNVCtrl/*.h %{buildroot}%{_includedir}/NVCtrl/

# Install main program
%make_install \
    DEBUG=1 \
    NV_USE_BUNDLED_LIBJANSSON=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix}

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
desktop-file-install --dir %{buildroot}%{_datadir}/applications/ doc/%{name}.desktop
cp doc/%{name}.png %{buildroot}%{_datadir}/pixmaps/

# Install autostart file to load settings at login
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-load.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-load.desktop

%if 0%{?suse_version} >= 1550 ||  0%{?sle_version} >= 150400
%ldconfig_scriptlets
%ldconfig_scriptlets -n nvidia-libXNVCtrl
%else
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n nvidia-libXNVCtrl -p /sbin/ldconfig
%postun -n nvidia-libXNVCtrl -p /sbin/ldconfig
%endif

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/libnvidia-gtk3.so.%{version}
%{_libdir}/libnvidia-wayland-client.so.%{version}
%{_mandir}/man1/%{name}.*
%config %{_sysconfdir}/xdg/autostart/%{name}-load.desktop

%files -n nvidia-libXNVCtrl
%license COPYING
%{_libdir}/libXNVCtrl.so.*

%files -n nvidia-libXNVCtrl-devel
%doc doc/NV-CONTROL-API.txt doc/FRAMELOCK.txt
%{_includedir}/NVCtrl
%{_libdir}/libXNVCtrl.so

%changelog
