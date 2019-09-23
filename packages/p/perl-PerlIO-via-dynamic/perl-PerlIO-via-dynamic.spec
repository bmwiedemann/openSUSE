#
# spec file for package perl-PerlIO-via-dynamic
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


Name:           perl-PerlIO-via-dynamic
Version:        0.14
Release:        0
%define cpan_name PerlIO-via-dynamic
Summary:        Dynamic Perlio Layers
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PerlIO-via-dynamic/
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'PerlIO::via::dynamic' is used for creating dynamic PerlIO layers. It is
useful when the behavior or the layer depends on variables. You should not
use this module as via layer directly (ie :via(dynamic)).

Use the constructor to create new layers, with two arguments: translate and
untranslate. Then use '$p-'via ($fh)> to wrap the handle. Once <$fh> is
destroyed, the temporary namespace for the IO layer will be removed.

Note that PerlIO::via::dynamic uses the scalar fields to reference to the
object representing the dynamic namespace.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc CHANGES README

%changelog
