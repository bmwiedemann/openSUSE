#
# spec file for package perl-File-Mork
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-File-Mork
Version:        0.4
Release:        0
%define cpan_name File-Mork
Summary:        Module to Read Mozilla Url History Files
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Mork/
Source0:        http://www.cpan.org/authors/id/S/SI/SIMONW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Module::Build) >= 0.400000
Requires:       perl(HTML::Entities)
%{perl_requires}

%description
This is a module that can read the Mozilla URL history file -- normally
$HOME/.mozilla/default/*.slt/history.dat -- and extract the id, url, name,
hostname, first visted dat, last visited date and visit count.

To find your history file it might be worth using *Mozilla::Backup* which
has some platform-independent code for finding the profiles of various
Mozilla-isms (including Firefox, Camino, K-Meleon, etc.).

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
%doc Changes examples

%changelog
