#
# spec file for package xmlformat
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


Name:           xmlformat
Version:        1.9
Release:        0
Summary:        XML document formatter
License:        BSD-3-Clause AND GPL-3.0-only
Group:          Productivity/Publishing/XML
URL:            https://github.com/someth2say/xmlformat
Source0:        https://github.com/someth2say/xmlformat/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  ruby
BuildRequires:  shunit2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%description
xmlformat is a configurable formatter (or "pretty-printer") for XML
documents. It provides control over indentation, line-breaking, and text
wrapping. These properties can be defined on a per-element basis.

xmlformat provides improved diagnostic information when a document is not
well-formed. (Prints line and token number, and stack trace).

Based on Kitebird's original implementation v1.04

%prep
%setup -q

%build
# --

%install
install -Dpm 0755 bin/xmlformat.pl  %{buildroot}%{_bindir}/xmlformat.pl
install -Dpm 0755 bin/xmlformat.rb  %{buildroot}%{_bindir}/xmlformat.rb
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/xmlformat %{buildroot}/%{_bindir}/xmlformat

%check
(cd test; ./test.sh )

%post
%{_sbindir}/update-alternatives --install %{_bindir}/xmlformat xmlformat %{_bindir}/xmlformat.rb 10
%{_sbindir}/update-alternatives --install %{_bindir}/xmlformat xmlformat %{_bindir}/xmlformat.pl 20

%postun
if [ ! -f %{_bindir}/xmlformat ] ; then
   update-alternatives --remove xmlformat %{_bindir}/xmlformat
fi

%files
%doc README.md *.html
%doc bin/xmlformat.conf
%license LICENSE.txt
%{_bindir}/xmlformat*
%ghost %_sysconfdir/alternatives/xmlformat

%changelog
