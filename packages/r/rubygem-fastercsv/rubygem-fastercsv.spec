#
# spec file for package rubygem-fastercsv
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-fastercsv
Version:        1.5.5
Release:        0
%define mod_name fastercsv
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  fdupes
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://fastercsv.rubyforge.org
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        FasterCSV is CSV, but faster, smaller, and cleaner
License:        GPL-2.0 or Ruby
Group:          Development/Languages/Ruby

%description
FasterCSV is intended as a complete replacement to the CSV standard library.
It
is significantly faster and smaller while still being pure Ruby code. It also
strives for a better interface.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING README CHANGELOG LICENSE" \
  -f
# MANUAL
%fdupes %{buildroot}%{_libdir}/ruby/gems/*/doc/%{mod_name}-%{version}

find %{buildroot}%{_libdir}/ruby/gems/ -name *.rb | xargs sed -i -e 's,/usr/local/bin/ruby,/usr/bin/ruby,'
# /MANUAL

%gem_packages

%changelog
