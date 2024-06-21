#
# spec file for package health-checker
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


%define _dracutmoduledir %(pkg-config --variable=dracutmodulesdir dracut)

Name:           health-checker
Version:        1.10+git20240111.cb84209
Release:        0
Summary:        Service for verifying that important services are running
License:        GPL-2.0-only
Group:          System/Base
URL:            https://github.com/kubic-project/health-checker
Source:         health-checker-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(systemd)
Requires:       health-checker-plugins = 1.0
BuildArch:      noarch

%description
health-checker is a service running once at every reboot to verify
that all important services are running. If it is the first reboot after
an update, an automatic rollback to the last working snapshot is made.
If this is not after an update, a reboot is made. If this does not help,
the services will be disabled.
This package does not contain any checks. For this, additional
plugins for different products are needed.

%package plugins-MicroOS
Summary:        Health-checker plugins for openSUSE MicroOS
Group:          System/Base
Requires:       %{name} >= %{version}
Provides:       health-checker-plugins = 1.0

%description plugins-MicroOS
This package contains health-checker plugins for testing that
the openSUSE MicroOS did boot correctly.

%package plugins-kubic
Summary:        Health-checker plugins for openSUSE Kubic
Group:          System/Base
Requires:       %{name} >= %{version}
Provides:       health-checker-plugins = 1.0

%description plugins-kubic
This package contains health-checker plugins for testing that
the openSUSE Kubic did boot correctly.

%package plugins-caasp
Summary:        Health-checker plugins for SUSE CaaS Platform
Group:          System/Base
Requires:       %{name} >= %{version}
Provides:       health-checker-plugins = 1.0

%description plugins-caasp
This package contains health-checker plugins for testing that
the SUSE CaaS Platform did boot correctly.

%package testing
Summary:        Test plugin for health-checker
Group:          System/Base
Requires:       %{name} >= %{version}
Provides:       health-checker-plugins = 1.0

%description testing
This package contains a script for testing the CaaSP health checker.
It will report success or failures depending on previous states.

%prep
%setup -q -n health-checker-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}%{_mandir}

%pre
%service_add_pre health-checker.service

%post
%service_add_post health-checker.service
%regenerate_initrd_post

%preun
%service_del_preun health-checker.service

%postun
%service_del_postun health-checker.service
%regenerate_initrd_post

%posttrans
%regenerate_initrd_posttrans

%files
%license COPYING
%doc NEWS README.md
%{_unitdir}/health-checker.service
%dir %{_libexecdir}/health-checker/
%{_libexecdir}/health-checker/btrfs-subvolumes-mounted.sh
%{_libexecdir}/health-checker/logind.sh
%{_libexecdir}/health-checker/tmp.sh
%{_sbindir}/health-checker
%{_mandir}/man8/health-checker.8%{?ext_man}
%{_mandir}/man8/health-checker.service.8%{?ext_man}
%dir %{_sysconfdir}/grub.d
%{_sysconfdir}/grub.d/*_health_check*
%{_dracutmoduledir}/50health-checker

%files plugins-MicroOS
%{_libexecdir}/health-checker/crio.sh
%{_libexecdir}/health-checker/etc-overlayfs.sh
%{_libexecdir}/health-checker/rebootmgr.sh

%files plugins-caasp
%{_libexecdir}/health-checker/etcd.sh

%files plugins-kubic
%{_libexecdir}/health-checker/kubelet.sh

%files testing
%{_libexecdir}/health-checker/health-check-tester.sh

%changelog
