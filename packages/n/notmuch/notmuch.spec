#
# spec file for package notmuch
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define pythons python3
%define libversion 5
Name:           notmuch
Version:        0.38.3
Release:        0
Summary:        The mail indexer
License:        GPL-3.0-or-later
URL:            https://notmuchmail.org
Source0:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz
Source1:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz.asc
# key fingerprint: 7A18 807F 100A 4570 C596  8420 7E4E 65C8 720B 706B
Source4:        notmuch.keyring
Patch0:         docs-Update-intersphinx_mapping.patch
BuildRequires:  libxapian-devel
# info pages
BuildRequires:  info
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(sfsexp)
BuildRequires:  pkgconfig(talloc)

%{bcond_without python3}
%{bcond_without emacs}

#FIXME: at the moment they are not enabled
%{bcond_with ruby}
%{bcond_with go}

# dtach is not present on SLE
# cannot run the tests there
%if 0%{?is_opensuse}
%{bcond_without tests}
%else
%{bcond_with tests}
%endif
# testsuite
%if %{with tests}
BuildRequires:  dtach
BuildRequires:  gdb
BuildRequires:  man
BuildRequires:  openssl
BuildRequires:  valgrind-devel
%endif
%if %{with emacs}
BuildRequires:  emacs-el
BuildRequires:  emacs-nox
%endif
%if %{with python3}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
%endif
%if %{with ruby}
BuildRequires:  ruby-devel
%endif
%if %{with go}
BuildRequires:  go
%endif

%description
A global-search and tag-based email system that can be used from a terminal or
from within a text editor. Notmuch provides a library interface so that its
indexing/searching/tagging features can be integrated elsewhere.

Notmuch is not much of an email program. It does not receive messages
(no POP or IMAP support), it does not send messages (no mail
composer, no network code at all). It does email search, for which it
uses the Xapian library.

%package        devel
Summary:        Development files for %{name}
Requires:       libnotmuch%{libversion} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the info pages for %{name}.

%package   -n libnotmuch%{libversion}
Summary:        A shared library for %{name}

%description -n libnotmuch%{libversion}
A global-search and tag-based email system which uses Xapian for indexing.

The libnotmuch%{libversion} package contains shared libraries for %{name}.

%if %{with python3}
%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
Recommends:     python-%{name}-doc = %{version}

%description -n python3-%{name}
Python3 interface (bindings) for %{name}

%package -n python-%{name}-doc
Summary:        Documentation of Python bindings for %{name}

%description -n python-%{name}-doc
Documentation of Python interface (bindings) for %{name}

%package -n python3-%{name}2
Summary:        Python3 bindings v2 for %{name}

%description -n python3-%{name}2
Python3 interface (bindings v2) for %{name}
%endif

%if %{with emacs}
%package emacs
Summary:        Emacs lisp email client based on %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       emacs
Requires:       emacs-el

%description emacs
%{name}-based email client written in emacs lisp
%endif

%prep
%autosetup -p1

%build
#hand-made configure script
#zsh completion is a part of zsh itself
export CFLAGS="%{?build_cflags}%{?!build_cflags:%optflags}"
export CXXFLAGS="%{?build_cxxflags}%{?!build_cxxflags:%optflags}"
export LDFLAGS="${RPM_LD_FLAGS}"
./configure \
%if %{without emacs}
  --without-emacs \
%endif
  --prefix=%{_prefix} \
  --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --localstatedir=%{_localstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --disable-dependency-tracking \
  --without-zsh-completion

%{make_build}

#TODO: bindings - go, ruby
pushd bindings

%if %{with python3}
cp -r python python3
pushd python3
python3 setup.py build
pushd docs
%{make_build} dirhtml
rm -f build/dirhtml/.buildinfo
popd
popd

pushd python-cffi
%pyproject_wheel
popd
%endif

popd

%install
%make_install

%if %{with python3}
pushd bindings/python3
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
pushd bindings/python-cffi
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
# Temporary: all tests pass except by known python-cffi ones, fixed upstream
exit 0

%if %{with tests}

# ensure that the tests are not running in parallel
export NOTMUCH_TEST_SERIALIZE=t

# this test fails on PPC64 (see id:87o8mpr5w6.fsf@tethera.net)
%ifarch ppc64
export NOTMUCH_SKIP_TESTS="T360-symbol-hiding"
%endif

# can only run the testsuite when debugging symbols are available (boo#1152451)
if echo "%{optflags}"|grep -q '\-g'; then
    %make_build check
fi

%endif
# {with tests}

%ldconfig_scriptlets -n libnotmuch%{libversion}

%files
%doc AUTHORS NEWS README
%license COPYING COPYING-GPL-3
%{_bindir}/%{name}
%{_bindir}/%{name}-emacs-mua
%{_mandir}/man1/%{name}*.1%{?ext_man}
%{_mandir}/man1/nmbug.1%{?ext_man}
%{_mandir}/man5/%{name}-hooks.5%{?ext_man}
%{_mandir}/man7/%{name}-search-terms.7%{?ext_man}
%{_mandir}/man7/%{name}-properties.7%{?ext_man}
%{_mandir}/man7/%{name}-sexp-queries.7%{?ext_man}

%files -n libnotmuch%{libversion}
%license COPYING COPYING-GPL-3
%{_libdir}/libnotmuch.so.%{libversion}*

%files devel
%license COPYING COPYING-GPL-3
%{_includedir}/%{name}.h
%{_libdir}/libnotmuch.so

%files doc
%license COPYING COPYING-GPL-3
%{_infodir}/nmbug.info%{?ext_info}
%{_infodir}/%{name}.info%{?ext_info}
%{_infodir}/%{name}-*.info%{?ext_info}

%if %{with python3}
%files -n python3-%{name}
%license COPYING COPYING-GPL-3
%doc bindings/python/README
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*egg-info

%files -n python-%{name}-doc
%license COPYING COPYING-GPL-3
%doc bindings/python3/docs/build/dirhtml/

%files -n python3-%{name}2
%license COPYING COPYING-GPL-3
%doc bindings/python/README
%{python3_sitearch}/%{name}2
%{python3_sitearch}/%{name}2*dist-info
%endif

%if %{with emacs}
%files emacs
%license COPYING COPYING-GPL-3
%{_datadir}/emacs/site-lisp/
%exclude %{_datadir}/applications/
%endif

%changelog
