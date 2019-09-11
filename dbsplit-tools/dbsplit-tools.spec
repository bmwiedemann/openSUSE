#
# spec file for package dbsplit-tools
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           dbsplit-tools
Group:          Productivity/Publishing/DocBook
BuildArch:      noarch
Requires:       perl-XML-DOM perl-XML-RegExp
Version:        0.6
Release:        119
License:        GPL-2.0+
Source0:        %name-%version.tar.bz2
Patch:          %name-%version-utf8.diff
Patch1:         %name-%version-license.diff
Patch2:         %name-%version-contact.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        DocBook Splitting tools

%description
Tools for splitting and merging DocBook documents,



%prep
%setup -q
%patch
%patch1
%patch2

%build

%install
make install PREFIX=%buildroot/%_prefix

%files
%defattr(-, root, root)
%doc README AUTHORS COPYING
%{_bindir}/*
%{_mandir}/man?/*

%changelog
