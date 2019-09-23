#
# spec file for package openstack-suse
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           openstack-suse
Version:        2015.2
Release:        0
Summary:        OpenStack SUSE
License:        Apache-2.0
Group:          Development/Libraries/Python
Url:            https://www.suse.com/products/suse-cloud/
Source1:        macros.openstack
Source2:        openstack-skeleton.init
Source99:       rpmlintrc
Requires:       %{name}-sudo = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       openstack-suse-macros = %{version}
Requires:       openstack-suse-sudo = %{version}
#NOTE(saschpe): We don't provide openstack-common here to not
#               collide with upstream, sorry:
#Provides:       openstack-common = %%{version}
#Obsoletes:      openstack-common < %%{version}

%description
This packages pulls in various other utility packages that are mainly useful
for OpenStack packaging. Some are even only used at build-time.

%package macros
Summary:        OpenStack SUSE - RPM Macros
Group:          Development/Libraries/Python
Provides:       openstack-macros = %{version}
Obsoletes:      openstack-macros < %{version}
Provides:       openstack-common-macros = %{version}
Obsoletes:      openstack-common-macros < %{version}

%description macros
This package provides OpenStack RPM macros. You need it to build OpenStack
packages.

%package sudo
Summary:        OpenStack SUSE - Sudo Support
Group:          Development/Libraries/Python
# For directory ownership:
BuildRequires:  sudo
Requires:       sudo
Provides:       openstack-common-sudo = %{version}
Obsoletes:      openstack-common-sudo < %{version}

%description sudo
OpenStack packages install sudo configuration files for rootwrap binaries
in /etc/sudoers.d. This directory is disabled by default, thus this package
enables it in /etc/sudoers.

%prep

%build

%install
# Make the base package non-empty for now:
echo "OpenStack SUSE" > README

# Macros sub-package
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.openstack
install -D -m755 %{SOURCE2} %{buildroot}%{_initddir}/openstack-skeleton

# compatibility macros for upstream packaging
%if 0%{?suse_version} < 1330
cat - >> %{buildroot}%{_sysconfdir}/rpm/macros.openstack <<EOF
%%__python2 /usr/bin/python2
%%python2_sitelib  %%python_sitelib
EOF
%endif

# Sudo sub-package, SLES sudo doesn't own /etc/sudoers.d, openSUSE-12.2 and later does:
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
install -d %{buildroot}%{_sysconfdir}/sudoers.d
%endif

# SLE_11_SP2 sudo package doesn't include this directory:
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%post sudo
if ! grep -qE "^#includedir /etc/sudoers.d" /etc/sudoers ; then
echo "#includedir /etc/sudoers.d" >> /etc/sudoers
fi

%postun sudo
sed -i "/^includedir \/etc\/sudoers\.d/d" /etc/sudoers
%endif

%files macros
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.openstack
%{_initddir}/openstack-skeleton

%files sudo
%defattr(-,root,root)
# SLE_11_SP2 sudo package doesn't create this directory, thus we have to own it:
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%dir %attr(0750, root, root) %{_sysconfdir}/sudoers.d
%endif

%changelog
