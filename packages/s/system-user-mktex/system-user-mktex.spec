#
# spec file for package system-user-mktex
#
# Copyright (c) 2021 SUSE LLC
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


Name:           system-user-mktex
Version:        1.0.0
Release:        0
License:        MIT
Summary:        System user and group 'mktex'
Group:          Productivity/Publishing/TeX/Base
Source0:        system-user-mktex.conf
BuildRequires:  sysuser-tools
BuildArch:      noarch
%if 0%{?suse_version} < 1550
Provides:       group(mktex)
%endif
%sysusers_requires

%description
This package provides a shared system user for TeXLive

%prep
%setup -q -c -T

%build
%sysusers_generate_pre %{SOURCE0} system-user-mktex system-user-mktex.conf

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_sysusersdir}/system-user-mktex.conf

%pre -f system-user-mktex.pre

%files
%{_sysusersdir}/system-user-mktex.conf

%changelog
