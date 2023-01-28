#
# spec file for package hivex
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2011 Michal Hrusecky <mhrusecky@novell.com>
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


%bcond_without perl_bingings
%bcond_without python_bindings
%bcond_without ocaml_bindings
Name:           hivex
Version:        1.3.23
Release:        0
Summary:        Windows "Registry Hive" extraction library
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            http://libguestfs.org/hivex.3.html
Source:         http://libguestfs.org/download/hivex/%{name}-%{version}.tar.gz
Source2:        http://libguestfs.org/download/hivex/%{name}-%{version}.tar.gz.sig
Source3:        %{name}.keyring
Source4:        %{name}.rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
Requires:       perl(Getopt::Long)
Requires:       perl(Pod::Usage)
Requires:       perl(Win::Hivex)
Requires:       perl(Win::Hivex::Regedit)

%description
Hivex is a library for extracting the contents of Windows "Registry
Hive" files. It is designed to be secure against buggy or malicious
registry files.

%package devel
Summary:        Development files for hivex
Requires:       libhivex0 = %{version}

%description devel
Development files for hivex. Hivex is a Windows Registry Hive extraction
library.

%package -n libhivex0
Summary:        Windows Registry Hive extraction library

%description -n libhivex0
Hivex is a Windows Registry Hive extraction library.

%if %{with perl_bingings}
%package -n perl-Win-Hivex
Summary:        Perl bindings for hivex
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Stringy)
BuildRequires:  perl(Test::More)
Requires:       perl = %{perl_version}
%{perl_requires}

%description -n perl-Win-Hivex
This subpackage contains the Perl bindings for hivex.
Hivex is a Windows Registry Hive extraction library.

%endif

%if %{with python_bindings}
%package -n python3-hivex
Summary:        Python bindings for libhivex
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
Provides:       python-hivex = %{version}-%{release}
Obsoletes:      python-hivex < %{version}-%{release}

%description -n python3-hivex
This subpackage contains the Python bindings for hivex.
Hivex is a Windows Registry Hive extraction library.
%endif

%if %{with ocaml_bindings}
%package -n ocaml-hivex
Summary:        OCAML bindings for libhivex
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros
%{?ocaml_preserve_bytecode}

%description -n ocaml-hivex
This subpackage contains the OCAML bindings for hivex.
Hivex is a Windows Registry Hive extraction library.

%package -n ocaml-hivex-devel
Summary:        OCAML bindings development files for libhivex
Requires:       %{name}-devel = %{version}
Requires:       ocaml-hivex = %{version}

%description -n ocaml-hivex-devel
This subpackage contains the OCAML bindings development file
for hivex. Hivex is a Windows Registry Hive extraction library.
%endif

%lang_package

%prep
%setup -q

sed -i 's:%{_bindir}/env perl:%{_bindir}/perl:' regedit/hivexregedit

%build
if type python3-config >/dev/null
then
	export PYTHON="python3"
	export PYTHON_LIBS=$(python3-config --libs)
	export PYTHON_CFLAGS=$(python3-config --cflags)
	export PYTHON_EXT_SUFFIX=.so
fi
%configure --disable-static
# 'INSTALLDIRS' ensures that perl libs are installed in the vendor dir instead of the site dir
%make_build \
	LD_RUN_PATH= \
	INSTALLDIRS=vendor

%install
%make_install INSTALLDIRS=vendor

%if %{with perl_bingings}
%perl_process_packlist
%perl_gen_filelist
# the macro above packages everything, here only the perl files are desrired
grep "%{perl_vendorarch}/" %{name}.files | tee t
mv t %{name}.files
%endif
#
rm -f %{buildroot}/%{_libdir}/*.{l,}a
touch %{name}.lang
%find_lang %{name}

%post -n libhivex0 -p /sbin/ldconfig
%postun -n libhivex0 -p /sbin/ldconfig

%files
%doc
%{_bindir}/*
%{_mandir}/*/*

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/*.so

%files -n libhivex0
%license LICENSE
%{_libdir}/*.so.*

%if %{with python_bindings}
%files -n python3-hivex
%{python3_sitearch}/*
%endif

%if %{with perl_bingings}
%post -n perl-Win-Hivex -p /sbin/ldconfig
%postun -n perl-Win-Hivex -p /sbin/ldconfig

%files -n perl-Win-Hivex -f %{name}.files
%endif
#

%if %{with ocaml_bindings}
%files -n ocaml-hivex
%license LICENSE

%files -n ocaml-hivex-devel
%{_libdir}/ocaml/hivex
%{_libdir}/ocaml/stublibs
%endif

%files lang -f %{name}.lang

%changelog
