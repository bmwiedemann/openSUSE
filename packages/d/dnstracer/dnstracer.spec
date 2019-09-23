#
# spec file for package dnstracer
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dnstracer
Version:        1.9
Release:        0
Summary:        Trace a DNS record to its start of authority
License:        BSD-2-Clause
Group:          Productivity/Networking/DNS/Utilities
Url:            http://www.mavetju.org/unix/dnstracer.php
Source:         http://www.mavetju.org/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc CHANGES CONTACT LICENSE README
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{ext_man}

%changelog
