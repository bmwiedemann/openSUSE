#
# spec file for package hivex
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without perl_bingings
%bcond_without python_bindings
%bcond_without ocaml_bindings

Name:           hivex
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkg-config
Requires:       perl(Getopt::Long)
Requires:       perl(Pod::Usage)
Requires:       perl(Win::Hivex)
Requires:       perl(Win::Hivex::Regedit)
Recommends:     %name-lang
Url:            http://libguestfs.org/hivex.3.html
Summary:        Windows "Registry Hive" extraction library
License:        LGPL-2.1 and GPL-2.0
Group:          Development/Libraries/C and C++
Version:        1.3.18
Release:        0
Source:         http://libguestfs.org/download/hivex/%name-%version.tar.gz
Source2:        http://libguestfs.org/download/hivex/%name-%version.tar.gz.sig
Source3:        %name.keyring
Source4:        %name.rpmlintrc

%description
Hivex is a library for extracting the contents of Windows "Registry
Hive" files. It is designed to be secure against buggy or malicious
registry files.

%package devel
Summary:        Development files for hivex
Group:          Development/Languages/C and C++
Requires:       libhivex0 = %version

%description devel
Development files for hivex. Hivex is a Windows Registry Hive extraction
library.

%package -n libhivex0
Summary:        Windows Registry Hive extraction library
Group:          System/Libraries

%description -n libhivex0
Hivex is a Windows Registry Hive extraction library.

%if %{with perl_bingings}
%package -n perl-Win-Hivex
Summary:        Perl bindings for hivex
Group:          Development/Languages/Perl
Requires:       perl = %perl_version
%if 0%{?suse_version} < 1140
BuildRequires:  perl-macros
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Stringy)
BuildRequires:  perl(Test::More)
%perl_requires

%description -n perl-Win-Hivex
This subpackage contains the Perl bindings for hivex.
Hivex is a Windows Registry Hive extraction library.

%endif

%if %{with python_bindings}
%package -n python-hivex
%define pyver %(python -c "import sys; print sys.version[:3]")
BuildRequires:  python
BuildRequires:  python-devel
Summary:        Python bindings for libhivex
Group:          Development/Languages/Python

%description -n python-hivex
This subpackage contains the Python bindings for hivex.
Hivex is a Windows Registry Hive extraction library.
%endif

%if %{with ocaml_bindings}
%package -n ocaml-hivex
%{?ocaml_preserve_bytecode}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros

Summary:        OCAML bindings for libhivex
Group:          Development/Languages/OCaml

%description -n ocaml-hivex
This subpackage contains the OCAML bindings for hivex.
Hivex is a Windows Registry Hive extraction library.

%package -n ocaml-hivex-devel
Summary:        OCAML bindings development files for libhivex
Group:          Development/Languages/OCaml
Requires:       hivex-devel = %{version}
Requires:       ocaml-hivex = %{version}

%description -n ocaml-hivex-devel
This subpackage contains the OCAML bindings development file
for hivex. Hivex is a Windows Registry Hive extraction library.
%endif

%lang_package

%prep
%setup -q

sed -i 's:/usr/bin/env perl:/usr/bin/perl:' regedit/hivexregedit

%build
if python --version && ! pkg-config python
then
	export PYTHON_LIBS="-lpython`python -c 'import distutils.sysconfig; print (distutils.sysconfig.get_python_version ());'`"
	export PYTHON_CFLAGS="-I`python -c 'import distutils.sysconfig; print (distutils.sysconfig.get_python_inc ());'`"
	export PYTHON_EXT_SUFFIX=.so
fi
%configure --disable-static
# 'INSTALLDIRS' ensures that perl libs are installed in the vendor dir instead of the site dir
make \
	INSTALLDIRS=vendor \
	LD_RUN_PATH= \
	%{?_smp_mflags}

%install
%make_install INSTALLDIRS=vendor

%if %{with perl_bingings}
%perl_process_packlist
%perl_gen_filelist
# the macro above packages everything, here only the perl files are desrired
grep "%perl_vendorarch/" %name.files | tee t
mv t %name.files
%endif
#
rm -f %buildroot/%_libdir/*.{l,}a
touch %name.lang
%find_lang %name

%post -n libhivex0 -p /sbin/ldconfig
%postun -n libhivex0 -p /sbin/ldconfig

%files
%doc README
%_bindir/*
%_mandir/*/*

%files devel
%_libdir/pkgconfig/*
%_includedir/*
%_libdir/*.so

%files -n libhivex0
%_libdir/*.so.*

%if %{with python_bindings}
%files -n python-hivex
%_libdir/python%pyver/site-packages/*
%endif

%if %{with perl_bingings}
%post -n perl-Win-Hivex -p /sbin/ldconfig

%postun -n perl-Win-Hivex -p /sbin/ldconfig

%files -n perl-Win-Hivex -f %name.files
%endif
#

%if %{with ocaml_bindings}
%files -n ocaml-hivex
%dir %{_libdir}/ocaml/hivex
%{_libdir}/ocaml/hivex/META
%{_libdir}/ocaml/hivex/hivex.cmi
%{_libdir}/ocaml/hivex/mlhivex.cma
%{_libdir}/ocaml/stublibs/*hivex.so*

%files -n ocaml-hivex-devel
%{_libdir}/ocaml/hivex/*hivex.a
%if %{ocaml_native_compiler}
%{_libdir}/ocaml/hivex/*hivex.cmx*
%endif
%{_libdir}/ocaml/hivex/hivex.mli
%endif

%files lang -f %name.lang

%changelog
