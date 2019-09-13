#
# spec file for package rubygem-log4r
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           rubygem-log4r
Version:        1.1.10
Release:        0
%define mod_name log4r
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://log4r.rubyforge.org
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Log4r, logging framework for ruby
License:        GPL-2.0+ or Ruby
Group:          Development/Languages/Ruby

%description
See also: http://logging.apache.org/log4j.

%prep

%build

%install
%gem_install \
  -f

%gem_packages

%changelog
