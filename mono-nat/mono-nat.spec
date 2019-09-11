#
# spec file for package mono-nat
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mono-nat
Version:        1.1.0
Release:        0
Summary:        A .NET library for automatic port forwarding
License:        MIT
Group:          Development/Languages/Mono
Url:            http://projects.qnetp.net/projects/show/mono-nat
Source:         http://projects.qnetp.net/attachments/download/76/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  mono-core
BuildRequires:  mono-data
BuildRequires:  mono-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package devel
Summary:        A .NET library for automatic port forwarding
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description
A .NET library for automatic port forwarding using either uPnP or nat-pmp

%description devel
A .NET library for automatic port forwarding using either uPnP or nat-pmp. The package config files for mono.nat

%prep
%setup -q

%build
./configure --libdir=%{_prefix}/lib
make

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/pkgconfig/
mv %{buildroot}%{_prefix}/lib/pkgconfig/mono.nat.pc %{buildroot}%{_datadir}/pkgconfig/mono.nat.pc

%files
%defattr(-,root,root)
%{_prefix}/lib/mono-nat

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/mono.nat.pc

%changelog
