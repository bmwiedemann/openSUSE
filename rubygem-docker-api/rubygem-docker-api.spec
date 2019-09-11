#
# spec file for package rubygem-docker-api
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


Name:           rubygem-docker-api
Version:        1.13.2
Release:        0
%define mod_name docker-api
%define mod_full_name %{mod_name}-%{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 3
Url:            https://github.com/swipely/docker-api
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        A simple REST client for the Docker Remote API
License:        MIT
Group:          Development/Languages/Ruby

%description
A simple REST client for the Docker Remote API.

%package doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}

%description doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%package testsuite
Summary:        Test suite for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}

%description testsuite
Test::Unit or RSpec files, useful for developers.

%prep
#gem_unpack
#if you need patches, apply them here and replace the # with a % sign in the surrounding lines
#gem_build

%build

%install
%gem_install -f
mkdir -p %{buildroot}%{_docdir}/%{name}
ln -s %{gem_base}/gems/%{mod_full_name}/README.md %buildroot/%{_docdir}/%{name}/README.md

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}
%{gem_base}/cache/%{mod_full_name}.gem
%{gem_base}/gems/%{mod_full_name}/
%exclude %{gem_base}/gems/%{mod_full_name}/spec
%{gem_base}/specifications/%{mod_full_name}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gem_base}/doc

%files testsuite
%defattr(-,root,root,-)
%{gem_base}/gems/%{mod_full_name}/spec

%changelog
