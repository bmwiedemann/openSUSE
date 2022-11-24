#
# spec file for package lua-markdown
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
%define mod_name markdown
%define upversion 0.33
Version:        0.331
Release:        0
Summary:        Markdown text-to-html markup system
License:        MIT
URL:            https://github.com/mpeterv/markdown
Source:         https://github.com/mpeterv/markdown/archive/%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
A pure-lua implementation of the Markdown text-to-html markup system.

%prep
%setup -q -n %{mod_name}-%{upversion}
sed -i '\|%{_bindir}/env |d' markdown.lua

%build
/bin/true

%install
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} markdown.lua

%check
lua%{lua_version} markdown-tests.lua

%files
%license LICENSE
%doc README.md
%{lua_noarchdir}/markdown*

%changelog
