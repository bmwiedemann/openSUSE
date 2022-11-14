#
# spec file for package tkdiff
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tkdiff
Version:        5.6
%define _version 5-6
Release:        0
Summary:        2 and 3-way diff/merge tool
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://tkdiff.sourceforge.io/
Source0:        https://sourceforge.net/projects/tkdiff/files/tkdiff/%{version}/tkdiff-%{_version}.zip
Source1:        README.SUSE
BuildRequires:  unzip
Requires:       diffutils
Requires:       tcl
Requires:       tk
BuildArch:      noarch

%description
TkDiff is a graphical 2 and 3-way diff/merge tool.

%prep
%setup -q -n tkdiff-%{_version}
cp %{SOURCE1} .

%build

%install
install -Dpm 0755 tkdiff \
  %{buildroot}%{_bindir}/tkdiff

%files
%doc README.SUSE
%{_bindir}/tkdiff

%changelog
