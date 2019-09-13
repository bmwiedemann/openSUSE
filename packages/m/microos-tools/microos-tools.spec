#
# spec file for package microos-tools
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


Name:           microos-tools
Version:        1.0+git20190812.97ca0ee
Release:        0
Summary:        Files and Scripts for openSUSE MicroOS
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/kubic-project/microos-tools
Source:         microos-tools-%{version}.tar.xz
BuildRequires:  distribution-release
Requires:       read-only-root-fs
Conflicts:      systemd-coredump
Obsoletes:      caasp-tools
BuildArch:      noarch

%description
Files, scripts and directories for openSUSE Kubic.

%prep
%setup -q

%build

%install
cp -a {etc,usr} %{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8

%pre
%service_add_pre setup-systemd-proxy-env.service

%post
%service_add_post setup-systemd-proxy-env.service

%preun
%service_del_preun setup-systemd-proxy-env.service

%postun
%service_del_postun setup-systemd-proxy-env.service

%files
%license COPYING
%config %{_sysconfdir}/systemd/system/systemd-firstboot.service
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%{_unitdir}
%{_prefix}/lib/sysctl.d/30-corefiles.conf
%{_libexecdir}/MicroOS-firstboot
%{_sbindir}/btrfsQuota
%{_sbindir}/setup-systemd-proxy-env
%{_mandir}/man8/btrfsQuota.8%{?ext_man}

%changelog
