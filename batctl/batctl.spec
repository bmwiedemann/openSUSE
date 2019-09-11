#
# spec file for package batctl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           batctl
Version:        2018.1
Release:        0
Summary:        B.A.T.M.A.N. advanced control and management tool
License:        GPL-2.0-only AND MIT
Group:          Productivity/Networking/Other
Url:            http://www.open-mesh.org/projects/batctl
Source0:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz
Source1:        http://downloads.open-mesh.org/batman/stable/sources/batctl/%{name}-%{version}.tar.gz.asc
Source2:        batctl.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0)

%description
Why do I need batctl?  B.A.T.M.A.N. advanced operates on layer 2 and
thus all hosts participating in the virtual switch are completely
transparent for all protocols above layer 2.  Therefore the common
diagnosis tools do not work as expected.  To overcome these problems
batctl was created.  At the moment batctl contains ping, traceroute,
tcpdump and interfaces to the kernel module settings.

%prep
%setup -q

%build
export CFLAGS='%{optflags}'
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 man/%{name}.8 %{buildroot}%{_mandir}/man8
install -m 755 %{name} %{buildroot}%{_bindir}

%files
%doc CHANGELOG.rst README.rst
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{ext_man}

%changelog
