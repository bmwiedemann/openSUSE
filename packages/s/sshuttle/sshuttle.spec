#
# spec file for package sshuttle
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


%global pythons python3
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           sshuttle
Version:        1.1.1
Release:        0
Summary:        VPN over an SSH tunnel
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/sshuttle/sshuttle
Source0:        https://files.pythonhosted.org/packages/source/s/sshuttle/sshuttle-%{version}.tar.gz
Source1:        %{name}.service
Source2:        sysconfig.%{name}
Patch0:         fix-pytest.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
Requires(post): %fillup_prereq
BuildArch:      noarch
%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
BuildRequires:  python3-Sphinx
%endif

%description
Transparent proxy server that works as a poor man's VPN. Forwards over ssh.
Doesn't require admin. Supports DNS tunneling.
sshuttle is a program that solves the following case:
- You have access to a remote network via ssh.
- You don't necessarily have admin access on the remote network.
- The remote network has no VPN, or only complex VPN
  protocols (IPsec, PPTP, etc).
- You don't want to create an SSH port forward for every
  single host/port on the remote network.
- You can't use openssh's PermitTunnel feature because
  it's disabled by default on openssh servers; plus it does
  TCP-over-TCP, which has terrible performance.

%prep
%setup -q
%patch0

%build
%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
(
cd docs/;
sed -i '/_scm/d' conf.py
sed -ri 's/(version = )get_version.*/\1 "%{version}"/g' conf.py
%make_build man
)
%endif
%python3_build

%install
%python3_install

%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m0644 docs/_build/man/%{name}.1 %{buildroot}/%{_mandir}/man1/
%endif

%fdupes %{buildroot}/%{python3_sitelib}/%{name}/

# systemd service
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -d -m 755 %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}

# sysconfig file
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}

%check
%pytest

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "%{name} user" %{name}
install -d -m 755 -o %{name} -g %{name} %{_localstatedir}/lib/%{name}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only %{name}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{python3_sitelib}/%{name}*
%{_bindir}/%{name}
%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
%{_mandir}/man1/%{name}.1%{?ext_man}
%endif
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%changelog
