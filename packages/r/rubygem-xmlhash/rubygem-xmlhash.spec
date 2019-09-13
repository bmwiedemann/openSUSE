#
# spec file for package rubygem-xmlhash
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-xmlhash
Version:        1.3.7
Release:        0
%define mod_name xmlhash
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  %{rubygem hoe}
BuildRequires:  %{rubygem pkg-config}
BuildRequires:  %{rubygem rake-compiler}
BuildRequires:  %{rubygem rake}
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/coolo/xmlhash
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Xmlhash is a naive form of XML::Simple
License:        MIT
Group:          Development/Languages/Ruby

%description
A small C module that wraps libxml2's xmlreader to parse a XML
string into a ruby hash.

%prep

%build

%install
%gem_install \
  --doc-files="History.txt README.txt" \
  -f
%gem_cleanup

%gem_packages

%changelog
