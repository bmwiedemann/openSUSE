#
# spec file for package perl-Lingua-EN-Tagger
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Lingua-EN-Tagger
Version:        0.31
Release:        0
#Upstream: GPL-1.0-or-later
%define cpan_name Lingua-EN-Tagger
Summary:        Part-of-speech tagger for English natural language processing
License:        GPL-3.0-only
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AC/ACOBURN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Parser) >= 3.45
BuildRequires:  perl(HTML::Tagset) >= 3.20
BuildRequires:  perl(Lingua::Stem) >= 0.81
BuildRequires:  perl(Memoize::ExpireLRU) >= 0.55
Requires:       perl(HTML::Parser) >= 3.45
Requires:       perl(HTML::Tagset) >= 3.20
Requires:       perl(Lingua::Stem) >= 0.81
Requires:       perl(Memoize::ExpireLRU) >= 0.55
%{perl_requires}

%description
The module is a probability based, corpus-trained tagger that assigns POS
tags to English text based on a lookup dictionary and a set of probability
values. The tagger assigns appropriate tags based on conditional
probabilities - it examines the preceding tag to determine the appropriate
tag for the current word. Unknown words are classified according to word
morphology or can be set to be treated as nouns or other parts of speech.

The tagger also extracts as many nouns and noun phrases as it can, using a
set of regular expressions.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
