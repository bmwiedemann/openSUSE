#
# spec file for package yast2-testsuite
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


Name:           yast2-testsuite
Version:        4.6.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:          System/YaST
License:        GPL-2.0-or-later
BuildRequires:  yast2-devtools >= 3.1.10
Requires:       dejagnu
Requires:       expect
# y2base -I includepath -M modulepath
Requires:       yast2-core >= 2.19.0

Summary:        YaST2 - Testsuite

BuildArch:      noarch

%description
This is a package for the YaST2 modules testsuite preparation and
execution.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

%files
%defattr(-,root,root)
%{yast_moduledir}
%{yast_ydatadir}
%{yast_yncludedir}
%doc %{yast_docdir}
%license COPYING

%changelog
