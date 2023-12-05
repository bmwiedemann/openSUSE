#
# spec file for package cnf
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


Name:           cnf
#               This will be set by osc services, that will run after this.
Version:        0.6.0~0
Release:        0
Summary:        A command-not-found handler for openSUSE
License:        MIT
URL:            https://github.com/openSUSE/cnf
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# TODO: move files into git
Source10:       command_not_found.bash
Source11:       command_not_found.zsh
BuildRequires:  cargo-packaging
BuildRequires:  gettext-tools
BuildRequires:  libsolv-devel
# Fixes unable to find ['libclang.so', 'libclang-*.so', 'libclang.so.*', 'libclang-*.so.*']
# and missing /usr/include/stddef.h included from /usr/include/stdio.h
BuildRequires:  clang
# Installing those won't help
#BuildRequires:  libclang13
#BuildRequires:  linux-glibc-devel

# replaces old Python program
Obsoletes:      scout-command-not-found < 0.2.8
Provides:       command-not-found = %{version}-%{release}
Provides:       scout-command-not-found = %{version}-%{release}
# cnf-rs was not the best name
Provides:       cnf-rs = %{version}-%{release}
Obsoletes:      cnf-rs < %{version}-%{release}
ExclusiveArch:  %{rust_tier1_arches} %{arm} riscv64

%description
A libsolv based command-not-found handler for openSUSE.

%package bash
Summary:        Integration of %{name} with bash
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and bash)
Obsoletes:      scout-command-not-found < 0.2.8
# cnf-rs was not the best name
Provides:       cnf-rs-bash = %{version}-%{release}
Obsoletes:      cnf-rs-bash < %{version}-%{release}
BuildArch:      noarch

%description bash
Bash setup code for command-not-found handler %{name}.

%package zsh
Summary:        Integration of %{name} with zsh
Supplements:    (%{name} and zsh)
Obsoletes:      scout-command-not-found < 0.2.8
# cnf-rs was not the best name
Provides:       cnf-rs-zsh = %{version}-%{release}
Obsoletes:      cnf-rs-zsh < %{version}-%{release}
BuildArch:      noarch

%description zsh
Zsh setup code for command-not-found handler %{name}.

%package locale
Summary:        Locale support for %{name}
Requires:       %{name} = %{version}-%{release}
# cnf-rs was not the best name
Provides:       cnf-rs-locale = %{version}-%{release}
Obsoletes:      cnf-rs-locale < %{version}-%{release}
BuildArch:      noarch

%description locale
Locale support for %{name}

%prep
# The number passed to -a (a stands for "after") should be equivalent to the Source tag number
# of the vendor tarball, 1 in this case (from Source1).
%autosetup -a1

%build
%{cargo_build}

%install
# using cargo_install (only supports bindir)
%{cargo_install}

# https://bugzilla.opensuse.org/show_bug.cgi?id=1215428#c2
# fish depends on a /usr/bin/command-not-found beeing present
ln -sfr %{buildroot}/%{_bindir}/cnf %{buildroot}/%{_bindir}/command-not-found

# shell integrations
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/bash_command_not_found
install -D -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/zsh_command_not_found

# i18n
ls -1 i18n/po/ | while read LOCALE; do
    msgfmt i18n/po/${LOCALE}/%{name}.po -o %{name}.mo
    install -D -m 0644 %{name}.mo %{buildroot}%{_datadir}/locale/${LOCALE}/LC_MESSAGES/%{name}.mo
done
%find_lang %{name}

# man page
install -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%attr(0755,root,root) %{_bindir}/%{name}
%{_bindir}/command-not-found
%{_mandir}/man1/%{name}*

%files bash
%config %{_sysconfdir}/bash_command_not_found

%files zsh
%config %{_sysconfdir}/zsh_command_not_found

%files locale -f %{name}.lang

%changelog
