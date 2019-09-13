#
# spec file for package kmscon
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Adam Mizerski <adam@mizerski.pl>
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


Name:           kmscon
Version:        8.1~1536176839
Release:        0
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
Group:          System/Console
URL:            https://github.com/Aetf/kmscon/
Source:         kmscon-%{version}.tar.xz
Patch1:         kmscon-no-date-time.patch
Patch2:         kmscon-x-linking.patch
BuildRequires:  autoconf >= 2.68
BuildRequires:  automake >= 1.11
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libtool >= 2.2
BuildRequires:  libtsm-devel >= 4.0.0
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  xz
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xkbcommon)
# O/P added for 13.1
Obsoletes:      %{name}-service < %{version}-%{release}
Provides:       %{name}-service = %{version}-%{release}

%description
Kmscon is a simple terminal emulator based on linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a userspace
console.

%prep
%autosetup -p1

%build
autoreconf -fvi
# fbdev is broken by design, drm2d is the most compatible
%configure --enable-debug --disable-static --with-fonts=pango --with-video=drm2d \
           --with-renderers=bbulk --with-sessions=terminal
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -m 644 -D -t %{buildroot}%{_unitdir} docs/*.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%dir %{_libdir}/kmscon
%{_libdir}/kmscon/mod-bbulk.so
%{_libdir}/kmscon/mod-pango.so
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1%{?ext_man}
%{_unitdir}/kmscon*.service

%changelog
