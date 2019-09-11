#
# spec file for package perl-CPAN-DistnameInfo
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-CPAN-DistnameInfo
Version:        0.12
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name CPAN-DistnameInfo
Summary:        Extract distribution name and version from a distribution filename
Url:            http://search.cpan.org/dist/CPAN-DistnameInfo/
Group:          Development/Libraries/Perl
#Source:         http://www.cpan.org/authors/id/G/GB/GBARR/CPAN-DistnameInfo-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
Many online services that are centered around CPAN attempt to associate
multiple uploads by extracting a distribution name from the filename of the
upload. For most distributions this is easy as they have used
ExtUtils::MakeMaker or Module::Build to create the distribution, which
results in a uniform name. But sadly not all uploads are created in this
way.

'CPAN::DistnameInfo' uses heuristics that have been learnt by the
http://search.cpan.org/ manpage to extract the distribution name and
version from filenames and also report if the version is to be treated as a
developer release

The constructor takes a single pathname, returning an object with the
following methods

* cpanid

  If the path given looked like a CPAN authors directory path, then this
  will be the the CPAN id of the author.

* dist

  The name of the distribution

* distvname

  The file name with any suffix and leading directory names removed

* filename

  If the path given looked like a CPAN authors directory path, then this
  will be the path to the file relative to the detected CPAN author
  directory. Otherwise it is the path that was passed in.

* maturity

  The maturity of the distribution. This will be either 'released' or
  'developer'

* extension

  The extension of the distribution, often used to denote the archive type
  (e.g. 'tar.gz')

* pathname

  The pathname that was passed to the constructor when creating the object.

* properties

  This will return a list of key-value pairs, suitable for assigning to a
  hash, for the known properties.

* version

  The extracted version

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README

%changelog
