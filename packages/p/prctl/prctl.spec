#
# spec file for package prctl
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


Name:           prctl
Version:        1.7
Release:        0
Summary:        A utility to perform process operations
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/hikerockies/prctl/
Source0:        https://github.com/hikerockies/prctl/archive/refs/tags/v%{version}.tar.gz#/prctl-%{version}.tar.gz
Source1:        COPYING
BuildRequires:  automake
Patch0:         prctl-destdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The prctl utility allows a user to control certain process behaviors in
the runtime environment.

%prep
%autosetup -p1
cp %{SOURCE1} .

%build
autoreconf -fiv
%configure
make

%install
export man1dir="%{_mandir}/man1"
%make_install

%files
%defattr(-, root, root)
%doc ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
