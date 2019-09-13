#
# spec file for package patterns-openSUSE
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


%bcond_with betatest

Name:           patterns-devel-ruby
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Ruby devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Ruby development pattern.

################################################################################

%package devel_ruby
%pattern_development
Summary:        Ruby Development
Group:          Metapackages
Provides:       pattern() = devel_ruby
Provides:       pattern-icon() = pattern-ruby-devel
Provides:       pattern-order() = 3420
Provides:       pattern-visible()

Requires:       ruby
Requires:       rubygems
Suggests:       ruby-devel
Suggests:       ruby-doc-html
Suggests:       ruby-doc-ri
Suggests:       ruby-examples
Suggests:       rubygem-mysql
Suggests:       rubygem-racc
Suggests:       rubygem-ruby-fcgi
Suggests:       ruby-test-suite
Suggests:       ruby-tk

%description devel_ruby
Tools and libraries for software development using the Ruby programming language.

%files devel_ruby
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_ruby.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/
echo 'This file marks the pattern devel_ruby to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/devel_ruby.txt

