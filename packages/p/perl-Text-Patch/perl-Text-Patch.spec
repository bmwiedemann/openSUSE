#
# spec file for package perl-Text-Patch
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Patch
Version:        1.8
Release:        0
%define cpan_name Text-Patch
Summary:        Patches text with given patch
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Patch/
Source:         http://www.cpan.org/authors/id/C/CA/CADE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Text::Diff)
Requires:       perl(Text::Diff)
%{perl_requires}

%description
Text::Patch combines source text with given diff (difference) data. Diff
data is produced by Text::Diff module or by the standard diff utility (man
diff, see -u option).

* patch( $source, $diff, options... )

  First argument is source (original) text. Second is the diff data. Third
  argument can be either hash reference with options or all the rest
  arguments will be considered patch options:

      $output = patch( $source, $diff, STYLE => "Unified", ... );
  
      $output = patch( $source, $diff, { STYLE => "Unified", ... } );

  Options are:

    STYLE => 'Unified'

  STYLE can be "Unified", "Context" or "OldStyle".

  The 'Unified' diff format looks like this:

    @@ -1,7 +1,6 @@
    -The Way that can be told of is not the eternal Way;
    -The name that can be named is not the eternal name.
     The Nameless is the origin of Heaven and Earth;
    -The Named is the mother of all things.
    +The named is the mother of all things.
    +
     Therefore let there always be non-being,
       so we may see their subtlety,
     And let there always be being,
    @@ -9,3 +8,6 @@
     The two are the same,
     But after they are produced,
       they have different names.
    +They both may be called deep and profound.
    +Deeper and more profound,
    +The door of all subtleties!

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
%doc ChangeLog COPYING README

%changelog
