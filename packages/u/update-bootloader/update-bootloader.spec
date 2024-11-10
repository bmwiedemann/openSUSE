#
# spec file for package update-bootloader
#
# Copyright (c) 2024 SUSE LLC
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


%if %{suse_version} > 1550
%define sbindir %{_sbindir}
%else
%define sbindir /sbin
%endif

%{!?_distconfdir:%global _distconfdir /etc}

Name:           update-bootloader
Version:        1.19
Release:        0
Requires:       coreutils
Requires:       util-linux
Obsoletes:      perl-Bootloader < %{version}-%{release}
Obsoletes:      perl-Bootloader-YAML < %{version}
Provides:       perl-Bootloader = %{version}-%{release}
Conflicts:      kexec-tools < 2.0.26.0
Summary:        Tool for boot loader configuration
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            https://github.com/openSUSE/perl-bootloader
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygem(asciidoctor)

%description
Shell script wrapper for configuring various boot loaders.

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot} SBINDIR=%{sbindir} ETCDIR=%{_distconfdir}
make doc
install -D -m 644 pbl.8 %{buildroot}%{_mandir}/man8/pbl.8
install -D -m 644 bootloader_entry.8 %{buildroot}%{_mandir}/man8/bootloader_entry.8
install -D -m 644 update-bootloader.8 %{buildroot}%{_mandir}/man8/update-bootloader.8
install -D -m 644 kexec-bootloader.8 %{buildroot}%{_mandir}/man8/kexec-bootloader.8
mkdir -p %{buildroot}/var/log
touch %{buildroot}/var/log/pbl.log

%post
echo -n >>/var/log/pbl.log
chmod 600 /var/log/pbl.log

%files
%defattr(-, root, root)
%license COPYING
%doc %{_mandir}/man8/*
%doc boot.readme
%{sbindir}/update-bootloader
%{sbindir}/pbl
%{sbindir}/kexec-bootloader
/usr/lib/bootloader
%if "%{_distconfdir}" == "/etc"
%config(noreplace) %{_distconfdir}/logrotate.d/pbl
%else
%{_distconfdir}/logrotate.d/pbl
%endif
%ghost %attr(0600,root,root) /var/log/pbl.log

%changelog
