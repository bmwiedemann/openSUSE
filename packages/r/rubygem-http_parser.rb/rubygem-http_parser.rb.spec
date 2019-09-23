#
# spec file for package rubygem-http_parser.rb
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-http_parser.rb
Version:        0.6.0
Release:        0
%define mod_name http_parser.rb
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
Url:            http://github.com/tmm1/http_parser.rb
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Simple callback-based HTTP request/response parser
License:        MIT
Group:          Development/Languages/Ruby

%description
Ruby bindings to http://github.com/ry/http-parser and
http://github.com/a2800276/http-parser.java.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE-MIT README.md" \
  -f
%gem_cleanup
# MANUAL
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name .gitmodules -print -delete
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name .gitkeep -print -delete
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name .gitignore -print -delete
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name \*.jar -print -delete
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version} -name '*.[h|c|o]' -print -delete
# /MANUAL

%gem_packages

%changelog
