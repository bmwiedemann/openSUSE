#
# spec file for package perl-Devel-CheckOS
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Devel-CheckOS
Version:        1.81
Release:        0
#Upstream:  This software is free-as-in-speech software, and may be used, distributed, and modified under the terms of either the GNU General Public Licence version 2 or the Artistic Licence. It's up to you which one you use. The full text of the licences can be found in the files GPL2.txt and ARTISTIC.txt, respectively.
%define cpan_name Devel-CheckOS
Summary:        Check What Os We're Running On
License:        GPL-2.0 or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-CheckOS/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Compare) >= 1.21
BuildRequires:  perl(File::Find::Rule) >= 0.28
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Data::Compare) >= 1.21
Requires:       perl(File::Find::Rule) >= 0.28
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(Test::More) >= 0.88
%{perl_requires}

%description
A learned sage once wrote on IRC:

   $^O is stupid and ugly, it wears its pants as a hat

Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS "families" such as "Unix", which includes things like
Linux, Solaris, AIX etc.

It spares perl the embarrassment of wearing its pants on its head by
covering them with a splendid Fedora.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc CHANGELOG GPL2.txt README TODO
%license ARTISTIC.txt

%changelog
