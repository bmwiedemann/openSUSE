#
# spec file for package nagios-rpm-macros
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2014-2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nagios-rpm-macros
Summary:        RPM Macros for Nagios based packages
License:        BSD-3-Clause
Group:          System/Monitoring
Version:        0.14
Release:        0
Url:            http://en.opensuse.org/Nagios
Source0:        macros.nagios
Source1:        %{name}-README
Source2:        nagios-rpm-macros-COPYING
Source3:        macros.check_mk
Source4:        macros.pnp4nagios
Source5:        macros.nagiosgrapher
Source6:        macros.icinga
Source7:        macros.icinga2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides rpm macros for building packages for 
Nagios, check_mk and/or Icinga.


%prep
%{__cp} %{S:1} README
%{__cp} %{S:2} COPYING

%build

%install
install -Dm644 %{S:0} %{buildroot}%{_sysconfdir}/rpm/macros.nagios
cat %{S:3} >> %{buildroot}%{_sysconfdir}/rpm/macros.nagios
cat %{S:4} >> %{buildroot}%{_sysconfdir}/rpm/macros.nagios
cat %{S:5} >> %{buildroot}%{_sysconfdir}/rpm/macros.nagios
cat %{S:6} >> %{buildroot}%{_sysconfdir}/rpm/macros.nagios
cat %{S:7} >> %{buildroot}%{_sysconfdir}/rpm/macros.nagios

# make sure that _rundir is working on older systems
%if ! %{defined _rundir}
sed -i 's|%%{_rundir}|%%{_localstatedir}/run|' %{buildroot}%{_sysconfdir}/rpm/macros.nagios
%endif

%clean
rm -rf %buildroot

%files 
%defattr(-,root,root)
%doc COPYING README
%config %{_sysconfdir}/rpm/macros.nagios

%changelog
