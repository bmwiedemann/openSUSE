#
# spec file for package perl-Exporter-Declare
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


Name:           perl-Exporter-Declare
Version:        0.114
Release:        0
%define cpan_name Exporter-Declare
Summary:        Exporting done right
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Exporter-Declare/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Fennec::Lite) >= 0.004
BuildRequires:  perl(Meta::Builder) >= 0.003
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Test::Exception) >= 0.290000
BuildRequires:  perl(Test::Simple) >= 0.88
BuildRequires:  perl(aliased)
Requires:       perl(Meta::Builder) >= 0.003
Requires:       perl(aliased)
%{perl_requires}

%description
Exporter::Declare is a meta-driven exporting tool. Exporter::Declare tries
to adopt all the good features of other exporting tools, while throwing
away horrible interfaces. Exporter::Declare also provides hooks that allow
you to add options and arguments for import. Finally, Exporter::Declare's
meta-driven system allows for top-notch introspection.

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
%doc README

%changelog
