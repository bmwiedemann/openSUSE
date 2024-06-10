#
# spec file for package lf
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


Name:           lf
Version:        32
Release:        0
Summary:        Terminal file manager (with sixel support)
License:        MIT
Group:          Productivity/File utilities
URL:            https://github.com/gokcehan/lf
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging

%description
lf (as in "list files") is a terminal file manager written in Go with a
heavy inspiration from ranger file manager

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a 1

%build
go build -v -buildmode=pie -ldflags="-s -w \
 -X main.gVersion=%{version}" \
 -mod vendor -trimpath .

%install
install -Dm755 -t "%{buildroot}%{_bindir}" lf
install -Dm644 -t "%{buildroot}%{_mandir}/man1" lf.1
install -Dm644 -t "%{buildroot}%{_docdir}/%{name}" README.md etc/lfrc.example
install -Dm644 -t "%{buildroot}%{_datadir}/applications" lf.desktop
install -Dm644 -t "%{buildroot}%{_datadir}/bash-completion/completions/lf" etc/lf.bash
install -Dm644 -t "%{buildroot}%{_datadir}/fish/vendor_functions.d" etc/lfcd.fish
install -Dm644 -t "%{buildroot}%{_datadir}/fish/vendor_completions.d/lf.fish" etc/lf.fish
install -Dm644 -t "%{buildroot}%{_datadir}/zsh/site-functions/_lf" etc/lf.zsh
install -Dm644 -t "%{buildroot}%{_licensedir}/lf" LICENSE

%files
%doc README.md lfrc.example
%license LICENSE

%{_mandir}/man1/lf.1*
%{_bindir}/lf
%{_datadir}/applications/%{name}.desktop

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
