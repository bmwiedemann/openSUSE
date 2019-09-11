#
# spec file for package dd_rhelp
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


Name:           dd_rhelp
Version:        0.3.0
Release:        0
Summary:        Bash Helper Script That Handles dd_rescue
License:        GPL-2.0-or-later
Group:          System/Base
Url:            http://www.kalysto.org/utilities/dd_rhelp/index.en.html
Source0:        http://www.kalysto.org/pkg/%{name}-%{version}.tar.gz
Patch1:         dd_rhelp_EOF.diff
Patch2:         dd_rhelp_Summary.diff
Patch3:         dd_rhelp.test.diff
Patch4:         dd_r_version.diff
BuildRequires:  bc
BuildRequires:  dd_rescue
# dd_rhelp (version 0.1.2) was splitted from dd_rescue after openSUSE 12.1 (at dd_rescue version 1.25)
Requires:       dd_rescue > 1.24_0.1.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
dd_rhelp is a bash helper script that handles dd_rescue. dd_rescue roughly acts
as the dd linux command with the caracteristic to NOT stop when it falls on
read/write.

dd_rhelp intelligently controls dd_rescue to first copy all blocks from areas
that work and only then tries to approach the bad spots from both sides.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -Dpm 0755 dd_rhelp %{buildroot}%{_bindir}

#UsrMerge
mkdir %{buildroot}/bin
ln -sf %{_bindir}/dd_rhelp %{buildroot}/bin
#EndUsrMerge

%check
./dd_rhelp.test

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog FAQ NEWS README THANKS TODO doc/example.txt
%{_bindir}/dd_rhelp
#UsrMerge
/bin/dd_rhelp
#EndUsrMerge

%changelog
