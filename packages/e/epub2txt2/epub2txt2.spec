#
# spec file for package epub2txt2
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


%global _commit_hash ac4e73fa79202ccc106b36c06c20e36c37345a58

Name:           epub2txt2
Version:        2.06
Release:        0
Summary:        Simple command-line utility for extracting text from EPUB documents
License:        GPL-3.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/kevinboone/epub2txt2
Source0:        https://github.com/kevinboone/epub2txt2/archive/%{_commit_hash}.tar.gz
Patch0:         54b41e87156bc823d5938749d71c4c57adc75b1b.patch
BuildRequires:  gcc
BuildRequires:  make
Requires:       unzip

%description
Simple command-line utility for extracting text from EPUB documents

%prep
%autosetup -n %{name}-%{_commit_hash} -p1

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/epub2txt
%{_mandir}/man1/epub2txt.1%{?ext_man}

%changelog
