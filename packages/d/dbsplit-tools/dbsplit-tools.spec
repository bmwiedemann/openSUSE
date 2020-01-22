#
# spec file for package dbsplit-tools
#
# Copyright (c) 2020 SUSE LLC
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


Name:           dbsplit-tools
Version:        0.6
Release:        0
Summary:        DocBook Splitting tools
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/DocBook
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-utf8.diff
Patch1:         %{name}-%{version}-license.diff
Patch2:         %{name}-%{version}-contact.diff
Requires:       perl-XML-DOM
Requires:       perl-XML-RegExp
BuildArch:      noarch

%description
Tools for splitting and merging DocBook documents,

%prep
%autosetup -p0

%build

%install
%make_install PREFIX=%{buildroot}/%{_prefix}

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/*
%{_mandir}/man?/*

%changelog
