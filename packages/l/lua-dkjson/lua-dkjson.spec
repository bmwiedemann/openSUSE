#
# spec file for package lua-dkjson
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
%define mod_name dkjson
%define uptag    release_2_5
Version:        2.5.2
Release:        0
Summary:        David Kolf's JSON module for Lua
License:        MIT
Group:          Development/Libraries/Other
URL:            http://dkjson.org/
Source:         http://dkolf.de/src/dkjson-lua.fsl/tarball/%{uptag}/dkjson.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
Requires:       %{flavor}-lpeg
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-dkjson
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-dkjson
%endif

%description
dkjson is a module for encoding and decoding JSON data. It
supports UTF-8.

JSON (JavaScript Object Notation) is a format for serializing
data based on the syntax for JavaScript data structures.

dkjson is written in Lua without any dependencies, but
when LPeg is available dkjson can use it to speed up decoding.

%prep
%setup -q -n %{uptag}/%{mod_name}

%build
/bin/true

%install
install -D -m 0644 -t %{buildroot}%{lua_noarchdir} -p dkjson.lua

%check
lua%{lua_version} speedtest.lua dkjson
lua%{lua_version} jsontest.lua

%files
# license is included in readme.txt file
%doc versions.txt readme.txt
%{lua_noarchdir}/%{mod_name}*

%changelog
