#
# spec file for package xrdp
#
# Copyright (c) 2023 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           xrdp
Version:        0.9.20
Release:        0
Summary:        Remote desktop protocol (RDP) server
License:        Apache-2.0 AND GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/neutrinolabs/xrdp
Source0:        https://github.com/neutrinolabs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/neutrinolabs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        xrdp.keyring
Source4:        sysconfig.xrdp
Source5:        force_stop
Source6:        xrdp.ini
Source7:        sesman.ini
Source100:      %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE xrdp-pam.patch - hfiguiere@novell.com refreshed by ftake@geeko.jp
Patch1:         xrdp-pam.patch
# PATCH-FIX-OPENSUSE xrdp-disable-8-bpp-vnc-support.patch bsc#991059 - fezhang@suse.com -- disable 8 bpp support for vnc connections
Patch4:         xrdp-disable-8-bpp-vnc-support.patch
# PATCH-FIX-OPENSUSE xrdp-support-KillDisconnected-for-Xvnc.patch boo#1101506 - fezhang@suse.com -- Support the KillDisconnected option for TigerVNC Xvnc sessions
Patch5:         xrdp-support-KillDisconnected-for-Xvnc.patch
# PATCH-FIX-OPENSUSE xrdp-systemd-services.patch boo#1138954 boo#1144327 - fezhang@suse.com -- Let systemd handle the daemons
Patch6:         xrdp-systemd-services.patch
# PATCH-FIX-UPSTREAM xrdp-update-pam.d-path.patch bsc#1203468 - yu.daike@suse.com -- update install script to accommodate with pam.d path move
Patch7:         xrdp-update-pam.d-path.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23468.patch bsc#1206300 - yu.daike@suse.com -- Buffer overflow in xrdp_login_wnd_create()
Patch8:         xrdp-CVE-2022-23468.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23478.patch bsc#1206302 - yu.daike@suse.com -- Out of Bound Write in xrdp_mm_trans_process_drdynvc_chan
Patch9:         xrdp-CVE-2022-23478.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23479.patch bsc#1206303 - yu.daike@suse.com -- Buffer overflow in xrdp_mm_chan_data_in() function
Patch10:        xrdp-CVE-2022-23479.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23480.patch bsc#1206306 - yu.daike@suse.com -- Buffer overflow in devredir_proc_client_devlist_announce_req
Patch11:        xrdp-CVE-2022-23480.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23481.patch bsc#1206307 - yu.daike@suse.com -- Out of Bound Read in xrdp_caps_process_confirm_active()
Patch12:        xrdp-CVE-2022-23481.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23482.patch bsc#1206310 - yu.daike@suse.com -- Out of Bound Read in xrdp_sec_process_mcs_data_CS_CORE()
Patch13:        xrdp-CVE-2022-23482.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23483.patch bsc#1206311 - yu.daike@suse.com -- Out of Bound Read in libxrdp_send_to_channel()
Patch14:        xrdp-CVE-2022-23483.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23484.patch bsc#1206312 - yu.daike@suse.com -- Integer Overflow in xrdp_mm_process_rail_update_window_text()
Patch15:        xrdp-CVE-2022-23484.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23493.patch bsc#1206313 - yu.daike@suse.com -- Out of Bound Read in xrdp_mm_trans_process_drdynvc_channel_close()
Patch16:        xrdp-CVE-2022-23493.patch
# PATCH-FIX-UPSTREAM xrdp-CVE-2022-23477.patch bsc#1206301 - yu.daike@suse.com -- Buffer over flow in audin_send_open() function
Patch17:        xrdp-CVE-2022-23477.patch
# Keep SLE only patches on the bottom starting from patch number 1001
# PATCH-FEATURE-SLE xrdp-avahi.diff bnc#586785 - hfiguiere@novell.com -- Add Avahi support.
Patch1001:      xrdp-avahi.diff
# PATCH-FIX-SLE xrdp-filter-tab-from-mstsc-on-focus-change.patch bnc#601996 bnc#623534 - dliang@novell.com -- filter the fake tab key which is used to notify the session
Patch1002:      xrdp-filter-tab-from-mstsc-on-focus-change.patch
# PATCH-FIX-SLE xrdp-bsc965647-allow-admin-choose-desktop.patch bsc#965647 - fezhang@suse.com -- Allow administrator choose the desktop displayed
Patch1003:      xrdp-bsc965647-allow-admin-choose-desktop.patch
# PATCH-FEATURE-SLE xrdp-fate318398-change-expired-password.patch fate#318398 - fezhang@suse.com -- enable user to update expired password via PAM
Patch1004:      xrdp-fate318398-change-expired-password.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  fuse-devel
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libavahi-devel
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(systemd)
Requires:       xorg-x11-Xvnc
Recommends:     xorgxrdp
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A terminal server, capable of accepting connection from rdesktop and
Microsoft's own terminal server / remote desktop clients.

