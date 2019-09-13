#
# spec file for package perl-Data-Entropy
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


Name:           perl-Data-Entropy
Version:        0.007
Release:        0
%define cpan_name Data-Entropy
Summary:        Entropy (randomness) management
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Entropy/
Source:         http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Data::Float) >= 0.008
BuildRequires:  perl(HTTP::Lite) >= 2.2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
#BuildRequires: perl(Data::Entropy)
#BuildRequires: perl(Data::Entropy::RawSource::CryptCounter)
#BuildRequires: perl(Data::Entropy::Source)
Requires:       perl(Crypt::Rijndael)
Requires:       perl(Data::Float) >= 0.008
Requires:       perl(HTTP::Lite) >= 2.2
Requires:       perl(Params::Classify)
Requires:       perl(parent)
%{perl_requires}

%description
This module maintains a concept of a current selection of entropy source.
Algorithms that require entropy, such as those in the
Data::Entropy::Algorithms manpage, can use the source nominated by this
module, avoiding the need for entropy source objects to be explicitly
passed around. This is convenient because usually one entropy source will
be used for an entire program run and so an explicit entropy source
parameter would rarely vary. There is also a default entropy source,
avoiding the need to explicitly configure a source at all.

If nothing is done to set a source then it defaults to the use of Rijndael
(AES) in counter mode (see the Data::Entropy::RawSource::CryptCounter
manpage and the Crypt::Rijndael manpage), keyed using Perl's built-in
'rand' function. This gives a data stream that looks like concentrated
entropy, but really only has at most the entropy of the 'rand' seed. Within
a single run it is cryptographically difficult to detect the correlation
between parts of the pseudo-entropy stream. If more true entropy is
required then it is necessary to configure a different entropy source.

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
