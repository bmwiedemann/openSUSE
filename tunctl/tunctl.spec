#
# spec file for package tunctl
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           tunctl
Version:        1.5
Release:        0
Summary:        Create and remove virtual network interfaces
License:        GPL-2.0+
Group:          System/Management
Url:            http://tunctl.sourceforge.net/
Source0:        http://sourceforge.net/projects/tunctl/files/tunctl/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-install-manpage-noexec.patch
BuildRequires:  docbook-utils-minimal
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
tunctl is a tool to set up and maintain persistent TUN/TAP network
interfaces, enabling user applications access to the wire side of a
virtual nework interface. Such interfaces is useful for connecting VPN
software, virtualization, emulation and a number of other similar
applications to the network stack.

tunctl originates from the User Mode Linux project.

%prep
%setup -q
%patch0

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} BIN_DIR=/sbin install
install -d -m 0755 %{buildroot}/%{_docdir}/%{name}/
install -m 0644 ChangeLog %{buildroot}/%{_docdir}/%{name}/

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%doc %{_mandir}/man8/%{name}.8*
%attr(0755,root,root) /sbin/tunctl

%changelog
