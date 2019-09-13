#
# spec file for package perl-OpenGL
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-OpenGL
Version:        0.70
Release:        0
#Upstream: CHECK(GPL-1.0+ or Artistic-1.0)
%define cpan_name OpenGL
Summary:        Perl bindings to the OpenGL API, GLU, and GLUT/FreeGLUT
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/OpenGL/
#Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHM/OpenGL-0.70.tar.gz # modified by pre_checkin.sh
Source0:        OpenGL-0.70.tar.gz
Source1:        cpanspec.yml
Patch0:         0001-Don-t-check-current-display-for-extensions.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
%if 0%{suse_version} >= 1500
BuildRequires:  Mesa-dri
%endif
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
# MANUAL END

%description
Perl bindings to the OpenGL API, GLU, and GLUT/FreeGLUT

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644
%patch0 -p1
# MANUAL BEGIN
find include -type f  \! -name glprocs.h -exec rm {} +
# MANUAL END

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" dist=NO_EXCLUSIONS
# Certain OpenGL calls may not be present in our OpenGL
# implementation, let us just ignore them.
sed 's/PERL_DL_NONLAZY=1//' -i Makefile
%{__make} %{?_smp_mflags}
%check
xvfb-run -a -s "+extension GLX -screen 0 1280x1024x24" %{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES COPYRIGHT examples fragment.arb fragment.cg fragment.glsl isosurf.bin KNOWN_PROBLEMS README Release_Notes SUPPORTS test.jpg test.tga TODO vertex.arb vertex.cg vertex.glsl

%changelog
