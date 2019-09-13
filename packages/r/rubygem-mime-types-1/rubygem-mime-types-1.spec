#
# spec file for package rubygem-mime-types-1
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           rubygem-mime-types-1
Version:        1.25.1
Release:        0
%define mod_name mime-types
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://mime-types.rubyforge.org/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        This library allows for the identification of a file's likely MIME
License:        MIT and Artistic-2.0 and GPL-2.0
Group:          Development/Languages/Ruby

%description
This library allows for the identification of a file's likely MIME content
type. This is release 1.25.1, fixing an issue with priority comparison for
mime-types 1.x. The current release is 2.0, which only supports Ruby 1.9 or
later.
Release 1.25.1 contains all features of 1.25, including the experimental
caching and lazy loading functionality. The caching and lazy loading features
were initially implemented by Greg Brockman (gdb). As these features are
experimental, they are disabled by default and must be enabled through the use
of environment variables. The cache is invalidated on a per-version basis; the
cache for version 1.25 will not be reused for any later version.
To use lazy loading, set the environment variable +RUBY_MIME_TYPES_LAZY_LOAD+
to any value other than 'false'. When using lazy loading, the initial startup
of MIME::Types is around 12–25× faster than normal startup (on my system,
normal startup is about 90 ms; lazy startup is about 4 ms). This isn't
generally useful, however, as the MIME::Types database has not been loaded.
Lazy startup and load is just *slightly* faster—around 1 ms. The real
advantage
comes from using the cache.
To enable the cache, set the environment variable +RUBY_MIME_TYPES_CACHE+ to a
filename where MIME::Types will have read-write access. The first time a new
version of MIME::Types is run using this file, it will be created, taking a
little longer than normal. Subsequent loads using the same cache file will be
approximately 3½× faster (25 ms) than normal loads. This can be combined with
+RUBY_MIME_TYPES_LAZY_LOAD+, but this is *not* recommended in a multithreaded
or multiprocess environment where all threads or processes will be using the
same cache file.
As the caching interface is still experimental, the only values cached are the
default MIME::Types database, not any custom MIME::Types added by users.
MIME types are used in MIME-compliant communications, as in e-mail or HTTP
traffic, to indicate the type of content which is transmitted. MIME::Types
provides the ability for detailed information about MIME entities (provided as
a set of MIME::Type objects) to be determined and used programmatically. There
are many types defined by RFCs and vendors, so the list is long but not
complete; don't hesitate to ask to add additional information. This library
follows the IANA collection of MIME types (see below for reference).
MIME::Types for Ruby was originally based on MIME::Types for Perl by Mark
Overmeer, copyright 2001 - 2009.
MIME::Types is built to conform to the MIME types of RFCs 2045 and 2231. It
tracks the {IANA registry}[http://www.iana.org/assignments/media-types/]
({ftp}[ftp://ftp.iana.org/assignments/media-types]) with some unofficial types
added from the {LTSW collection}[http://www.ltsw.se/knbase/internet/mime.htp]
and added by the users of MIME::Types.

%prep

%build

%install
%gem_install \
  --doc-files="History.rdoc Licence.rdoc README.rdoc" \
  -f

%gem_packages

%changelog
