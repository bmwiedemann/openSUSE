#
# spec file for package keylightctl
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

%define goipath github.com/endocrimes/keylightctl
%define git_commit 77d5a0ef6a93949d92a8442fa1fb60e40b356c17

Name:           keylightctl
Version:        0.0.3
Release:        0
Summary:        CLI for managing Elgato Keylight (Air) 
License:        GPL-3.0-or-later
URL:            https://github.com/endocrimes/keylightctl
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14
%{go_provides}

%description
A command line tool for controlling Elgato Key Lights and Key Light Airs.

%prep
%setup -qa1

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -mod vendor -buildmode pie -ldflags "%{goipath}/internal/version.gitCommit=%{git_commit}}" 

%install
%goinstall

%post
%postun

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog

