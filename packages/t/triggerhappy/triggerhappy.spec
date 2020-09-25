#
# spec file for package triggerhappy
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           triggerhappy
Version:        0.5.0
Release:        0
Summary:        Lightweight hotkey daemon
License:        GPL-3.0+
Group:          System/Base
Url:            https://github.com/wertarbyte/triggerhappy
Source:         https://github.com/wertarbyte/triggerhappy/archive/release/0.5.0.tar.gz
Patch:          0001-Fix-systemd-service.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Triggerhappy
- a lightweight hotkey daemon -

by Stefan Tomanek <stefan.tomanek+th@wertarbyte.de>
http://github.com/wertarbyte/triggerhappy/

Triggerhappy is a hotkey daemon developed with small and embedded systems in
mind, e.g. linux based routers. It attaches to the input device files and
interprets the event data received and executes scripts configured in its
configuration.

%prep
%setup -q -n %{name}-release-%{version}
%patch -p1

%build
make %{?_smp_mflags}

%install
%make_install
install -D -m 644 -t %{buildroot}/usr/lib/systemd/system systemd/%{name}.service systemd/%{name}.socket
install -D -m 644 udev/triggerhappy-udev.rules %{buildroot}/usr/lib/udev/rules.d/98-triggerhappy.rules
mkdir -p %{buildroot}/etc/triggerhappy/triggers.d/

%pre
%service_add_pre %{name}.service %{name}.socket

%post
%service_add_post %{name}.service %{name}.socket

%postun
%service_del_postun %{name}.service %{name}.socket

%preun
%service_del_preun %{name}.service %{name}.socket

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING triggerhappy.conf.examples
%{_sbindir}/th*
%{_mandir}/man1/th*
%dir %{_udevrulesdir}
%{_udevrulesdir}/??-%{name}.rules
%{_unitdir}/%{name}.*
%dir /etc/triggerhappy
%dir /etc/triggerhappy/triggers.d/

%changelog
