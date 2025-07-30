#
# spec file for package amfora
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


%global revision  2534983

Name:           amfora
Version:        1.11.0
Release:        0
Summary:        CLI/Terminal based gemini browser
License:        GPL-3.0-only
URL:            https://github.com/makeworld-the-better-one/amfora
Source:         amfora-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.18

%description
A fancy terminal browser for the Gemini protocol.

%prep
%autosetup -D -a 1

%build
%make_build GOFLAGS="-buildmode=pie" \
  VERSION="%{version}" COMMIT="%{revision}" BUILDER="openSUSE"

%check
# check if binary is working
./amfora --version

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README.md default-config.toml
%{_bindir}/amfora
%{_datadir}/applications/amfora.desktop

%changelog
