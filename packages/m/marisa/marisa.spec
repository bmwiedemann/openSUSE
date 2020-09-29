#
# spec file for package marisa
#
# Copyright (c) 2020 SUSE LLC
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


Name:           marisa
Version:        0.2.6
Release:        0
Summary:        Matching Algorithm with Recursively Implemented StorAge
License:        LGPL-2.1-or-later OR BSD-2-Clause
Group:          System/I18n/Japanese
URL:            https://github.com/s-yata/marisa-trie/
Source:         https://github.com/s-yata/marisa-trie/archive/v%{version}/%{name}-trie-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  ruby-devel
BuildRequires:  swig
Provides:       marisa-trie = %{version}
Obsoletes:      marisa-trie < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
static and space-efficient trie data structure. And libmarisa is a C++
library to provide an implementation of MARISA. Also, the package of
libmarisa contains a set of command line tools for building and
operating a MARISA-based dictionary.

A MARISA-based dictionary supports not only lookup but also reverse
lookup, common prefix search and predictive search.

%package -n libmarisa0
Summary:        Matching Algorithm with Recursively Implemented StorAge
Group:          System/Libraries

%description -n libmarisa0
The libmarisa0 package contains runtime libraries for marisa.

%package -n perl-marisa
Summary:        Perl bindings for %{name}
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}
%{perl_requires}

%description -n perl-marisa
Perl bindings for %{name}.

%package -n python3-marisa
Summary:        Python3 bindings for %{name}
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description -n python3-marisa
Python3 bindings for %{name}.

%package -n ruby-marisa
Summary:        Ruby bindings for %{name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
Requires:       ruby

%description -n ruby-marisa
Ruby bindings for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       perl-marisa = %{version}
Requires:       python3-marisa = %{version}
Requires:       ruby-marisa = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n marisa-trie-%{version}

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

# build ruby
pushd bindings/ruby
ruby extconf.rb --with-opt-include=../../include --with-opt-lib=../../lib/marisa/.libs --vendor
make %{?_smp_mflags}
popd

# build python
pushd bindings/python
swig -Wall -c++ -python -py3 -outdir . ../marisa-swig.i
mv ../marisa-swig_wrap.cxx .
python3 setup.py build_ext --include-dirs=../../include --library-dirs=../../lib/marisa/.libs
python3 setup.py build
popd

# build perl
pushd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" INC="-I../../include" LIBS="-L../../lib/marisa/.libs"
make %{?_smp_mflags}
popd

%install
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libdir}/libmarisa.{la,a}

# install ruby
pushd bindings/ruby
make install DESTDIR=%{buildroot} hdrdir=%{_includedir}/ruby-%{rb_ver} rubyhdrdir=%{_includedir}/ruby-%{rb_ver}
popd

# install python
pushd bindings/python
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -rf %{buildroot}%{python3_sitearch}/__pycache__
popd

# install perl
pushd bindings/perl
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{perl_vendorarch}/auto/marisa/.packlist
rm -rf %{buildroot}%{perl_vendorarch}/benchmark.pl
rm -rf %{buildroot}%{perl_vendorarch}/sample.pl
popd
sed -i '1s/^=head2 .*:/=head2/' %{buildroot}%{perl_archlib}/perllocal.pod

%post -n libmarisa0 -p /sbin/ldconfig

%postun -n libmarisa0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README.md
%license COPYING.md
%{_bindir}/%{name}-benchmark
%{_bindir}/%{name}-build
%{_bindir}/%{name}-common-prefix-search
%{_bindir}/%{name}-dump
%{_bindir}/%{name}-lookup
%{_bindir}/%{name}-predictive-search
%{_bindir}/%{name}-reverse-lookup

%files -n libmarisa0
%defattr(-,root,root)
%{_libdir}/libmarisa.so.0
%{_libdir}/libmarisa.so.0.0.0

%files -n ruby-marisa
%defattr(-,root,root)
%{rb_vendorarchdir}/%{name}.so

%files -n python3-marisa
%defattr(-,root,root)
%{python3_sitearch}/_marisa.*.so
%{python3_sitearch}/marisa.py
%{python3_sitearch}/marisa-0.0.0-py%{py3_ver}.egg-info

%files -n perl-marisa
%defattr(-,root,root)
%{perl_archlib}/perllocal.pod
%dir %{perl_vendorarch}/auto/
%{perl_vendorarch}/auto/marisa
%{perl_vendorarch}/marisa.pm

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libmarisa.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
