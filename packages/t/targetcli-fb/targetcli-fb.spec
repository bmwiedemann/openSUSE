#
# spec file for package targetcli-fb
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           targetcli-fb
Version:        2.1.49
Release:        0
Summary:        A command shell for managing the Linux LIO kernel target
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/open-iscsi/%{name}
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}.service
BuildRequires:  %{python_module configshell-fb}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module rtslib-fb}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd
Requires:       python-configshell-fb
Requires:       python-dbus-python
Requires:       python-rtslib-fb
Requires:       python-six
Requires:       targetcli-fb-common
Requires(post): update-alternatives
Requires(postun): update-alternatives
%ifpython3
Provides:       targetcli    = %{version}-%{release}
Provides:       targetcli-fb = %{version}-%{release}
%endif
Obsoletes:      targetcli
Obsoletes:      targetcli-fb
BuildArch:      noarch
%if 0%{?sle_version} >= 150000
# explicit Provides advertising RBD support
Provides:       targetcli-rbd = %{version}
Obsoletes:      targetcli-rbd < %{version}
%endif
%{?systemd_requires}
Patch1:         Split-out-blockdev-readonly-state-detection-helper.patch
Patch2:         rbd-support.patch
Patch3:         saveconfig-compress-the-backup-config-files
Patch4:         targetcli-fb-fix-raise-exception-error-in-save_backups
Patch5:         Add-emulate_pr-backstore-attribute.patch
Patch6:         do-not-remove-the-first-digit-when-auto-completing-the-tpg-tag
Patch7:         iscsi-discovery_auth-enable-is-a-number-not-a-string

%python_subpackages

%description
targetcli-fb is a command-line interface for configuring the LIO generic
SCSI target, present in 3.x Linux kernel versions.

targetcli-fb is a fork of the "targetcli" code written by RisingTide Systems.
The "-fb" differentiates between the original and this version. Please ensure
to use either all "fb" versions of the targetcli components -- targetcli,
rtslib, and configshell, or stick with all non-fb versions, since they are
no longer strictly compatible.

%package -n %{name}-common
Summary:        Common targetcli-fb subpackage for either flavor of Python
Group:          System/Management
Provides:       %{python_module targetcli-fb-common}

%description -n %{name}-common
targetcli-fb-common is the invariant base package needed by both
python2-targetcli-fb and python3-targetcli-fb.

%prep
%setup -q
%patch1 -p1
%if 0%{?sle_version} >= 150000
# RBD support is dependent on LIO changes present in the SLE/Leap kernel
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/targetcli
install -d -m755 %{buildroot}%{_sysconfdir}/target
install -d -m755 %{buildroot}%{_sysconfdir}/target/backup
install -d -m755 %{buildroot}%{_sbindir}
install -D -m644 targetcli.8 %{buildroot}%{_mandir}/man8/targetcli.8
install -D -m644 %{SOURCE1} %{buildroot}%{_unitdir}/targetcli.service
%fdupes %{buildroot}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rctargetcli

%post
%python_install_alternative targetcli

%postun
%python_uninstall_alternative targetcli

%pre
%{service_add_pre targetcli.service}

%preun
%{stop_on_removal targetcli}

%post -n %{name}-common
%{service_add_post targetcli.service}

%postun -n %{name}-common
%{service_del_postun targetcli.service}

%pre -n %{name}-common
%{service_add_pre targetcli.service}

%preun -n %{name}-common
%{service_del_preun targetcli.service}

%files %{python_files}
%python_alternative %{_bindir}/targetcli
%{python_sitelib}/*

%files -n %{name}-common
%doc COPYING README.md THANKS
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc %{_mandir}/man8/targetcli.8%{ext_man}
%{_unitdir}/targetcli.service
%{_sbindir}/rctargetcli

%changelog
