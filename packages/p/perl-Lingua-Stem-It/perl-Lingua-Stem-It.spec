#
# spec file for package perl-Lingua-Stem-It
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


Name:           perl-Lingua-Stem-It
Version:        0.02
Release:        0
%define cpan_name Lingua-Stem-It
Summary:        Porter's stemming algorithm for Italian
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-Stem-It/
Source:         http://www.cpan.org/authors/id/A/AC/ACALPINI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

The algorithm is implemented exactly (I hope :-) as described in:

    http://snowball.tartarus.org/algorithms/italian/stemmer.html

The code is carefully crafted to work in conjunction with the the
Lingua::Stem manpage module by Benjamin Franz, from which I've also
borrowed some functionalities (caching and exception list).

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes README

%changelog
