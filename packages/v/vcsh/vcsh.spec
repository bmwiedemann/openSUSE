#
# spec file for package vcsh
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           vcsh
Version:        2.0.10
Release:        0
Summary:        Config manager for $HOME based on git
License:        GPL-2.0-or-later
URL:            https://github.com/RichiH/vcsh
Source0:        https://github.com/RichiH/vcsh/releases/download/v2.0.10/vcsh-2.0.10.tar.zst
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pkgconfig
# Source0 is .tar.zst, rpmuncompress needs the binary in the build root
BuildRequires:  zstd
BuildRequires:  pkgconfig(bash-completion)
Requires:       bash
Requires:       git-core
BuildArch:      noarch

%description
vcsh allows you to have several git repositories, all maintaining
their working trees in $HOME without clobbering each other. That, in
turn, means you can have one repository per config set (zsh, vim,
ssh, etc), picking and choosing which configs you want to use on
which machine.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup

%build
# Tests need perl(Shell::Command), which is not in Factory
%configure --disable-tests
# configure rewrites aminclude.am, making it newer than Makefile.in, so make
# would try to re-run automake; restore the order instead
touch Makefile.in
%make_build

%install
# docdir is hardcoded in Makefile.am, ignoring configure --docdir
%make_install docdir=%{_docdir}/%{name}
# Upstream installs licenses itself; use the macro instead
rm -rf %{buildroot}%{_datadir}/licenses
%fdupes -s %{buildroot}%{_prefix}

%files
%license LICENSE.md
%dir %{_docdir}/%{name}
%doc CONTRIBUTORS
%doc %{_docdir}/%{name}/changelog
%doc %{_docdir}/%{name}/error_codes.md
%doc %{_docdir}/%{name}/INSTALL.md
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/sample_hooks
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_vcsh

%changelog
