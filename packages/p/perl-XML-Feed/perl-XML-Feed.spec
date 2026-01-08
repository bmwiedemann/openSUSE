#
# spec file for package perl-XML-Feed
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name XML-Feed
Name:           perl-XML-Feed
Version:        1.0.0
Release:        0
# v1.0.0 -> normalize -> 1.0.0
%define cpan_version v1.0.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XML Syndication Feed Support
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Flexible)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::Natural)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Feed::Find)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build) >= 0.420
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Fetch)
BuildRequires:  perl(XML::Atom) >= 0.380
BuildRequires:  perl(XML::LibXML) >= 1.660
BuildRequires:  perl(XML::RSS) >= 1.470
BuildRequires:  perl(XML::XPath)
Requires:       perl(Class::ErrorHandler)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Flexible)
Requires:       perl(DateTime::Format::ISO8601)
Requires:       perl(DateTime::Format::Mail)
Requires:       perl(DateTime::Format::Natural)
Requires:       perl(DateTime::Format::W3CDTF)
Requires:       perl(Feed::Find)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::TokeParser)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Module::Pluggable)
Requires:       perl(URI::Fetch)
Requires:       perl(XML::Atom) >= 0.380
Requires:       perl(XML::LibXML) >= 1.660
Requires:       perl(XML::RSS) >= 1.470
Provides:       perl(XML::Feed) = %{version}
Provides:       perl(XML::Feed::Content) = 0.650.0
Provides:       perl(XML::Feed::Enclosure) = 0.650.0
Provides:       perl(XML::Feed::Entry) = 0.650.0
Provides:       perl(XML::Feed::Entry::Format::Atom) = 0.650.0
Provides:       perl(XML::Feed::Entry::Format::RSS) = 0.650.0
Provides:       perl(XML::Feed::Format::Atom) = 0.650.0
Provides:       perl(XML::Feed::Format::RSS) = 0.650.0
Provides:       perl(XML::Feed::Util) = 0.650.0
%undefine       __perllib_provides
%{perl_requires}

%description
_XML::Feed_ is a syndication feed parser for both RSS and Atom feeds. It
also implements feed auto-discovery for finding feeds, given a URI.

_XML::Feed_ supports the following syndication feed formats:

* * RSS 0.91

* * RSS 1.0

* * RSS 2.0

* * Atom

The goal of _XML::Feed_ is to provide a unified API for parsing and using
the various syndication formats. The different flavors of RSS and Atom
handle data in different ways: date handling; summaries and content;
escaping and quoting; etc. This module attempts to remove those differences
by providing a wrapper around the formats and the classes implementing
those formats (XML::RSS and XML::Atom::Feed). For example, dates are
handled differently in each of the above formats. To provide a unified API
for date handling, _XML::Feed_ converts all date formats transparently into
DateTime objects, which it then returns to the caller.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog.md Changes README

%changelog
