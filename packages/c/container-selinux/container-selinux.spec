#
# spec file for package container-selinux
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


%global selinuxtype targeted
%global moduletype services
%global modulenames container
# Usage: _format var format
# Expand 'modulenames' into various formats as needed
# Format must contain '$x' somewhere to do anything useful
%global _format() export %{1}=""; for x in %{modulenames}; do %{1}+=%{2}; %{1}+=" "; done;
# Version of SELinux we were using
%define selinux_policyver %(rpm -q selinux-policy --qf '%%{version}')
Name:           container-selinux
Version:        2.238.0
Release:        0
Summary:        SELinux policies for container runtimes
License:        GPL-2.0-only
URL:            https://github.com/containers/container-selinux
Source0:        container-selinux-%{version}.tar.xz
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-policy-%{selinuxtype}
Requires:       selinux-policy >= %(rpm -q selinux-policy --qf '%%{version}-%%{release}')
Requires(posttrans): policycoreutils
Requires(posttrans): /usr/bin/sed
Requires(posttrans): selinux-policy-base >= %{selinux_policyver}
Requires(posttrans): selinux-policy-targeted >= %{selinux_policyver}
Requires(posttrans): selinux-tools
BuildArch:      noarch

%description
SELinux policy modules for use with container runtimes.

%prep
%setup -q

%build
%make_build

%install
# install policy modules
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/services
install -p -m 644 container.if %{buildroot}%{_datadir}/selinux/devel/include/services
install -m 0644 $MODULES %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}/%{_datadir}/containers/selinux
install -m 644 container_contexts %{buildroot}/%{_datadir}/containers/selinux/contexts
install -d %{buildroot}%{_datadir}/udica/templates
install -m 0644 udica-templates/*.cil %{buildroot}%{_datadir}/udica/templates
install -d %{buildroot}%{_mandir}/man8/
install -pm 0644 container_selinux.8 %{buildroot}%{_mandir}/man8/

%check

%pre
%selinux_relabel_pre -s %{selinuxtype}

%postun
if [ $1 -eq 0 ]; then
   %selinux_modules_uninstall -s %{selinuxtype} %{modulenames} docker
fi

%posttrans
# Install all modules in a single transaction
if [ $1 -eq 1 ]; then
   %{_sbindir}/setsebool -P -N virt_use_nfs=1 virt_sandbox_use_all_caps=1
fi
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%{_sbindir}/semodule -n -s %{selinuxtype} -r container 2> /dev/null ||:
%{_sbindir}/semodule -n -s %{selinuxtype} -d docker 2> /dev/null ||:
%{_sbindir}/semodule -n -s %{selinuxtype} -d gear 2> /dev/null ||:
%selinux_modules_install -s %{selinuxtype} $MODULES
. %{_sysconfdir}/selinux/config
sed -e "\|container_file_t|h; \${x;s|container_file_t||;{g;t};a\\" -e "container_file_t" -e "}" -i %{_sysconfdir}/selinux/${SELINUXTYPE}/contexts/customizable_types
matchpathcon -qV %{_sharedstatedir}/containers || restorecon -R %{_sharedstatedir}/containers &> /dev/null || :
%selinux_relabel_post -s %{selinuxtype}

%files
%license LICENSE
%doc README.md
%{_datadir}/selinux/*
%dir %{_datadir}/containers
%dir %{_datadir}/containers/selinux
%{_datadir}/containers/selinux/contexts
%dir %{_datadir}/udica
%dir %{_datadir}/udica/templates
%{_datadir}/udica/templates/*
%{_mandir}/man8/container_selinux.8*

%changelog
