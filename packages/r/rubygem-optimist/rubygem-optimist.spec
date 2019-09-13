#
# spec file for package rubygem-optimist
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

Name:           rubygem-optimist
Version:        3.0.0
Release:        0
%define mod_name optimist
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://manageiq.github.io/optimist/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Optimist is a commandline option parser for Ruby that just gets out
License:        MIT
Group:          Development/Languages/Ruby

%description
Optimist is a commandline option parser for Ruby that just
gets out of your way. One line of code per option is all you need to write.
For that, you get a nice automatically-generated help page, robust option
parsing, command subcompletion, and sensible defaults for everything you don't
specify.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt README.md" \
  -f

%gem_packages

%changelog
