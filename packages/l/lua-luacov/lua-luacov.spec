#
# spec file for package lua-luacov
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


%define flavor @BUILD_FLAVOR@
%define mod_name luacov
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%alternatives_requires_exclude
Version:        0.17.0
Release:        0
Summary:        Coverage analysis tool for Lua scripts
License:        MIT
URL:            https://github.com/lunarmodules/luacov
Source:         https://github.com/lunarmodules/luacov/archive/refs/tags/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-datafile
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
LuaCov is a simple coverage analysis tool for Lua scripts. When a Lua
script is run with the luacov module, it generates a stats file. The
luacov command-line script then processes this file generating a report
indicating which code paths were not traversed, which is useful for
verifying the effectiveness of a test suite.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
:

%install
install -Dm644 src/luacov.lua %{buildroot}%{lua_noarchdir}/luacov.lua
cp -p -r src/luacov %{buildroot}%{lua_noarchdir}/
install -D -m 0755 -p -t %{buildroot}%{_bindir} src/bin/luacov

# Alternatives handling
mv -v %{buildroot}%{_bindir}/luacov{,-%{lua_version}}
chmod +x %{buildroot}%{_bindir}/luacov-%{lua_version}
sed -i -e 's,# *\!%{_bindir}/.*lua.*$,#!%{_bindir}/lua%{lua_version},' \
    %{buildroot}%{_bindir}/luacov-%{lua_version}

%if %{with libalternatives}
# alternatives - create configuration file
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/luacov
mkdir -p %{buildroot}%{_datadir}/libalternatives/luacov
cat > %{buildroot}%{_datadir}/libalternatives/luacov/%{lua_value}.conf <<EOF
binary=%{_bindir}/luacov-%{lua_version}
EOF
%else
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/luacov
ln -sf %{_sysconfdir}/alternatives/luacov %{buildroot}%{_bindir}/luacov
%endif

%if %{without libalternatives}
%post
update-alternatives --force \
    --install %{_bindir}/luacov luacov %{_bindir}/luacov-%{lua_version} %{lua_value}

%postun
if [ ! -f %{_bindir}/luacov-%{lua_version} ] ; then
   update-alternatives --remove luacov %{_bindir}/luacov-%{lua_version}
fi
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/luacov
%{_bindir}/luacov-%{lua_version}
%{lua_noarchdir}/luacov.lua
%{lua_noarchdir}/luacov
%if %{with libalternatives}
%dir %{_datadir}/libalternatives
%{_datadir}/libalternatives/luacov
%else
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/moon
%endif

%changelog
