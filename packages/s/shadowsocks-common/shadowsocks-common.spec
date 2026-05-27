#
# spec file for package shadowsocks-common
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 hillwood Yang <hillwood@opensuse.org>
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

%global selinuxtype targeted

Name:           shadowsocks-common
Version:        1.0.0
Release:        0
Summary:        Shdowsocks Common File
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/shadowsocks
Source0:        shadowsocks.sysuser
Source1:        shadowsocks.tmpfiles
Source2:        %{name}.te
Source3:        %{name}.fc
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-policy-targeted
Requires(pre):  shadowsocks-sysuser = %{version}-%{release}
BuildArch:      noarch
%{sysusers_requires}

%description
Shdowsocks Common File.

%package -n shadowsocks-sysuser
Summary:        Shdowsocks Daemon System User
Requires:       sysuser-shadow
%{sysusers_requires}

%description -n shadowsocks-sysuser
Shdowsocks Daemon System User.

%package -n shadowsocks-common-selinux
Summary:        Selinux support for shadowsocks-libev and shadowsocks-common
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-targeted

%description -n shadowsocks-common-selinux
This package adds SELinux common enforcement to shadowsocks-libev and
shadowsocks-common

%prep
cp %{SOURCE2} shadowsocks_common.te
cp %{SOURCE3} shadowsocks_common.fc

%build
make -f %{_datadir}/selinux/devel/Makefile shadowsocks_common.pp

%install
install -d %{buildroot}%{_sysconfdir}/shadowsocks
install -Dm0644 shadowsocks_common.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/shadowsocks_common.pp

mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE0} %{buildroot}%{_sysusersdir}/shadowsocks.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/shadowsocks.conf

%sysusers_generate_pre %{SOURCE0} shadowsocks shadowsocks.conf

%pre -n shadowsocks-sysuser -f shadowsocks.pre

%post -n shadowsocks-sysuser
%tmpfiles_create %{_tmpfilesdir}/shadowsocks.conf

%post -n shadowsocks-common-selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/shadowsocks_common.pp
%selinux_relabel_post -s %{selinuxtype}

%preun -n shadowsocks-common-selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} shadowsocks_common
fi

%posttrans -n shadowsocks-common-selinux
%selinux_relabel_post -s %{selinuxtype}

%files
%attr(750,root,shadowsocks) %dir %{_sysconfdir}/shadowsocks

%files -n shadowsocks-sysuser
%{_prefix}/lib/sysusers.d/shadowsocks.conf
%{_tmpfilesdir}/shadowsocks.conf

%files -n shadowsocks-common-selinux
%{_datadir}/selinux/packages/%{selinuxtype}/shadowsocks_common.pp

%changelog
