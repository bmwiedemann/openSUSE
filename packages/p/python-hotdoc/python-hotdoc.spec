#
# spec file for package python-hotdoc
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-hotdoc
Version:        0.18.3
Release:        0
Summary:        A documentation tool micro-framework
License:        LGPL-2.1-or-later
URL:            https://github.com/hotdoc/hotdoc
Source:         https://files.pythonhosted.org/packages/source/h/hotdoc/hotdoc-%{version}.tar.gz
# Prebuilt default-theme dist/ (hotdoc_bootstrap_theme @0ce3e58, built locally
# with npm: standalone meson configure of the in-tree theme sources + ninja).
# Upstream 0.18.3 no longer ships dist/ in the sdist, and the meson theme
# subproject needs npm + network at configure time, unavailable offline.
# Regenerate with: copy hotdoc/hotdoc_bootstrap_theme + hotdoc/less aside,
# meson setup builddir <theme> -Dinstall=true -Dless_include_path=<less>,
# ninja -C builddir, then tar -C builddir/src dist.
Source1:        hotdoc-bootstrap-theme-dist-0.18.3.tar.gz
# PATCH-FIX-UPSTREAM: install the prebuilt theme dist/ when present instead of
# fetching npm dependencies over the network via the theme subproject, so the
# package builds offline. No-op on git checkouts (dist/ is gitignored there).
Patch0:         use-prebuilt-theme-dist.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module meson-python}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
# Needed for %%check: the cmark C module init imports hotdoc.utils.utils
BuildRequires:  %{python_module toposort}
BuildRequires:  %{python_module wheel}
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
# The c extension needs libclang.so and llvm-config
Requires:       clang-devel
Requires:       llvm-devel
Requires:       python-PyYAML >= 6.0.2
Requires:       python-appdirs >= 1.4.4
Requires:       python-dbus-deviation >= 0.6.1
Requires:       python-feedgen >= 1.0.0
Requires:       python-lxml >= 5.4.0
Requires:       python-networkx >= 3.4
Requires:       python-pkgconfig >= 1.6.0
Requires:       python-schema >= 0.7.7
Requires:       python-toposort >= 1.10
Requires:       python-wheezy.template >= 3.2.3
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
# The hotdoc cli files were provided as separate package between Aug and Nov 2020
Obsoletes:      hotdoc < %{version}-%{release}
Provides:       hotdoc = %{version}-%{release}
%endif
%python_subpackages

%description
Hotdoc is a documentation framework. It provides an interface for extensions
to plug upon, along with some base objects (formatters, ...)

Hotdoc is distributed with a set of extensions that perform various tasks,
such as parsing C and extracting symbols with clang, parsing
gobject-introspection (gir) files, highlighting the syntax of code snippets
with prism, etc.

%prep
%autosetup -p1 -n hotdoc-%{version}
# Theme dist/ is carried as Source1 (see comment above it); the meson theme
# subproject is skipped by Patch0 when it is present.
tar -xzf %{SOURCE1} -C hotdoc/hotdoc_bootstrap_theme
# cmake.subproject('cmark') only looks under subprojects/, which upstream
# leaves to wrap-git fetching; point it at the pinned in-tree sources instead.
mkdir -p subprojects
cp -r cmark subprojects/cmark

sed -i -e '1s,#! %{_bindir}/env sh,#!%{_bindir}/sh,' ./hotdoc/extensions/gi/transition_scripts/translate_sections.sh

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hotdoc
%python_clone -a %{buildroot}%{_bindir}/hotdoc_dep_printer
%python_group_libalternatives hotdoc hotdoc_dep_printer
# Installed modules are imported, never executed: drop their shebangs.
%python_expand find %{buildroot}%{$python_sitearch}/hotdoc -name '*.py' -exec sed -i '1{/^#!/d}' {} +
# Web assets must not be executable.
%python_expand find %{buildroot}%{$python_sitearch}/hotdoc -name '*.js' -perm -111 -exec chmod a-x {} +
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Smoke-test the meson-built C extensions from the built tree. The parent
# packages are import-light, so no extra test dependencies are needed.
# NOTE: the source tree must not shadow the built modules on sys.path,
# so empty (cwd) entries are dropped. No cd here: the per-flavor file ops
# the expand macro emits assume the source dir as cwd.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -B -c "import sys; sys.path = [p for p in sys.path if p]; import hotdoc.parsers.cmark, hotdoc.parsers.search, hotdoc.parsers.c_comment_scanner"

%pre
%python_libalternatives_reset_alternative hotdoc
%python_libalternatives_reset_alternative hotdoc_dep_printer

%post
%python_install_alternative hotdoc hotdoc_dep_printer

%postun
%python_uninstall_alternative hotdoc

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitearch}/hotdoc
%{python_sitearch}/hotdoc-%{version}*-info
%python_alternative %{_bindir}/hotdoc
%python_alternative %{_bindir}/hotdoc_dep_printer

%changelog
