#
# spec file for package scons
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


%define modname scons
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           scons%{psuffix}
Version:        3.0.5
Release:        0
Summary:        Replacement for Make
License:        MIT
Group:          Development/Tools/Building
URL:            http://www.scons.org/
Source0:        https://github.com/SCons/%{modname}/archive/%{version}.tar.gz
#http://www.scons.org/doc/%%{version}/HTML/scons-user.html
Source1:        scons-user.html-%{version}.tar.bz2
# Adjust to exclude all failing tests
Source2:        grep-filter-list.txt
# Local modification
Patch8:         scons-3.0.0-fix-install.patch
BuildRequires:  fdupes
BuildRequires:  grep
BuildRequires:  python3-base >= 3.5
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools
Requires:       python3-base >= 3.5
%if %{with test}
# texlive texlive-latex3 biber texmaker ghostscript
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
# For tests
BuildRequires:  clang
BuildRequires:  docbook-xsl-pdf2index
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxslt-tools
BuildRequires:  pcre-devel
BuildRequires:  subversion
BuildRequires:  swig
BuildRequires:  xmlgraphics-fop
%endif

%description
SCons is a make replacement that provides a range of enhanced features,
such as automated dependency generation and built-in compilation cache
support. SCons rule sets are Python scripts, which means that SCons
provides itself as well as the features. SCons allows you to use the
full power of Python to control compilation.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1

sed -i -e '/QT_LIBPATH = os.path.join.*QTDIR/s/lib/%{_lib}/' \
    src/engine/SCons/Tool/qt.py
sed -i 's|%{_bindir}/env python|%{_bindir}/python3|' src/script/*

cp %{SOURCE2} grep-filter-list.txt
chmod -x src/CHANGES.txt README.rst src/RELEASE.txt

# the test is marked skipped but fails; and all are windows based so
# we can safely ignore them
rm -r test/MSVC/
rm -r test/MSVS/
rm -r test/Win32/
rm test/fixture/no_msvc/no_regs_sconstruct.py
rm test/fixture/no_msvc/no_msvcs_sconstruct.py
rm test/LEX/live_mingw.py
rm test/Decider/MD5-winonly-firstbuild.py

%build
python3 bootstrap.py build/scons
cd build/scons
%python3_build

%install
%if !%{with test}
cd build/scons
ls -lh build/lib
%python3_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --record installed_files.txt
%fdupes %{buildroot}%{python3_sitelib}
%endif

%check
%if %{with test}
%ifnarch aarch64 armv7l ppc64 ppc64le s390x
TEMP_FILE=$(mktemp --tmpdir %{modname}-test.XXXXXX)
trap 'rm -f -- "$TEMP_FILE"' INT TERM HUP EXIT
find src/ test/ -name \*.py \
    | grep -F -v -f grep-filter-list.txt >$TEMP_FILE
python3 runtest.py -f $TEMP_FILE
%else
echo "Skiping tests on this architecture due to failures"
%endif
%endif

%if !%{with test}
%files
%license LICENSE
%doc src/CHANGES.txt README.rst src/RELEASE.txt
%{_bindir}/*
%{python3_sitelib}/SCons
%{python3_sitelib}/%{modname}*.egg-info
%{_mandir}/man1/*%{ext_man}
%endif

%changelog
