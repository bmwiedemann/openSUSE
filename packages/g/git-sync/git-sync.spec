#
# spec file for package git-sync
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


Name:           git-sync
Version:        0.0.0~git20151024.eb9adaf
Release:        0
Summary:        One-script git synchronization
License:        CC0-1.0
Group:          Development/Tools/Version Control

Url:            https://github.com/simonthum/git-sync
Source0:        %{name}-%{version}.tar.xz
Patch0:         no-env.patch
BuildArch:      noarch
BuildRequires:  git-core
Requires:       git-core

%description
This script synchronizes, almost automatically, "tracking" repositories
where a nice history is not as crucial as having one at all.

%prep
%autosetup -p1

%build

%install
install -vdm 0755 %{buildroot}%{_bindir}
cp %{name} %{buildroot}%{_bindir}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
