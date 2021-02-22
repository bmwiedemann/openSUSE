#
# spec file for package nginx-macros
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


Name:           nginx-macros
Version:        0.0.1
Release:        0
Summary:        Just some macros to make packaging nginx and modules easier
License:        BSD-2-Clause
Group:          Productivity/Networking/Web/Proxy
URL:            https://nordisch.org
Source0:        nginx.macros
BuildArch:      noarch

%description
Just some macros to make packaging nginx and modules easier.

%prep

%build

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.nginx

%files
%{_rpmmacrodir}/macros.nginx

%changelog
