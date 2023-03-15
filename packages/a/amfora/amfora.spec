#
# spec file for package amfora
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


Name:           amfora
Version:        1.9.2
Release:        0
Summary:        CLI/Terminal based gemini browser
License:        GPL-3.0-only
URL:            https://github.com/makeworld-the-better-one/amfora
Source:         amfora-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.17
BuildRequires:  golang-packaging

%description
A fancy terminal browser for the Gemini protocol.

%prep
%autosetup -D -a 1

%build
GOFLAGS="-buildmode=pie" GIT_TAG="v%{version}" make amfora

%check
# check if binary is working
./amfora --version

%install
install -Dm 755 amfora %{buildroot}/%{_bindir}/amfora

%files
%license LICENSE
%doc README.md
%{_bindir}/amfora

%changelog
