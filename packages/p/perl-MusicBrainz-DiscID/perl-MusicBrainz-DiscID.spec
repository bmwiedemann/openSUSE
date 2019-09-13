#
# spec file for package perl-MusicBrainz-DiscID
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


Name:           perl-MusicBrainz-DiscID
Version:        0.04
Release:        0
#Upstream: GPL-1.0-or-later
%define cpan_name MusicBrainz-DiscID
Summary:        Perl interface for the MusicBrainz libdiscid library
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NJ/NJH/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libdiscid) >= 0.2.2
Requires:       perl(Carp)
Requires:       perl(XSLoader)
# MANUAL END

%description
MusicBrainz::DiscID is a class to calculate a MusicBrainz DiscID from an
audio CD in the drive.

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
%doc Changes examples README.md

%changelog
