#
# spec file for package rubygem-fast_xs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-fast_xs
Version:        0.8.0
Release:        0
%define mod_name fast_xs
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
Url:            http://fast-xs.rubyforge.org/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-fast_xs-rpmlintrc
Source2:        gem2rpm.yml
Summary:        fast_xs provides C extensions for escaping text
License:        MIT
Group:          Development/Languages/Ruby

%description
fast_xs provides C extensions for escaping text.
The original String#fast_xs method is based on the xchar code by Sam Ruby:
* http://intertwingly.net/stories/2005/09/28/xchar.rb
* http://intertwingly.net/blog/2005/09/28/XML-Cleansing
_why also packages an older version with Hpricot (patches submitted).
The version here should be compatible with the latest version of Hpricot
code.
Ruby on Rails will automatically use String#fast_xs from either Hpricot
or this gem version with the bundled Builder package.
String#fast_xs is an almost exact translation of Sam Ruby's original
implementation (String#to_xs), but it does escape "&quot;" (which is an
optional, but all parsers are able ot handle it.  XML::Builder as
packaged in Rails 2.0 will be automatically use String#fast_xs instead
of String#to_xs available.

%prep

%build

%install
%gem_install \
  --doc-files="History.rdoc README.rdoc" \
  -f
%gem_cleanup

%gem_packages

%changelog
