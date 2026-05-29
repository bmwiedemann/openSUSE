#
# spec file for package lua-fennel
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020 Fabio Pesari
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
%define mod_name fennel
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Version:        1.6.0
Release:        0
Summary:        Lisp dialect that compiles to Lua
License:        MIT
Group:          Development/Languages/Lua
URL:            https://fennel-lang.org/
Source0:        https://git.sr.ht/~technomancy/fennel/archive/%{version}.tar.gz#/lua-%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}
BuildRequires:  lua-macros
BuildArch:      noarch
%{lua_provides}
%if "%{flavor}" != ""
Requires:       %{flavor}
Obsoletes:      lua-%{mod_name}
%if "%{lua_version}" == "%{lua_version_default}"
Suggests:       lua-%{mod_name}-doc = %{version}
%endif
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif

%description
Fennel is a lisp that compiles to Lua. Features include:

• Full Lua compatibility - You can use any function or library from
  Lua.
• Zero overhead - Compiled code should be just as or more efficient
  than hand-written Lua.
• Compile-time macros - Ship compiled code with no runtime
  dependency on Fennel.
• Embeddable - Fennel is a one-file library as well as an
  executable.
  Embed it in other programs to support runtime extensibility and
  interactive development.

%if "%{lua_version}" == "%{lua_version_default}"
%package -n lua-%{mod_name}-doc
Summary:        Man pages for Fennel
Group:          Documentation/Other
BuildArch:      noarch
Conflicts:      lua-fennel < %{version}-%{release}

%description -n lua-%{mod_name}-doc
Man pages and reference documentation for Fennel, a Lisp dialect
that compiles to Lua. Includes pages covering the command-line
interface, the Lua API, the language reference, and the tutorial.
%endif

%prep
%autosetup -p1 -n fennel-%{version}

%build
%make_build %{?_make_output_sync} PREFIX=%{_prefix} LUA="lua" fennel
sed -i -e 's@#!%{_bindir}/env lua$@#!%{_bindir}/lua@' fennel

%install
%make_install %{?_make_output_sync} PREFIX=%{_prefix} install
mv -v %{buildroot}%{_bindir}/fennel{,-%{lua_version}}
chmod +x %{buildroot}%{_bindir}/fennel-%{lua_version}
sed -i -e 's,# *\!%{_bindir}/.*lua.*$,#!'$(alts -t lua)',' \
    %{buildroot}%{_bindir}/fennel-%{lua_version}

%if "%{lua_version}" != "%{lua_version_default}"
rm -rv %{buildroot}%{_mandir}
%endif

%if %{with libalternatives}
# alternatives - create configuration file
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/fennel
mkdir -p %{buildroot}%{_datadir}/libalternatives/fennel
cat > %{buildroot}%{_datadir}/libalternatives/fennel/%{lua_value}.conf <<EOF
binary=%{_bindir}/fennel-%{lua_version}
EOF
%else
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/fennel
ln -sf %{_sysconfdir}/alternatives/fennel %{buildroot}%{_bindir}/fennel
%endif

%check
%make_build %{?_make_output_sync} test

%if %{without libalternatives}
%post
%{_sbindir}/update-alternatives --install %{_bindir}/fennel fennel \
    %{_bindir}/fennel-%{lua_version} %{lua_value}

%postun
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove fennel
    %{_bindir}/fennel-%{lua_version}
fi
%endif

%files
%doc README.md api.md changelog.md reference.md tutorial.md
%license LICENSE
%if ! %{with libalternatives}
%ghost %{_sysconfdir}/alternatives/fennel
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/fennel
%{_datadir}/libalternatives/fennel/%{lua_value}.conf
%endif

%{_bindir}/fennel
%{_bindir}/fennel-%{lua_version}
%{lua_noarchdir}/fennel.lua

%if "%{lua_version}" == "%{lua_version_default}"
%files -n lua-%{mod_name}-doc
%{_mandir}/man*/fennel*%{?ext_man}
%endif

%changelog
