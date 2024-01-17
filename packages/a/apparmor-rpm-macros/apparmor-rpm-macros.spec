#
# spec file for package apparmor-rpm-macros
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


Name:           apparmor-rpm-macros
Version:        1.0
Release:        0
Summary:        RPM macros used to setup apparmor profiles
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://bugs.launchpad.net/apparmor
Source:         macros.apparmor
Requires:       coreutils
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define  macrodir /usr/lib/rpm/macros.d

%description
Package that provides RPM macros used to setup apparmor profiles for packaging.

%prep

%build

%install
mkdir -p %{buildroot}%{macrodir}
install -m644 %{S:0} %{buildroot}%{macrodir}/

%files
%defattr(-,root,root)
%{macrodir}/macros.apparmor

%changelog
