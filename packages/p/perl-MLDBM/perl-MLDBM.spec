#
# spec file for package perl-MLDBM
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MLDBM
Version:        2.05
Release:        0
%define cpan_name MLDBM
Summary:        store multi-level Perl hash structure in single level tied hash
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MLDBM/
Source:         http://www.cpan.org/authors/id/C/CH/CHORNY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
#BuildRequires: perl(FreezeThaw)
#BuildRequires: perl(MLDBM)
%{perl_requires}

%description
This module can serve as a transparent interface to any TIEHASH package
that is required to store arbitrary perl data, including nested references.
Thus, this module can be used for storing references and other arbitrary
data within DBM databases.

It works by serializing the references in the hash into a single string. In
the underlying TIEHASH package (usually a DBM database), it is this string
that gets stored. When the value is fetched again, the string is
deserialized to reconstruct the data structure into memory.

For historical and practical reasons, it requires the *Data::Dumper*
package, available at any CPAN site. *Data::Dumper* gives you really
nice-looking dumps of your data structures, in case you wish to look at
them on the screen, and it was the only serializing engine before version
2.00. However, as of version 2.00, you can use any of *Data::Dumper*,
*FreezeThaw* or *Storable* to perform the underlying serialization, as
hinted at by the the SYNOPSIS manpage overview above. Using *Storable* is
usually much faster than the other methods.

See the the BUGS manpage section for important limitations.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
