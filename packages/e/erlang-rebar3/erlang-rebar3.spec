#
# spec file for package erlang-rebar3
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


%define mod_ver %(echo "%{version}" | cut -d "+" -f1)
%if 0%{?suse_version}
%if 1%{?erlang_libdir:0}
%define erlang_libdir %{_libdir}/erlang/lib
%endif
%endif
Name:           erlang-rebar3
Version:        3.18.0
Release:        0
Summary:        Tool for working with Erlang projects
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/erlang/rebar3
Source:         rebar3-%{version}.tar.xz
Patch0:         add-rebar3-escript.patch
Patch1:         erlang-rebar3-0001-Skip-deps.patch
BuildRequires:  erlang >= 22
BuildRequires:  erlang-erlware_commons
BuildRequires:  erlang-providers
Requires:       erlang
Requires:       erlang-erlware_commons
Requires:       erlang-providers

%description
Rebar3 is an Erlang tool that makes it easy to create, develop, and release
Erlang libraries, applications, and systems in a repeatable manner.

Rebar3 is the spiritual successor to rebar 2.x, which was the first usable
build tool for Erlang that ended up seeing widespread community adoption. It
however had several shortcomings that made it difficult to use with larger
projects or with teams with users new to Erlang.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Development/Tools/Building
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for rebar3.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          Development/Tools/Building
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for rebar3.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Development/Tools/Building
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for rebar3.

%prep
%setup -q -n rebar3-%{version}
%patch0 -p1
%patch1 -p1

%build
EBIN_PATHS=$(x1=(%{erlang_libdir}/*/ebin); x2=(${x1[*]#*rebar*}); IFS=":"; echo "${x2[*]}")
DIAGNOSTIC=1 ./bootstrap bare compile --paths $EBIN_PATHS --separator :

%install
install -Dm755 rebar3 %{buildroot}%{_bindir}/rebar3
# Install RPM macros:
#install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.erlang-rebar
for dir in ebin priv ; do
  install -d %{buildroot}%{erlang_libdir}/rebar3-%{mod_ver}/${dir}
  cp -r ./_build/bootstrap/lib/rebar/${dir}/* %{buildroot}%{erlang_libdir}/rebar3-%{mod_ver}/${dir}/
done

mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions
ln -s %{erlang_libdir}/rebar3-%{mod_ver}/priv/shell-completion/bash/rebar3 %{buildroot}/%{_datadir}/bash-completion/completions/rebar3
mkdir -p %{buildroot}/%{_datadir}/fish/vendor_completions.d
ln -s %{erlang_libdir}/rebar3-%{mod_ver}/priv/shell-completion/zsh/_rebar3 %{buildroot}/%{_datadir}/fish/vendor_completions.d/rebar3.fish
mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
ln -s %{erlang_libdir}/rebar3-%{mod_ver}/priv/shell-completion/fish/rebar3.fish %{buildroot}/%{_datadir}/zsh/site-functions/_rebar3
install -Dm644 manpages/rebar3.1 %{buildroot}%{_mandir}/man1/rebar3.1

%files
%license LICENSE
%doc README.md THANKS rebar.config.sample CONTRIBUTING.md
%{_bindir}/rebar3
%dir %{erlang_libdir}/rebar3-%{mod_ver}
%{erlang_libdir}/rebar3-%{mod_ver}/ebin
%{erlang_libdir}/rebar3-%{mod_ver}/priv
%{_mandir}/man1/rebar3.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