%package devel
Summary:        Development files for xrdp
Group:          Development/Libraries/C and C++
Requires:       libpainter0 = %{version}
Requires:       librfxencode0 = %{version}

%description devel
This package contains the development headers for xrdp.

%package -n libpainter0
Summary:        Library for manipulating memory bitmaps
Group:          System/Libraries

%description -n libpainter0
This package contains libraries for manipulating memory bitmaps.

%package -n librfxencode0
Summary:        Library for the JPEG2000 codec for RDP
Group:          System/Libraries

%description -n librfxencode0
This package contains libraries for the JPEG2000 codec for RDP.

%prep
%setup -q
%patch1 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%if 0%{?sle_version}
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%endif

%build
sh ./bootstrap
%configure \
   --enable-ipv6 \
   --enable-painter \
   --with-systemdsystemunitdir=%{_unitdir} \
   --enable-vsock \
   --enable-fuse
make %{?_smp_mflags} V=1

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -name '*.a' -delete
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}/%{_fillupdir}
install -m 644 %{SOURCE4} %{buildroot}/%{_fillupdir}/sysconfig.xrdp
mkdir -p %{buildroot}/%{_libexecdir}/initscripts/legacy-actions/xrdp
install -m 755 %{SOURCE5} %{buildroot}/%{_libexecdir}/initscripts/legacy-actions/xrdp/force_stop
install -m 644 %{SOURCE6} %{SOURCE7} %{buildroot}/%{_sysconfdir}/xrdp/

ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcxrdp
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcxrdp-sesman

# remove a private key and certification file generated during make and
# use certification file created at the post phase
rm -f %{buildroot}/%{_sysconfdir}/xrdp/{cert,key}.pem

%fdupes -s %{buildroot}

%pre
%service_add_pre xrdp-sesman.service
%service_add_pre xrdp.service

%post
/sbin/ldconfig
%service_add_post xrdp-sesman.service
%service_add_post xrdp.service
%{fillup_only -n xrdp}
if [ ! -e %{_sysconfdir}/xrdp/rsakeys.ini ]; then
    xrdp-keygen xrdp %{_sysconfdir}/xrdp/rsakeys.ini
    if [ $? -ne 0 ] || [ ! -e %{_sysconfdir}/xrdp/rsakeys.ini ]; then
        echo "Could not generate rsakeys.ini, please check manually!"
    fi
fi
exit 0

%preun
%stop_on_removal
%service_del_preun xrdp.service
%service_del_preun xrdp-sesman.service

%postun
/sbin/ldconfig
%service_del_postun xrdp.service
%service_del_postun xrdp-sesman.service
%restart_on_update

%post -n libpainter0 -p /sbin/ldconfig

%postun -n libpainter0 -p /sbin/ldconfig

%post -n librfxencode0 -p /sbin/ldconfig

%postun -n librfxencode0 -p /sbin/ldconfig

%files
%defattr(-,root,root)

%dir %{_datadir}/xrdp
%dir %{_libdir}/xrdp
%config(noreplace) %{_sysconfdir}/pam.d/xrdp-sesman
%license COPYING
%{_bindir}/xrdp*
%{_datadir}/xrdp/*
%{_libdir}/xrdp/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_libexecdir}/initscripts/legacy-actions/xrdp
%{_sbindir}/rc*
%{_sbindir}/xrdp*
%dir %{_sysconfdir}/xrdp
%config(noreplace) %{_sysconfdir}/xrdp/km*.ini
%dir %{_sysconfdir}/xrdp/pulse
%config(noreplace) %{_sysconfdir}/xrdp/pulse/default.pa
%config(noreplace) %{_sysconfdir}/xrdp/reconnectwm.sh
%ghost %config(noreplace) %{_sysconfdir}/xrdp/rsakeys.ini
%config(noreplace) %{_sysconfdir}/xrdp/startwm.sh
%config(noreplace) %{_sysconfdir}/xrdp/xrdp_keyboard.ini
%config(noreplace) %{_sysconfdir}/xrdp/sesman.ini
%config(noreplace) %{_sysconfdir}/xrdp/xrdp.ini

%{_unitdir}/xrdp*

%ghost %{_localstatedir}/log/xrdp-sesman.log

%config %{_fillupdir}/sysconfig.xrdp

%files devel
%defattr(-,root,root)
%{_includedir}/ms-*
%{_includedir}/painter.h
%{_includedir}/rfxcodec_*
%{_includedir}/xrdp_*
%{_libdir}/libpainter.so
%{_libdir}/librfxencode.so
%{_libdir}/pkgconfig/libpainter.pc
%{_libdir}/pkgconfig/rfxcodec.pc
%{_libdir}/pkgconfig/xrdp.pc

%files -n libpainter0
%{_libdir}/libpainter.so.*

%files -n librfxencode0
%{_libdir}/librfxencode.so.*

%changelog
