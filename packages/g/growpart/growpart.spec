#
# spec file for package growpart
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


%define base_version 0.30
Name:           growpart
Version:        %{base_version}
Release:        0
Summary:        Grow a partition
License:        GPL-3.0-only
Group:          System/Management
Url:            http://launchpad.net/cloud-utils
Source0:        cloud-utils-%{base_version}.tar.gz
Patch:          licenseGPLv3.patch
Requires:       util-linux
Requires:       gptfdisk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Grow a partition. This is predominantly useful in the cloud when an instance
is started with a larger root partition than the image size. The root
partition can be expanded to take up the additional size.

%prep
%autosetup -p1 -n cloud-utils-%{base_version}

%build

%install
install -Dm0755 -t %{buildroot}%{_sbindir} bin/growpart
install -Dm0644 -t %{buildroot}%{_mandir}/man1 man/growpart.1

%files
%defattr(-,root,root,-)
%license LICENSE-GPLv3
%{_sbindir}/growpart
%{_mandir}/man1/*

%changelog
