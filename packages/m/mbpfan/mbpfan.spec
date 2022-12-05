#
# spec file for package mbpfan
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


Name:           mbpfan
Version:        2.3.0
Release:        0
Summary:        A simple daemon to control fan speed on all MacBook/MacBook Pros
License:        GPL-3.0-only
URL:            https://github.com/linux-on-mac/mbpfan
Source0:        https://github.com/linux-on-mac/mbpfan/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         harden_mbpfan.service.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
ExclusiveArch:  x86_64

%description
This is an enhanced version of Allan McRae mbpfan

mbpfan is a daemon that uses input from coretemp module and sets the
fan speed using the applesmc module. This enhanced version assumes any
number of processors and fans (max. 10).

* It only uses the temperatures from the processors as input.
* It requires coretemp and applesmc kernel modules to be loaded.
* It requires root use
* It daemonizes or stays in foreground
* Verbose mode for both syslog and stdout
* Users can configure it using the file %{_sysconfdir}/mbpfan.conf

%prep
%setup -q
%patch0 -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1550
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%else
%{set_build_flags}
%endif
%make_build

%install
# Installing the binary
install -Dpm 0755 -t %{buildroot}%{_sbindir}/ bin/%{name}
# Installing the systemd service
install -Dpm 0644 -t %{buildroot}%{_unitdir}/ %{name}.service
# Installing the configuration file
install -Dpm 0644 -t %{buildroot}%{_sysconfdir}/ %{name}.conf
# Installing the manual
install -Dpm 0644 -t %{buildroot}%{_mandir}/man8/ %{name}.8.gz

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man8/mbpfan.8%{?ext_man}

%config(noreplace) %{_sysconfdir}/%{name}.conf

%doc README.md AUTHORS

%license COPYING

%changelog
