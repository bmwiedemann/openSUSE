#
# spec file for package lua-macros
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


%if %{undefined _rpmmacrodir}
%define _rpmmacrodir %{_rpmconfigdir}/macros.d
%endif
Name:           lua-macros
Version:        20210827
Release:        0
Summary:        Macros for lua language
License:        MIT
Group:          Development/Languages/Other
URL:            https://www.lua.org
Source0:        macros.lua
Source1:        install-lua-rock.sh
%if 0%{?suse_version} > 1600
Requires:       lua-interpreter
%elif 0%{?suse_version} >= 1500
# on SLE 12 lua is lua5.2 unconditionally, avoid
Requires:       lua
%endif
Requires:       pkgconfig
BuildArch:      noarch

%description
RPM macros for lua packaging

%prep
cp -p %{SOURCE0} .

%build
:

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.lua
install -Dm755 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/install-lua-rock.sh

%files
%{_rpmmacrodir}/macros.lua
%{_rpmconfigdir}/install-lua-rock.sh

%changelog
