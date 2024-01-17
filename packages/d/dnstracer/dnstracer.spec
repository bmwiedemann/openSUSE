#
# spec file for package dnstracer
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


Name:           dnstracer
Version:        1.10
Release:        0
Summary:        Trace a DNS record to its start of authority
License:        BSD-2-Clause
Group:          Productivity/Networking/DNS/Utilities
URL:            https://www.mavetju.org/unix/dnstracer.php
Source:         https://www.mavetju.org/download/dnstracer-%{version}.tar.bz2

%description
Dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
%setup -q -n %{name}

%build
%make_build

%install
install -m 755 -d "%{buildroot}/%{_bindir}" 
install -m 755 -d "%{buildroot}/%{_mandir}/man8" 
%make_install PREFIX="%{buildroot}/%{_prefix}" MANPREFIX="%{buildroot}/%{_mandir}/man8"

%files
%license LICENSE
%doc CHANGES CONTACT README
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
