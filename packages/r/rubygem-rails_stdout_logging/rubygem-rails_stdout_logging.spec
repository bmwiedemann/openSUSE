#
# spec file for package rubygem-rails_stdout_logging
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-rails_stdout_logging
Version:        0.0.5
Release:        0
%define mod_name rails_stdout_logging
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/heroku/rails_stdout_logging
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Overrides Rails' built in logger to send all logs to stdout
License:        MIT
Group:          Development/Languages/Ruby

%description
Sets Rails to log to stdout.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
