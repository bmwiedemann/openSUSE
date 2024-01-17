#
# spec file for package rinstall
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


Name:           rinstall
Version:        0.2.0
Release:        0
Summary:        Declarative install for programs
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        GPL-3.0-or-later
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
URL:            https://github.com/danyspin97/rinstall
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        macros.%{name}
BuildRequires:  cargo-packaging

%description
An helper tool that installs software and additional data into the system.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}
install -m 0644 -D -t %{buildroot}%{_rpmconfigdir}/macros.d %{SOURCE3}

%check
%{cargo_test}

%files
%doc README.md CHANGELOG.md
%{_bindir}/rinstall
%{_rpmconfigdir}/macros.d/macros.%{name}

%changelog
