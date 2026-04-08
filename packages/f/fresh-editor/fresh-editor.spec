#
# spec file for package fresh-editor
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define shortname fresh
Name:           fresh-editor
Version:        0.2.21
Release:        0
Summary:        A terminal text editor you can just use
License:        GPL-2.0-only
URL:            https://getfresh.dev/
Source0:        %{shortname}-v%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Why another text editor? Fresh brings the intuitive, conventional UX of editors like VS Code and Sublime Text to the terminal.
While veterans like Emacs and Vim - and newer editors like Neovim and Helix - are excellent for power users who prefer modal, highly specialized workflows, they often present a steep learning curve for those used to standard GUI interactions. Fresh is built for the developer who wants a familiar, non-modal experience out-of-the-box, without sacrificing the speed and portability of the command line. Keyboard bindings, mouse support, menus, command palette etc. are all designed to be familiar to most modern users.
Architecturally, Fresh is built to handle multi-gigabyte files or slow network streams efficiently, maintaining a negligible memory overhead regardless of file size. While traditional editors struggle with latency and RAM bloat on large files, Fresh delivers consistent, high-speed performance on any scale.
The goal for Fresh is to be an intuitive and accessible, high-performance terminal-based editor that "just works" on any hardware, for everyone.

%prep
%autosetup -p1 -a1 -n %{shortname}-v%{version}

%build
%{cargo_build}

%install
install -D -m 0755 target/release/%{shortname} %{buildroot}%{_bindir}/%{shortname}

%files
%license LICENSE
%doc CHANGELOG.md README.md docs/troubleshooting.md docs/privacy.md
%{_bindir}/fresh

%changelog
