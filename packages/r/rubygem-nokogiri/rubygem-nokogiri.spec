#
# spec file for package rubygem-nokogiri
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.16.7
Release:        0
%define mod_name nokogiri
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  %{rubygem mini_portile2 >= 2.8.2}
BuildRequires:  %{rubygem openssl}
BuildRequires:  %{rubygem pkg-config}
BuildRequires:  libxml2-devel >= 2.6.21
BuildRequires:  libxslt-devel
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 3.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  update-alternatives
URL:            https://nokogiri.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-nokogiri-rpmlintrc
Source2:        gem2rpm.yml
# MANUAL
Patch0:         only-complain-about-version-diff-if-it-is-older.patch
# /MANUAL
Summary:        Nokogiri (鋸) makes it easy and painless to work with XML and HTML
License:        MIT

%description
Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby.
It provides a
sensible, easy-to-understand API for reading, writing, modifying, and querying
documents. It is
fast and standards-compliant by relying on native parsers like libxml2,
libgumbo, or xerces.

%prep
%gem_unpack
%patch -P 0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
# MANUAL
%gem_unpack
perl -p -i.back -e 's/.*mini_portile.*//g' %{mod_full_name}.gemspec
diff -urN %{mod_full_name}.gemspec{.back,} ||:
rm -f %{mod_full_name}.gemspec.back

MINI_PORTILE2_VERSION="2.8.2"

if grep -q "~> ${MINI_PORTILE2_VERSION}" ext/nokogiri/extconf.rb ; then
  perl -p -i.back -e 's/~> ${MINI_PORTILE2_VERSION}/>= ${MINI_PORTILE2_VERSION}/g' ext/nokogiri/extconf.rb
  diff -urN ext/nokogiri/extconf.rb{.back,} ||:
  rm -f ext/nokogiri/extconf.rb.back
else
  echo "Check which version of mini_portile2 we need to build nokogiri now"
  exit 1
fi
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build
cd ..
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
