#
# spec file for package withlock
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           withlock
Version:        0.4
Release:        0
Summary:        A locking wrapper script
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/poeml/withlock
Requires:       python
Source0:        http://mirrorbrain.org/files/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
withlock is a locking wrapper script to make sure that some program isn't run
more than once. It is ideal to prevent periodic jobs spawned by cron from
stacking up.

The locks created are valid only while the wrapper is running, and thus will
never require a cleanup, as after a reboot. Thus, the wrapper is safe and easy
to use, and much better than implementing half-hearted locking within scripts.

%prep
%setup

%build
#
%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install 

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{_defaultdocdir}/%{name}
%{_bindir}/%{name}
%doc %{_mandir}/man1/*

%changelog
