#
# spec file for package perl-PAR
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


Name:           perl-PAR
Version:        1.016
Release:        0
%define cpan_name PAR
Summary:        Perl Archive Toolkit
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Zip) >= 1.00
BuildRequires:  perl(AutoLoader) >= 5.66_02
BuildRequires:  perl(Compress::Zlib) >= 1.30
BuildRequires:  perl(Digest::SHA) >= 5.45
BuildRequires:  perl(PAR::Dist) >= 0.32
Requires:       perl(Archive::Zip) >= 1.00
Requires:       perl(AutoLoader) >= 5.66_02
Requires:       perl(Compress::Zlib) >= 1.30
Requires:       perl(Digest::SHA) >= 5.45
Requires:       perl(PAR::Dist) >= 0.32
%{perl_requires}

%description
This module lets you use special zip files, called *P*erl *Ar*chives, as
libraries from which Perl modules can be loaded.

It supports loading XS modules by overriding *DynaLoader* bootstrapping
methods; it writes shared object file to a temporary file at the time it is
needed.

A _.par_ file is mostly a zip of the _blib/_ directory after the build
process of a CPAN distribution. To generate a _.par_ file yourself, all you
have to do is compress the modules under _arch/_ and _lib/_, e.g.:

    % perl Makefile.PL
    % make
    % cd blib
    % zip -r mymodule.par arch/ lib/

Afterward, you can just use _mymodule.par_ anywhere in your '@INC', use
*PAR*, and it will Just Work. Support for generating _.par_ files is going
to be in the next (beyond 0.2805) release of Module::Build.

For convenience, you can set the 'PERL5OPT' environment variable to '-MPAR'
to enable 'PAR' processing globally (the overhead is small if not used);
setting it to '-MPAR=/path/to/mylib.par' will load a specific PAR file.
Alternatively, consider using the _par.pl_ utility bundled with the
PAR::Packer distribution, or using the self-contained _parl_ utility which
is also distributed with PAR::Packer on machines without PAR.pm installed.

Note that self-containing scripts and executables created with _par.pl_ and
_pp_ may also be used as _.par_ archives:

    % pp -o packed.exe source.pl        # generate packed.exe (see PAR::Packer)
    % perl -MPAR=packed.exe other.pl    # this also works
    % perl -MPAR -Ipacked.exe other.pl  # ditto

Please see SYNOPSIS for most typical use cases.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS Changes README
%license LICENSE

%changelog
