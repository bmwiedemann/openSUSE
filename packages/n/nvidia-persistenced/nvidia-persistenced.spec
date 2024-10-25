#
# spec file for package nvidia-persistenced
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


Name:           nvidia-persistenced
Version:        560.35.03
Release:        0
Summary:        A daemon to maintain persistent software state in the NVIDIA driver
License:        MIT
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.service

BuildRequires:  gcc
BuildRequires:  libtirpc-devel
BuildRequires:  m4
BuildRequires:  systemd-rpm-macros

Requires(post): systemd
Requires(preun):systemd
Requires(postun):systemd
### we cannot require it since it's part of NVIDIA's proprietary userspace libs,
### which we cannot ship
#Requires:       libnvidia-cfg.so.1()(64bit)

%description
The %{name} utility is used to enable persistent software state in the NVIDIA
driver. When persistence mode is enabled, the daemon prevents the driver from
releasing device state when the device is not in use. This can improve the
startup time of new clients in this scenario.

%prep
%autosetup
# Remove additional CFLAGS added when enabling DEBUG
sed -i -e '/+= -O0 -g/d' utils.mk

%build
export CFLAGS="%{optflags} -I%{_includedir}/tirpc"
%make_build \
    DEBUG=1 \
    LIBS="-ldl -ltirpc" \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%install
%make_install \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

# Systemd unit files
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%{_bindir}/%{name}
%attr(644, root, root) %{_mandir}/man1/%{name}.1.*
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service

%changelog
