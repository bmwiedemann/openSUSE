#
# spec file for package perl-Lingua-EN-Sentence
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Lingua-EN-Sentence
Version:        0.31
Release:        0
%define cpan_name Lingua-EN-Sentence
Summary:        Split Text Into Sentences
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-EN-Sentence/
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.380000
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(warnings) >= 1.12
Requires:       perl(warnings) >= 1.12
%{perl_requires}

%description
The 'Lingua::EN::Sentence' module contains the function get_sentences,
which splits text into its constituent sentences, based on a regular
expression and a list of abbreviations (built in and given).

Certain well know exceptions, such as abbreviations, may cause incorrect
segmentations. But some of them are already integrated into this code and
are being taken care of. Still, if you see that there are words causing the
get_sentences function to fail, you can add those to the module, so it
notices them.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples LICENCE README

%changelog
