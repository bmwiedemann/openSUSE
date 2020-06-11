#
# spec file for package rubygem-nokogiri
#
# Copyright (c) 2020 SUSE LLC
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

Name:           rubygem-nokogiri
Version:        1.10.9
Release:        0
%define mod_name nokogiri
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby25 ruby26
%define rb_build_ruby_abis ruby:2.5.0 ruby:2.6.0
%endif
BuildRequires:  %{rubygem pkg-config}
BuildRequires:  libxml2-devel >= 2.6.21
BuildRequires:  libxslt-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 2.3.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://nokogiri.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-nokogiri-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among
Nokogiri's many features is the ability to search documents via XPath
or CSS3 selectors.

%prep


%build

%install
# MANUAL
%gem_unpack
#########################################################################
#
# IMPORTANT!
#
# This is not covered by our gem2rpm automation yet. If you see it removed
# in the diff please add it back
#
# IMPORTANT!
#
#########################################################################
sed -i -e 's/.*mini_portile.*//g' %{mod_full_name}.gemspec
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build
export NOKOGIRI_USE_SYSTEM_LIBRARIES=1
# /MANUAL
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.md README.md" \
  -f
%gem_cleanup
# MANUAL
rm -rvf %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_full_name}/ports
# /MANUAL

%gem_packages

%changelog
