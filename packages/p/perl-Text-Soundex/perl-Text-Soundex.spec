#
# spec file for package perl-Text-Soundex
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Soundex
Version:        3.05
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name Text-Soundex
Summary:        Implementation of the soundex algorithm
License:        HPND
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Soundex/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Soundex is a phonetic algorithm for indexing names by sound, as pronounced
in English. The goal is for names with the same pronunciation to be encoded
to the same representation so that they can be matched despite minor
differences in spelling. Soundex is the most widely known of all phonetic
algorithms and is often used (incorrectly) as a synonym for "phonetic
algorithm". Improvements to Soundex are the basis for many modern phonetic
algorithms. (Wikipedia, 2007)

This module implements the original soundex algorithm developed by Robert
Russell and Margaret Odell, patented in 1918 and 1922, as well as a
variation called "American Soundex" used for US census data, and current
maintained by the National Archives and Records Administration (NARA).

The soundex algorithm may be recognized from Donald Knuth's *The Art of
Computer Programming*. The algorithm described by Knuth is the NARA
algorithm.

The value returned for strings which have no soundex encoding is defined
using '$Text::Soundex::nocode'. The default value is 'undef', however
values such as ''Z000'' are commonly used alternatives.

For backward compatibility with older versions of this module the
'$Text::Soundex::nocode' is exported into the caller's namespace as
'$soundex_nocode'.

In scalar context, 'soundex()' returns the soundex code of its first
argument. In list context, a list is returned in which each element is the
soundex code for the corresponding argument passed to 'soundex()'. For
example, the following code assigns @codes the value '('M200', 'S320')':

   @codes = soundex qw(Mike Stok);

To use 'Text::Soundex' to generate codes that can be used to search one of
the publically available US Censuses, a variant of the soundex algorithm
must be used:

    use Text::Soundex;
    $code = soundex_nara($name);

An example of where these algorithm differ follows:

    use Text::Soundex;
    print soundex("Ashcraft"), "\n";       # prints: A226
    print soundex_nara("Ashcraft"), "\n";  # prints: A261

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
