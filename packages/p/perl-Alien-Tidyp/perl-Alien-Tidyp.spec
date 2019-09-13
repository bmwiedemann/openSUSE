#
# spec file for package perl-Alien-Tidyp
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


Name:           perl-Alien-Tidyp
Version:        1.4.7
Release:        0
%define cpan_name Alien-Tidyp
Summary:        Building, finding and using tidyp library - L<http://www.tidyp.com>
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Alien-Tidyp/
Source:         http://www.cpan.org/authors/id/K/KM/KMX/%{cpan_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(Module::Build) >= 0.4211
Requires:       perl(File::ShareDir) >= 1.00
%{perl_requires}
# MANUAL
BuildRequires:  libtidyp-devel

%description
Building, finding and using tidyp library - L<http://www.tidyp.com>

%prep
%setup -q -n %{cpan_name}-v%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes patches README sharedir TODO

%changelog
