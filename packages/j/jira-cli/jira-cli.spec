#
# spec file for package jira-cli
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
# nodebuginfo


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
%define shortname jira
Name:           jira-cli
Version:        1.5.1
Release:        0
Summary:        CLI tool for Atlassian JIRA inspired by the Github CLI tool
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/ankitpokhrel/jira-cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.19

%description
JiraCLI is an interactive command line tool for Atlassian Jira that will help
you avoid Jira UI to some extent. This tool is not yet considered complete but
has all the essential features required to improve your workflow with Jira. The
tool started with the idea of making issue search and navigation as
straightforward as possible. The tool now includes all necessary features like
issue creation, cloning, linking, ticket transition, and much more. The TUI is
heavily inspired by the GitHub CLI.

%prep
%autosetup -a 1

%build
# Build the binary.
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie \
   ./cmd/%{shortname}

%install
# Install the binary.
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{shortname}

%changelog
