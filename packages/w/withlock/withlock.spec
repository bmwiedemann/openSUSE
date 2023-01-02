#
# spec file for package withlock
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


Name:           withlock
Version:        0.5
Release:        0
Summary:        A locking wrapper script
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/poeml/withlock
Source0:        %{name}-%{version}.tar.gz
Patch0:         fix-use-python3.patch
Patch1:         withlock-0.5-fixboo864785.patch
Requires:       python3
BuildArch:      noarch

%description
withlock is a locking wrapper script to make sure that some program isn't run
more than once. It is ideal to prevent periodic jobs spawned by cron from
stacking up.

The locks created are valid only while the wrapper is running, and thus will
never require a cleanup, as after a reboot. Thus, the wrapper is safe and easy
to use, and much better than implementing half-hearted locking within scripts.

%prep
%autosetup -p1

%build
# nop

%install
install -D -m 0755 -t %{buildroot}%{_bindir}/ %{name}
install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ %{name}.1

%files
%license LICENSE-2.0.txt
%doc README.md withlock.1.html
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
