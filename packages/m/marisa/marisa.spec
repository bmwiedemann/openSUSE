#
# spec file for package marisa
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without python
%bcond_with perl
%bcond_with ruby
Name:           marisa
Version:        0.3.1
Release:        0
Summary:        Matching Algorithm with Recursively Implemented StorAge
License:        BSD-2-Clause OR LGPL-2.1-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/s-yata/marisa-trie/
Source:         https://github.com/s-yata/marisa-trie/archive/v%{version}/%{name}-trie-%{version}.tar.gz
Source99:       baselibs.conf
Patch0:         marisa-trie-%{version}-bindings-python3.patch
BuildRequires:  chrpath
BuildRequires:  cmake
%if 0%{?suse_version} < 1600
BuildRequires:  gcc15-c++
%else
BuildRequires:  gcc-c++
%endif
%if %{with perl}
BuildRequires:  perl
%endif
BuildRequires:  pkg-config
%if %{with python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%endif
%if %{with ruby}
BuildRequires:  ruby-devel
%endif
Provides:       marisa-trie = %{version}
Obsoletes:      marisa-trie < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if %{with python}
%define python_subpackage_only 1
%python_subpackages
%endif

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

%if %{with perl}
%package -n perl-marisa
Summary:        Perl bindings for %{name}
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}
%{perl_requires}

%description -n perl-marisa
Perl bindings for %{name}.

%endif

%if %{with python}
%package -n python-marisa
Summary:        Python bindings for %{name}
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description -n python-marisa
Python bindings for %{name}.
%endif

%if %{with ruby}
%package -n ruby-marisa
Summary:        Ruby bindings for %{name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
Requires:       ruby

%description -n ruby-marisa
Ruby bindings for %{name}.
%endif

%package -n marisa-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{with perl}
Requires:       perl-marisa = %{version}
%endif
%if %{with python}
Requires:       python3-marisa = %{version}
%endif
%if %{with ruby}
Requires:       ruby-marisa = %{version}
%endif

%description -n marisa-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n marisa-trie-%{version}
%autopatch -p1

%build
%if 0%{?suse_version} < 1600
export CC=%{_bindir}/gcc-15
export CXX=%{_bindir}/g++-15
%cmake -DCMAKE_C_COMPILER=%{_bindir}/gcc-15 \
       -DCMAKE_CXX_COMPILER=%{_bindir}/g++-15 \
       -DENABLE_TOOLS=ON
%else
%cmake -DENABLE_TOOLS=ON
%endif
make %{?_smp_mflags}

# build ruby
%if %{with ruby}
pushd ../bindings/ruby
ruby extconf.rb --with-opt-include=../../include --with-opt-lib=../../lib/marisa/.libs --vendor
make %{?_smp_mflags}
popd
%endif

# build python
%if %{with python}
pushd ../bindings/python3
#swig -Wall -c++ -python -py3 -outdir . ../marisa-swig.i
#mv ../marisa-swig_wrap.cxx .
export CFLAGS="-I%{_builddir}/%{name}-trie-%{version}/include -L%{_builddir}/%{name}-trie-%{version}/build"
export CXXFLAGS="-I%{_builddir}/%{name}-trie-%{version}/include -L%{_builddir}/%{name}-trie-%{version}/build"
%pyproject_wheel
popd
%endif

# build perl
%if %{with perl}
pushd ../bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" INC="-I../../include" LIBS="-L../../lib/marisa/.libs"
make %{?_smp_mflags}
popd
%endif

%install
%cmake_install

rm -rf %{buildroot}%{_libdir}/libmarisa.{la,a}
# install libs
mkdir -p %{buildroot}%{_libdir}
install -m 0755 build/libmarisa.so.0.3.1 %{buildroot}%{_libdir}
ln -sf %{_libdir}/libmarisa.so.0.3.1 %{buildroot}%{_libdir}/libmarisa.so
ln -sf %{_libdir}/libmarisa.so.0.3.1 %{buildroot}%{_libdir}/libmarisa.so.0

# install tools
mkdir -p %{buildroot}%{_bindir}
for i in benchmark build common-prefix-search dump lookup predictive-search reverse-lookup; do
  chrpath -d build/marisa-$i;
  install -m 0755 build/marisa-$i %{buildroot}%{_bindir}/marisa-$i;
done

# install ruby
%if %{with ruby}
pushd bindings/ruby
make install DESTDIR=%{buildroot} hdrdir=%{_includedir}/ruby-%{rb_ver} rubyhdrdir=%{_includedir}/ruby-%{rb_ver}
popd
%endif

# install python
%if %{with python}
pushd bindings/python3
%pyproject_install
popd
%endif

# install perl
%if %{with perl}
pushd bindings/perl
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{perl_vendorarch}/auto/marisa/.packlist
rm -rf %{buildroot}%{perl_vendorarch}/benchmark.pl
rm -rf %{buildroot}%{perl_vendorarch}/sample.pl
popd
sed -i '1s/^=head2 .*:/=head2/' %{buildroot}%{perl_archlib}/perllocal.pod
%endif

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
%{_libdir}/libmarisa.so.%{version}

%if %{with ruby}
%files -n ruby-marisa
%defattr(-,root,root)
%{rb_vendorarchdir}/%{name}.so

%endif
%if %{with python}
%files %{python_files marisa}
%defattr(-,root,root)
%{python_sitearch}/_marisa.*.so
%{python_sitearch}/marisa.py
%{python_sitearch}/marisa-0.0.0.dist-info
%{python_sitearch}/__pycache__/marisa.cpython-*.pyc
%endif

%if %{with perl}
%files -n perl-marisa
%defattr(-,root,root)
%{perl_archlib}/perllocal.pod
%dir %{perl_vendorarch}/auto/
%{perl_vendorarch}/auto/marisa
%{perl_vendorarch}/marisa.pm
%endif

%files -n marisa-devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libmarisa.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/Marisa

%changelog
