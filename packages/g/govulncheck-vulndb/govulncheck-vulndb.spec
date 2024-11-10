#
# spec file for package govulncheck-vulndb
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


%define shortname vulndb

Name:           govulncheck-vulndb
Version:        0.0.20241108T172500
Release:        0
Summary:        Local copy of Go vulnerability database
License:        CC-BY-4.0
Group:          Development/Languages/Go
URL:            https://pkg.go.dev/vuln/
Source:         %{shortname}.zip
Suggests:       govulncheck
BuildArch:      noarch
BuildRequires:  unzip
# SLE-12 has s390 but the Go compiler is not supported on that arch
ExcludeArch:    s390

%description
govulncheck-vulndb provides a local copy of the Go vulnerability database
https://vuln.go.dev as files in the Open Source Vulnerability (OSV) schema.
This allows tools such as govulncheck to be used in offline environments.

Usage:

govulncheck -db file:///usr/share/vulndb

%prep
unzip %{SOURCE0} -d %{shortname}

%build

%install
install -d %{buildroot}%{_datadir}/%{shortname}
find . -name "*.json" -exec install -Dm644 \{\} %{buildroot}%{_datadir}/\{\} \;

%check

%files
%{_datadir}/%{shortname}

%changelog
