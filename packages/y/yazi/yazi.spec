#
# spec file for package yazi
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


Name:           yazi
Version:        0.2.3
Release:        0
Summary:        Blazing fast terminal file manager written in Rust, based on async I/O
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/sxyazi/yazi
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         0001-use-system-jit.patch
Requires:       file
BuildRequires:  cargo-packaging
BuildRequires:  lua54-devel

# Override "-C debuginfo=2" from cargo-packaging, to solve rustc SIGSEGV exception:
#   error: rustc interrupted by SIGSEGV, printing backtrace
#   /usr/lib/librustc_driver-16d66626a1fefc07.so(+0x7aafa6)[0x7fbd6ffaafa6]
# Tested with rustc 1.75.0 (82e1608df 2023-12-21) by xtexChooser
%global build_rustflags %build_rustflags -C debuginfo=0

# Suggests:       nerd-fonts
Suggests:       ffmpegthumbnailer
Suggests:       unar
Suggests:       jq
Suggests:       poppler
Suggests:       fd
Suggests:       rg
Suggests:       fzf
Suggests:       zoxide

%description
Yazi (means "duck") is a terminal file manager written in Rust, based on non-blocking async I/O. It aims to provide an efficient, user-friendly, and customizable file management experience.

💡 A new article explaining its internal workings: Why is Yazi Fast?

    🚀 Full Asynchronous Support: All I/O operations are asynchronous, CPU tasks are spread across multiple threads, making the most of available resources.
    💪 Powerful Async Task Scheduling and Management: Provides real-time progress updates, task cancellation, and internal task priority assignment.
    🖼️ Built-in Support for Multiple Image Protocols: Also integrated with Überzug++, covering almost all terminals.
    🌟 Built-in Code Highlighting and Image Decoding: Combined with the pre-loading mechanism, greatly accelerates image and normal file loading.
    🔌 Concurrent Plugin System: UI plugins (rewriting most of the UI), functional plugins (coming soon), custom previewer, and custom preloader; Just some pieces of Lua.
    🧰 Integration with fd, rg, fzf, zoxide
    💫 Vim-like input/select component, auto-completion for cd paths
    🏷️ Multi-Tab Support, Scrollable Preview (for videos, PDFs, archives, directories, code, etc.)
    🔄 Bulk Renaming, Visual Mode, File Chooser
    🎨 Theme System, Custom Layouts, Trash Bin, CSI u
    ... and more!

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%autosetup -a1 -p0

%build
export YAZI_GEN_COMPLETIONS=true
%{cargo_build}

%install
%{cargo_install -p yazi-fm}
install -Dm 644 yazi-config/completions/yazi.bash %{buildroot}%{_datadir}/bash-completion/completions/yazi
install -Dm 644 yazi-config/completions/yazi.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/yazi.fish
install -Dm 644 yazi-config/completions/_yazi %{buildroot}%{_datadir}/zsh/site-functions/_yazi

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
