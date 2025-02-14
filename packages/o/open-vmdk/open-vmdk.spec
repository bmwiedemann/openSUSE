#
# spec file for package open-vmdk
#
# Copyright (c) 2025 SUSE LLC
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


Name:           open-vmdk
Version:        0.3.10
Release:        0
Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/vmware/open-vmdk
Source0:        https://github.com/vmware/open-vmdk/archive/refs/tags/v%{version}.tar.gz
Patch0:         shebang.patch
BuildRequires:  zlib-devel
Requires:       coreutils
Requires:       grep
Requires:       python3-PyYAML
Requires:       python3-lxml
Requires:       sed
Requires:       tar
Requires:       util-linux

%description
Tools to create OVA files from raw disk images. This includes 'vmdk-convert'
to create VMDKs from raw disk images, and 'ova-compose' to create OVA files
that can be imported by VMware vSphere or Fusion and Workstation.

%prep

%setup -q
%autopatch -p1

%build
%make_build

%install
install -d %{buildroot}%{_sysconfdir}
%make_install
install templates/*.ovf %{buildroot}%{_datadir}/%{name}

%files

%dir %{_datadir}/%{name}
%{_datadir}/%{name}
%{_bindir}/*
%config %{_sysconfdir}/*

%changelog
