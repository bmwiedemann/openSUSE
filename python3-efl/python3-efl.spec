#
# spec file for package python3-efl
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define efl_version 1.20.0

Name:           python3-efl
Version:        1.20.0
Release:        0
Summary:        Python bindings of efl
License:        GPL-3.0 and LGPL-3.0
Group:          Development/Libraries/Python
Url:            http://enlightenment.org
Source:         python-efl-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(elementary) >= %efl_version
BuildRequires:  pkgconfig(emotion)
BuildRequires:  pkgconfig(eo) >= %efl_version
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(python)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
Python bindings of the enlightenment foundation libraries (efl)

%package doc
Summary:        Documentation for python-efl
Group:          Documentation/HTML
BuildRequires:  python-sphinx

%description doc
HTML formated documentation for python-efl module.

%package examples
Summary:        Examples of python-efl usage
Group:          Documentation/Other

%description examples
Some examples of usage of python-efl.

%prep
%setup -q -n python-efl-%{version}
# drop build date from doc to fix build-compare
sed -i "s/\(html_last_updated_fmt = \).*/\\1None/" ./doc/conf.py

%build
export CFLAGS="$CFLAGS -Wno-declaration-after-statement"
python3 setup.py build -g
python3 setup.py build_doc

%install
export DISABLE_CYTHON=1

# module itself
python3 setup.py install --prefix="%{_prefix}" --root=%{buildroot}

# documentation
install -m 0755 -d "%{buildroot}/%{_docdir}/%{name}"
cp -R build/sphinx/html "%{buildroot}/%{_docdir}/%{name}"
rm "%{buildroot}/%{_docdir}/%{name}"/html/.buildinfo
%if 0%{?suse_version}
%fdupes -s "%{buildroot}/%{_docdir}/%{name}"
%endif

# examples
install -m 0755 -d "%{buildroot}/%{_datadir}/%{name}"
cp -R examples/  "%{buildroot}/%{_datadir}/%{name}/"
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -pr COPYING %{buildroot}/%{_docdir}/%{name}/
cp -pr COPYING.LESSER %{buildroot}/%{_docdir}/%{name}/
cp -pr AUTHORS %{buildroot}/%{_docdir}/%{name}/

%files
%defattr(-,root,root)
%{_libdir}/python*/*/*
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/html/

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/html/

%files examples
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
