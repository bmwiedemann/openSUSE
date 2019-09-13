#
# spec file for package rubygem-text-hyphen
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


Name:           rubygem-text-hyphen
Version:        1.4.1
Release:        0
%define mod_name text-hyphen
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Text::Hyphen is a Ruby library to hyphenate words in various
License:        GPL-2.0+
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Text::Hyphen is a Ruby library to hyphenate words in various languages using
Ruby-fied versions of TeX hyphenation patterns. It will properly hyphenate
various words according to the rules of the language the word is written in.
The algorithm is based on that of the TeX typesetting system by Donald E.
Knuth.
This is originally based on the Perl implementation of
{TeX::Hyphen}[http://search.cpan.org/author/JANPAZ/TeX-Hyphen-0.140/lib/TeX/Hyphen.pm]
and the {Ruby port}[http://rubyforge.org/projects/text-format]. The language
hyphenation pattern files are based on the sources available from
{CTAN}[http://www.ctan.org] as of 2004.12.19 and have been manually translated
by Austin Ziegler.
This is a small feature release adding Russian language support and fixing a
bug in the custom hyphen support introduced last version. This release
provides
both Ruby 1.8.7 and Ruby 1.9.2 support (but please read below). In short, Ruby
1.8 support is deprecated and I will not be providing any bug fixes related to
Ruby 1.8. New features will be developed and tested against Ruby 1.9 only.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.rdoc License.rdoc README.rdoc" \
  -f

%gem_packages

%changelog
