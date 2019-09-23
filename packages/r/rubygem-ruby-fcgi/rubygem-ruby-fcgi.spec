#
# spec file for package rubygem-ruby-fcgi
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


Name:           rubygem-ruby-fcgi
Version:        0.8.9
Release:        0
%define mod_name ruby-fcgi
%define mod_full_name %{mod_name}-%{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-devel
BuildRequires:  ruby-macros >= 3
BuildRequires:  rubygem(rdoc) > 3.10
Url:            http://github.com/saks/fcgi
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        FastCGI library for Ruby
License:        MIT
Group:          Development/Languages/Ruby
# MANUAL
BuildRequires:  FastCGI-devel
Provides:       %{mod_name} = %{version}-%{release}
Obsoletes:      %{mod_name} < %{version}

%description
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific APIs. For
more information, see http://www.fastcgi.com/. This is the fork of fcgi
implementation for ruby but with ruby1.9 - ruby1.9.1 compability

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
%gem_cleanup
mkdir -p %{buildroot}%{_docdir}/%{name}
ln -s %{gem_base}/gems/%{mod_full_name}/ChangeLog %buildroot/%{_docdir}/%{name}/ChangeLog
ln -s %{gem_base}/gems/%{mod_full_name}/LICENSE %buildroot/%{_docdir}/%{name}/LICENSE
ln -s %{gem_base}/gems/%{mod_full_name}/README %buildroot/%{_docdir}/%{name}/README
ln -s %{gem_base}/gems/%{mod_full_name}/README.rdoc %buildroot/%{_docdir}/%{name}/README.rdoc
# MANUAL
find %{buildroot}%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/ -type f -perm +111 -print0 | xargs -r0 chmod -v a-x

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}
%{gem_base}/cache/%{mod_full_name}.gem
%{gem_base}/gems/%{mod_full_name}/
%{gem_extensions}/%{mod_full_name}
%exclude %{gem_base}/gems/%{mod_full_name}/test
%{gem_base}/specifications/%{mod_full_name}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gem_base}/doc

%files testsuite
%defattr(-,root,root,-)
%{gem_base}/gems/%{mod_full_name}/test

%changelog
