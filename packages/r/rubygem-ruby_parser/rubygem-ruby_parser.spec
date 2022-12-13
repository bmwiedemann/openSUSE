#
# spec file for package rubygem-ruby_parser
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-ruby_parser
Version:        3.19.2
Release:        0
%define mod_name ruby_parser
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby < 4}
BuildRequires:  %{ruby >= 2.1}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/seattlerb/ruby_parser
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc--which does by default use a C extension). It outputs
s-expressions which can be manipulated and converted back to ruby via
the ruby2ruby gem.
As an example:
def conditional1 arg1
return 1 if arg1 == 0
return 0
end
becomes:
s(:defn, :conditional1, s(:args, :arg1),
s(:if,
s(:call, s(:lvar, :arg1), :==, s(:lit, 0)),
s(:return, s(:lit, 1)),
nil),
s(:return, s(:lit, 0)))
Tested against 801,039 files from the latest of all rubygems (as of 2013-05):
* 1.8 parser is at 99.9739% accuracy, 3.651 sigma
* 1.9 parser is at 99.9940% accuracy, 4.013 sigma
* 2.0 parser is at 99.9939% accuracy, 4.008 sigma
* 2.6 parser is at 99.9972% accuracy, 4.191 sigma
* 3.0 parser has a 100% parse rate.
* Tested against 2,672,412 unique ruby files across 167k gems.
* As do all the others now, basically.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc README.rdoc" \
  -f
# MANUAL
perl -p -i -e 's|#!\S+|#!/usr/bin/ruby|g' %{buildroot}%{_libdir}/*/gems/*/gems/%{mod_full_name}/test/*
# /MANUAL

%gem_packages

%changelog
