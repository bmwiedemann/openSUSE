#
# spec file for package ddcutil-service
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Michael Hamilton <michael@actrix.gen.nz>
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


Name:           ddcutil-service
Version:        1.0.9
Release:        0
Summary:        D-Bus service for libddcutil VESA DDC Monitor Virtual Control Panel
License:        GPL-2.0-or-later
%if %{defined fedora_version}
Group:          Hardware/Other
%endif
%if %{defined suse_version}
Group:          System/GUI/Other
%endif
URL:            https://github.com/digitaltrails/ddcutil-service
Source0:        https://github.com/digitaltrails/ddcutil-service/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libddcutil-devel >= 1.4.0
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
%if %{defined fedora_version}
Requires:       dbus-1-daemon
%endif
%if %{defined suse_version}
Requires:       dbus-1
%endif
Recommends:     ddcutil-i2c-udev-rules

%description
ddcutil-service is D-Bus service wrapper for libddcutil which
implements the VESA DDC Monitor Control Command Set. In general,
most things that can be controlled using a monitor's on-screen
display can be controlled by this service.

%prep
%autosetup

%build
%make_build

%install
install -d -m 0755 %{buildroot}%{_bindir} \
                   %{buildroot}%{_mandir}/man1/ \
                   %{buildroot}%{_mandir}/man7/ \
                   %{buildroot}%{_datadir}/%{name}/examples \
                   %{buildroot}%{_datadir}/dbus-1/services
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0644 com.ddcutil.DdcutilService.service %{buildroot}%{_datadir}/dbus-1/services/
install -m 0755 examples/* %{buildroot}%{_datadir}/%{name}/examples/
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/
install -m 0644 %{name}.7 %{buildroot}%{_mandir}/man7/
install -m 0644 -D -t %{buildroot}%{_prefix}/lib/modules-load.d/ i2c-dev/%{name}.conf

# The post modprobe is helpful for the user, but not really necessary, don't error if it fails
%post
%{_prefix}/sbin/modprobe i2c-dev ||:

%files
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/examples
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/services
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/com.ddcutil.DdcutilService.service
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man7/%{name}.7%{?ext_man}
%{_datadir}/%{name}/examples/dbus-enable-info-logging.bash
%{_datadir}/%{name}/examples/dbus-send-query-brightness.bash
%{_datadir}/%{name}/examples/ddcutil-dasbus-client.py
%{_datadir}/%{name}/examples/ddcutil-dasbus-signal-receiver.py
%{_datadir}/%{name}/examples/ddcutil-qtdbus-client.py
%{_datadir}/%{name}/examples/ddcutil-qtdbus-signal-receiver.py
%{_datadir}/%{name}/examples/busctl.bash
%{_datadir}/%{name}/examples/dbus-enable-signals.bash
%{_datadir}/%{name}/examples/dbus-set-polling-interval.bash
%{_datadir}/%{name}/examples/dbus-send-introspect.bash
%{_datadir}/%{name}/examples/dbus-send-detect.bash
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/%{name}.conf

%changelog
