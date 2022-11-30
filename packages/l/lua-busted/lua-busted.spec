#
# spec file for package lua-busted
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Togan Muftuoglu toganm@opensuse.org
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


%define flavor @BUILD_FLAVOR@
%define mod_name busted
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%define upversion 2.0.0
Version:        2.0.0
Release:        0
Summary:        Unit testing framework with a focus on being easy to use
License:        MIT
Group:          Development/Languages/Other
URL:            http://olivinelabs.com/busted/
Source:         https://github.com/Olivine-Labs/%{mod_name}/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-cliargs >= 3.0-1
BuildRequires:  %{flavor}-devel
# For testing
# BuildRequires:  %%{flavor}-copas
BuildRequires:  %{flavor}-lua-ev
BuildRequires:  %{flavor}-luafilesystem
BuildRequires:  %{flavor}-luassert >= 1.7.8-0
BuildRequires:  %{flavor}-luasystem >= 0.2.0-0
BuildRequires:  %{flavor}-luaterm >= 0.1-1
BuildRequires:  %{flavor}-mediator_lua >= 1.1-0
BuildRequires:  %{flavor}-moonscript
BuildRequires:  %{flavor}-penlight >= 1.3.2-2
BuildRequires:  %{flavor}-say >= 1.3-0
BuildRequires:  curl
BuildRequires:  lua-macros
BuildRequires:  openssl
BuildRequires:  unzip
Requires:       %{flavor}
Requires:       %{flavor}-cliargs
Requires:       %{flavor}-dkjson >= 2.1.0-0
Requires:       %{flavor}-lua-ev
Requires:       %{flavor}-luafilesystem
Requires:       %{flavor}-luassert >= 1.7.8-0
Requires:       %{flavor}-luasystem >= 0.2.0-0
Requires:       %{flavor}-luaterm >= 0.1-1
Requires:       %{flavor}-mediator_lua >= 1.1-0
Requires:       %{flavor}-penlight
Requires:       %{flavor}-say >= 1.3-0
Requires:       curl
Requires:       openssl
Requires:       unzip
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
busted is a unit testing framework with a focus on being easy to
use. busted works with lua >= 5.1, moonscript, terra, and LuaJIT
>= 2.0.0.

busted test specs read naturally without being too verbose. You
can even chain asserts and negations, such as assert.not.equals.
Nest blocks of tests with contextual descriptions using describe,
and add tags to blocks so you can run arbitrary groups of tests.

An extensible assert library allows you to extend and craft your
own assert functions specific to your case with method chaining.
A modular output library lets you add on your own output format,
along with the default pretty and plain terminal output, JSON
with and without streaming, and TAP-compatible output that allows
you to run busted specs within most CI servers. You can even
register phrases for internationaliation with custom or built-in
language packs.

%prep
%setup -q -n %{mod_name}-%{version}
sed -i 's|^#!%{_bindir}/env lua|#!%{_bindir}/lua%{lua_version}|' bin/busted

%build
/bin/true

%install
install -v -m 0755 -p -d %{buildroot}%{lua_noarchdir}
cp -r -p -v busted %{buildroot}%{lua_noarchdir}
install -v -D -m 0755 -p bin/busted %{buildroot}%{_bindir}/busted-%{lua_version}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/busted
ln -sf %{_sysconfdir}/alternatives/busted \
    %{buildroot}%{_bindir}/busted

# shell completions
install -v -D -m 0644 -p completions/bash/busted.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/busted-%{lua_version}
install -v -D -m 0644 -p completions/zsh/_busted \
    %{buildroot}%{_datadir}/zsh/vendor-completions/_busted-%{lua_version}
touch %{buildroot}%{_sysconfdir}/alternatives/busted.bash
touch %{buildroot}%{_sysconfdir}/alternatives/busted.zsh
ln -sf %{_sysconfdir}/alternatives/busted.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/busted
ln -sf %{_sysconfdir}/alternatives/busted.zsh \
    %{buildroot}%{_datadir}/zsh/vendor-completions/_busted

%post
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/busted busted %{_bindir}/busted-%{lua_version} %{lua_value} \
    --slave %{_datadir}/bash-completion/completions/busted busted.bash \
        %{_datadir}/bash-completion/completions/busted-%{lua_version} \
    --slave %{_datadir}/zsh/vendor-completions/_busted busted.zsh \
        %{_datadir}/zsh/vendor-completions/_busted-%{lua_version}

%postun
if [ ! -f %{_bindir}/busted-%{lua_version} ] ; then
	%{_sbindir}/update-alternatives --remove busted %{_bindir}/busted-%{lua_version}
fi

%check
bin/busted -v spec

%files
%license LICENSE
%doc README.md TODO.md CONTRIBUTING.md
%ghost %{_sysconfdir}/alternatives/busted
%ghost %{_sysconfdir}/alternatives/busted.bash
%ghost %{_sysconfdir}/alternatives/busted.zsh
%{_bindir}/busted
%{_bindir}/busted-%{lua_version}
%{lua_noarchdir}/busted
%{_datadir}/bash-completion/completions/busted
%{_datadir}/bash-completion/completions/busted-%{lua_version}
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/vendor-completions/_busted
%{_datadir}/zsh/vendor-completions/_busted-%{lua_version}

%changelog
