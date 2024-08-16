#
# spec file for package wlprop
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Georg Pfuetzenreuter <mail+rpm@georg-pfuetzenreuter.net>
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


Name:           wlprop
Version:        0~git0.758c548
Release:        0
Summary:        Script to query Wayland window properties
License:        MIT
URL:            https://gist.github.com/crispyricepc/f313386043395ff06570e02af2d9a8e0
Source:         https://gist.githubusercontent.com/crispyricepc/f313386043395ff06570e02af2d9a8e0/raw/758c548bfb4be5b437c428c8062b3987f126f002/wlprop.sh
Requires:       awk
Requires:       jq
Requires:       slurp
Requires:       sway

%description
Shell script allowing to query window properties on Sway.
Wayland equivalent for "xprop".

%prep
sed '1s/env //' %{SOURCE0} > %{name}

%build

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
set -u
%if 0%{?suse_version} < 1600
result='a %{_bindir}/sh script, UTF-8 Unicode text executable'
%else
result='a %{_bindir}/sh script, Unicode text, UTF-8 text executable'
%endif
test "$(file -b %{buildroot}%{_bindir}/%{name})" = "$result"

%files
%{_bindir}/%{name}

%changelog
