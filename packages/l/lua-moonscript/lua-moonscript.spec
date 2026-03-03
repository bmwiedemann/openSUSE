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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
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
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
:

%install
%if ! %{with test}
install -m 0755 -p -d %{buildroot}%{lua_noarchdir}
cp -r -p moonscript %{buildroot}%{lua_noarchdir}
cp -r -p moon %{buildroot}%{lua_noarchdir}
install -D -m 0755 -p -t %{buildroot}%{_bindir} bin/moon{,c}

# Prepare alternatives handling
mv -v %{buildroot}%{_bindir}/moon{,-%{lua_version}}
mv -v %{buildroot}%{_bindir}/moonc{,-%{lua_version}}
chmod +x %{buildroot}%{_bindir}/moon-%{lua_version}
chmod +x %{buildroot}%{_bindir}/moonc-%{lua_version}
sed -i -e 's,# *\!%{_bindir}/.*lua.*$,#!%{_bindir}/%{lua_version},' \
    %{buildroot}%{_bindir}/moon-%{lua_version} \
    %{buildroot}%{_bindir}/moonc-%{lua_version}

%if %{with libalternatives}
# alternatives - create configuration file
echo "### lua_value = %{lua_value}"
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/moon
mkdir -p %{buildroot}%{_datadir}/libalternatives/moon
cat > %{buildroot}%{_datadir}/libalternatives/moon/%{lua_value}.conf <<EOF
binary=%{_bindir}/moon-%{lua_version}
EOF
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/moonc
mkdir -p %{buildroot}%{_datadir}/libalternatives/moonc
cat > %{buildroot}%{_datadir}/libalternatives/moonc/%{lua_value}.conf <<EOF
binary=%{_bindir}/moonc-%{lua_version}
EOF
%else
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/moon
ln -sf %{_sysconfdir}/alternatives/moon %{buildroot}%{_bindir}/moon
touch %{buildroot}%{_sysconfdir}/alternatives/moonc
ln -sf %{_sysconfdir}/alternatives/moonc %{buildroot}%{_bindir}/moonc
%endif
%endif


%if ! %{with test}
%if %{without libalternatives}
%post
update-alternatives --force \
    --install %{_bindir}/moon moon %{_bindir}/moon-%{lua_version} 15 \
    --slave %{_bindir}/moonc moonc %{_bindir}/moonc-%{lua_version}

%postun
if [ ! -f %{_bindir}/moon-%{lua_version} ] ; then
   update-alternatives --remove moon %{_bindir}/moon-%{lua_version}
fi
%endif
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
%if %{with libalternatives}
%dir %{_datadir}/libalternatives
%{_datadir}/libalternatives/moon
%{_datadir}/libalternatives/moonc
%else
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/moon
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/moonc
%endif
%endif

%changelog
