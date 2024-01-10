#
# spec file for package growpart
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


Name:           growpart
Version:        0.33
Release:        0
Summary:        Grow a partition
License:        GPL-3.0-only
Group:          System/Management
URL:            https://github.com/canonical/cloud-utils
Source0:        https://github.com/canonical/cloud-utils/archive/refs/tags/%{version}.tar.gz#/cloud-utils-%{version}.tar.gz
Requires:       gptfdisk
Requires:       util-linux
BuildArch:      noarch

%description
Grow a partition. This is predominantly useful in the cloud when an instance is
started with a larger root partition than the image size. The root partition
can be expanded to take up the additional size.

%prep
%autosetup -p1 -n cloud-utils-%{version}

%build

%install
install -Dm0755 -t %{buildroot}%{_sbindir} bin/growpart
install -Dm0644 -t %{buildroot}%{_mandir}/man1 man/growpart.1
install -Dm0644 -t %{buildroot}/%{_defaultlicensedir}/growpart LICENSE

%files
%license LICENSE
%{_sbindir}/growpart
%{_mandir}/man1/*

%changelog
