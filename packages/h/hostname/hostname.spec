#
# spec file for package hostname
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           hostname
Version:        3.21
Release:        0
Summary:        Utility to Set/Show the Host Name or Domain Name
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Url:            https://tracker.debian.org/pkg/hostname
Source:         http://http.debian.net/debian/pool/main/h/%{name}/%{name}_%{version}.tar.gz#/%{name}-%{version}.tar.gz
# net-tools requires hostname, but we know we do not rely on ourselves to build
#!BuildIgnore:  hostname

%description
This package provides commands which can be used to display the system's DNS
name, and to display or set its hostname or NIS domain name.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -D_GNU_SOURCE"

%install
install -D -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -d -m 755 %{buildroot}/bin/
ln -sf %{_bindir}/%{name} %{buildroot}/bin/%{name}
install -D -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
for prog in dnsdomainname domainname ypdomainname nisdomainname; do
    ln -sf %{_bindir}/%{name} %{buildroot}/bin/$prog
    ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/$prog
    ln -sf hostname.1 %{buildroot}%{_mandir}/man1/${prog}.1
done

%files
%license COPYRIGHT
%doc debian/changelog
/bin/%{name}
/bin/domainname
/bin/dnsdomainname
/bin/nisdomainname
/bin/ypdomainname
%{_bindir}/%{name}
%{_bindir}/domainname
%{_bindir}/dnsdomainname
%{_bindir}/nisdomainname
%{_bindir}/ypdomainname
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/domainname.1%{ext_man}
%{_mandir}/man1/dnsdomainname.1%{ext_man}
%{_mandir}/man1/nisdomainname.1%{ext_man}
%{_mandir}/man1/ypdomainname.1%{ext_man}

%changelog
