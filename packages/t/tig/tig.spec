#
# spec file for package tig
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


Name:           tig
Version:        2.5.8
Release:        0
Summary:        An ncurses-based text-mode interface for git
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://jonas.github.io/tig/
Source0:        https://github.com/jonas/tig/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  readline-devel >= 6.3
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(ncurses)
Requires:       git-core

%description
Tig is a git repository browser that additionally can act as a pager
for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p1

%build
%configure \
	--with-ncurses \
	--docdir=%{_docdir}
%make_build

%install
%make_install install-doc-man
install -Dpm 0644 contrib/tig-completion.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 0644 contrib/tig-completion.bash \
  %{buildroot}%{_datadir}/zsh/site-functions/%{name}-completion.bash
install -Dpm 0644 contrib/tig-completion.zsh \
  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license COPYING
%doc NEWS.adoc README.adoc
%doc contrib/*.tigrc
%{_bindir}/tig
%config %{_sysconfdir}/tigrc
%{_mandir}/man1/tig.1%{?ext_man}
%{_mandir}/man5/tigrc.5%{?ext_man}
%{_mandir}/man7/tigmanual.7%{?ext_man}

%files bash-completion
%license COPYING
%{_datadir}/bash-completion

%files zsh-completion
%license COPYING
%{_datadir}/zsh

%changelog
