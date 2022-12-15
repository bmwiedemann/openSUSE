#
# spec file for package build-compare
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


Name:           build-compare
Version:        20221206T204012.bb70754
Release:        0
Summary:        Build Result Compare Script
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/build-compare
Source1:        COPYING
Source2:        same-build-result.sh
Source3:        pkg-diff.sh
Source4:        functions.sh
Source5:        srpm-check.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#!BuildIgnore:  build-compare
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       bash
Requires:       coreutils
Requires:       cpio
Requires:       diffutils
Requires:       file
Requires:       gawk
Requires:       grep
Requires:       rpm
Requires:       sed
%endif

%description
This package contains scripts to find out if the build result differs
to a former build.

%prep
%setup -q -c -T
install -p -m 0644 %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/build/
install -m 0755 %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_prefix}/lib/build/

%files
%if 0%{?suse_version} < 1500
%defattr(-,root,root)
%doc COPYING
%else
%license COPYING
%endif
%{_prefix}/lib/build

%changelog
