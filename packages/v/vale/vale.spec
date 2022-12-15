#
# spec file for package vale
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
# nodebuginfo


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           vale
Version:        2.21.3
Release:        0
Summary:        CLI tool to lint prose text with syntax awareneness and extensible markup format support
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/errata-ai/vale
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.18

%description
Vale is a command-line tool that brings code-like linting to prose. It's fast,
cross-platform (Windows, macOS, and Linux), and highly customizable.

Vale has support for markup: Vale has a rich understanding of many markup
formats, allowing it to avoid syntax-related false positives and intelligently
exclude code snippets from prose-related rules.

Vale includes a highly customizable extension system capable of enforcing your
style-be it a standard editorial style guide or a custom in-house set of rules
(such as those created by GitLab, Homebrew, Linode, CockroachDB, and Spotify).

https://vale.sh/

%prep
%autosetup -a 1

%build
# Build the binary.
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie \
   ./cmd/vale

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"
# Install empty styles directory for use by other packages
install --directory %{buildroot}%{_datarootdir}/%{name}/styles

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
# Package empty styles directory for use by other packages
%dir %{_datarootdir}/%{name}
%dir %{_datarootdir}/%{name}/styles

%changelog
