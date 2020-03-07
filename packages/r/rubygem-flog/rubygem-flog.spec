#
# spec file for package rubygem-flog
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-flog
Version:        4.6.4
Release:        0
%define mod_name flog
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://ruby.sadi.st/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Flog reports the most tortured code in an easy to read pain report
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Flog reports the most tortured code in an easy to read pain
report. The higher the score, the more pain the code is in.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc README.rdoc" \
  -f
# MANUAL
perl -p -i -e 's|#!\S+|#!/usr/bin/ruby|g' %{buildroot}%{_libdir}/*/gems/*/gems/%{mod_full_name}/bin/flog
# /MANUAL

%gem_packages

%changelog
