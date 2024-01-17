#
# spec file for package lua-moonscript
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
%if "%{flavor}" == "test"
%define flavor lua54
%bcond_without test
%else
%bcond_with test
%endif
%define mod_name moonscript
%define upversion 0.5.0
Version:        0.5.0
Release:        0
Summary:        A programmer friendly language that compiles to Lua
License:        MIT
Group:          Development/Libraries/Other
URL:            http://moonscript.org/
Source:         https://github.com/leafo/moonscript/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-alt-getopt
BuildRequires:  %{flavor}-argparse >= 0.5
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-loadkit
BuildRequires:  %{flavor}-lpeg >= 0.10
BuildRequires:  %{flavor}-luafilesystem >= 1.5
BuildRequires:  lua-macros
Requires:       %{flavor}
Requires:       %{flavor}-alt-getopt
Requires:       %{flavor}-argparse
Requires:       %{flavor}-loadkit
Requires:       %{flavor}-lpeg
Requires:       %{flavor}-luafilesystem
Requires(post): update-alternatives
Requires(postun): update-alternatives
# optionally BuildRequires:  %%{flavor}-lnotify
BuildArch:      noarch
%lua_provides
%if ! %{with test}
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
%else
Name:           %{flavor}-moonscript-test
BuildRequires:  %{flavor}-busted
%endif

%description
A programmer friendly language that compiles to Lua.

%prep
%setup -q -n %{mod_name}-%{upversion}
sed -i 's|^#!%{_bindir}/env lua|#!%{_bindir}/lua%{lua_version}|' bin/moon{,c}

%build
/bin/true

%install
%if ! %{with test}
install -m 0755 -p -d %{buildroot}%{lua_noarchdir}
cp -r -p moonscript %{buildroot}%{lua_noarchdir}
cp -r -p moon %{buildroot}%{lua_noarchdir}
install -D -m 0755 -p -t %{buildroot}%{_bindir} bin/moon{,c}

# Alternatives
# create a dummy target for /etc/alternatives/vim
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mv %{buildroot}%{_bindir}/moon{,-%{lua_version}}
mv %{buildroot}%{_bindir}/moonc{,-%{lua_version}}
ln -s -f %{_sysconfdir}/alternatives/moonc %{buildroot}%{_bindir}/moonc
ln -s -f %{_sysconfdir}/alternatives/moon %{buildroot}%{_bindir}/moon
%endif

%if ! %{with test}
%post
update-alternatives --force \
    --install %{_bindir}/moon moon %{_bindir}/moon-%{lua_version} 15 \
    --slave %{_bindir}/moonc moonc %{_bindir}/moonc-%{lua_version}

%postun
if [ ! -f %{_bindir}/moon-%{lua_version} ] ; then
   update-alternatives --remove moon %{_bindir}/moon-%{lua_version}
fi
%endif

%check
%if %{with test}
busted
%endif

%if ! %{with test}
%files
%doc CHANGELOG.md README.md docs
%{_bindir}/moon
%{_bindir}/moon-%{lua_version}
%{_bindir}/moonc
%{_bindir}/moonc-%{lua_version}
%{lua_noarchdir}/moon*
%ghost %{_sysconfdir}/alternatives/moon
%ghost %{_sysconfdir}/alternatives/moonc
%endif

%changelog
