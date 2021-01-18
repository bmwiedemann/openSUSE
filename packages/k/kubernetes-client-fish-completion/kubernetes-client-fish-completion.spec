#
# spec file for package kubernetes-client-fish-completion
#
# Copyright (c) 2021 SUSE LLC
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


Name:           kubernetes-client-fish-completion
Version:        0.1604972537+git.da5fa3c
Release:        0
Summary:		Kubectl completion for fish shell
License:        MIT
URL:           	https://github.com/evanlucas/fish-kubectl-completions
Source:        	%{name}-%{version}.tar.xz
BuildRequires: 	fish
Supplements:   	packageand(kubernetes-client:fish)
BuildArch:      noarch

%description
Kubectl completion for fish shell

%prep
%setup -q

%build

%install
install -D -m 644 completions/kubectl.fish "%{buildroot}/%{_datadir}/fish/vendor_completions.d/kubectl.fish"

%files
%defattr(-,root,root)
%{_datadir}/fish/vendor_completions.d/kubectl.fish
%license LICENSE
%doc README.md

%changelog
