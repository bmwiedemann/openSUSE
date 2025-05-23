#
# spec file for package rubygem-sexp_processor
#
# Copyright (c) 2024 SUSE LLC
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-sexp_processor
Version:        4.17.2
Release:        0
%define mod_name sexp_processor
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby < 4}
BuildRequires:  %{ruby >= 2.6}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/seattlerb/sexp_processor
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        sexp_processor branches from ParseTree bringing all the generic sexp
License:        MIT

%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.

%prep

%build

%install
%gem_install \
  --doc-files="History.rdoc README.rdoc" \
  -f
# MANUAL
perl -p -i -e 's|#!\S+|#!/usr/bin/ruby|g' %{buildroot}%{_libdir}/*/gems/*/gems/%{mod_full_name}/test/*
# /MANUAL

%gem_packages

%changelog
