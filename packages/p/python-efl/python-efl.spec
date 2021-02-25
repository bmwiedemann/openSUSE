#
# spec file for package python-efl
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-efl
Version:        1.25.0
Release:        0
Summary:        Python bindings of evas
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Development/Libraries/Python
URL:            http://enlightenment.org
Source:         https://download.enlightenment.org/rel/bindings/python/%{name}-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  dbus-1-python3-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(emotion)
BuildRequires:  pkgconfig(eo)
BuildRequires:  pkgconfig(evas)
# cc1 uses too much memory on x86
#ExcludeArch:    %ix86
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# pre-unification mess
%if "%{python_flavor}" == "python2"
Obsoletes:      python-evas < %{version}
Provides:       python-evas = %{version}
Obsoletes:      python-ecore < %{version}
Provides:       python-ecore = %{version}
Obsoletes:      python-edje < %{version}
Provides:       python-edje = %{version}
Obsoletes:      python-emotion < %{version}
Provides:       python-emotion = %{version}
Obsoletes:      python-e_dbus < %{version}
Provides:       python-e_dbus = %{version}
Obsoletes:      python-elementary < %{version}
Provides:       python-elementary = %{version}
%endif
%endif

%if 0%{?suse_version}
%python_subpackages
%else
%package -n python3-efl
Summary:        Python bindings of evas
Group:          Development/Languages/Python

%description -n python3-efl
Python bindings of the Enlightenment Foundation Libraries (efl).
%endif

%description
Python bindings of the Enlightenment Foundation Libraries (efl).

%if 0%{?suse_version}
%package -n python-efl-doc
Summary:        Documentation for python-efl
Group:          Documentation/HTML
BuildRequires:  %{python_module Sphinx}
Provides:       python3-efl-doc
Conflicts:      otherproviders(python3-efl-doc)

%description -n python-efl-doc
HTML formated documentation for python-efl module.

%package -n python-efl-examples
Summary:        Examples of python-efl usage
Group:          Documentation/Other
Provides:       python3-efl-examples
Conflicts:      otherproviders(python3-efl-examples)

%description -n python-efl-examples
Some examples of usage of python-efl.
%endif

%prep
%setup -q
# drop build date from doc to fix build-compare
sed -i "s/\(html_last_updated_fmt = \).*/\\1None/" ./doc/conf.py

%build
export CFLAGS="$CFLAGS -Wno-declaration-after-statement"
%ifarch %ix86
export CFLAGS="$CFLAGS -O0"
%endif
%if 0%{?suse_version}
%{python_expand $python setup.py build -g
$python setup.py build_doc}
%else
%py2_build
%py3_build
%endif

%install
export DISABLE_CYTHON=1

# module itself
%{?suse_version:%python_install}
%{!?suse_version:%py2_install}
%{!?suse_version:%py3_install}

# documentation
%if 0%{?suse_version}
for _name in python-efl python3-efl; do
  install -m 0755 -d "%{buildroot}/%{_docdir}/$_name"
  cp -R build/sphinx/html "%{buildroot}/%{_docdir}/$_name"
  rm "%{buildroot}/%{_docdir}/$_name"/html/.buildinfo
done

%python_expand %fdupes %{buildroot}%{_docdir}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# examples
for _name in python-efl python3-efl; do
  install -m 0755 -d "%{buildroot}/%{_datadir}/$_name"
  cp -R examples/  "%{buildroot}/%{_datadir}/$_name/"
  mkdir -p %{buildroot}/%{_docdir}/$_name
done
# Remove examples installed under python-efl namespace
rm -r "%{buildroot}/%{_datadir}/%{name}/examples"
rm -r "%{buildroot}/%{_docdir}/%{name}/"
%endif

%if 0%{?suse_version}
%files %{python_files}
%{python_sitearch}/*
%exclude %{_docdir}/python3-efl/html/

%files -n python-efl-doc
%{_docdir}/python3-efl

%files -n python-efl-examples
%{_datadir}/python3-efl
%endif

%if !0%{?suse_version}
%files -n python-efl
%license AUTHORS COPYING*
%{python_sitearch}/*

%files -n python3-efl
%license AUTHORS COPYING*
%{python3_sitearch}/*
%endif

%changelog
