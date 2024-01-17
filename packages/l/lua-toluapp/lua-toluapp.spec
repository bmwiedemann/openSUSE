#
# spec file for package lua-toluapp
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


%define flavor @BUILD_FLAVOR@
%define mod_name toluapp
%define lua_suffix %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2 |sed -e 's:\.:_:')
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%if "%{flavor}" == "lua51"
%define lua_suffix 5_1
%endif
%if "%{flavor}" == "lua52"
%define lua_suffix 5_2
%endif
%if "%{flavor}" == "lua53"
%define lua_suffix 5_3
%endif
%if "%{flavor}" == "lua54"
%define lua_suffix 5_4
%endif
Version:        1.0.93
Release:        0
Summary:        C/C++ with Lua Integration Tool
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/LuaDist/toluapp
Source:         https://github.com/LuaDist/toluapp/archive/%{version}/toluapp-%{version}.tar.gz
Patch0:         toluapp-libdir.patch
Patch1:         toluapp-versioned-shared-lib.patch
Patch2:         toluapp-build-compare.patch
Patch3:         tolua++-1.0.93-lua52.patch
Patch4:         toluapp-scons-py3.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org - scons Options() is deprecated in 0.98.1, use Variables() instead
Patch5:         scons-0.98.1-Options-deprecated.patch
#PATCH-FIX-OPENSUSE mlin@suse.com - scons env.Copy() has been deprecated, use env.Clone() instead if needed
Patch6:         toluapp-fix-deprecared-env-copy.patch
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scons >= 2.3.0
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to c++ such as:
* support for std::string as a basic type (this can be turned off by a command
  line option)
* support for class templates

%package -n toluapp-%{lua_version}
Summary:        C/C++ with Lua Integration Tool
Group:          Development/Languages/Other
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n toluapp-%{lua_version}
tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to c++ such as:
* support for std::string as a basic type (this can be turned off by a command
  line option)
* support for class templates

%package -n libtolua++-%{lua_suffix}-1
Summary:        Runtime libraries for tolua++
Group:          System/Libraries

%description -n libtolua++-%{lua_suffix}-1
This package provides shared libraries for tolua++.

%package -n libtolua++-%{lua_suffix}-devel
Summary:        Development headers for tolua++
Group:          Development/Libraries/C and C++
Requires:       toluapp-%{lua_version}
Conflicts:      otherproviders(toluapp-devel)
Provides:       toluapp-devel = %{version}

%description -n libtolua++-%{lua_suffix}-devel
This package provides development headers for tolua++.

%prep
%setup -q -n toluapp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%if "%{flavor}" != "lua51"
%patch3 -p1
%endif
sed -i "s/@SUFFIX@/%{lua_version}/" SConstruct

%build
cat <<'EOF' > config_linux.py
import re,os

CCFLAGS = re.split(r"\s+", os.environ['CCFLAGS'])
LIBS = re.split(r"\s+", os.environ['LIBS'])
prefix = "%{_prefix}"
EOF
cp config_linux.py config_posix.py

CCFLAGS="%{optflags} -fPIC -I%{lua_incdir}" \
LIBS="-llua -lm -ldl" \
scons %{?_smp_mflags} \
    prefix="%{_prefix}" \
    libdir="%{_libdir}" \
    shared=1 \
    lib bin \
    -Q CCFLAGS="%{optflags} -I%{lua_incdir} -fPIC -DDATAPATH=\\\"%{lua_noarchdir}/%{name}\\\"" \

%install
CCFLAGS="%{optflags} -fPIC -I%{lua_incdir}" \
LIBS="-llua -lm -ldl" \
scons  %{?_smp_mflags} \
    prefix="%{buildroot}%{_prefix}" \
    libdir="%{buildroot}%{_libdir}" \
    shared=1 \
    install \
    -Q CCFLAGS="%{optflags} -I%{lua_incdir} -fPIC -DDATAPATH=\\\"%{lua_noarchdir}/%{name}\\\"" \

# pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/tolua++.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
sharedlibdir=%{_libdir}
includedir=%{_includedir}

Name: tolua++
Description: C/C++ with Lua Integration Tool
Version: %{version}

Libs: -ltolua++-%{lua_version}
Cflags: -I%{_includedir}
EOF

mkdir -p %{buildroot}%{lua_noarchdir}/%{name}
install -p -m 644 src/bin/lua/*.lua %{buildroot}%{lua_noarchdir}/%{name}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/tolua++
ln -sf %{_sysconfdir}/alternatives/tolua++ %{buildroot}%{_bindir}/tolua++

%post -n libtolua++-%{lua_suffix}-1 -p /sbin/ldconfig
%postun -n libtolua++-%{lua_suffix}-1 -p /sbin/ldconfig
%post -n toluapp-%{lua_version}
/sbin/ldconfig
%{_sbindir}/update-alternatives --install %{_bindir}/tolua++ tolua++ %{_bindir}/toluapp-%{lua_version} %{lua_value}

%postun -n toluapp-%{lua_version}
/sbin/ldconfig
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove tolua++ %{_bindir}/toluapp-%{lua_version}
fi

%files -n toluapp-%{lua_version}
%doc COPYRIGHT README
%ghost %{_sysconfdir}/alternatives/tolua++
%{_bindir}/tolua++
%{_bindir}/toluapp-%{lua_version}
%{lua_noarchdir}/%{name}

%files -n libtolua++-%{lua_suffix}-devel
%{_includedir}/tolua++.h
%{_libdir}/libtolua++-%{lua_version}.so
%{_libdir}/pkgconfig/tolua++.pc

%files -n libtolua++-%{lua_suffix}-1
%{_libdir}/libtolua++-%{lua_version}.so.1
%{_libdir}/libtolua++-%{lua_version}.so.%{version}

%changelog
