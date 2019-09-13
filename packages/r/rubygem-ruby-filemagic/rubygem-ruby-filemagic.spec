#
# spec file for package rubygem-ruby-filemagic
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-ruby-filemagic
Version:        0.7.2
Release:        0
%define mod_name ruby-filemagic
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires: file-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 1.9.3}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
Url:            http://github.com/blackwinter/ruby-filemagic
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-ruby-filemagic-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Ruby bindings to the magic(4) library
License:        Ruby
Group:          Development/Languages/Ruby

%description
Ruby bindings to the magic(4) library.

%prep

%build

%install
%gem_install \
  --doc-files="ChangeLog README" \
  -f
%gem_cleanup
# MANUAL
rm %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_full_name}/test/pylink
# /MANUAL


%gem_packages

%changelog
