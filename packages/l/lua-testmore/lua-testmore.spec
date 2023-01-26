#
# spec file
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
%define mod_name testmore
Version:        0.3.6+git2
Release:        0
Summary:        A Lua port of the Perl Test::More unit testing framework
License:        MIT
Group:          Development/Languages/Other
URL:            https://framagit.org/fperrad/lua-TestMore
Source:         lua-TestMore-%{version}.tar.xz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
BuildArch:      noarch

%description
lua-TestMore is a port of the Perl5 module Test::More. It uses the
Test Anything Protocol as output, that allows a compatibility with
the Perl QA ecosystem. It's an extensible framework.
See lua-TestAssertion an extension which provides many Lua friendly
assertions. It allows a simple and efficient way to write tests
(without OO style). Some tests could be marked as TODO or skipped.
Errors could be fully checked with error_like().

%prep
%autosetup -n lua-TestMore-%{version}

%build

%install
%make_install LUAVER="%{lua_version}" PREFIX=/usr

%check
make check

%files
%license COPYRIGHT
%doc README.md CHANGES
%{lua_noarchdir}

%changelog
