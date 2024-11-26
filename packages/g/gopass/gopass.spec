#
# spec file for package gopass
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


%global make_args PREFIX=%{_prefix} GOPASS_REVISION=v%{version}
Name:           gopass
Version:        1.15.15
Release:        0
Summary:        The slightly more awesome standard unix password manager for teams
License:        MIT
URL:            https://www.gopass.pw/
Source:         https://github.com/gopasspw/gopass/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        system_config
Source9:        series
Patch0:         do-not-strip.patch
BuildRequires:  fish
BuildRequires:  golang-packaging
BuildRequires:  gpg2
BuildRequires:  pkgconfig
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.22
BuildRequires:  pkgconfig(bash-completion)
Requires:       git-core
%{go_nostrip}

%description
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (bash and %{name})
BuildArch:      noarch
Provides:       gopass-completion-bash = %{version}-%{release}
Obsoletes:      gopass-completion-bash < %{version}-%{release}

%description bash-completion
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package holds the shell completion for bash.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (fish and %{name})
BuildArch:      noarch
Provides:       gopass-completion-fish = %{version}-%{release}
Obsoletes:      gopass-completion-fish < %{version}-%{release}

%description fish-completion
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package holds the shell completion for fish.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (zsh and %{name})
BuildArch:      noarch
Provides:       gopass-completion-zsh = %{version}-%{release}
Obsoletes:      gopass-completion-zsh < %{version}-%{release}

%description zsh-completion
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package holds the shell completion for zsh.

%package impersonate-pass
Summary:        Provide %{_bindir}/pass as drop-in replacement
Requires:       %{name} = %{version}
Conflicts:      password-store
BuildArch:      noarch

%description impersonate-pass
Manage your credentials with ease. In a globally distributed team, on multiple devices or fully offline on an air gapped machine.

Works everywhere - The same user experience on Linux, MacOS, *BSD or Windows
Built for teams - Built from our experience working in distributed development teams
Full autonomy - No network connectivity required, unless you want it

This package provides a symlink to make this a drop in replacement for password-store.

%prep
%autosetup -p1 -a1

%build
%make_build %{make_args}

%install
%make_install %{make_args}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/gopass/config
ln -sf gopass %{buildroot}%{_bindir}/pass

%files
%license LICENSE
%doc *.md
%config(noreplace) %{_sysconfdir}/gopass/
%{_bindir}/gopass
%{_mandir}/man1/gopass.1%{?ext_man}

%files bash-completion
%license LICENSE
%{_datadir}/bash-completion/completions/gopass

%files fish-completion
%license LICENSE
%{_datadir}/fish/vendor_completions.d/gopass.fish

%files zsh-completion
%license LICENSE
%{_datadir}/zsh/site-functions/_gopass

%files impersonate-pass
%license LICENSE
%{_bindir}/pass

%changelog
