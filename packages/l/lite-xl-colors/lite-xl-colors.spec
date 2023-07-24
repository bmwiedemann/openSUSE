#
# spec file for package lite-xl-colors
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

%define programname lite-xl
Name:           lite-xl-colors
Version:        git20230412.000e6aa
Release:        0
Summary:        Additional colors for %{programname}
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-colors
Source:         %{name}-%{version}.tar.gz
Requires:       lite-xl
BuildArch:      noarch

%description
Color themes for the Lite XL text editor, originally forked from the lite colors repository.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{programname}/colors
install -D -m644 colors/* %{buildroot}%{_datadir}/%{programname}/colors

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/%{programname}
%dir %{_datadir}/%{programname}/colors
%{_datadir}/%{programname}/colors/*

%changelog

