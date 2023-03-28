#
# spec file for package subunit
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


%define skip_python2 1
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%else
%define python_sitelib %{python3_sitelib}
%define python_files() -n python3-%{**}
%endif
%bcond_with python2
Name:           subunit
Version:        1.4.2
%global majver  %(awk 'BEGIN { OFS="."; FS="[\\.\\+]+" } {print $1, $2, $3}' <<< %{version})
# %%global majver  1.4
Release:        0
Summary:        C library for the subunit testing protocol
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/testing-cabal/subunit
# Source0:        %%{name}-%%{version}.tar.xz
Source0:        https://github.com/testing-cabal/%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module extras}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools >= 1.8.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  check-devel
BuildRequires:  cppunit-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
%python_subpackages

%description
Subunit C bindings.  See the python-subunit package for test processing
functionality.

%package -n libsubunit0
Summary:        Binary libraries for %{name}
Group:          System/Libraries
Requires:       %{name}%{?_isa} >= %{version}-%{release}

%description -n libsubunit0
Binary libraries for %{name}

%package devel
Summary:        Header files for developing C applications that use subunit
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libsubunit0 = %{version}-%{release}

%description devel
Header files and libraries for developing C applications that use subunit.

%package -n libcppunit_subunit0
Summary:        Subunit integration into cppunit
Group:          System/Libraries
Requires:       %{name}%{?_isa} >= %{version}-%{release}

%description -n libcppunit_subunit0
Subunit integration into cppunit.

%package -n libcppunit_subunit0-devel
Summary:        Header files for applications that use cppunit and subunit
Group:          Development/Libraries/C and C++
Requires:       cppunit-devel%{?_isa}
Requires:       libcppunit_subunit0%{?_isa} = %{version}-%{release}
Requires:       subunit-devel%{?_isa} = %{version}-%{release}

%description -n libcppunit_subunit0-devel
Header files and libraries for developing applications that use cppunit
and subunit.

%package -n perl-subunit
Summary:        Perl bindings for subunit
Group:          Development/Libraries/Perl
Requires:       perl-base = %{perl_version}
BuildArch:      noarch

%description -n perl-subunit
Subunit Perl bindings.  See the python3-python-subunit package for test
processing functionality.

%package shell
Summary:        Shell bindings for subunit
Group:          Development/Libraries/Other
BuildArch:      noarch

%description shell
Subunit shell bindings.  See the python3-python-subunit package for test
processing functionality.

%if 0%{?python_subpackage_only}
%package -n python-python-%{name}
Summary:        Streaming protocol for test results
Group:          Development/Libraries/Python
Requires:       python-extras
Requires:       python-testtools >= 1.8.0
BuildArch:      noarch

%description -n python-python-%{name}
Subunit is a streaming protocol for test results.  The protocol is a
binary encoding that is generated and parsed.  By design, all the
components of the protocol conceptually fit into the xUnit TestCase ->
TestResult interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for Python, C, C++ and Shell. Bindings can be
written for other languages.

A number of useful things can be done easily with subunit:
- Test aggregation: Tests run separately can be combined and then
  reported/displayed together.  For instance, tests from different
  languages can be shown as a seamless whole.
- Test archiving: A test run may be recorded and replayed later.
- Test isolation: Tests that may crash or otherwise interact badly with
  each other can be run separately and then aggregated, rather than
  interfering with each other.
- Grid testing: subunit can act as the necessary serialization and
  deserialization to get test runs on distributed machines to be
  reported in real time.

%else

%package -n python3-python-%{name}
Summary:        Streaming protocol for test results
Group:          Development/Libraries/Python
Requires:       python3-extras
Requires:       python3-testtools >= 1.8.0
BuildArch:      noarch

%description -n python3-python-%{name}
Subunit is a streaming protocol for test results.  The protocol is a
binary encoding that is generated and parsed.  By design, all the
components of the protocol conceptually fit into the xUnit TestCase ->
TestResult interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for Python, C, C++ and Shell. Bindings can be
written for other languages.

A number of useful things can be done easily with subunit:
- Test aggregation: Tests run separately can be combined and then
  reported/displayed together.  For instance, tests from different
  languages can be shown as a seamless whole.
