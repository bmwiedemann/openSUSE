#
# spec file for package yast2-widget-demo
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


Name:           yast2-widget-demo
Version:        0.9.1
Release:        0
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Requires:       yast2
Requires:       yast2-ruby-bindings

BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-ruby-bindings
# for the install task
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# for tests
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)

Summary:        YaST2 - widget demo
License:        GPL-2.0-only OR GPL-3.0-only

%description
A YaST2 module to demonstrate the UI widgets and for style sheet testing


%prep
%setup -n %{name}-%{version}

%check
rake test:unit

%build

%install
# No .desktop file here, so we can't use %yast_install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%{yast_clientdir}
%{yast_libdir}
%{yast_docdir}
%license COPYING

%changelog
