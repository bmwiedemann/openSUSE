#
# spec file for package cmpi-bindings
#
# Copyright (c) 2023 SUSE LLC
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
# nodebuginfo


%if 0%{?suse_version} >= 1500
%define python3 1
%else
%define python3 0
%endif
%if %{python3}
%define pywbemname %{name}-py3wbem
%else
%define pywbemname %{name}-pywbem
%endif

URL:            http://github.com/kkaempf/cmpi-bindings

Name:           cmpi-bindings
Version:        1.0.4
Release:        0
Summary:        Adapter to write and run CMPI-type CIM providers
License:        BSD-3-Clause AND CPL-1.0
Group:          Development/Libraries/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  gcc-c++

# We need swig threads support.
BuildRequires:  swig >= 1.3.34

BuildRequires:  sblim-cmpi-devel

BuildRequires:  perl
%if %{python3}
BuildRequires:  python3-devel
%else
BuildRequires:  python-devel
%endif

%if 0%{?rhel_version} > 0
BuildRequires:  -vim
%endif

%if 0%{?fedora} + 0%{?rhel_version} + 0%{?centos_version}  > 0

BuildRequires:  curl-devel
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  ruby-libs

%if 0%{?rhel_version} < 500
# rdoc needs irb/slex in rhel4
BuildRequires:  irb
%endif

%if (0%{?rhel_version} >= 500 && 0%{?rhel_version} < 600) || 0%{?centos_version} >= 500 || 0%{?fedora} < 17
# rdoc is separate from rhel5 on
BuildRequires:  ruby-rdoc
%endif

%if 0%{?fedora} > 18
BuildRequires:  rubypick
%endif

%if 0%{?fedora} || 0%{?rhel_version} >= 600 || 0%{?centos_version} >= 600
BuildRequires:  perl-devel
%endif

%endif

%if 0%{?suse_version} > 0

%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
%endif

%if 0%{?suse_version} > 1010
BuildRequires:  libcurl-devel
%else
# SLE10
BuildRequires:  curl-devel
%endif

# SLE9
%if 0%{?suse_version} < 920
BuildRequires:  pkgconfig
BuildRequires:  ruby
%else
BuildRequires:  pkg-config
BuildRequires:  ruby-devel
%endif

%endif

Source:         %{name}-%{version}.tar.bz2

%description
-

%prep
%setup -q

%build

# enforce installed FindRuby

if [ -f /usr/share/cmake/Modules/FindRuby.cmake ]; then
  rm -f cmake/modules/FindRuby.cmake
fi

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
%if %{python3}
      -DBUILD_PYTHON3=yes \
%else
      -DBUILD_PYTHON2=yes \
%endif
      -DBUILD_RUBY_GEM=no \
      ..
make %{?_smp_mflags}

%install
cd build
mkdir -p %{buildroot}/%{_datadir}/cmpi
%make_install
mkdir -p %{buildroot}/%{_docdir}
%if 0%{?suse_version} < 1500
cp -a swig/ruby/html %{buildroot}/%{_docdir}/cmpi-bindings-ruby-docs
%endif

%package -n cmpi-bindings-ruby
Summary:        Adapter to write and run CMPI-type CIM providers in Ruby
Group:          Development/Languages/Ruby
# for the debug package. we dont use debug_package_requires here as it would enforce to install both packages.
Provides:       %{name} = %{version}-%{release}
%if 0%{?ruby_sitelib} == 0
%{!?ruby_sitelib: %global ruby_sitelib %(ruby -r rbconfig -e 'vd = RbConfig::CONFIG["vendorlibdir"]; print(vd ? vd : RbConfig::CONFIG["sitelibdir"])')}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -r rbconfig -e 'vad = RbConfig::CONFIG["vendorarchdir"]; print(vad ? vad : RbConfig::CONFIG["sitearchdir"])')}
%endif

%description -n cmpi-bindings-ruby
Adapter to write and run CMPI-type CIM providers in Ruby

%files -n cmpi-bindings-ruby
%defattr(-,root,root,-)
%dir %{_libdir}/cmpi
%{_libdir}/cmpi/librbCmpiProvider.so
%{ruby_sitelib}/cmpi.rb
%dir %{ruby_sitelib}/cmpi
%dir %{ruby_sitelib}/cmpi/providers
%{ruby_sitelib}/cmpi/provider.rb

%if 0%{?suse_version} < 1500
# ruby 2.5.0 broke swig-rdoc
%package -n cmpi-bindings-ruby-doc
Summary:        RDoc-style documentation for cmpi-bindings-ruby
Group:          Documentation/HTML

%description -n cmpi-bindings-ruby-doc
RDoc-style documentation for cmpi-bindings-ruby

%files -n cmpi-bindings-ruby-doc
%defattr(-,root,root,-)
%dir %{_docdir}/cmpi-bindings-ruby-docs
%{_docdir}/cmpi-bindings-ruby-docs
%endif

%package -n %{pywbemname}
%if %{python3}
Summary:        Adapter to write and run CMPI-type CIM providers in Python 3
%else
Summary:        Adapter to write and run CMPI-type CIM providers in Python 2
%endif
Group:          Development/Languages/Python
# for the debug package. we dont use debug_package_requires here as it would enforce to install both packages.
Provides:       %{name} = %{version}-%{release}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%if %{python3}
%{!?py3_requires: %define py3_requires Requires: python3}
%{py3_requires}
%else
%{!?py_requires: %define py_requires Requires: python}
%{py_requires}
%endif

%description -n %{pywbemname}
-

%files -n %{pywbemname}
%defattr(-,root,root,-)
%dir %{_libdir}/cmpi
%dir %{_datadir}/cmpi
%if %{python3}
%{_libdir}/cmpi/libpy3CmpiProvider.so
%{python_sitelib}/cmpi_pywbem_bindings.py*
%{python_sitelib}/cmpi.py*
%{python_sitelib}/__pycache__/cmpi*
%else
%{_libdir}/cmpi/libpyCmpiProvider.so
%{python2_sitelib}/cmpi_pywbem_bindings.py*
%{python2_sitelib}/cmpi.py*
%endif

%package -n cmpi-bindings-perl
Requires:       perl = %{perl_version}
Summary:        Adapter to write and run CMPI-type CIM providers in Perl
Group:          Development/Languages/Perl
# for the debug package. we dont use debug_package_requires here as it would enforce to install both packages.
Provides:       %{name} = %{version}-%{release}

%description -n cmpi-bindings-perl
-

%files -n cmpi-bindings-perl
%defattr(-,root,root,-)
%dir %{_libdir}/cmpi
%{_libdir}/cmpi/libplCmpiProvider.so
%dir %{_datadir}/cmpi
%{perl_vendorlib}/cmpi-bindings.pl
%{perl_vendorlib}/cmpi.pm

%changelog
