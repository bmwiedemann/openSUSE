#
# spec file for package gron
#
# Copyright (c) 2022, Martin Hauke <mardnh@gmx.de>
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

Name:           gron
Version:        0.7.1
Release:        0
Summary:        Make JSON greppable
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/tomnomnom/gron
#Git-Clone:     https://github.com/tomnomnom/gron.git
Source:         https://github.com/tomnomnom/gron/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging
%{go_provides}

%description
gron transforms JSON into discrete assignments to make it easier
to grep for what you want and see the absolute 'path' to it. It
eases the exploration of APIs that return large blobs of JSON but
have terrible documentation.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} github.com/tomnomnom/gron
%{gobuild} -mod=vendor .

%install
%{goinstall}

%files
%license LICENSE
%doc ADVANCED.mkd CHANGELOG.mkd CONTRIBUTING.mkd README.mkd
%{_bindir}/gron

%changelog
