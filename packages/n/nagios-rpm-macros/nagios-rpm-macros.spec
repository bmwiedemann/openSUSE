#
# spec file for package nagios-rpm-macros
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


Name:           nagios-rpm-macros
Version:        0.14
Release:        0
Summary:        RPM Macros for Nagios based packages
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            http://en.opensuse.org/Nagios
Source0:        macros.nagios
Source1:        %{name}-README
Source2:        nagios-rpm-macros-COPYING
Source3:        macros.check_mk
Source4:        macros.pnp4nagios
Source5:        macros.nagiosgrapher
Source6:        macros.icinga
Source7:        macros.icinga2
BuildArch:      noarch

# _rpmmacrodir doesn't exist on SLES 12 or RHEL 7
%if %{undefined _rpmmacrodir}
%define _rpmmacrodir %{_rpmconfigdir}/macros.d
%endif

%description
This package provides rpm macros for building packages for
Nagios, check_mk and/or Icinga.

%prep
cp %{SOURCE1} README
cp %{SOURCE2} COPYING

%build

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.nagios
cat %{SOURCE3} >> %{buildroot}%{_rpmmacrodir}/macros.nagios
cat %{SOURCE4} >> %{buildroot}%{_rpmmacrodir}/macros.nagios
cat %{SOURCE5} >> %{buildroot}%{_rpmmacrodir}/macros.nagios
cat %{SOURCE6} >> %{buildroot}%{_rpmmacrodir}/macros.nagios
cat %{SOURCE7} >> %{buildroot}%{_rpmmacrodir}/macros.nagios

# make sure that _rundir is working on older systems
%if ! %{defined _rundir}
sed -i 's|%%{_rundir}|%%{_localstatedir}/run|' %{buildroot}%{_rpmmacrodir}/macros.nagios
%endif

%files
%license COPYING
%doc README
%{_rpmmacrodir}/macros.nagios

%changelog
