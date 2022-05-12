#
# spec file for package seidl
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


Name:           seidl
Summary:        Complementary light pint client
Url:            https://github.com/grisu48/seidl
Version:        0.1
Release:        0
License:        MIT
Group:          Metapackages
Source:         seidl-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  go >= 1.14

%description
seidl is a lightweight pint query utility designed for easy usage. It displays the current SUSE publiccloud images according to customizable filter rules.

In aims at complementing the public-cloud-info-client by the feature to display all current not-deleted and not-deprecated images in a nice table on the console.


%prep
%autosetup -D

%build
make seidl

%install
install -D -m 0755 seidl "%{buildroot}/%{_bindir}/seidl"

%fdupes %{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/seidl

%changelog
