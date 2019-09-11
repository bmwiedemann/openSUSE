#
# spec file for package rubygem-abstract
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


Name:           rubygem-abstract
Version:        1.0.0
Release:        0
%define mod_name abstract
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://rubyforge.org/projects/abstract
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        a library which enable you to define abstract method in Ruby
License:        Ruby
Group:          Development/Languages/Ruby

%description
'abstract.rb' is a library which enable you to define abstract method in Ruby.

%prep

%build

%install
%gem_install \
  --doc-files="ChangeLog README.txt" \
  -f

%gem_packages

%changelog
