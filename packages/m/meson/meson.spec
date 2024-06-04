#
# spec file for package meson
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000
%global pythons python311
%else
%global pythons python3
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define name_ext -test
%bcond_without test
%else
%define name_ext %{nil}
%bcond_with test
%endif
%define _name   mesonbuild
%{!?vim_data_dir:%global vim_data_dir %{_datadir}/vim}
%bcond_with     setuptools
%bcond_without  mono
Name:           meson%{name_ext}
Version:        1.4.1
Release:        0
Summary:        Python-based build system
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://mesonbuild.com/
Source:         https://github.com/%{_name}/meson/releases/download/%{version}/meson-%{version}.tar.gz
Source1:        https://github.com/%{_name}/meson/releases/download/%{version}/meson-%{version}.tar.gz.asc
Source2:        meson.keyring
# PATCH-FIX-OPENSUSE meson-test-installed-bin.patch dimstar@opensuse.org -- We want the test suite to run against /usr/bin/meson coming from our meson package.
Patch0:         meson-test-installed-bin.patch
# PATCH-FIX-OPENSUSE give more time to testsuites that run emulated
Patch1:         extend-test-timeout-on-qemu-builds.patch
# PATCH-FIX-OPENSUSE meson-distutils.patch -- meson is ring0 and therefor setuptools is not available
Patch2:         meson-distutils.patch

BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with setuptools}
BuildRequires:  %{python_module setuptools}
Requires:       python3-setuptools
%endif
%if "%{flavor}" != "test"
Requires:       ninja >= 1.8.2
# meson-gui was last used in openSUSE Leap 42.1.
Provides:       meson-gui = %{version}
Obsoletes:      meson-gui < %{version}
BuildArch:      noarch
%else
ExclusiveArch:  x86_64
BuildRequires:  %{python_module devel}
BuildRequires:  bison
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000
BuildRequires:  clang17
%else
BuildRequires:  clang >= 15
%endif
BuildRequires:  clang-tools >= 15
BuildRequires:  cups-devel
BuildRequires:  distribution-release
BuildRequires:  flex
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000
BuildRequires:  gcc13-c++
BuildRequires:  gcc13-fortran
BuildRequires:  gcc13-obj-c++
BuildRequires:  gcc13-objc
%else
BuildRequires:  gcc-c++ >= 12
BuildRequires:  gcc-fortran >= 12
BuildRequires:  gcc-obj-c++ >= 12
BuildRequires:  gcc-objc >= 12
%endif
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  gmock
BuildRequires:  gnustep-make
BuildRequires:  googletest-devel
BuildRequires:  itstool
BuildRequires:  java-headless
BuildRequires:  libboost_log-devel
# This will be required to build to python311
BuildRequires:  libboost_python3-devel
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpcap-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
%if 0%{?sle_version} == 150400 || 0%{?sle_version} == 150500
BuildRequires:  libstdc++6-devel-gcc11
%endif
BuildRequires:  libwmf-devel
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000
BuildRequires:  llvm17-devel
%else
BuildRequires:  llvm-devel
%endif
BuildRequires:  meson = %{version}
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  wxWidgets-any-devel
BuildRequires:  zlib-devel-static
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} < 1550
BuildRequires:  libboost_python-devel
# Leap / SLE 15.x
BuildRequires:  python2-PyYAML
BuildRequires:  python2-devel
BuildRequires:  python3-devel
%endif
%if %{with mono}
BuildRequires:  mono(csharp)
%endif
%endif
# meson makes use of macros that were only defined with rpm 4.15
%if (0%{?suse_version} < 1550 && 0%{?sle_version} < 150400)
Conflicts:      rpm-build < 4.15
%endif

%description
Meson is a build system designed to optimise programmer productivity.
It aims to do this by providing support for software development
tools and practices, such as unit tests, coverage reports, Valgrind,
CCache and the like. Supported languages include C, C++, Fortran,
Java, Rust. Build definitions are written in a non-turing complete
Domain Specific Language.

%package vim
Summary:        Vim syntax highlighting support for meson.build files
Group:          Productivity/Text/Editors
Requires:       vim
Supplements:    (vim and %{name})
BuildArch:      noarch

%description vim
Meson is a build system designed to optimise programmer productivity.
It aims to do this by providing support for software development
tools and practices, such as unit tests, coverage reports, Valgrind,
CCache and the like. Supported languages include C, C++, Fortran,
Java, Rust. Build definitions are written in a non-turing complete
Domain Specific Language.

This package provides meson.build syntax highlighting support for
Vim/NeoVim.

