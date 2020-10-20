#
# spec file for package container-selinux
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
Version:        2.145.0
Release:        0
Summary:        SELinux policies for container runtimes
License:        GPL-2.0-only
URL:            https://github.com/containers/container-selinux
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  selinux-policy >= %{selinux_policyver}
BuildRequires:  selinux-policy-devel >= %{selinux_policyver}
Requires:       selinux-policy >= %(rpm -q selinux-policy --qf '%%{version}-%%{release}')
Requires(post): policycoreutils
Requires(post): /usr/bin/sed
Requires(post): selinux-policy-base >= %{selinux_policyver}
Requires(post): selinux-policy-targeted >= %{selinux_policyver}
Requires(post): selinux-tools
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

%check

%pre
%selinux_relabel_pre -s %{selinuxtype}

%post
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

%postun
if [ $1 -eq 0 ]; then
   %selinux_modules_uninstall -s %{selinuxtype} %{modulenames} docker
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files
%license LICENSE
%doc README.md
%{_datadir}/selinux/*
%dir %{_datadir}/containers
%dir %{_datadir}/containers/selinux
%{_datadir}/containers/selinux/contexts

%changelog
