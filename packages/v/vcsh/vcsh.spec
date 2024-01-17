#
# spec file for package vcsh
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           vcsh
Version:        1.20151229
Release:        0
Summary:        Config manager for $HOME based on git
License:        GPL-2.0-only
Group:          System/Management
Url:            https://github.com/RichiH/vcsh
Source0:        https://github.com/RichiH/vcsh/archive/v%{version}.tar.gz
# Tests require perl modules that aren't in openSUSE repos
Patch0:         disable-tests.patch
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  zsh
Requires:       bash
Requires:       git-core
BuildArch:      noarch

%description
vcsh allows you to have several git repositories, all maintaining
their working trees in $HOME without clobbering each other. That, in
turn, means you can have one repository per config set (zsh, vim,
ssh, etc), picking and choosing which configs you want to use on
which machine.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
zsh command line completion support for %{name}.

%prep
%setup -q
%patch0

%build

%install
%make_install DOCDIR_PREFIX=%{_docdir} ZSHDIR=%{_sysconfdir}/zsh_completion.d
%fdupes -s %{buildroot}/%{_prefix}

%files
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/hooks
%doc %{_docdir}/%{name}/README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%files zsh-completion
%config %{_sysconfdir}/zsh_completion.d/_vcsh

%changelog
