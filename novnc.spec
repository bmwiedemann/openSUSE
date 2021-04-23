#
# spec file for package novnc
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           novnc
Version:        1.2.0
Release:        0
Summary:        VNC client using HTML5 (Web Sockets, Canvas) with encryption support
License:        MPL-2.0 AND LGPL-3.0-only
Group:          System/Daemons
URL:            https://github.com/novnc/noVNC
Source0:        noVNC-%{version}.tar.gz
Patch1:         novnc-0.3-manpage.patch
Patch2:         novnc-1.1.0-fix-interpreter.patch
%if 0%{?suse_version} < 1330
Requires:       python2-websockify
%else
Requires:       python3-websockify
%endif
BuildArch:      noarch

%description
This package provides a Websocket implementation of the VNC client.
It is used by OpenStack Horizon to provide a console view of running
instances.

%prep
%setup -q -n noVNC-%{version}
%patch1 -p1
%patch2

%build

%install
mkdir -p %{buildroot}/%{_usr}/share/novnc/utils
install -m 444 *html %{buildroot}/%{_usr}/share/novnc
install -m 444 vnc.html %{buildroot}/%{_usr}/share/novnc/index.html
install -m 444 vnc_lite.html %{buildroot}/%{_usr}/share/novnc/vnc_auto.html

mkdir -p %{buildroot}/%{_usr}/share/novnc/app/
cp -rp app  %{buildroot}/%{_usr}/share/novnc

mkdir -p %{buildroot}/%{_usr}/share/novnc/core
cp -rp core  %{buildroot}/%{_usr}/share/novnc

mkdir -p %{buildroot}/%{_usr}/share/novnc/vendor
cp -rp vendor  %{buildroot}/%{_usr}/share/novnc

mkdir -p %{buildroot}/%{_bindir}
install utils/launch.sh  %{buildroot}/%{_bindir}/novnc_server

mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/novnc_server.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/novnc_server
%{_datadir}/novnc/
%{_mandir}/man1/novnc_server.1%{?ext_man}

%changelog
