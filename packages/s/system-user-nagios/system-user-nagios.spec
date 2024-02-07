#
# spec file for package system-user-nagios
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

%if 0%{?suse_version} >= 01550
  %bcond_without sysuser
%else
  %bcond_with sysuser
%endif


Name:           system-user-nagios
Version:        1.0.0
Release:        0
Summary:        System user and group nagios
BuildRequires:  nagios-rpm-macros
License:        MIT
URL:            https://en.opensuse.org/openSUSE:Packaging_guidelines#Users_and_Groups
Source1:        README.SUSE
%if %{with sysuser}
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  /bin/logger
Requires(pre):  coreutils
Requires(pre):  grep
Requires(pre):  shadow
%define         nnmmsg logger -t %{name}/rpm
%endif
BuildArch:      noarch

%description
This package provides the user and group 'nagios' for various applications.

%prep
install -m0644 %{SOURCE1} README.SUSE
cat > system-user-nagios.conf << EOF
#Type Name      ID      GECOS                      Home directory     Shell
u     %{nagios_user}    -       "User for Nagios"          %{nagios_localstatedir}    /bin/false
g     %{nagios_command_group}    -
m     %{nagios_user}    %{nagios_command_group}
EOF

%build
%if %{with sysuser}
%sysusers_generate_pre system-user-nagios.conf nagios system-user-nagios.conf
%endif

%install
%if %{with sysuser}
install -D -m 0644 system-user-nagios.conf %{buildroot}%{_sysusersdir}/system-user-nagios.conf
%endif

%if %{with sysuser}
%pre -f nagios.pre
%else
%pre 
if ! getent group %{nagios_group} 2>/dev/null ; then
	groupadd -r    %{nagios_group} 2>/dev/null || 
	%{nnmmsg} "Added group %{nagios_group}"
fi
if ! getent group %{nagios_command_group} 2>/dev/null ; then
	groupadd -r %{nagios_command_group} 2>/dev/null || 
	%{nnmmsg} "Added group %{nagios_command_group}"
fi
if ! getent passwd %{nagios_user} 2>/dev/null ; then
	useradd  -r -g %{nagios_group} -d %{nagios_localstatedir} -s /bin/false -c "User for Nagios" %{nagios_user} 2>/dev/null || 
	%{nnmmsg} "Added user %{nagios_user} with default group %{nagios_group}"
fi
if ! getent group %{nagios_command_group} | grep -q %{nagios_user} ; then 
	usermod -a -G %{nagios_command_group} %{nagios_user} || 
	%{nnmmsg} "Added user %{nagios_user} to %{nagios_command_group}"
fi
%endif

%files
%defattr(-,root,root)
%doc README.SUSE
%if %{with sysuser}
%{_sysusersdir}/system-user-nagios.conf
%endif

%changelog
