#
# spec file for package shells-cli
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


Name:           shells-cli
Version:        0~20210507
Release:        0
Summary:        Shells.com command line interface
License:        MIT
URL:            https://github.com/Shells-com/shells-cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.16
%go_nostrip
%go_provides

%description
Command line tool for interacting with the Shells.com backend system.

%prep
%autosetup -a 1

%build
%goprep github.com/Shells-com/shells-cli
%gobuild .

%install
%goinstall

%check
%gotest github.com/Shells-com/shells-cli

%files
%license LICENSE
%{_bindir}/shells-cli

%changelog
