#
# spec file for package perl-File-Remove
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-File-Remove
Version:        1.60
Release:        0
%define cpan_name File-Remove
Summary:        Remove files and directories
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd) >= 3.29
BuildRequires:  perl(File::Spec) >= 3.29
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Cwd) >= 3.29
Requires:       perl(File::Spec) >= 3.29
%{perl_requires}

%description
*File::Remove::remove* removes files and directories. It acts like
*/bin/rm*, for the most part. Although 'unlink' can be given a list of
files, it will not remove directories; this module remedies that. It also
accepts wildcards, * and ?, as arguments for filenames.

*File::Remove::trash* accepts the same arguments as *remove*, with the
addition of an optional, infrequently used "other platforms" hashref.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
