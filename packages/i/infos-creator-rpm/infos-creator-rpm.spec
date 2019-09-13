#
# spec file for package infos-creator-rpm
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           infos-creator-rpm
Version:        0.3
Release:        0
Summary:        Creates virt-builder index file part from kiwi job
License:        MIT
Group:          System/Management
Url:            https://github.com/cbosdo/%{name}
Source0:        v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       qemu-tools
Requires:       xz
Conflicts:      kiwi_post_run
Provides:       kiwi_post_run

%description
OBS kiwi_post_run hook to create virt-builder site index part out of a kiwi
job.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/build/
install -Dm 755 kiwi_post_run %{buildroot}%{_prefix}/lib/build/

%files
%defattr(-,root,root)
/usr/lib/build/kiwi_post_run

%changelog
