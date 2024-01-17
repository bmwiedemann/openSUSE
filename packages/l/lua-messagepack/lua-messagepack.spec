#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
%define mod_name messagepack
%define rname MessagePack
Version:        0.5.2
Release:        0
Summary:        MessagePack is an efficient binary serialization format
License:        MIT
Group:          Development/Libraries/Other
URL:            https://framagit.org/fperrad/lua-MessagePack
Source:         https://framagit.org/fperrad/lua-MessagePack/raw/releases/lua-messagepack-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%lua_provides -n lua-MessagePack
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
MessagePack is an efficient binary serialization format.
It lets you exchange data among multiple languages like JSON but it's faster and
smaller.
It's a pure Lua implementation, without dependency.
And it's really fast with LuaJIT.

%prep
%setup -q -n lua-%{rname}-%{version}

%build
:

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} LUAVER=%{lua_version} install

%files
%doc CHANGES COPYRIGHT README.md
%{lua_noarchdir}

%changelog
