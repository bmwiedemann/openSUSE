#
# spec file for package netsed
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           netsed
Version:        1.4
Release:        0
Summary:        Network packet stream editor
License:        GPL-2.0-or-later
URL:            http://silicone.homelinux.org/projects/netsed/
Source:         http://silicone.homelinux.org/release/netsed/%{name}-%{version}.tar.gz

%description
NetSED is a utility designed to alter the contents of packets forwarded through
the network in real time.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install \
	DESTDIR=%{buildroot} \
	PREFIX=%{_prefix} \
	%{nil}

%files
%license LICENSE
%doc NEWS README TODO
%{_bindir}/%{name}

%changelog
