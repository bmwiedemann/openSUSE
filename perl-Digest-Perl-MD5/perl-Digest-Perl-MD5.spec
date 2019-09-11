#
# spec file for package perl-Digest-Perl-MD5
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


Name:           perl-Digest-Perl-MD5
Version:        1.9
Release:        0
%define cpan_name Digest-Perl-MD5
Summary:        Perl implementation of Ron Rivests MD5 Algorithm
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Digest-Perl-MD5/
Source:         http://www.cpan.org/authors/id/D/DE/DELTA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This modules has the same interface as the much faster 'Digest::MD5'. So
you can easily exchange them, e.g.

	BEGIN {
	  eval {
	    require Digest::MD5;
	    import Digest::MD5 'md5_hex'
	  };
	  if ($@) { # ups, no Digest::MD5
	    require Digest::Perl::MD5;
	    import Digest::Perl::MD5 'md5_hex'
	  }		
	}

If the 'Digest::MD5' module is available it is used and if not you take
'Digest::Perl::MD5'.

You can also install the Perl part of Digest::MD5 together with
Digest::Perl::MD5 and use Digest::MD5 as normal, it falls back to
Digest::Perl::MD5 if it cannot load its object files.

For a detailed Documentation see the 'Digest::MD5' module.

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
%doc CHANGES rand.f

%changelog
