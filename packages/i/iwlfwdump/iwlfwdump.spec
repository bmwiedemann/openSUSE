#
# spec file for package iwlfwdump
#
# Copyright (c) 2023 SUSE LLC
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

%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%endif

Name:           iwlfwdump
Version:        1
Release:        0
Summary:	Firmware dump utility
License:        GPL-2.0-only
URL:            https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi/debugging
Source0:        50-iwlfwdump.rules
Source1:        iwlfwdump
Source2:        logrotate
Recommends:     logrotate
Buildarch:      noarch

%description
An utility to automatically dump firmware dumps to /var/log/.

%prep

%build

%install
install -d %{buildroot}%{_sbindir}/ %{buildroot}%_udevrulesdir/ %{buildroot}%{_distconfdir}/logrotate.d/
install -m 644 %SOURCE0 %{buildroot}/%{_udevrulesdir}/
install -m 755 %SOURCE1 %{buildroot}/%{_sbindir}/
install -m 644 %SOURCE2 %{buildroot}/%{_distconfdir}/logrotate.d/%{name}

%files
%_udevrulesdir/50-iwlfwdump.rules
%{_sbindir}/iwlfwdump
%{_distconfdir}/logrotate.d/%{name}

%changelog
