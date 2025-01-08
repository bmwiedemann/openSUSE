#
# spec file for package perl-Alien-wxWidgets
#
# Copyright (c) 2024 SUSE LLC
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


Name:           perl-Alien-wxWidgets
Version:        0.69
Release:        0
%define cpan_name Alien-wxWidgets
Summary:        Building, finding and using wxWidgets binaries
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDOOTSON/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-Alien-wxWidgets-do_not_build_wxgtk.patch
Patch1:         perl-Alien-wxWidgets-dump_sorted_config.patch
Patch2:         perl-Alien-wxWidgets-ignore_cbuilder_version.patch
# MANUAL
#BuildArch:     noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.24
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Module::Pluggable) >= 2.6
Requires:       perl(Module::Pluggable) >= 2.6
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
BuildRequires:  wxWidgets-3_2-nostl-devel
%else
BuildRequires:  wxWidgets-ansi-devel
%endif
# MANUAL END

%description
Please see Alien for the manifesto of the Alien namespace.

In short 'Alien::wxWidgets' can be used to detect and get configuration
settings from an installed wxWidgets.

%prep
%autosetup -p0 -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
# this copy of GNU patch is only used on win32, remove it for license clarity
# see https://build.opensuse.org/request/show/237465
rm -vf inc/src/patch*
# MANUAL END

%build
yes no | %__perl ./Build.PL installdirs=vendor
yes no | ./Build
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.txt

%changelog
