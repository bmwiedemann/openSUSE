#
# spec file for package dummy-release
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


Name:           dummy-release
Version:        15
Release:        0
Provides:       distribution-release
Conflicts:      otherproviders(distribution-release)
Requires:       this-is-only-for-build-envs
Summary:        SUSE release version files
License:        BSD-3-Clause
Group:          System/Fhs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the files: /etc/issue,
/etc/issue.net and /etc/os-release

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc
echo -e "\nWelcome to Dummy Product - Kernel \\\r (\\\l).\n\n" > $RPM_BUILD_ROOT/etc/issue
echo -e "Welcome to Dummy Product (%{_target_cpu}) - Kernel %%r (%%t)." > $RPM_BUILD_ROOT/etc/issue.net
touch $RPM_BUILD_ROOT/etc/motd

echo 'NAME=Dummy' > $RPM_BUILD_ROOT/etc/os-release
echo 'ID_LIKE="suse"' >> $RPM_BUILD_ROOT/etc/os-release

%files
%defattr(644,root,root,755)
/etc/os-release
%config(noreplace) /etc/motd
%config(noreplace) /etc/issue
%config(noreplace) /etc/issue.net

%changelog
