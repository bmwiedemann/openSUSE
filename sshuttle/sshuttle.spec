#
# spec file for package sshuttle
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
Name:           sshuttle
Version:        0.78.4
Release:        0
Summary:        VPN over an SSH tunnel
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/sshuttle/sshuttle
Source0:        https://files.pythonhosted.org/packages/source/s/sshuttle/sshuttle-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
Requires:       python3-setuptools
%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
BuildRequires:  python3-Sphinx
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module setuptools_scm}
%endif
BuildArch:      noarch

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
%setup -q -n sshuttle-%{version}

%build
%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
(
cd docs/;
sed -i '/_scm/d' conf.py
sed -ri 's/(version = )get_version.*/\1 "%{version}"/g' conf.py
make %{?_smp_mflags} man
)
%endif
%python3_build

%install
%python3_install

%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
mkdir -pm0755  %{buildroot}/%{_mandir}/man1/
install -m0644 docs/_build/man/sshuttle.1 %{buildroot}/%{_mandir}/man1/
%endif

%check
pytest

%files
%{python3_sitelib}/sshuttle*
%{_bindir}/sshuttle
%if (0%{?suse_version} >= 1320 || 0%{?suse_version} == 1310)
%{_mandir}/man1/sshuttle.1%{?ext_man}
%endif

%changelog
