#
# spec file for package perl-GStreamer1
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define cpan_name GStreamer1
Name:           perl-GStreamer1
Version:        0.003
Release:        0
Summary:        Perl interface to the GStreamer library
License:        BSD-2-Clause
Group:          Development/Languages/Perl
Url:            https://metacpan.org/pod/GStreamer1
Source:         https://cpan.metacpan.org/authors/id/T/TM/TMURRAY/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Glib::Object::Introspection) >= 0.009
BuildRequires:  pkgconfig(gstreamer-1.0)
Requires:       perl(Glib::Object::Introspection) >= 0.009
Requires:       typelib-1_0-Gst-1_0
Requires:       typelib-1_0-GstApp-1_0
%{perl_requires}

%description
This package provides perl bindings for GStreamer 1.x.
GStreamer is a library for constructing graphs of media-handling
components. The applications it supports range from simple
OGG Vorbis playback, audio/video streaming to complex audio
(mixing) and video (non-linear editing) processing.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE='%{optflags}'
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root)
%doc CHANGELOG examples

%changelog
