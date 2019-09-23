#
# spec file for package rubygem-jaro_winkler
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

Name:           rubygem-jaro_winkler
Version:        1.5.3
Release:        0
%define mod_name jaro_winkler
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/tonytonyjan/jaro_winkler
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        %{name}-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string
License:        MIT
Group:          Development/Languages/Ruby

%description
jaro_winkler is an implementation of Jaro-Winkler distance algorithm which is
written in C extension and will fallback to pure Ruby version in platforms
other than MRI/KRI like JRuby or Rubinius. Both of C and Ruby implementation
support any kind of string encoding, such as UTF-8, EUC-JP, Big5, etc.
%prep

%build

%install
%gem_install \
  -f
%gem_cleanup

%gem_packages

%changelog
