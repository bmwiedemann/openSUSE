#
# spec file for package mwic
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


%{!?license: %global license %doc}
Name:           mwic
Version:        0.7.9
Release:        0
Summary:        A spellchecker with grouping support
License:        MIT
Group:          Productivity/Office/Other
URL:            http://jwilk.net/software/mwic
Source:         https://github.com/jwilk/mwic/releases/download/%{version}/mwic-%{version}.tar.gz
Source1:        https://github.com/jwilk/mwic/releases/download/%{version}/mwic-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  python3-devel >= 3.2
BuildRequires:  python3-docutils
Requires:       python3-pyenchant
Requires:       python3-regex
BuildArch:      noarch

%description
mwic is a spell-checker that groups possible misspellings and shows
them in their contexts. This is useful for checking technical
documents that often contain words that are not included in standard
dictionaries.

%prep
%setup -q

%build
sed -i '1s%^#!.*%#!/usr/bin/python3%' mwic

%install
make DESTDIR=%{buildroot} PREFIX=/usr -C doc
%{make_install} PREFIX=/usr

%files
%doc doc/changelog
%license doc/LICENSE
%{_bindir}/mwic
%{_prefix}/share/mwic
%{_mandir}/man1/mwic.1%{?ext_man}

%changelog
