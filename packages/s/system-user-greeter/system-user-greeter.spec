#
# spec file for package system-user-greeter
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


Name:           system-user-greeter
Version:        1
Release:        0
Summary:        System user and group greeter
License:        MIT
Group:          System/Management
BuildRequires:  sysuser-tools
BuildArch:      noarch
%sysusers_requires

%description
The greeter system user and group, used by login managers such as greetd

%prep

%build
echo " #Type Name    ID GECOS Home                          Shell
u     greeter -  -     %{_localstatedir}/lib/greetd  -
m     greeter video" > %{name}.conf

%sysusers_generate_pre %{name}.conf greeter

%install
install -D -m 0644 %{name}.conf %{buildroot}%{_sysusersdir}/%{name}.conf

%pre -f greeter.pre

%files
%{_sysusersdir}/%{name}.conf

%changelog
