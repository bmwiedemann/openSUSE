#
# spec file for package transactional-update
#
# Copyright (c) 2020 SUSE LLC
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


Name:           transactional-update
Version:        2.25.1
Release:        0
Summary:        Transactional Updates with btrfs and snapshots
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/transactional-update
Source:         https://github.com/openSUSE/transactional-update/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        transactional-update.check
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  libzypp
BuildRequires:  pkgconfig
BuildRequires:  python3-lxml
BuildRequires:  rpm-devel
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       /usr/bin/bc
Requires:       btrfsprogs
Requires:       logrotate
Requires:       lsof
# psmisc is needed because of fuser
Requires:       psmisc
Requires:       rsync
Requires:       snapper
Requires:       zypper
Recommends:     rebootmgr

%description
transactional-update is a tool to update a system in an atomic
way with zypper, btrfs and snapshots.

%prep
%setup -q

%build
if [ -x autogen.sh ]; then
	./autogen.sh
fi
%configure --with-doc --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}
# Use "up" for non-rolling releases
%if %{defined sle_version} && %{undefined is_susecasp}
sed -i 's/^UPDATE_METHOD=.*/UPDATE_METHOD=up/' etc/transactional-update.conf
%endif

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/zypp/systemCheck.d/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/zypp/systemCheck.d/
%fdupes %{buildroot}%{_mandir}

%pre
%service_add_pre %{name}.service %{name}.timer create-dirs-from-rpmdb.service

%post
%service_add_post %{name}.service %{name}.timer create-dirs-from-rpmdb.service
%regenerate_initrd_post

%posttrans
%regenerate_initrd_posttrans

%preun
%service_del_preun %{name}.service %{name}.timer create-dirs-from-rpmdb.service

%postun
%service_del_postun %{name}.service %{name}.timer create-dirs-from-rpmdb.service
%regenerate_initrd_post

%files
%license COPYING
%doc NEWS
%doc %{_docdir}/%{name}/transactional-update.txt
%config(noreplace) %{_sysconfdir}/logrotate.d/transactional-update
%{_unitdir}/transactional-update.service
%{_unitdir}/transactional-update.timer
%{_unitdir}/create-dirs-from-rpmdb.service
%{_sbindir}/create_dirs_from_rpmdb
%{_sbindir}/transactional-update
%{_sbindir}/tu-rebuild-kdump-initrd
%dir %{_prefix}%{_sysconfdir}
%{_prefix}%{_sysconfdir}/transactional-update.conf
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/50transactional-update/
%{_mandir}/man5/transactional-update.conf.5%{?ext_man}
%{_mandir}/man8/transactional-update.8%{?ext_man}
%{_mandir}/man8/transactional-update.timer.8%{?ext_man}
%{_mandir}/man8/transactional-update.service.8%{?ext_man}
%exclude %{_docdir}/%{name}/*.html

%package zypp-config
Summary:        Zypper rule to prevent uninstallation of transactional-update
Group:          System/Base
BuildArch:      noarch
Requires:       transactional-update

%description zypp-config
Adds a zypper rule to prevent accidental uninstallation of
transactional-update.

%files zypp-config
%config(noreplace) %{_sysconfdir}/zypp/systemCheck.d/transactional-update.check

%changelog
