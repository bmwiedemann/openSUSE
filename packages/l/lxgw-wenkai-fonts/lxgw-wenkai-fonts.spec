#
# spec file for package lxgw-wenkai-fonts
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


Name:           lxgw-wenkai-fonts
Version:        1.300
Release:        0
Summary:        An open-source Chinese font derived from Fontworks' Klee One.
License:        OFL-1.1
URL:            https://github.com/lxgw/LxgwWenKai
Source0:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/lxgw-wenkai-v%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%description
An open-source Chinese font derived from Fontworks' Klee One.

%prep
%setup -q -n lxgw-wenkai-v%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c

%files
%license License.txt
%{_ttfontsdir}

%changelog
