#
# spec file for package lua-luasocket
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define flavor lua
%define mod_name luasocket
Name:           %{flavor}-%{mod_name}
Version:        3.0~rc1+git20170515.5a17f79
Release:        0
Summary:        Network support for the Lua language
License:        MIT
Group:          Development/Languages/Other
Url:            https://github.com/diegonehab/luasocket
Source:         %{mod_name}-%{version}.tar.xz
Patch0:         luasocket-makefile.patch
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
%if "%{flavor}" == "lua53"
Provides:       luasocket = %{version}
Obsoletes:      luasocket < %{version}
%endif
%if "%{flavor}" == "lua"
ExclusiveArch:  do_not_build
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
%doc doc/*
%doc README
%{lua_archdir}/mime
%{lua_archdir}/socket
%{lua_noarchdir}/ltn12.lua
%{lua_noarchdir}/mime.lua
%{lua_noarchdir}/socket.lua
%{lua_noarchdir}/socket/

%files devel
%{lua_incdir}/*.h

%changelog
