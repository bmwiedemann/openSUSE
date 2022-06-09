#
# spec file for package fprintd
#
# Copyright (c) 2022 SUSE LLC
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
Supplements:    modalias(usb:v05BAp0007d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v05BAp000Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp1600d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp2580d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v08FFp5501d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1162p0300d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v147Ep2016d*dc*dsc*dp*ic*isc*ip*)
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
