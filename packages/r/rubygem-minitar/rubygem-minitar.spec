#
# spec file for package rubygem-minitar
#
# Copyright (c) 2021 SUSE LLC
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

Name:           rubygem-minitar
Version:        0.9
Release:        0
%define mod_name minitar
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 1.8}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/halostatue/minitar/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        The minitar library is a pure-Ruby library that provides the ability
License:        Ruby
Group:          Development/Languages/Ruby

%description
The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.
This is release 0.9, adding a minor feature to Minitar.unpack and
Minitar::Input#extract_entry that when <tt>:fsync => false</tt> is provided,
fsync will be skipped.
minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernández Pradier for the rpa-base
project.

%prep

%build

%install
%gem_install \
  --doc-files="History.md Licence.md README.rdoc" \
  -f

%gem_packages

%changelog
