#
# spec file for package galileo-mura
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

Name:           galileo-mura
Version:        0.9
Release:        0%{?dist}
Summary:        Utilities for setting and reading mura correction on Galileo
License:        MIT
URL:            https://gitlab.com/evlaV/galileo-mura-extractor

Source:         https://gitlab.com/evlaV/galileo-mura-extractor/-/archive/v%version/galileo-mura-extractor-v%version.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja

%description
This package provides utilities for setting
and reading mura correction on Galileo.

%prep
%autosetup -n %{name}-extractor-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/galileo-mura-extractor
%{_bindir}/galileo-mura-setup
%{_bindir}/galileo-mura-download

%changelog