%prep
%autosetup -N -n meson-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%if !%{with setuptools}
%patch -P 2 -p1
%endif

%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000
# AddressSanitizer fails here because of ulimit.
sed -i "/def test_generate_gir_with_address_sanitizer/{
       s/$/\n        raise unittest.SkipTest('ulimit')/;
       }" unittests/linuxliketests.py

# Expects modern glibc with pthread symbols in libc.so
rm -rf test\ cases/rust/17\ staticlib\ link\ staticlib
%endif

# Remove hashbang from non-exec script
sed -i '1{/\/usr\/bin\/env/d;}' \
  ./mesonbuild/rewriter.py \
  ./mesonbuild/scripts/cmake_run_ctgt.py

# We do not have appleframeworks available at this moment - can't run the test suite for it
# boost is currently borked too
rm -r "test cases/frameworks/1 boost" \
      "test cases/objc/2 nsstring"
# remove gtest check that actually works because our gtest has .pc files
rm -rf test\ cases/failing/85\ gtest\ dependency\ with\ version

%build
%if %{without test}
%python_build
%else
# Ensure we have no mesonbuild / meson in CWD, thus guaranteeing we use meson in $PATH
rm -r meson.py mesonbuild
%endif

%install
# If this is the test suite, we don't need anything else but the meson package
%if %{without test}
%python_install

install -Dpm 0644 data/macros.meson \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.meson

install -Dpm 0644 data/syntax-highlighting/vim/ftdetect/meson.vim \
  -t %{buildroot}%{vim_data_dir}/site/ftdetect/
install -Dpm 0644 data/syntax-highlighting/vim/indent/meson.vim \
  -t %{buildroot}%{vim_data_dir}/site/indent/
install -Dpm 0644 data/syntax-highlighting/vim/syntax/meson.vim \
  -t %{buildroot}%{vim_data_dir}/site/syntax/

# entry points are not distutils-able
%if !%{with setuptools}
mkdir -p %{buildroot}%{_bindir}
echo """#!%{_bindir}/python3
from mesonbuild.mesonmain import main
import sys

sys.exit(main())
""" > %{buildroot}%{_bindir}/%{name}
chmod +x %{buildroot}%{_bindir}/%{name}
%{python_expand %{$python_fix_shebang}

# ensure egg-info is a directory
rm %{buildroot}%{$python_sitelib}/*.egg-info
cp -r meson.egg-info %{buildroot}%{$python_sitelib}/meson-%{version}-py%{$python_version}.egg-info
}

# Fix missing data files with distutils
while read line; do
  if [[ "$line" = %{_name}/* ]]; then
    [[ "$line" = *.py ]] && continue
    cp "$line" "%{buildroot}%{python_sitelib}/$line"
  fi
done < meson.egg-info/SOURCES.txt
%endif
%endif

%if %{with test}
%check

%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000
# Use gcc-13 for clang-tidy
install -d -m 0755 bin
ln -s /usr/bin/cpp-13 bin/cpp
ln -s /usr/bin/g++-13 bin/c++
ln -s /usr/bin/g++-13 bin/g++
ln -s /usr/bin/gcc-13 bin/cc
ln -s /usr/bin/gcc-13 bin/gcc
export PATH="${PWD}/bin:${PATH}"
c++ --version

# Fix shebang in test cases getting executed by ninja
%{python_expand find test\ cases -type f -name "*.py" \
    -exec sed -i "1s@#!.*python.*@#!$(realpath %{_bindir}/$python)@" {} +}
%endif

export LANG=C.UTF-8
export MESON_EXE=%{_bindir}/meson
export PYTHONDONTWRITEBYTECODE=1

# See prep section for removed tests
%python_flavored_alternatives \
%python_expand $python run_tests.py --failfast
%endif

%files
%license COPYING
%if !%{with test}
%{_bindir}/meson
%{python_sitelib}/%{_name}/
%{python_sitelib}/meson-*
%dir %{_datadir}/polkit-1/
%dir %{_datadir}/polkit-1/actions/
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
%{_rpmconfigdir}/macros.d/macros.meson
%{_mandir}/man1/meson.1%{?ext_man}

%files vim
%doc data/syntax-highlighting/vim/README
%dir %{vim_data_dir}/
%dir %{vim_data_dir}/site/
%dir %{vim_data_dir}/site/ftdetect/
%dir %{vim_data_dir}/site/indent/
%dir %{vim_data_dir}/site/syntax/
%{vim_data_dir}/site/ftdetect/meson.vim
%{vim_data_dir}/site/indent/meson.vim
%{vim_data_dir}/site/syntax/meson.vim
%endif

%changelog
