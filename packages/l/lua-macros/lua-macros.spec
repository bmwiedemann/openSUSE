#
# spec file for package lua-macros
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           lua-macros
Version:        20170611
Release:        0
Summary:        Macros for lua language
License:        MIT
Group:          Development/Languages/Other
Url:            http://www.lua.org
Source0:        macros.lua
Requires:       lua
BuildArch:      noarch

%description
RPM macros for lua packaging

%prep
:

%build
:

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_libexecdir}/rpm/macros.d/macros.lua

%files
%{_libexecdir}/rpm/macros.d/macros.lua

%changelog
