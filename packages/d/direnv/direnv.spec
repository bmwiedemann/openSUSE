#
# spec file for package direnv
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


%define gopackagepath github.com/direnv/direnv
Name:           direnv
Version:        2.35.0
Release:        0
Summary:        Environment switcher for shells
License:        MIT
Group:          Productivity/File utilities
URL:            https://direnv.net/
Source0:        https://github.com/direnv/direnv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         resolve-bin-path.patch
BuildRequires:  fish
BuildRequires:  go >= 1.6
BuildRequires:  make
BuildRequires:  zstd

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%description
direnv knows how to hook into bash, zsh, tcsh and fish shell to load
or unload environment variables depending on the current directory.
This allows to have project-specific environment variables and not
clutter the "~/.profile" file.

%prep
%autosetup -a1 -p1

%build
%make_build PREFIX=%{_prefix} \
%ifnarch ppc64
  GO_BUILD_FLAGS="-buildmode=pie"
%endif

%install
%make_install PREFIX=%{_prefix}

export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions

direnv hook bash > %{buildroot}%{_sysconfdir}/bash_completion.d/direnv.sh
direnv hook fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
direnv hook zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-stdlib.1%{?ext_man}
%{_mandir}/man1/%{name}.toml.1%{?ext_man}
%{_mandir}/man1/%{name}-fetchurl.1%{?ext_man}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/fish/vendor_conf.d/%{name}.fish

%files bash-completion
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/direnv.sh

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
