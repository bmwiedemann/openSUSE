#
# spec file for package tdfiglet
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


Name:           tdfiglet
Version:        0.5+3
Release:        0
Summary:        Shell Art
Group:		Amusements/Games/Other
License:        BSD-3-Clause
URL:            https://github.com/tat3r/tdfiglet
Source0:        %{name}-%{version}.tar.gz
Patch0:         Makefile-0.1.patch

%description
Because figlet ASCII is not as cool.

%if ! 0%{?suse_version}
%global debug_package %{nil}
%endif

%prep
%setup -q

%patch0 -p1

%build
make %{?_smp_mflags} -f Makefile

%install
%make_install

%files
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
