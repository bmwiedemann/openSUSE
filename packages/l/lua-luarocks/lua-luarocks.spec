#
# spec file for package lua-luarocks
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


%define flavor @BUILD_FLAVOR@%{nil}
%define mod_name luarocks
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
Version:        3.9.1
Release:        0
Summary:        A deployment and management system for Lua modules
License:        MIT
Group:          Development/Languages/Other
URL:            https://luarocks.org
Source0:        https://luarocks.org/releases/%{mod_name}-%{version}.tar.gz
Patch0:         lib64.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  curl
BuildRequires:  lua-macros
BuildRequires:  openssl
BuildRequires:  unzip
Requires:       %{flavor}
Requires:       curl
Requires:       openssl
Requires:       unzip
Requires:       zip
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
LuaRocks allows you to install Lua modules as self-contained packages
called "rocks", which also contain version dependency
information. This information is used both during installation, so
that when one rock is requested all rocks it depends on are installed
as well, and at run time, so that when a module is required, the
correct version is loaded. LuaRocks supports both local and remote
repositories, and multiple local rocks trees.

%prep
%autosetup -n %{mod_name}-%{version} -p1

%build
# Not an autotools based system
./configure \
  --prefix=%{_prefix} \
  --lua-version=%{lua_version}
make %{?_smp_mflags} build

%install
%make_install
mv %{buildroot}%{_bindir}/luarocks{,-%{lua_version}}
mv %{buildroot}%{_bindir}/luarocks-admin{,-%{lua_version}}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/luarocks
ln -sf %{_sysconfdir}/alternatives/luarocks %{buildroot}%{_bindir}/luarocks
touch %{buildroot}%{_sysconfdir}/alternatives/luarocks-admin
ln -sf %{_sysconfdir}/alternatives/luarocks %{buildroot}%{_bindir}/luarocks-admin

# rockstree
mkdir -p %{buildroot}%{luarocks_treedir}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/luarocks luarocks %{_bindir}/luarocks-%{lua_version} %{lua_value} \
  --slave %{_bindir}/luarocks-admin luarocks-admin %{_bindir}/luarocks-%{lua_version}

%postun
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove luarocks %{_bindir}/luarocks-%{lua_version}
fi

%files
%license COPYING
%doc README.md CHANGELOG.md
%dir %{_sysconfdir}/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/config-%{lua_version}.lua
%ghost %{_sysconfdir}/alternatives/luarocks
%ghost %{_sysconfdir}/alternatives/luarocks-admin
%{_bindir}/luarocks
%{_bindir}/luarocks-admin
%{_bindir}/luarocks-%{lua_version}
%{_bindir}/luarocks-admin-%{lua_version}
%{lua_noarchdir}/luarocks
%dir %{_prefix}/lib/luarocks/rocks-%{lua_version}
%dir %{_prefix}/lib/luarocks

%changelog
