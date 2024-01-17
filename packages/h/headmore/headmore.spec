#
# spec file for package headmore
#
# Copyright (c) 2016 Howard Guo <guohouzuo@gmail.com>
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

Name:           headmore
Version:        1.2
Release:        0
License:        GPL-3.0
Summary:        VNC client for character terminals
Url:            https://github.com/HouzuoGuo/headmore
Group:          Productivity/Networking/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(caca) pkgconfig(libvncclient)
BuildRequires:  libgcrypt-devel libjpeg8-devel libopenssl-devel libpng16-compat-devel

%description
headmore is a client for Virtual Network Computing (VNC),
it is designed for running in character terminals such as
Linux VT, xterm, or any other terminal emulator. headmore
is fully capable of directing keyboard input to VNC and
control mouse cursor movements.

%prep
%setup -q

%build
gzip headmore.1
make

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%defattr(-,root,root)
%doc key-map.png LICENSE README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
