#
# spec file for package wrapsix
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


Name:           wrapsix
Version:        0.2.1
Release:        0
Summary:        Software implementation of NAT64
License:        GPL-3.0-only
Group:          System/Daemons
URL:            https://www.wrapsix.org/
#Git-Clone:     https://github.com/xHire/wrapsix.git
Source:         https://www.wrapsix.org/download/%{name}-%{version}.tar.bz2
Source1:        %{name}.service
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  systemd-rpm-macros
%systemd_requires

%description
WrapSix is a NAT64 gateway, implemented in userspace. So far, it is
faster than than Ecdysis (a kernelspace implementation) and Tayga
(another userspace implementation).

%prep
%setup -q

%build
autoreconf -fi
%configure \
  --docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
rm -f %{buildroot}/%{_docdir}/%{name}/{COPYING,NEWS}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_sbindir}/wrapsix
%{_sbindir}/rcwrapsix
%config %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service

%changelog