- Test archiving: A test run may be recorded and replayed later.
- Test isolation: Tests that may crash or otherwise interact badly with
  each other can be run separately and then aggregated, rather than
  interfering with each other.
- Grid testing: subunit can act as the necessary serialization and
  deserialization to get test runs on distributed machines to be
  reported in real time.
%endif

%package filters
Summary:        Command line filters for processing subunit streams
Group:          Development/Tools/Other
Requires:       python3-junitxml
Requires:       python3-python-%{name} = %{version}-%{release}
Requires:       typelib-1_0-Gtk-3_0
BuildArch:      noarch

%description filters
Command line filters for processing subunit streams.

%prep
%autosetup -p1

fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Help the dependency generator
for filt in python/subunit/filter_scripts/*; do
  sed -i.orig '1{\@^#! */usr/bin/env python@d}' $filt
  touch -r $filt.orig ${filt}
  rm ${filt}.orig
done

%build
# Generate the configure script
autoreconf -fvi
export INSTALLDIRS=perl
# any python will do, this is only for the non-python part of the package
PYTHON=$(find %_bindir -name 'python3*[0-9]' -print -quit)
export PYTHON
%configure \
  --enable-shared \
  --disable-static

%make_build
%pyproject_wheel

%install
%pyproject_install

%{python_expand chmod 0755 %{buildroot}%{$python_sitelib}/%{name}/run.py

# Eliminate duplicates
rm -fr %{buildroot}%{$python_sitelib}/subunit/tests
%fdupes %{buildroot}%{$python_sitelib}
}

# NON-PYTHON STUFF
# We set pkgpython_PYTHON for efficiency to disable automake python compilation
%make_install pkgpython_PYTHON='' INSTALL="%{_bindir}/install -p"

# Install the shell interface
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cp -p shell/share/%{name}.sh %{buildroot}%{_sysconfdir}/profile.d

# Remove unwanted libtool files
find %{buildroot} -type f -name "*.la" -delete -print

# Fix perl installation
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{perl_sitelib}/Subunit* %{buildroot}%{perl_vendorlib}
rm -fr %{buildroot}%{perl_archlib} %{buildroot}%{perl_sitearch}

# Fix permissions
chmod 0755 %{buildroot}%{_bindir}/subunit-diff

# Fix timestamps
touch -r c/include/%{name}/child.h %{buildroot}%{_includedir}/%{name}/child.h
touch -r c++/SubunitTestProgressListener.h \
      %{buildroot}%{_includedir}/%{name}/SubunitTestProgressListener.h
touch -r perl/subunit-diff %{buildroot}%{_bindir}/subunit-diff

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib} PYTHON=%{$python}
# https://bugs.launchpad.net/subunit/+bug/1323410
find . -name sample\*.py -exec chmod +x '{}' \;
%make_build check
}

%post -n libsubunit0 -p /sbin/ldconfig
%postun -n libsubunit0 -p /sbin/ldconfig
%post -n libcppunit_subunit0 -p /sbin/ldconfig
%postun -n libcppunit_subunit0 -p /sbin/ldconfig

%files
%doc NEWS README.rst
%license Apache-2.0 BSD COPYING

%files -n libsubunit0
%doc NEWS README.rst
%license Apache-2.0 BSD COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc c/README
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/child.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files -n libcppunit_subunit0
%{_libdir}/libcppunit_%{name}.so.*

%files -n libcppunit_subunit0-devel
%doc c++/README
%{_includedir}/%{name}/SubunitTestProgressListener.h
%{_libdir}/libcppunit_%{name}.so
%{_libdir}/pkgconfig/libcppunit_%{name}.pc

%files -n perl-subunit
%license Apache-2.0 BSD COPYING
%{_bindir}/%{name}-diff
%{perl_vendorlib}/*

%files shell
%doc shell/README
%license Apache-2.0 BSD COPYING
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%files %{python_files python-%{name}}
%license Apache-2.0 BSD COPYING
%{python_sitelib}/%{name}/
%{python_sitelib}/python_%{name}-%{majver}*-info

%files filters
%{_bindir}/*
%exclude %{_bindir}/%{name}-diff

%changelog
