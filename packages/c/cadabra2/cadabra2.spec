#
# spec file for package cadabra2
#
# Copyright (c) 2025 SUSE LLC
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


# Disable testing for 32-bit due to invalid free issue in test canonicalise: https://github.com/kpeeters/cadabra2/issues/280
%ifarch %ix86
%bcond_with tests
%else
%bcond_without tests
%endif
%{?sle15_python_module_pythons}
%if 0%{?suse_version} >= 1600
%global pythons python3
%endif
%if 0%{?suse_version} >= 1650
%bcond_without jupyter
%else
%bcond_with jupyter
%endif
Name:           cadabra2
Version:        2.5.12
Release:        0
Summary:        A computer algebra system for solving problems in field theory
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://cadabra.science/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM cadabra2-disable-components-test.patch gh#kpeeters/cadabra2#212 badshah400@gmail.com -- Disable a test that crashes for unknown reasons
Patch0:         cadabra2-disable-components-test.patch
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module gobject-devel}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module sympy}
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
Requires:       python3 >= 3.8
Recommends:     %{name}-doc
%if %{with jupyter}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  jupyter-jupyter_core-filesystem
%endif
# SECTION For test
%if %{with tests}
BuildRequires:  %{python_module gmpy2}
%endif
# /SECTION
Recommends:     %{name}-examples

%description
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory. It has extensive
functionality for tensor computer algebra, tensor polynomial
simplification including multi-term symmetries, fermions and
anti-commuting variables, Clifford algebras and Fierz transformations,
implicit coordinate dependence, multiple index types and many more.
The input format is a subset of TeX. Both a command-line and a
graphical interface are available.

Key features of Cadabra2:
- Input and output using TeX notation.
- Designed for field-theory problems, with handling of anti-commuting
  and non-commuting objects without special notations for their
  products, gamma matrix algebra, Fierz identities, Dirac conjugation,
  vielbeine, flat and curved, covariant and contravariant indices,
  implicit dependence of tensors on coordinates, partial and covariant
  derivatives...
- Powerful tensor simplification algorithms, not just for mono-term
  symmetries but also for multi-terms symmetries like the Bianchi
  identity, or dimensionally-dependent symmetries like the Schouten
  identity.

%package gui
Summary:        GUI for cadabra2: computer algebra system for problems in field theory
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Obsoletes:      cadabra < 2.0
Provides:       cadabra = %{version}

%description gui
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides the GUI for %{name} and it's desktop menu integration.

%package examples
Summary:        A computer algebra system for solving problems in field theory
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
BuildArch:      noarch

%description examples
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides examples for %{name}.

%package doc
Summary:        A computer algebra system for solving problems in field theory
Group:          Documentation/HTML
Obsoletes:      cadabra-doc < 2.0
Provides:       cadabra-doc = %{version}
BuildArch:      noarch

%description doc
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides html documentation for %{name}.

%package -n jupyter-cadabra2-kernel
Summary:        Jupyter kernel for cadabra2
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Requires:       jupyter-notebook

%description -n jupyter-cadabra2-kernel
Cadabra2 is a computer algebra system (CAS) designed specifically for
the solution of problems encountered in field theory.

This package provides a jupyter kernel for %{name}.

%prep
%autosetup -p1

rm examples/.gitignore
# Remove timestamps from Doxygen HTML files
echo "HTML_TIMESTAMP = NO" >> config/Doxyfile
# REMOVE HASHBANG FROM NON-EXEC SCRIPT
sed -i "1{/#!\/usr\/bin\/env python/d}" libs/appdirs/cdb_appdirs.py

%build
%{python_expand #
%cmake \
  -DCMAKE_MANDIR:PATH=%{_mandir} \
  -DINSTALL_LATEX_DIR:PATH=%{_datadir}/texmf \
  -DENABLE_FRONTEND:BOOL=ON \
  -DENABLE_SYSTEM_JSONCPP:BOOL=ON \
  -DENABLE_MATHEMATICA:BOOL=OFF \
  -DBUILD_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
  -DPython_EXECUTABLE=%{_bindir}/$python \
  -DENABLE_PY_JUPYTER=%{?with_jupyter:ON}%{!?with_jupyter:OFF} \
  %{nil}
}

%cmake_build
cd ..
%make_build doc

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/texmf/tex/latex/cadabra2/
ln %{buildroot}%{_datadir}/cadabra2/latex/* %{buildroot}%{_datadir}/texmf/tex/latex/cadabra2/

%if %{with tests}
%check
export PATH=${PATH}:%{buildroot}%{_bindir}
export PYTHONDONTWRITEBYTECODE=1
# Set HOME to current dir to allow tests that try to
# write config files to home dir to run without perm issues
export HOME=`pwd`
%ctest
%endif

%files
%doc README.rst
%license doc/license.txt
%{_bindir}/cadabra2cadabra
%{_bindir}/cadabra2latex
%{_bindir}/cadabra-server
%{_bindir}/cdb-nbtool
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}ipynb
%{_bindir}/%{name}python
%{_bindir}/%{name}html
%{_datadir}/%{name}/
%{_datadir}/texmf
%{python3_sitearch}/cadabra2*.so
%{python3_sitearch}/cadabra2_defaults.py
%{python3_sitearch}/cdb_appdirs.py
%{python3_sitearch}/cdb/
%{_mandir}/man1/cadabra*.1%{?ext_man}

%files gui
%license doc/license.txt
%{_bindir}/%{name}-gtk
%{_datadir}/icons/hicolor/*/apps/cadabra2-gtk.*
%{_datadir}/applications/*.cadabra2-gtk.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml

%if %{with jupyter}
%files -n jupyter-cadabra2-kernel
%license doc/license.txt
%{python3_sitearch}/cadabra2_jupyter/
%{python3_sitearch}/notebook/
%{_jupyter_kernel_dir}/cadabra2/
%endif

%files examples
%doc examples/

%files doc
%doc doxygen/html

%changelog
