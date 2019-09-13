#
# spec file for package calamaris
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           calamaris
Version:        2.59
Release:        0
Summary:        A Report Generator
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            http://calamaris.cord.de
Source:         http://cord.de/%{name}-%{version}.tar.gz
Patch0001:      0001_perl.patch
BuildArch:      noarch

%description
Calamaris parses log files from Squid V1.1.x, V1.2.x, V2.x, and NetCache in
native log format and generates a report.

%prep
%setup -q
%patch0001

%build

%install
install -Dpm 0755 calamaris \
  %{buildroot}%{_bindir}/calamaris
install -Dpm 0644 calamaris.1 \
  %{buildroot}/%{_mandir}/man1/calamaris.1

%files
%license COPYRIGHT
%doc CHANGES EXAMPLES README
%{_bindir}/calamaris
%{_mandir}/man1/calamaris.1%{?ext_man}

%changelog
