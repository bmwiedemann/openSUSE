#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define mod_name luasocket
Version:        3.1.0
Release:        0
Summary:        Network support for the Lua language
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/lunarmodules/luasocket
Source:         %{mod_name}-%{version}.tar.xz
Patch0:         luasocket-makefile.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
%lua_provides
%lua_provides -e
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
Recommends:     %{flavor}-%{mod_name}-doc
%endif

%description
LuaSocket is a Lua extension library that is composed by two parts: a C core
that provides support for the TCP and UDP transport layers, and a set of Lua
modules that add support for functionality commonly needed by applications
that deal with the Internet.

Among the support modules, the most commonly used implement the SMTP, HTTP
and FTP. In addition there are modules for MIME, URL handling and LTN12.

%package devel
Summary:        Header files for %{flavor}-%{mod_name}
Group:          Development/Languages/Other
Requires:       %{flavor}-%{mod_name} = %{version}

%description devel
This subpackage contains header files for developing applications that
want to make use of %{flavor}-%{mod_name}.

%package doc
Summary:        Documentation for %{flavor}-%{mod_name}
Group:          Development/Languages/Other
BuildArch:      noarch

%description doc
This subpackage contains documentation for %{flavor}-%{mod_name}.

%prep
%setup -q -n %{mod_name}-%{version}
%patch0 -p1

%build
%{_bindir}/iconv -f ISO8859-1 -t UTF8 LICENSE >LICENSE.UTF8
mv -f LICENSE.UTF8 LICENSE
make %{?_smp_mflags} OPTFLAGS="%{optflags} -fPIC -I%{lua_incdir}" linux

%install
make install-unix OPTFLAGS="%{optflags}" INSTALL_TOP=%{buildroot} INSTALL_TOP_CDIR=%{buildroot}%{lua_archdir} INSTALL_TOP_LDIR=%{buildroot}%{lua_noarchdir}

# install development files
install -d %{buildroot}%{lua_incdir}
install -p -m 0644 src/*.h %{buildroot}%{lua_incdir}

%files
%license LICENSE
%{lua_archdir}/mime
%{lua_archdir}/socket
%{lua_noarchdir}/ltn12.lua
%{lua_noarchdir}/mime.lua
%{lua_noarchdir}/socket.lua
%{lua_noarchdir}/socket/

%files devel
%dir %{lua_incdir}
%{lua_incdir}/*.h

%files doc
%doc docs/*
%doc README.md

%changelog
