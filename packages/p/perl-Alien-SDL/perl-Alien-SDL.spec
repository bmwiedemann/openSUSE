#
# spec file for package perl-Alien-SDL
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


Name:           perl-Alien-SDL
Version:        1.446
Release:        0
%define cpan_name Alien-SDL
Summary:        Building, Finding and Using Sdl Binaries
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Alien-SDL/
Source0:        http://www.cpan.org/authors/id/F/FR/FROGGS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Fetch) >= 0.24
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(Text::Patch) >= 1.4
Requires:       perl(Capture::Tiny)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Which)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  libSDL_Pango-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_net-devel
BuildRequires:  libSDL_ttf-devel
# MANUAL END

%description
Please see the Alien manpage for the manifesto of the Alien namespace.

In short 'Alien::SDL' can be used to detect and get configuration settings
from an installed SDL and related libraries. Based on your platform it
offers the possibility to download and install prebuilt binaries or to
build SDL & co. from source codes.

The important facts:

* * The module does not modify in any way the already existing SDL
  installation on your system.

* * If you reinstall SDL libs on your system you do not need to
  reinstall Alien::SDL (providing that you use the same directory for
  the new installation).

* * The prebuild binaries and/or binaries built from sources are always
  installed into perl module's 'share' directory.

* * If you use prebuild binaries and/or binaries built from sources
  it happens that some of the dynamic libraries (*.so, *.dll) will not
  automaticly loadable as they will be stored somewhere under perl module's
  'share' directory. To handle this scenario Alien::SDL offers some special
  functionality (see below).

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"  --travis
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

# MANUAL BEGIN
sed "s:^%{_bindir}:%%attr(755,root,root) %{_bindir}:" %{name}.files -i
# MANUAL END
%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE patches README README.md TODO

%changelog
