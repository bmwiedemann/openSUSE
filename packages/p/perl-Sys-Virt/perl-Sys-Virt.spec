#
# spec file for package perl-Sys-Virt
#
# Copyright (c) 2022 SUSE LLC
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


Name:           perl-Sys-Virt
Version:        8.10.0
Release:        0
%define cpan_name Sys-Virt
Summary:        Represent and manage a libvirt hypervisor connection
License:        ClArtistic OR GPL-2.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/Sys-Virt
Source:         %{cpan_name}-%{version}.tar.gz
Patch0:         suse-set-migration-constraints.patch
# Build
BuildRequires:  libvirt-devel >= %{version}
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
# Runtime
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::XPath::XMLParser)
BuildRequires:  perl(base)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%if 0%{?suse_version} >= 1500
BuildRequires:  perl(Test::CPAN::Changes)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
The Sys::Virt module provides a Perl XS binding to the libvirt virtual
machine management APIs. This allows machines running within arbitrary
virtualization containers to be managed with a consistent API.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%license LICENSE
%doc AUTHORS Changes HACKING perl-Sys-Virt.spec README

%changelog
