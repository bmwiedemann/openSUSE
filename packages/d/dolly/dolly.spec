#
# spec file for package dolly
#
# Copyright (c) 2021 SUSE LLC
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

%define _fwdefdir %{_prefix}/lib/firewalld/services
%define vers 0.63.6

Name:           dolly
Summary:        Tool for cloning data of one machine to other machines
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
Version:        %vers
Release:        0
URL:            http://www.cs.inf.ethz.ch/stricker/CoPs/patagonia/dolly.html
Source0:        https://github.com/openSUSE/dolly/archive/%{version}.tar.gz#/dolly-%{version}.tar.bz2
Source1:        dolly.conf
Source2:        dolly.md
Source3:        dolly_firewall.xml

#SLE15* does not contain pandoc packages
%if 0%{?is_opensuse}
%ifnarch i586
BuildRequires:  pandoc
Requires:       gzip
%endif
%endif

%description
Dolly is used to clone data of one machine to (possibly many)
other machines. It can distribute image files (even gnu-zipped),
partitions or whole hard disk drives to other partitions or
hard disk drives. As it forms a "virtual TCP ring" to distribute
data, it works best with fast switched networks.

As dolly can clone whole partitions block-wise, it works for 
most filesystems, including the types for Linux, Windows, Oberon,
Solaris.

%prep
%autosetup -p1
#mv %{name}-%{version}/* .
#rmdir %{name}-%{commit}/

%build
make %{?_smp_mflags}
%if 0%{?is_opensuse}
%ifnarch i586
pandoc --standalone -t man %{SOURCE2} -o dolly.1
gzip dolly.1
%endif
%endif

%install
install -D -m 755 $RPM_BUILD_DIR/%{name}-%{version}/dolly %{buildroot}%{_sbindir}/dolly
install -D -m 644  %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf
# install firewall conf
mkdir -p %{buildroot}/%{_fwdefdir}
install -m 644 %{S:3} %{buildroot}/%{_fwdefdir}/dolly.xml

%if 0%{?is_opensuse}
%ifnarch i586
install -D -m 644 dolly.1.gz %{buildroot}%{_mandir}/man1/dolly.1.gz
%endif
%endif

%files
%doc README.md dolly.example
%defattr(-,root,root,-)
%dir %{_prefix}/lib/firewalld
%dir %{_fwdefdir}
%attr(755,root,root) %{_sbindir}/dolly
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(644,root,root) %config(noreplace) %{_fwdefdir}/dolly.xml
%if 0%{?is_opensuse}
%ifnarch i586
%{_mandir}/man1/dolly.1.gz
%endif
%endif

%changelog
