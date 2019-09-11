#
# spec file for package perl-Daemon-Generic
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Daemon-Generic
Version:        0.85
Release:        0
#Upstream:  the same terms as Perl itself.
%define cpan_name Daemon-Generic
Summary:        Framework to Provide Start/Stop/Reload for a Daemon
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Daemon-Generic/
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Eval::LineNumbers)
BuildRequires:  perl(Event)
BuildRequires:  perl(File::Flock) >= 2013.06
BuildRequires:  perl(File::Slurp)
Requires:       perl(File::Flock) >= 2013.06
Requires:       perl(File::Slurp)
%{perl_requires}

%description
Daemon::Generic provides a framework for starting, stopping, reconfiguring
daemon-like programs. The framework provides for standard commands that
work for as init.d files and as apachectl-like commands.

Programs that use Daemon::Generic subclass Daemon::Generic to override its
behavior. Almost everything that Genric::Daemon does can be overridden as
needed.

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
%doc Changes README

%changelog
