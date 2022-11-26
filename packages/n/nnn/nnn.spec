#
# spec file for package nnn
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


Name:           nnn
Version:        4.7
Release:        0
Summary:        Terminal based file browser
License:        BSD-2-Clause
Group:          Productivity/File utilities
URL:            https://github.com/jarun/nnn#nnn
Source0:        https://github.com/jarun/nnn/releases/download/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        https://github.com/jarun/nnn/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source99:       nnn.keyring
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
Recommends:     sshfs
%if 0%{?leap_version} == 420300
BuildRequires:  ncurses-devel
%else
BuildRequires:  pkgconfig(ncursesw)
%endif

%description
nnn is a fork of noice, a terminal file browser with keyboard
shortcuts for navigation, opening files and running tasks. There is
no config file and MIME associations are hard-coded.

%package bash-completion
Summary:        Bash completions for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build strip

%install
%make_install PREFIX=%{_prefix}

install -Dm0644 misc/auto-completion/fish/nnn.fish $RPM_BUILD_ROOT%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm0644 misc/auto-completion/bash/nnn-completion.bash $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 misc/auto-completion/zsh/_nnn $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh/

%changelog
