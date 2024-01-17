#
# spec file for package sipcalc
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           sipcalc
Version:	1.1.6
Release:	0
License:	BSD-3-Clause
Summary:	Console based ip subnet calculator with IPv4 and IPv6 support
Url:		http://www.routemeister.net/projects/sipcalc
Group:		Productivity/Networking/System
Source:		%{name}-%{version}.tar.gz	
Source1:	%{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sipcalc is an console based ip subnet calculator with IPv4 and IPv6 support.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/sipcalc.1.gz
%{_bindir}/sipcalc

%changelog
