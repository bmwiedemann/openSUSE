#
# spec file for package targetcli-fb
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           targetcli-fb
Version:        2.1.58
Release:        0
Summary:        A command shell for managing the Linux LIO kernel target
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/open-iscsi/%{name}
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}.service
BuildRequires:  %{python_module configshell-fb}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module rtslib-fb}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(systemd)
Requires:       python-configshell-fb
Requires:       python-dbus-python
Requires:       python-rtslib-fb
Requires:       python-six
Requires:       targetcli-fb-common
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       targetcli    = %{version}-%{release}
Provides:       targetcli-fb = %{version}-%{release}
%endif
Obsoletes:      targetcli < %{version}-%{release}
Obsoletes:      targetcli-fb < %{version}-%{release}
BuildArch:      noarch
%{?systemd_ordering}

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
targetcli-fb-common is the invariant base package needed by
all python-version-dependant packages, such as python3-*-targetcli-fb.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/targetcli
%python_clone -a %{buildroot}%{_bindir}/targetclid
install -d -m755 %{buildroot}%{_sysconfdir}/target
install -d -m755 %{buildroot}%{_sysconfdir}/target/backup
install -d -m755 %{buildroot}%{_sbindir}
install -D -m644 targetcli.8 %{buildroot}%{_mandir}/man8/targetcli.8
install -D -m644 targetclid.8 %{buildroot}%{_mandir}/man8/targetclid.8
install -D -m644 %{S:1} %{buildroot}%{_unitdir}/targetcli.service
install -D -m644 systemd/targetclid.service %{buildroot}%{_unitdir}/targetclid.service
install -D -m644 systemd/targetclid.socket %{buildroot}%{_unitdir}/targetclid.socket
%fdupes %{buildroot}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rctargetcli
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rctargetclid

%post
%python_install_alternative targetcli
%python_install_alternative targetclid

%postun
%python_uninstall_alternative targetcli
%python_uninstall_alternative targetclid

%pre
%{service_add_pre targetcli.service targetclid.socket targetclid.service}

%preun
%{stop_on_removal targetclid targetcli}
%{service_del_preun targetcli.service targetclid.socket targetclid.service}

%post -n %{name}-common
%{service_add_post targetcli.service targetclid.socket targetclid.service}

%postun -n %{name}-common
%{service_del_postun targetcli.service targetclid.socket targetclid.service}

%pre -n %{name}-common
%{service_add_pre targetcli.service targetclid.socket targetclid.service}

%preun -n %{name}-common
%{service_del_preun targetcli.service targetclid.socket targetclid.service}

%files %{python_files}
%python_alternative %{_bindir}/targetcli
%python_alternative %{_bindir}/targetclid
%{python_sitelib}/*

%files -n %{name}-common
%license COPYING
%doc README.md THANKS
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc %{_mandir}/man8/targetcli.8%{ext_man}
%doc %{_mandir}/man8/targetclid.8%{ext_man}
%{_unitdir}/targetcli.service
%{_unitdir}/targetclid.service
%{_unitdir}/targetclid.socket
%{_sbindir}/rctargetcli
%{_sbindir}/rctargetclid

%changelog
