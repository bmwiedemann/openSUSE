#
# spec file for package selinux-policy-gaming
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global selinuxtype targeted
%global selinuxbooleans selinuxuser_execmod=1 selinuxuser_execstack=1 selinuxuser_execheap=1

Name:           selinux-policy-targeted-gaming
Version:        3
Release:        0
Summary:        SELinux policy changes for a simplified gaming experience
License:        MIT
URL:            https://en.opensuse.org/Portal:SELinux/Common_issues#Steam_Proton,_Bottles,_WINE,_Lutris,_not_working
Source1:        README.md
BuildArch:      noarch
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-%{selinuxtype}
Requires:       selinux-tools
Requires:       selinux-policy
Requires:       selinux-policy-%{selinuxtype}
Requires:       policycoreutils-python-utils

%description
SELinux policy changes for a simplified gaming experience

%prep

%build
cp -a %{SOURCE1} .

%install

%check

%files
%doc README.md

%post
# first install
if [ $1 -eq 1 ]; then
    %selinux_set_booleans -s %{selinuxtype} %{selinuxbooleans}
fi

%postun
if [ $1 -eq 0 ]; then
    %selinux_unset_booleans -s %{selinuxtype} %{selinuxbooleans}
fi

%changelog

