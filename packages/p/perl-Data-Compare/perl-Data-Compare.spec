#
# spec file for package perl-Data-Compare
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


Name:           perl-Data-Compare
Version:        1.25
Release:        0
%define cpan_name Data-Compare
Summary:        Compare Perl Data Structures
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Compare/
Source0:        http://www.cpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Find::Rule) >= 0.1
Requires:       perl(File::Find::Rule) >= 0.1
%{perl_requires}

%description
Compare two perl data structures recursively. Returns 0 if the structures
differ, else returns 1.

A few data types are treated as special cases:

* Scalar::Properties objects

  This has been moved into a plugin, although functionality remains the
  same as with the previous version. Full documentation is in the
  Data::Compare::Plugins::Scalar::Properties manpage.

* Compiled regular expressions, eg qr/foo/

  These are stringified before comparison, so the following will match:

      $r = qr/abc/i;
      $s = qr/abc/i;
      Compare($r, $s);

  and the following won't, despite them matching *exactly* the same text:

      $r = qr/abc/i;
      $s = qr/[aA][bB][cC]/;
      Compare($r, $s);

  Sorry, that's the best we can do.

* CODE and GLOB references

  These are assumed not to match unless the references are identical - ie,
  both are references to the same thing.

You may also customise how we compare structures by supplying options in a
hashref as a third parameter to the 'Compare()' function. This is not yet
available through the OO-ish interface. These options will be in force for
the *whole* of your comparison, so will apply to structures that are
lurking deep down in your data as well as at the top level, so beware!

* ignore_hash_keys

  an arrayref of strings. When comparing two hashes, any keys mentioned in
  this list will be ignored.

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
%doc ARTISTIC.txt CHANGELOG GPL2.txt MAINTAINERS-NOTE NOTES README TODO

%changelog
