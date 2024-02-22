#
# spec file for package hostap-utils
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hostap-utils
Version:        0.4.7
Release:        0
Summary:        Tools for Prism2 cards
License:        GPL-2.0+
Group:          Hardware/Wifi
Url:            http://hostap.epitest.fi/
Source:         http://w1.fi/releases/%{name}-%{version}.tar.gz
Patch0:         hostap-utils.diff
BuildRequires:  openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains various tools for configuring Prism2 cards driven
by the HostAP kernel module. In particular, it contains a utility to
query and flash firmware of Prism2 adapters.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags}" CC="gcc" make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_sbindir}
install -m 755 hostap_crypt_conf %{buildroot}/%{_sbindir}
install -m 755 hostap_diag %{buildroot}/%{_sbindir}
install -m 755 hostap_io_debug %{buildroot}/%{_sbindir}
install -m 755 hostap_rid %{buildroot}/%{_sbindir}
install -m 755 prism2_param %{buildroot}/%{_sbindir}
install -m 755 prism2_srec %{buildroot}/%{_sbindir}
install -m 755 split_combined_hex %{buildroot}/%{_sbindir}

%files
%defattr(-,root,root)
%{_sbindir}/*
%doc README ChangeLog

%changelog
