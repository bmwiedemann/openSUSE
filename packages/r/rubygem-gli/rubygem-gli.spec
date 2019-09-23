#
# spec file for package rubygem-gli
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-gli
Version:        2.13.1
Release:        0
%define mod_name gli
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            http://davetron5000.github.com/gli
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Build command-suite CLI apps that are awesome
License:        Apache-2.0
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Build command-suite CLI apps that are awesome.  Bootstrap your app, add
commands, options and documentation while maintaining a well-tested idiomatic
command-line app.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.txt README.rdoc" \
  -f

%gem_packages

%changelog
