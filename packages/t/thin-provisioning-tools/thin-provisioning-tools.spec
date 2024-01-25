#
# spec file for package thin-provisioning-tools
#
# Copyright (c) 2024 SUSE LLC
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


Name:           thin-provisioning-tools
Version:        1.0.10
Release:        0
Summary:        Thin Provisioning Tools
License:        GPL-3.0-only
URL:            https://github.com/jthornber/thin-provisioning-tools/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  suse-module-tools
Requires(post): coreutils
Requires(postun): coreutils
Conflicts:      device-mapper < 1.02.115

%description
A suite of tools for thin provisioning on Linux.

%prep
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%doc README.md
%license COPYING
%{_bindir}/pdata_tools

%changelog
