#
# spec file
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

%bcond_without test
%define flavor @BUILD_FLAVOR@
%define mod_name luarepl
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%define rock_version 0.10-1
Version:        0.10
Release:        0
Summary:        A Lua REPL implemented in Lua for embedding in other programs
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/hoelzro/lua-repl
Source:         lua-repl-%{version}.tar.xz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-luarocks
BuildRequires:  %{flavor}-devel
%if %{with test}
BuildRequires:  perl
BuildRequires:  %{flavor}-testmore
%endif
Requires:       %{flavor}
Requires:       bash-sh
# https://github.com/hoelzro/lua-repl#recommended-packages
Recommends:     %{flavor}-linenoise
# Enable filename_completion plugin
Suggests:       %{flavor}-filesystem
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
This project has two uses:
- An alternative to the standalone interpreter included with Lua, one that
supports things like plugins, tab completion, and automatic insertion of
return in front of expressions.
- A REPL library you may embed in your application, to provide all of the
niceties of the standalone interpreter included with Lua and then some.

%prep
%autosetup -n lua-repl-%{version}
# Fix the Lua shebang of rep.lua script
sed -i -r '1s/env (lua)/\1%{lua_version}/' rep.lua

%build
%luarocks_build "%{mod_name}-%{rock_version}.rockspec"

%install
%luarocks_install *.rock

# Version the rep.lua file
sed -i -r -e "s#%{buildroot}##" -e "s#(/bin/rep.lua)#\1-%{lua_version}#" \
    "%{buildroot}/usr/bin/rep.lua"
mv %{buildroot}%{_bindir}/rep.lua{,-%{lua_version}}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/rep.lua
ln -sf %{_sysconfdir}/alternatives/rep.lua %{buildroot}%{_bindir}/rep.lua
mkdir -p %{buildroot}%{luarocks_treedir}/%{mod_name}/%{rock_version}/bin
touch %{buildroot}%{luarocks_treedir}/%{mod_name}/%{rock_version}/bin/rep.lua-%{lua_version}
ln -sf %{luarocks_treedir}/%{mod_name}/%{rock_version}/bin/rep.lua \
%{buildroot}%{luarocks_treedir}/%{mod_name}/%{rock_version}/bin/rep.lua-%{lua_version}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/rep.lua rep.lua %{_bindir}/rep.lua-%{lua_version} %{lua_value}

%postun
if [ "$1" = 0 ] ; then
 %{_sbindir}/update-alternatives --remove rep.lua %{_bindir}/rep.lua-%{lua_version}
fi

%if %{with test}
%check
make test
%endif

%files
%license %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc/COPYING
%docdir %{luarocks_treedir}/%{mod_name}/%{rock_version}/doc
%{lua_noarchdir}
%{luarocks_treedir}/%{mod_name}
%ghost %{_sysconfdir}/alternatives/rep.lua
%{_bindir}/rep.lua
%{_bindir}/rep.lua-%{lua_version}

%changelog
