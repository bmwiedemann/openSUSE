#
# spec file for package warewulf4
#
# Copyright (c) 2021 SUSE LLC
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


%global provider        github
%global provider_tld    com
%global project         hpcng
%global repo            warewulf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

ExclusiveArch:  x86_64 aarch64

Name:           warewulf4
Version:        4.2.0
Release:        0
Summary:        A suite of tools for clustering
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://warewulf.hpcng.org/docs/
Source0:        https://github.com/hpcng/warewulf/archive/v%{version}.tar.gz#/warewulf-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        warewulf.conf
Source3:        warewulf4-rpmlintrc
# no firewalld in sle12
%if 0%{?sle_version} >= 150000 || 0%{?suse_version} > 1500
BuildRequires:  firewalld
%endif
BuildRequires:  go >= 1.15
BuildRequires:  golang-packaging
BuildRequires:  make
BuildRequires:  sysuser-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch0:         LocalStateDir-is-configureable-to-meet-FHS.patch
Requires:       %{name}-overlay
Requires:       dhcp-server
Requires:       ipmitool
Requires:       tftp

%{go_nostrip}

%description
Warewulf v4 combines ultra scalability, flexibility, and simplicity with being light weight, non-intrusive, and a great tool for scientists and seasoned system administrators alike. Warewulf empowers you to scalably and easily manage thousands of compute resources.

%package overlay
# Smells like a circular dependcy, but needed in this case as the
# files belong to the warewulf user
Requires(pre):  %{name}
Summary:        Default overlay for warewulf
Group:          Productivity/Clustering/Computing

%description overlay
Includes the default overlays so that they can be updated seprately.

%prep
%setup -q -n warewulf-%{version}
%setup -q -D -T -a 1 -n warewulf-%{version}
%autopatch -p1

%build
%goprep %{import_path}

make %{?_smp_mflags}

%install
LOCALSTATE=%{_localstatedir}/lib/warewulf/ %{makeinstall}
mkdir -p %{buildroot}%{_sbindir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcwarewulfd
chmod 755 %{buildroot}%{_localstatedir}/lib/warewulf/overlays/system/default/warewulf/init.d/*
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv -v %{buildroot}%{_sysconfdir}/bash_completion.d/warewulf %{buildroot}%{_datadir}/bash-completion/completions/wwctl
cp %{S:2} %{buildroot}%{_sysconfdir}/warewulf/warewulf.conf
# create systemuser
echo "u warewulf -" > system-user-%{name}.conf
echo "g warewulf -" >> system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf %{name} system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf

%pre -f %{name}.pre
%service_add_pre warewulfd.service

%post
%service_add_post warewulfd.service

%preun
%service_del_preun warewulfd.service

%postun
%service_del_postun warewulfd.service

%files
%defattr(-,root,root)
%doc README.md LICENSE.md
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf/dhcp
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf/ipxe
%{_datadir}/bash-completion/completions/wwctl
%{_mandir}/man1/wwctl*1.gz
%config(noreplace) %{_sysconfdir}/warewulf/warewulf.conf
%config(noreplace) %{_sysconfdir}/warewulf/hosts.tmpl
%config(noreplace) %{_sysconfdir}/warewulf/dhcp/*.conf
%config(noreplace) %{_sysconfdir}/warewulf/ipxe/*.ipxe
%{_prefix}/lib/firewalld/services/warewulf.xml
%{_localstatedir}/lib/warewulf
%exclude %{_localstatedir}/lib/warewulf/overlays
%{_bindir}/wwctl
%{_sbindir}/rcwarewulfd
%{_unitdir}/warewulfd.service
%{_sysusersdir}/system-user-%{name}.conf

%files overlay
# The configuration files in this location are for the compute
# nodes, so when modified we do not replace them as sensible
# admin will read the changelog
%config(noreplace) %{_localstatedir}/lib/warewulf/overlays

%changelog
