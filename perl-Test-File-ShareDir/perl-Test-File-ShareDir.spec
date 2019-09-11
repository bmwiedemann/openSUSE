#
# spec file for package perl-Test-File-ShareDir
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


Name:           perl-Test-File-ShareDir
Version:        1.001002
Release:        0
%define cpan_name Test-File-ShareDir
Summary:        Create a Fake ShareDir for your modules for testing
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-File-ShareDir/
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Path::Tiny) >= 0.018
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(Class::Tiny)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(Path::Tiny) >= 0.018
Requires:       perl(Scope::Guard)
Requires:       perl(parent)
%{perl_requires}

%description
'Test::File::ShareDir' is some low level plumbing to enable a distribution
to perform tests while consuming its own 'share' directories in a manner
similar to how they will be once installed.

This allows 'File::ShareDir' to see the _latest_ version of content instead
of simply whatever is installed on whichever target system you happen to be
testing on.

*Note:* This module only has support for creating 'new' style share dirs
and are NOT compatible with old File::ShareDirs.

For this reason, unless you have File::ShareDir 1.00 or later installed,
this module will not be usable by you.

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
%license LICENSE

%changelog
