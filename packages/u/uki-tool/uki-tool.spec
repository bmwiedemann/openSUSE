#
# spec file for package uki-tool
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


%define archive_name unified-kernel-image-tool
%define bin_name uki-tool

Name:           uki-tool
Version:        1.4.1+0.g2720d37
Release:        0
Summary:        Tool for the UKI and static-initrd project
License:        MIT
URL:            https://github.com/keentux/unified-kernel-image-tool.git
Source:         %{archive_name}-%{version}.tar.xz
#PATCH-FIXED-UPSTREAM
Patch:          create-pcrkeys-arg.patch
BuildArch:      noarch
BuildRequires:  ShellCheck
BuildRequires:  bash-sh
BuildRequires:  coreutils
Requires:       awk
Requires:       bash-sh
Requires:       bind-utils
Requires:       binutils
Requires:       coreutils
Requires:       e2fsprogs
Requires:       rpm
Requires:       squashfs
# Require to have lsinitrd
Requires:       dracut

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tool that regroups useful command dealing with the Unified Kernel Image (UKI)
and static-initrd project. Write in Shell script, and adapted for the packaging.

%package doc
Summary:        Documentation for the package uki-tool
Group:          Documentation/Man
BuildRequires:  gzip
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
This package contains the documentation for the uki-tool.

%prep
%autosetup -p1 -n %{archive_name}-%{version}

%build
sh ./build.sh

%install
sh ./install.sh \
    --prefix "%{buildroot}"\
    --bindir="%{_bindir}"\
    --mandir="%{_mandir}"

%files
%defattr(-,root,root)
%{_bindir}/%{bin_name}

%files doc
%doc README.md LICENSE AUTHORS CHANGELOG.md
%{_mandir}/man1/%{bin_name}.1%{?ext_man}

%changelog
