#
# spec file for package jo
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


Name:           jo
Version:        1.9
Release:        0
Summary:        JSON output from a shell
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/jpmens/jo/
#Git-Clone:     https://github.com/jpmens/jo.git
Source:         https://github.com/jpmens/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig

%description
This is jo, a small utility to create JSON objects

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Text/Utilities
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%package zsh-completion
Summary:        ZSH completion for %{name}
Group:          Productivity/Text/Utilities
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%prep
%setup -q

%build
autoreconf -fiv
export bashcompdir=%{_datadir}/bash-completion/completions/
%configure
%make_build

%install
%make_install
install -d %{buildroot}/%{_sysconfdir}/zsh_completion.d
mv %{buildroot}%{_datadir}/zsh/site-functions/_jo %{buildroot}%{_sysconfdir}/zsh_completion.d/%{name}

%check
%make_build check

%files
%license COPYING
%doc README ChangeLog AUTHORS
%{_bindir}/jo
%{_mandir}/man1/jo.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}.bash

%files zsh-completion
%dir %{_sysconfdir}/zsh_completion.d
%config %{_sysconfdir}/zsh_completion.d/%{name}

%changelog
