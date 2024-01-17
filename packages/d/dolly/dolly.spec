#
# spec file for package dolly
#
# Copyright (c) 2022 SUSE LLC
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


Name:           dolly
Summary:        Tool for cloning data of one machine to other machines
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
Version:        0.64.2
Release:        0
URL:            https://github.com/openSUSE/dolly
Source0:        dolly-%{version}.tar.xz

#SLE15* does not contain pandoc packages
%if 0%{?is_opensuse}
%ifnarch i586
BuildRequires:  firewalld
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
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?is_opensuse}
%ifnarch i586
make %{?_smp_mflags}
%else
make %{?_smp_mflags} dolly
%endif
%else
make %{?_smp_mflags} dolly
%endif

%install
%make_install
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcdolly

%pre
%service_add_pre dolly.service dolly.socket

%post
%service_add_post dolly.service dolly.socket

%preun
%service_del_preun dolly.service dolly.socket

%postun
%service_del_postun dolly.service dolly.socket

%files
%doc README.md send_multiple_files.pl
%license LICENSE
%defattr(-,root,root,-)
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%attr(755,root,root) %{_sbindir}/dolly
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/firewalld/services/dolly.xml
%if 0%{?is_opensuse}
%ifnarch i586
%{_mandir}/man1/dolly.1.gz
%endif
%endif
%{_sbindir}/rcdolly
%{_unitdir}/dolly.service
%{_unitdir}/dolly.socket

%changelog
