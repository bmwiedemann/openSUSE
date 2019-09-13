#
# spec file for package perl-SDL
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-SDL
Version:        2.548
Release:        0
%define cpan_name SDL
Summary:        SDL bindings to Perl
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FROGGS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source2:        perl-SDL.rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  Mesa-devel
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_Pango-devel
BuildRequires:  libSDL_gfx-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_net-devel
BuildRequires:  libSDL_sound-devel
BuildRequires:  libSDL_ttf-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::SDL) >= 1.446
BuildRequires:  perl(CPAN) >= 1.92
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.260301
BuildRequires:  perl(File::ShareDir) >= 1.0
BuildRequires:  perl(Module::Build) >= 0.400000
BuildRequires:  perl(Test::Most) >= 0.21
BuildRequires:  perl(Test::Simple) >= 0.88
BuildRequires:  perl(Tie::Simple)
Requires:       perl(CPAN) >= 1.92
Requires:       perl(File::ShareDir) >= 1.0
Requires:       perl(Tie::Simple)
%{perl_requires}

%description
SDL Perl are a set of bindings to the Simple DirectMedia Layer (SDL).

Simple DirectMedia Layer is a cross-platform multimedia library designed to
provide low level access to audio, keyboard, mouse, joystick, 3D hardware via
OpenGL, and 2D video framebuffer. It is used by MPEG playback software,
emulators, and many popular games, including the award winning Linux port of
"Civilization: Call To Power."

%prep
%setup -q -n %{cpan_name}-%{version}
%ifarch %arm ppc64 ppc64le
# Remove hanging test. See: https://github.com/PerlGameDev/SDL/issues/289
rm t/sdlx_controller_interface.t
%endif

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGELOG examples MacOSX OFL-FAQ.txt OFL.txt scripts share src test TODO
%license COPYING

%changelog
