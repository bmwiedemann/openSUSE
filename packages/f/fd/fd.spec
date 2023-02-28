#
# spec file for package fd
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


Name:           fd
Version:        8.7.0
Release:        0
Summary:        An alternative to the "find" utility
License:        Apache-2.0 AND MIT
Group:          Productivity/File utilities
URL:            https://github.com/sharkdp/fd
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
Provides:       bundled(crate(aho-corasick)) = 0.7.18
Provides:       bundled(crate(ansi_term)) = 0.12.1
Provides:       bundled(crate(anyhow)) = 1.0.52
Provides:       bundled(crate(atty)) = 0.2.14
Provides:       bundled(crate(autocfg)) = 1.0.1
Provides:       bundled(crate(bitflags)) = 1.3.2
Provides:       bundled(crate(bstr)) = 0.2.17
Provides:       bundled(crate(cc)) = 1.0.72
Provides:       bundled(crate(cfg-if)) = 1.0.0
Provides:       bundled(crate(chrono)) = 0.4.19
Provides:       bundled(crate(clap)) = 2.34.0
Provides:       bundled(crate(crossbeam-utils)) = 0.8.5
Provides:       bundled(crate(ctrlc)) = 3.2.1
Provides:       bundled(crate(diff)) = 0.1.12
Provides:       bundled(crate(dirs-next)) = 2.0.0
Provides:       bundled(crate(dirs-sys-next)) = 0.1.2
Provides:       bundled(crate(fd-find)) = 8.3.1
Provides:       bundled(crate(filetime)) = 0.2.15
Provides:       bundled(crate(fnv)) = 1.0.7
Provides:       bundled(crate(fs_extra)) = 1.2.0
Provides:       bundled(crate(fuchsia-cprng)) = 0.1.1
Provides:       bundled(crate(getrandom)) = 0.2.3
Provides:       bundled(crate(globset)) = 0.4.8
Provides:       bundled(crate(hermit-abi)) = 0.1.19
Provides:       bundled(crate(humantime)) = 2.1.0
Provides:       bundled(crate(ignore)) = 0.4.18
Provides:       bundled(crate(jemalloc-sys)) = 0.3.2
Provides:       bundled(crate(jemallocator)) = 0.3.2
Provides:       bundled(crate(lazy_static)) = 1.4.0
Provides:       bundled(crate(libc)) = 0.2.112
Provides:       bundled(crate(log)) = 0.4.14
Provides:       bundled(crate(lscolors)) = 0.8.1
Provides:       bundled(crate(memchr)) = 2.4.1
Provides:       bundled(crate(memoffset)) = 0.6.4
Provides:       bundled(crate(nix)) = 0.23.1
Provides:       bundled(crate(normpath)) = 0.3.1
Provides:       bundled(crate(num-integer)) = 0.1.44
Provides:       bundled(crate(num-traits)) = 0.2.14
Provides:       bundled(crate(num_cpus)) = 1.13.1
Provides:       bundled(crate(once_cell)) = 1.9.0
Provides:       bundled(crate(proc-macro2)) = 1.0.32
Provides:       bundled(crate(quote)) = 1.0.10
Provides:       bundled(crate(rand)) = 0.4.6
Provides:       bundled(crate(rand_core)) = 0.3.1
Provides:       bundled(crate(rand_core)) = 0.4.2
Provides:       bundled(crate(rdrand)) = 0.4.0
Provides:       bundled(crate(redox_syscall)) = 0.2.10
Provides:       bundled(crate(redox_users)) = 0.4.0
Provides:       bundled(crate(regex)) = 1.5.4
Provides:       bundled(crate(regex-syntax)) = 0.6.25
Provides:       bundled(crate(remove_dir_all)) = 0.5.3
Provides:       bundled(crate(same-file)) = 1.0.6
Provides:       bundled(crate(strsim)) = 0.8.0
Provides:       bundled(crate(syn)) = 1.0.82
Provides:       bundled(crate(tempdir)) = 0.3.7
Provides:       bundled(crate(term_size)) = 0.3.2
Provides:       bundled(crate(test-case)) = 1.2.1
Provides:       bundled(crate(textwrap)) = 0.11.0
Provides:       bundled(crate(thread_local)) = 1.1.3
Provides:       bundled(crate(time)) = 0.1.43
Provides:       bundled(crate(unicode-width)) = 0.1.9
Provides:       bundled(crate(unicode-xid)) = 0.2.2
Provides:       bundled(crate(users)) = 0.11.0
Provides:       bundled(crate(vec_map)) = 0.8.2
Provides:       bundled(crate(version_check)) = 0.9.4
Provides:       bundled(crate(walkdir)) = 2.3.2
Provides:       bundled(crate(wasi)) = 0.10.2+wasi-snapshot_preview1
Provides:       bundled(crate(winapi)) = 0.3.9
Provides:       bundled(crate(winapi-i686-pc-windows-gnu)) = 0.4.0
Provides:       bundled(crate(winapi-util)) = 0.1.5
Provides:       bundled(crate(winapi-x86_64-pc-windows-gnu)) = 0.4.0

%description
fd is an alternative to GNU find. It features:

* Colorized terminal output (similar to ls).
* The search is case-insensitive by default. It switches to
  case-sensitive if the pattern contains an uppercase character.
* By default, ignores patterns from .gitignore, and ignores hidden
  directories and files.
* Supports regular expressions and Unicode awareness.
* A parallel execution similar to GNU Parallel is available.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for fd, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for fd, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for fd, generated during the build.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}
make completions

%install
%{cargo_install}

# install shell completions and man page
install -Dm644 autocomplete/fd.bash %{buildroot}%{_datadir}/bash-completion/completions/fd
install -Dm644 autocomplete/fd.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/fd.fish
install -Dm644 autocomplete/_fd %{buildroot}%{_datadir}/zsh/site-functions/_fd
install -Dm644 doc/fd.1 %{buildroot}%{_mandir}/man1/fd.1

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/fd
%{_mandir}/man1/fd.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
