#
# spec file for package drc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           drc
Version:        3.2.3
Release:        0
Summary:        Tools to generate digital room correction filters
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://drc-fir.sourceforge.net/
Source:         https://sourceforge.net/projects/drc-fir/files/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  gcc-c++

%description
DRC is a program used to generate correction filters for acoustic compensation
of HiFi and audio systems in general, including listening room compensation. DRC
generates just the FIR correction filters, which can be used with a real time or
offline convolver to provide real time or offline correction. DRC doesn't
provide convolution features, and provides only some simplified, although really
accurate, measuring tools.

%package doc
Summary:        Documentation files for drc
Group:          Documentation/Other
Recommends:     gnuplot
Recommends:     octave-cli
Recommends:     octave-forge-signal

%description doc
This package contains documentation for drc and Octave scripts to generate
comparison graphs.

%prep
%setup -q
dos2unix COPYING

%build
CXXFLAGS="%{optflags}" CFLAGS="%{optflags}" make -C source %{?_smp_mflags}

%install
%make_install -C source
rm -r %{buildroot}%{_datadir}/doc/%{name}-%{version}
install -d %{buildroot}%{_docdir}/%{name}
cp -r source/doc/octave %{buildroot}%{_docdir}/%{name}
cp -r doc %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%{_bindir}/drc
%{_bindir}/lsconv
%{_bindir}/glsweep
%{_datadir}/drc

%files doc
%doc readme.txt
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/octave/XOver.txt

%changelog
