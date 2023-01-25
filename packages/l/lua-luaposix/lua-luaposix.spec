#
# spec file for package lua-luaposix
#
# Copyright (c) 2020 SUSE LLC
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
%define mod_name luaposix
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        35.1
Release:        0
Summary:        POSIX library for Lua
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/luaposix/luaposix
Source0:        https://github.com/luaposix/luaposix/archive/v%{version}/%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl
Requires:       %{flavor}
%lua_provides

%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.

%package -n %{mod_name}-doc
Summary:        Documentation on luaposix
Group:          Documentation/HTML
BuildArch:      noarch

%description -n %{mod_name}-doc
This package contains the documentation for %{flavor}-luaposix.

%prep
%autosetup -n luaposix-%{version}

%build
# avoid setting USER tag
export USER=""
build-aux/luke PREFIX=%{_prefix} all

%install
build-aux/luke PREFIX=%{buildroot}%{_prefix} INST_LIBDIR=%{buildroot}%{lua_archdir} \
    INST_LUADIR=%{buildroot}%{lua_noarchdir} install

%files
%doc README.md NEWS.md AUTHORS
%license LICENSE
%{lua_archdir}/posix
%{lua_noarchdir}/posix

# Only produce docs during one flavor to avoid duplicate binary.
%ifluadefault
%files -n %{mod_name}-doc
%doc doc/*
%endif

%changelog
