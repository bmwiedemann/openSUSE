#
# spec file for package perl-GStreamer1
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name GStreamer1
Name:           perl-GStreamer1
Version:        0.3.0
Release:        0
# 0.003 -> normalize -> 0.3.0
%define cpan_version 0.003
#Upstream:  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: conditions and the following disclaimer. conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
License:        BSD-2-Clause
Summary:        Bindings for GStreamer 1.0, the open source multimedia framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMURRAY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::CheckLib) >= 0.900
BuildRequires:  perl(Glib::Object::Introspection) >= 0.9
BuildRequires:  perl(Test::Pod)
Requires:       perl(Glib::Object::Introspection) >= 0.9
Provides:       perl(GStreamer1) = %{version}
Provides:       perl(GStreamer1::Caps::Simple) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(gstreamer-1.0)
Requires:       typelib-1_0-Gst-1_0
Requires:       typelib-1_0-GstApp-1_0
# MANUAL END

%description
GStreamer1 implements a framework that allows for processing and encoding
of multimedia sources in a manner similar to a shell pipeline.

Because it's introspection-based, most of the classes follow directly from
the C API. Therefore, most of the documentation is by example rather than a
full breakdown of the class structure.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
#make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGELOG examples

%changelog
