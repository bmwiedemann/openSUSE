#
# spec file for package fprintd
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


Name:           fprintd
Version:        1.94.2
Release:        0
Summary:        D-Bus service for Fingerprint reader access
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://fprint.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  gobject-introspection
BuildRequires:  gtk-doc >= 1.3
BuildRequires:  intltool
BuildRequires:  meson >= 0.46.1
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-cairo
BuildRequires:  python3-dbus-python
BuildRequires:  python3-dbusmock
BuildRequires:  python3-libpamtest
BuildRequires:  python3-pydbus
BuildRequires:  typelib-1_0-FPrint-2_0
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfprint-2) >= 1.94.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pam_wrapper)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
ExcludeArch:    s390 s390x
%{?systemd_requires}

%description
The fprint project provides a central system
to support consumer fingerprint reader devices.

%package pam
Summary:        PAM module for fingerprint authentication
License:        GPL-2.0-or-later
Group:          Productivity/Security
Requires:       %{name} = %{version}
Requires(postun):coreutils
Requires(postun):pam
Requires(postun):pam-config
# on biarch platforms we need to have it before the call of pam-config
Supplements:    modalias(usb:v045Ep00BBd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v045Ep00BCd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v045Ep00BDd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v045Ep00CAd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0483p2015d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0483p2016d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0483p2017d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0903d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0907d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C02d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C03d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C04d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C05d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C06d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C07d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C08d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C09d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C0Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C0Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C0Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C0Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C0Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C0Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C10d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C11d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C12d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C13d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C14d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C15d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C16d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C17d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C18d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C19d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C1Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C1Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C1Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C1Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C1Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C1Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C20d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C21d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C22d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C22d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C23d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C24d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C25d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C26d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C27d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C28d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C29d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C2Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C2Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C2Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C2Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C2Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C2Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C30d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C31d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C32d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C33d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C3Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C42d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C4Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C4Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C4Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C58d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C63d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C6Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C7Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C7Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C82d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C88d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04F3p0C8Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v05BAp0007d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v05BAp0008d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v05BAp000Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v061Ap0110d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp00BDd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp00C2d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp00DFd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp00F0d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp00F9d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp00FCd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0100d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0103d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0104d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0123d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0126d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0129d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp015Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v06CBp0168d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1600d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1660d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1680d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1681d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1682d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1683d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1684d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1685d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1686d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1687d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1688d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1689d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp168Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp168Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp168Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp168Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp168Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp168Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2500d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2550d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2580d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2660d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2680d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2681d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2682d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2683d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2684d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2685d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2686d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2687d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2688d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2689d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp268Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp268Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp268Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp268Dd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp268Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp268Fd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2691d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2810d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp5501d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp5731d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v10A5pA305d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v10A5pD205d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v10A5pD805d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v10A5pDA04d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v10A5pFFE0d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0001d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0005d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0008d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0010d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0011d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0015d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0017d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0018d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0050d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v138Ap0091d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v147Ep1000d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v147Ep1001d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v147Ep2016d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v147Ep2020d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v147Ep3001d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1C7Ap0570d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1C7Ap0571d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1C7Ap0603d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p5840d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6014d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6094d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p609Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p60A2d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p631Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p634Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6384d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p639Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p63ACd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p63BCd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p63CCd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6496d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6584d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p658Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6592d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6594d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p659Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p659Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p6A94d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v298Dp1010d*dc*dsc*dp*ic*isc*ip*)
Obsoletes:      pam_fprint < 0.2-7
Provides:       pam_fprint = %{version}-%{release}
Obsoletes:      pam_thinkfinger < 0.3
Provides:       pam_thinkfinger = 0.3
Obsoletes:      pam_fp < 0.1
Provides:       pam_fp = 0.1

%description pam
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary:        Development files for %{name}
License:        GFDL-1.1-or-later
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       gtk-doc
BuildArch:      noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%package doc
Summary:        Development documents of fprintd
License:        GPL-2.0-or-later
Group:          Productivity/Security
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
This package contains Development documents for fprintd

%lang_package

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%if 0%{?sle_version} == 150300 && 0%{?is_opensuse}
%meson -Dgtk_doc=true -Dpam=true -Dpam_modules_dir=/%{_lib}/security
%else
%meson -Dgtk_doc=true -Dpam=true -Dpam_modules_dir=%{_pam_moduledir}
%endif
%meson_build

%install
%meson_install

install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}/%{_localstatedir}/lib/fprint
%find_lang %{name} %{?no_lang_C}

%pre
%service_add_pre fprintd.service

%post
%service_add_post fprintd.service

%preun
%service_del_preun fprintd.service

%postun
%service_del_postun fprintd.service

%postun pam
if [ "$1" = "0" ]; then
        %{_sbindir}/pam-config -d --fprintd ||:
fi

%files
%license COPYING
%doc README AUTHORS TODO
%{_sbindir}/rc%{name}
%{_bindir}/fprintd-*
%{_libexecdir}/fprintd
%config %{_sysconfdir}/fprintd.conf
%{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy
%{_localstatedir}/lib/fprint
%{_mandir}/man1/fprintd.1%{?ext_man}
%{_unitdir}/fprintd.service

%files lang -f %{name}.lang

%files pam
%doc pam/README
%if 0%{?sle_version} == 150300 && 0%{?is_opensuse}
/%{_lib}/security/pam_fprintd.so
%else
%{_pam_moduledir}/pam_fprintd.so
%endif
%{_mandir}/man8/pam_fprintd.8%{?ext_man}

%files doc
%{_datadir}/gtk-doc/html/%{name}

%files devel
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
