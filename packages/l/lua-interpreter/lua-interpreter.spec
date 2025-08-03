#
# spec file for package lua-interpreter
#
# Copyright (c) 2025 SUSE LLC
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

Name:           lua-interpreter
Version:        5
Release:        0
Summary:        Shared superstructure for Lua interpreters
License:        MIT
URL:            https://www.lua.org/
Source99:       lua-interpreter.rpmlintrc
BuildRequires:  alts
Requires:       alts
BuildArch:      noarch

%description
Shared package owning resources shared among Lua interpreters.

%prep
true

%build
:

%install
mkdir -p %{buildroot}%{_bindir}
ln -s -f %{_bindir}/alts %{buildroot}%{_bindir}/lua
ln -s -f %{_bindir}/alts %{buildroot}%{_bindir}/luac

# alternatives - create libalternatives configuration directory
mkdir -p %{buildroot}%{_datadir}/libalternatives/lua
mkdir -p %{buildroot}%{_datadir}/libalternatives/luac

%files
%{_bindir}/lua
%{_bindir}/luac
%{_datadir}/libalternatives/lua
%{_datadir}/libalternatives/luac

%changelog
