#
# spec file for package xmlformat
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xmlformat
Version:        1.04
Release:        0
Summary:        XML document formatter
License:        BSD-3-Clause
Group:          Productivity/Publishing/XML
URL:            http://www.kitebird.com/software/xmlformat/
Source0:        http://www.kitebird.com/software/xmlformat/%{name}-%{version}.tar.bz2
BuildRequires:  perl
BuildArch:      noarch

%description
xmlformat is a configurable formatter (or "pretty-printer") for XML
documents. It provides control over indentation, line-breaking, and text
wrapping. These properties can be defined on a per-element basis.

xmlformat provides improved diagnostic information when a document is not
well-formed. (Prints line and token number, and stack trace).

%prep
%setup -q

%build

%install
install -Dpm 0755 xmlformat.pl  \
  %{buildroot}%{_bindir}/xmlformat.pl
install -Dpm 0755 xmlformat.rb  \
  %{buildroot}%{_bindir}/xmlformat.rb

%files
%doc BUGS ChangeLog INSTALL LICENSE README TODO
%doc bad* test.conf
%doc docs tests
%{_bindir}/xmlformat.*

%changelog
