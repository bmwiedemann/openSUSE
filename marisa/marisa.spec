#
# spec file for package marisa
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


%{!?py_ver: %global py_ver %(python -c "import sys; v=sys.version_info[:2]; print '%%d.%%d'%%v" 2>/dev/null || echo PYTHON-NOT-FOUND)}
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%if 0%{?sles_version} < 1110
%{!?rb_arch: %global rb_arch %(/usr/bin/ruby -e 'print RUBY_PLATFORUM')}
%{!?rb_ver: %global rb_ver %(/usr/bin/ruby -e 'puts VERSION.sub(/\\\.\\\d$/,"")')}
%{!?rb_vendorarch: %global rb_vendorarch %{_libdir}/ruby/site_ruby/%{rb_ver}/%{rb_arch}}
%endif

Name:           marisa
Version:        0.2.4
Release:        0
Summary:        Matching Algorithm with Recursively Implemented StorAge
License:        LGPL-2.1+ or BSD-2-Clause
Group:          System/I18n/Japanese
Url:            https://code.google.com/p/marisa-trie/
Source:         https://marisa-trie.googlecode.com/files/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  python-devel
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
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description -n perl-marisa
Perl bindings for %{name}.

%package -n python-marisa
Summary:        Python bindings for %{name}
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
%py_requires

%description -n python-marisa
Python bindings for %{name}.

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
Requires:       python-marisa = %{version}
Requires:       ruby-marisa = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

# build ruby
pushd bindings/ruby
ruby extconf.rb --with-opt-include="%{_builddir}/%{name}-%{version}/lib" --vendor
make %{?_smp_mflags}
popd

# build python
pushd bindings/python
python setup.py build_ext --include-dirs="%{_builddir}/%{name}-%{version}/lib" --library-dirs="%{_builddir}/%{name}-%{version}/lib/.libs"
python setup.py build
popd

# build perl
pushd bindings/perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" INC="-I%{_builddir}/%{name}-%{version}/lib" LIBS="-L%{_builddir}/%{name}-%{version}/lib/.libs"
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
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd

# install perl
pushd bindings/perl
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{perl_vendorarch}/auto/marisa/.packlist
popd
sed -i '1s/^=head2 .*:/=head2/' %{buildroot}%{perl_archlib}/perllocal.pod

%post -n libmarisa0 -p /sbin/ldconfig

%postun -n libmarisa0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING
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
%if 0%{?suse_version} > 1210
%{rb_vendorarchdir}/%{name}.so
%else
%{rb_vendorarch}/%{name}.so
%endif

%files -n python-marisa
%defattr(-,root,root)
%{python_sitearch}/_marisa.so
%{python_sitearch}/marisa.*
%if 0%{?suse_version} >= 1110
%{python_sitearch}/marisa-0.0.0-py%{py_ver}.egg-info
%endif

%files -n perl-marisa
%defattr(-,root,root)
%{perl_archlib}/perllocal.pod
%if 0%{?suse_version} >= 1140
%dir %{perl_vendorarch}/auto/
%endif
%{perl_vendorarch}/auto/marisa
%{perl_vendorarch}/marisa.pm
%{perl_vendorarch}/sample.pl

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libmarisa.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
