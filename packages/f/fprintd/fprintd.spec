#
# spec file for package fprintd
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fprintd
Version:        0.8.1
Release:        0
Summary:        D-Bus service for Fingerprint reader access
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://fprint.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/libfprint/fprintd/uploads/bdd9f91909f535368b7c21f72311704a/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Source2:        README.SUSE
BuildRequires:  gtk-doc >= 1.3
BuildRequires:  intltool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfprint) > 0.1.0
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-lang
ExcludeArch:    s390 s390x
%{?systemd_requires}

%description
D-Bus service to access fingerprint readers.

%package pam
Summary:        PAM module for fingerprint authentication
License:        GPL-2.0-or-later
Group:          Productivity/Security
Requires:       %{name} = %{version}
Requires(postun): coreutils
Requires(postun): pam
Requires(postun): pam-config
# on biarch platforms we need to have it before the call of pam-config
Recommends:     yast2-fingerprint-reader
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
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtk-doc
BuildArch:      noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%lang_package

%prep
%autosetup -p1

%build
cp %{SOURCE2} .
%configure \
    --libdir=/%{_lib}/ \
    --disable-static \
    --enable-gtk-doc \
    --enable-pam
make %{?_smp_mflags}

%install
%make_install
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
%{_bindir}/fprintd-*
%{_libexecdir}/fprintd
# FIXME This file should be marked as config when it does something useful
%{_sysconfdir}/fprintd.conf
%{_sysconfdir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy
%{_localstatedir}/lib/fprint
%{_mandir}/man1/fprintd.1%{?ext_man}
%{_unitdir}/fprintd.service
%doc README.SUSE

%files lang -f %{name}.lang

%files pam
%doc pam/README
/%{_lib}/security/pam_fprintd.so

%files devel
%{_datadir}/gtk-doc/html/fprintd
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
