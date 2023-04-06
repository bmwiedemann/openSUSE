#
# spec file for package ngspice-doc
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


Name:           ngspice-doc
Version:        40
Release:        0
Summary:        Documentation for the ngspice Mixed-signal simulator
Group:          Documentation/Other
License:        CC-BY-SA-4.0 AND BSD-3-Clause
URL:            https://ngspice.sourceforge.io
Source0:        https://ngspice.sourceforge.io/docs/ngspice-%{version}-manual.pdf
Recommends:     ngspice = %{version}
BuildArch:      noarch

%description -n ngspice-doc
Ngspice is a mixed-level/mixed-signal circuit simulator.

This package contains the user manual in PDF format.

%prep
cp %{S:0} .

%build
# Nothing do do here

%install
# Nothing do do here

%files -n ngspice-doc
%doc ngspice-%{version}-manual.pdf

%changelog
