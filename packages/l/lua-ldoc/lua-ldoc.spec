#
# spec file for package lua-ldoc
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
%define mod_name ldoc
%define rname LDoc
Version:        1.4.6
Release:        0
Summary:        LuaDoc-compatible documentation generation system
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/stevedonovan/LDoc
Source:         https://github.com/stevedonovan/LDoc/archive/%{version}.tar.gz#/%{rname}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-ldoc
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-ldoc
%endif

%description
LDoc is a LuaDoc-compatible documentation generator which can
also process C extension source. Markdown may be optionally used
to render comments, as well as integrated readme documentation
and pretty-printed example files.

%prep
%setup -q -n %{rname}-%{version}

%build
/bin/true

%install
mkdir -v -p %{buildroot}%{lua_noarchdir}/ldoc
cp -v -r -p ldoc %{buildroot}%{lua_noarchdir}

%files
%dir %{lua_noarchdir}/ldoc
%{lua_noarchdir}/ldoc*

%changelog
