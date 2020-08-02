#
# spec file for package build-compare
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


Name:           build-compare
Summary:        Build Result Compare Script
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://github.com/openSUSE/build-compare
Version:        20200727T175347.d95eb35
Release:        0
Source1:        COPYING
Source2:        same-build-result.sh
Source3:        pkg-diff.sh
Source4:        functions.sh
Source5:        srpm-check.sh
%if 0%{?suse_version}
Requires:       bash
Requires:       cpio
Requires:       coreutils
Requires:       diffutils
Requires:       file
Requires:       gawk
Requires:       grep
Requires:       rpm
Requires:       sed
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#!BuildIgnore:  build-compare

%description
This package contains scripts to find out if the build result differs
to a former build.


%prep
%setup -q -c -T

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/build/ $RPM_BUILD_ROOT/%_defaultdocdir/%name
install -m 0755 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 $RPM_BUILD_ROOT/usr/lib/build/
install -m 0644 %SOURCE1 $RPM_BUILD_ROOT/%_defaultdocdir/%name/

%files
%defattr(-,root,root)
%doc %_defaultdocdir/%name
/usr/lib/build

%changelog
