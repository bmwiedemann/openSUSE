#
# spec file for package traceroute
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


Name:           traceroute
Version:        2.1.0
Release:        0
Summary:        Packet route path tracing utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other   
Url:            http://traceroute.sourceforge.net/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch0:         traceroute-autotools.patch
Patch1:         traceroute-secure_getenv.patch
BuildRequires:  automake
Provides:       net-tools:%{_sbindir}/%{name}
Provides:       tcptraceroute
Obsoletes:      tcptraceroute <= 1.5.beta7

%description
Traceroute tracks the route packets taken from an IP network on their way to a given host.
It utilizes the IP protocol's time to live (TTL) field and attempts to elicit an ICMP TIME_EXCEEDED 
response from each gateway along the path to the host. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export LDFLAGS="-Wl,-z,relro,-z,now"
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
ln -sf %{_sbindir}/%{name} %{buildroot}%{_sbindir}/%{name}6
ln -s %{_mandir}/man8/traceroute.8 %{buildroot}%{_mandir}/man8/traceroute6.8
install -D -m0755 wrappers/tcptraceroute %{buildroot}%{_bindir}/tcptraceroute
install -m0644 wrappers/tcptraceroute.8 %{buildroot}%{_mandir}/man8/tcptraceroute.8

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README
%{_bindir}/tcptraceroute
%{_sbindir}/%{name}
%{_sbindir}/%{name}6
%{_mandir}/man8/traceroute*.8*
%{_mandir}/man8/tcptraceroute.8*

%changelog
