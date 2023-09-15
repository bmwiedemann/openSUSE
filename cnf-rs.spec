#
# spec file for package cnf-rs
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


Name:           cnf-rs
#               This will be set by osc services, that will run after this.
Version:        0.5.2~0
Release:        0
Summary:        A command-not-found handler for openSUSE
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        MIT
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
URL:            https://github.com/vyskocilm/cnf-rs
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
Group:          System/Console
%endif
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
# TODO: move files into git
Source10:       command_not_found.bash
Source11:       command_not_found.zsh
Source12:       cnf-rs-auto.sh
BuildRequires:  cargo-packaging
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
BuildRequires:  clang15
%else
BuildRequires:  clang16
%endif
BuildRequires:  gettext-tools
BuildRequires:  libsolv-devel
# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
Provides:       bundled(crate(bindgen)) = 0.65.1
Provides:       bundled(crate(bitflags)) = 1.3.2
Provides:       bundled(crate(cexpr)) = 0.6.0
Provides:       bundled(crate(cfg-if)) = 1.0.0
Provides:       bundled(crate(clang-sys)) = 1.6.1
Provides:       bundled(crate(cnf-rs)) = 0.1.0
Provides:       bundled(crate(configparser)) = 3.0.2
Provides:       bundled(crate(either)) = 1.8.1
Provides:       bundled(crate(glob)) = 0.3.1
Provides:       bundled(crate(lazy_static)) = 1.4.0
Provides:       bundled(crate(lazycell)) = 1.3.0
Provides:       bundled(crate(libc)) = 0.2.140
Provides:       bundled(crate(libloading)) = 0.7.4
Provides:       bundled(crate(log)) = 0.4.17
Provides:       bundled(crate(memchr)) = 2.5.0
Provides:       bundled(crate(minimal-lexical)) = 0.2.1
Provides:       bundled(crate(nom)) = 7.1.3
Provides:       bundled(crate(once_cell)) = 1.17.1
Provides:       bundled(crate(peeking_take_while)) = 0.1.2
Provides:       bundled(crate(prettyplease)) = 0.2.4
Provides:       bundled(crate(proc-macro2)) = 1.0.56
Provides:       bundled(crate(quote)) = 1.0.26
Provides:       bundled(crate(regex)) = 1.7.3
Provides:       bundled(crate(regex-syntax)) = 0.6.29
Provides:       bundled(crate(rustc-hash)) = 1.1.0
Provides:       bundled(crate(shlex)) = 1.1.0
Provides:       bundled(crate(syn)) = 2.0.15
Provides:       bundled(crate(unicode-ident)) = 1.0.8
Provides:       bundled(crate(which)) = 4.4.0
Provides:       bundled(crate(winapi)) = 0.3.9
Provides:       bundled(crate(winapi-i686-pc-windows-gnu)) = 0.4.0
Provides:       bundled(crate(winapi-x86_64-pc-windows-gnu)) = 0.4.0
ExclusiveArch:  %{rust_tier1_arches}

%description
A libsolv based command-not-found handler for openSUSE.

%package bash
Summary:        Integration of %{name} with bash
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and bash)
Obsoletes:      scout-command-not-found < 0.2.8
BuildArch:      noarch
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
Group:          System/Console
%endif

%description bash
Bash setup code for command-not-found handler %{name}.

%package zsh
Summary:        Integration of %{name} with zsh
Supplements:    (%{name} and zsh)
Obsoletes:      scout-command-not-found < 0.2.8
BuildArch:      noarch
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
Group:          System/Console
%endif

%description zsh
Zsh setup code for command-not-found handler %{name}.

%package locale
Summary:        Locale support for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
Group:          System/Localization
%endif

%description locale
Locale support for %{name}

%prep
# The number passed to -a (a stands for "after") should be equivalent to the Source tag number
# of the vendor tarball, 1 in this case (from Source1).
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
# using cargo_install (only supports bindir)
%{cargo_install}

# shell integrations
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/bash_command_not_found
install -D -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/zsh_command_not_found

# i18n
ls -1 i18n/po/ | while read LOCALE; do
    msgfmt i18n/po/${LOCALE}/cnf_rs.po -o cnf_rs.mo
    install -D -m 0644 cnf_rs.mo %{buildroot}%{_datadir}/locale/${LOCALE}/LC_MESSAGES/cnf_rs.mo
done
%find_lang cnf_rs

# man page
install -D -m 0644 cnf-rs.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%attr(0755,root,root) %{_bindir}/cnf-rs
%{_mandir}/man1/cnf-rs*

%files bash
%config %{_sysconfdir}/bash_command_not_found

%files zsh
%config %{_sysconfdir}/zsh_command_not_found

%files locale -f cnf_rs.lang

%changelog
