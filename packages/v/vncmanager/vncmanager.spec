#
# spec file for package vncmanager
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


%define vncgroup vnc
%define vncuser vnc

Name:           vncmanager
Version:        1.0.2
Release:        0
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libgnutls-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
Requires(post): xorg-x11-Xvnc
Requires:       vncmanager-greeter
Requires:       xorg-x11-Xvnc
Requires:       xorg-x11-Xvnc:/usr/lib/vnc/with-vnc-key.sh
Recommends:     vncmanager-controller

URL:            https://github.com/openSUSE/vncmanager
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Session manager for VNC
License:        MIT
Group:          System/X11/Utilities
Source:         vncmanager-%{version}.tar.gz
Source1:        tmpfile.conf
Patch1:         n_use_port_5901.patch
Patch2:         n_use_with_vnc_key_wrapper.patch
Patch3:         U_Add-xvnc-args-configuration-option.patch
Patch4:         n_disable_mit_shm.patch
Patch5:         U_ControllerConnection-Split-iostream-into-istream-and.patch
Patch6:         n_vncmanager-add-target-to-service.patch
Patch7:         u_Fix_tight_decoder_on_888_encodings.patch
Patch8:         u_Fix-PixelFormat-ntoh-and-PixelFormat-hton.patch
Patch9:         u_Fix-TightCompressionControl-definition-for-big-endian.patch

%description
Session manager for VNC. It listens on VNC port and spawns Xvnc processes for incoming clients.

%pre
%service_add_pre vncmanager.service

%post
%service_add_post vncmanager.service
[ -x /usr/bin/systemd-tmpfiles ] && /usr/bin/systemd-tmpfiles --create %_tmpfilesdir/%{name}.conf || :

%preun
%service_del_preun vncmanager.service

%postun
%service_del_postun vncmanager.service

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_VERBOSE_MAKEFILE=ON
make %{?_smp_mflags}

%install
%cmake_install

# tmpfiles
install -d -m 0755 %{buildroot}/usr/lib/tmpfiles.d/
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/%{name}.conf

# systemd
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcvncmanager

%files
%defattr(-,root,root)
%{_bindir}/vncmanager
%{_unitdir}/vncmanager.service
%{_sbindir}/rcvncmanager
%dir %attr(0755,%{vncuser},%{vncuser}) %{_sysconfdir}/vnc
%config(noreplace) %{_sysconfdir}/vnc/vncmanager.conf
/usr/lib/tmpfiles.d/%{name}.conf
%ghost %dir /run/vncmanager
%doc LICENSE

%changelog
