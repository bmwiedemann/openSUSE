#
# spec file for package growpart-generator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           growpart-generator
Version:        0.8
Release:        0
Summary:        Grow a partition automatically 
License:        GPL-3.0-only
Group:          System/Management
Url:            https://build.opensuse.org/package/show/devel:kubic/growpart-generator
Source1:        growpart-generator.sh
Source2:        gpl-3.0.txt
Requires:       growpart
Requires:       systemd
BuildArch:      noarch

%description
This systemd generator implements the "x-growpart.grow" mount options in /etc/fstab
allowing to grow the referenced partition to its maximum size.
It behaves like "x-systemd.growfs" and is usually used in combination with that.

%prep
%setup -q -T -c
cp %{SOURCE2} .

%build

%install
install -Dm0755 -t %{buildroot}%{_libexecdir}/systemd/system-generators %{SOURCE1}

%files
%license gpl-3.0.txt
# Dir ownership to avoid the systemd BuildRequires
%dir %{_libexecdir}/systemd/
%dir %{_libexecdir}/systemd/system-generators/
%{_libexecdir}/systemd/system-generators/growpart-generator.sh

%changelog
